#!/usr/bin/env python3
"""
generate.py — staged-lowering course content generator.

Pipeline (each stage gated by human review):

  spec/units/<id>.yaml  --[outline]-->  build/units/<id>/outline.md
        |  review the outline, then: make freeze UNIT=<id>
        v
  build/units/<id>/outline.md (FROZEN)  --[content]-->  lecture.md, lab.md, claims-to-verify.md

Each artifact is a pure function of its committed inputs (course spec + style + refs
+ unit spec + that unit's reviewer feedback), so every build is reproducible and every
iteration lives in git. Inputs are hashed; an artifact is regenerated only when its
inputs change (or with --force). Regenerating an outline auto-invalidates its freeze,
forcing re-review before content is lowered again.

Usage:
  python scripts/generate.py --stage outline [--unit 01-pathfinding] [--force]
  python scripts/generate.py --stage content [--unit 01-pathfinding] [--force]
  python scripts/generate.py --stage all     [--unit ...] [--force]

Requires ANTHROPIC_API_KEY in the environment. See README.md.
"""
import argparse
import datetime
import hashlib
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency. Run: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "spec"
PROMPTS = ROOT / "prompts"
REVIEW = ROOT / "review"
BUILD = ROOT / "build"
CACHE = ROOT / ".build-cache"

# --- Tunables ---------------------------------------------------------------
# Model is pinned for reproducibility. Bump to "claude-opus-4-8" for final prose
# if you want maximum quality on the content stage. See docs.claude.com for ids.
MODEL = "claude-sonnet-4-6"
TEMPERATURE = {"outline": 0.2, "content": 0.5, "brief": 0.3}
MAX_TOKENS = {"outline": 4000, "content": 8000, "brief": 4000}

FILE_MARKER = re.compile(r"^<<<FILE:\s*(.+?)\s*>>>\s*$", re.MULTILINE)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n\n?", re.DOTALL)


# --- Small helpers ----------------------------------------------------------
def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return "uncommitted"


def unit_ids():
    return sorted(p.stem for p in (SPEC / "units").glob("*.yaml"))


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER.sub("", text, count=1)


def input_hash(stage: str, parts: list[str]) -> str:
    h = hashlib.sha256()
    h.update(f"{MODEL}|{stage}".encode())
    for p in parts:
        h.update(b"\x00")
        h.update(p.encode("utf-8"))
    return h.hexdigest()[:16]


def cache_file(unit: str, stage: str) -> Path:
    return CACHE / f"{unit}.{stage}.hash"


def cached_hash(unit: str, stage: str) -> str | None:
    f = cache_file(unit, stage)
    return f.read_text().strip() if f.exists() else None


def write_cache(unit: str, stage: str, h: str):
    CACHE.mkdir(exist_ok=True)
    cache_file(unit, stage).write_text(h)


def frozen_marker(unit: str) -> Path:
    return BUILD / "units" / unit / ".frozen"


def provenance(stage: str, h: str) -> str:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    return (
        "---\n"
        f"generated_by: generate.py\n"
        f"stage: {stage}\n"
        f"model: {MODEL}\n"
        f"spec_sha: {git_sha()}\n"
        f"input_hash: {h}\n"
        f"generated_at: {now}\n"
        "---\n\n"
    )


def call_claude(system: str, user: str, stage: str) -> str:
    # Imported lazily so --help works without the SDK installed.
    from anthropic import Anthropic

    client = Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS[stage],
        temperature=TEMPERATURE[stage],
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")


def parse_multifile(text: str) -> dict[str, str]:
    """Split a response that uses <<<FILE: name>>> markers into {name: body}."""
    parts = FILE_MARKER.split(text)
    if len(parts) < 3:               # no markers found
        return {}
    names, bodies = parts[1::2], parts[2::2]
    return {n.strip(): b.strip() + "\n" for n, b in zip(names, bodies)}


# --- Common inputs ----------------------------------------------------------
def common_inputs() -> dict[str, str]:
    return {
        "course": read(SPEC / "course.yaml"),
        "style": read(SPEC / "style.md"),
        "refs": read(SPEC / "refs.yaml"),
    }


def feedback_for(unit: str) -> str:
    f = REVIEW / "units" / unit / "feedback.md"
    return read(f) if f.exists() else "(none)"


# --- Stages -----------------------------------------------------------------
def build_outline(unit: str, force: bool):
    c = common_inputs()
    spec_text = read(SPEC / "units" / f"{unit}.yaml")
    fb = feedback_for(unit)
    parts = [c["course"], c["style"], c["refs"], spec_text, fb,
             read(PROMPTS / "outline.md")]
    h = input_hash("outline", parts)

    out = BUILD / "units" / unit / "outline.md"
    if not force and out.exists() and cached_hash(unit, "outline") == h:
        print(f"  [skip] {unit} outline (unchanged)")
        return

    user = (
        f"# Course\n{c['course']}\n\n"
        f"# House style\n{c['style']}\n\n"
        f"# Approved references (cite ONLY from these)\n{c['refs']}\n\n"
        f"# Unit specification\n{spec_text}\n\n"
        f"# Reviewer feedback (incorporate)\n{fb}\n\n"
        f"Produce the structural outline for this unit now."
    )
    print(f"  [gen ] {unit} outline ...")
    body = call_claude(read(PROMPTS / "outline.md"), user, "outline")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(provenance("outline", h) + body, encoding="utf-8")
    write_cache(unit, "outline", h)

    # An outline regen invalidates any prior approval — force re-review.
    if frozen_marker(unit).exists():
        frozen_marker(unit).unlink()
        print(f"  [note] {unit} outline changed → freeze cleared, re-review before content")


def build_content(unit: str, force: bool):
    if not frozen_marker(unit).exists():
        print(f"  [gate] {unit} outline not frozen — review "
              f"build/units/{unit}/outline.md then `make freeze UNIT={unit}`")
        return

    c = common_inputs()
    spec_text = read(SPEC / "units" / f"{unit}.yaml")
    outline = strip_frontmatter(read(BUILD / "units" / unit / "outline.md"))
    fb = feedback_for(unit)
    parts = [c["course"], c["style"], c["refs"], spec_text, outline, fb,
             read(PROMPTS / "content.md")]
    h = input_hash("content", parts)

    udir = BUILD / "units" / unit
    done = all((udir / f).exists() for f in ("lecture.md", "lab.md", "claims-to-verify.md"))
    if not force and done and cached_hash(unit, "content") == h:
        print(f"  [skip] {unit} content (unchanged)")
        return

    user = (
        f"# Course\n{c['course']}\n\n"
        f"# House style\n{c['style']}\n\n"
        f"# Approved references (cite ONLY from these)\n{c['refs']}\n\n"
        f"# Unit specification\n{spec_text}\n\n"
        f"# FROZEN structural outline (realise this exactly)\n{outline}\n\n"
        f"# Reviewer feedback (incorporate)\n{fb}\n\n"
        f"Produce the content files now."
    )
    print(f"  [gen ] {unit} content ...")
    resp = call_claude(read(PROMPTS / "content.md"), user, "content")
    files = parse_multifile(resp)
    if not files:
        sys.exit(f"  [err ] {unit}: model did not return <<<FILE: ...>>> markers; "
                 f"re-run, and consider lowering content into smaller units.")

    fm = provenance("content", h)
    for name, body in files.items():
        (udir / name).write_text(fm + body, encoding="utf-8")
        print(f"         wrote build/units/{unit}/{name}")
    write_cache(unit, "content", h)


# --- Brief stage ------------------------------------------------------------
def build_brief(force: bool):
    c = common_inputs()
    brief_spec = read(SPEC / "assessment-brief.yaml")
    parts = [c["course"], c["style"], brief_spec, read(PROMPTS / "brief.md")]
    h = input_hash("brief", parts)

    out = BUILD / "assessment-brief.md"
    if not force and out.exists() and cached_hash("_brief", "brief") == h:
        print("  [skip] assessment brief (unchanged)")
        return

    user = (
        f"# Course spec\n{c['course']}\n\n"
        f"# House style\n{c['style']}\n\n"
        f"# Assessment spec\n{brief_spec}\n\n"
        f"Produce the student-facing assessment brief now."
    )
    print("  [gen ] assessment brief ...")
    body = call_claude(read(PROMPTS / "brief.md"), user, "brief")

    BUILD.mkdir(exist_ok=True)
    out.write_text(provenance("brief", h) + body, encoding="utf-8")
    write_cache("_brief", "brief", h)
    print(f"         wrote {out.relative_to(ROOT)}")


# --- Entry point ------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Staged course content generator.")
    ap.add_argument("--stage", choices=["outline", "content", "all", "brief"], default="all")
    ap.add_argument("--unit", help="unit id (filename stem). Default: all units.")
    ap.add_argument("--force", action="store_true", help="regenerate even if inputs unchanged")
    args = ap.parse_args()

    if args.stage == "brief":
        print("Assessment brief:")
        build_brief(args.force)
        print("Done.")
        return

    units = [args.unit] if args.unit else unit_ids()
    if not units:
        sys.exit("No unit specs found under spec/units/.")

    for unit in units:
        if not (SPEC / "units" / f"{unit}.yaml").exists():
            sys.exit(f"Unknown unit: {unit}")
        print(f"Unit {unit}:")
        if args.stage in ("outline", "all"):
            build_outline(unit, args.force)
        if args.stage in ("content", "all"):
            build_content(unit, args.force)

    print("Done. Review build/, commit (or open a PR) to record this iteration.")


if __name__ == "__main__":
    main()
