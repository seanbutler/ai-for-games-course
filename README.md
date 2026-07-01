# AI and Games — WM9SL-15

Spec-driven course content for the MSc Games Engineering module at the University of Warwick. The spec files in `02-inputs/` are the source of known truth; everything in `06-output/` is generated and should never be hand-edited.

## How it works

Content is produced in two stages with a human review gate between them:

```
01-prompts
        │
    [input] - overall prompts for writing style etc
        │        
02-inputs
        │
    [input] - external documents from the university
        │        
03-spec/units/<id>.yaml
        │
    [outline]  -  Claude Code reads all inputs and produces the outline in conversation
        │
06-output/units/<id>/outline.md   ←  you review and iterate in conversation
        │
    [approve]  -  say "approve"; spec is copied to 05-approved-spec/
        │
    [content]  -  Claude Code reads the frozen outline and produces content in conversation
        │
06-output/units/<id>/
    lecture.md
    lab.md
    claims-to-verify.md
```

The outline stage fixes structure, timings, and outcome mapping. The content stage only realises that frozen structure into prose. Changing the spec after approval requires a fresh outline and re-approval before content can be regenerated.

## Layout

```
01-prompts/          System instructions for each generation stage
  outline.md           Tells Claude how to produce a structural outline
  content.md           Tells Claude how to produce lecture / lab / claims files
  brief.md             Tells Claude how to produce the student-facing assessment brief

02-inputs/           Reference documents
  ModuleSpec.pdf       Official Warwick module specification

03-spec/             The source of truth — edit these
  course.yaml          Module identity, learning outcomes, unit list, assessment structure
  style.md             House voice: British English, classical-first, C++ code, citation rules
  refs.yaml            Approved reference list; Claude cites only from here
  assessment-brief.yaml  Student-facing assessment spec (used to generate the brief)
  units/               One YAML file per unit

04-review/           Reviewer feedback, fed back into the next generation
  units/<id>/
    feedback.md        Notes from reviewing the outline or content; consumed on next regen

05-approved-spec/    Specs locked for content generation
  units/               Copied here by the approve step; content cannot be generated without this

06-output/           Generated artifacts — committed so iterations are examinable in git
  units/<id>/
    outline.md
    lecture.md
    lab.md
    claims-to-verify.md
  assessment-brief.md
```

## Units

| # | Unit | Status |
|---|---|---|
| 01 | Introduction to AI in Games | spec only |
| 02 | Search and Pathfinding | spec only |
| 03 | Collision Detection, Response, and Spatial Perception | outline |
| 04 | Decision Making | spec only |
| 05 | ML Foundations | spec only |
| 06 | Neural Networks | spec only |
| 07 | AI Agents and Learning | spec only |
| 08 | AI Content Systems | spec only |
| 09 | Modern AI Applications | spec only |
| 10 | AI at Scale | spec only |
| 11 | AI Tooling Pipeline | spec only |

## The iteration loop

To change an outline or content, either:

- **Edit the spec** in `03-spec/units/<id>.yaml` for a structural change, then ask for a fresh outline.
- **Add a note to `04-review/units/<id>/feedback.md`** for a one-off correction; it will be incorporated on the next generation.

When a feedback note turns out to be a standing rule (voice, format, a recurring structural pattern), promote it into `03-spec/style.md` so it applies everywhere.

## Accuracy

`03-spec/refs.yaml` is the citation ground truth. Claude is instructed to cite only from it and to flag — never invent — anything it would need beyond that list. Every content generation also produces `claims-to-verify.md`, a checklist of technical assertions to audit before teaching. Curate `refs.yaml` yourself; the seeded entries are starting points only.

## Generating PDFs

From any markdown file in `06-output/`:

```bash
pandoc --pdf-engine=xelatex -o output.pdf 06-output/units/03-collision-and-perception/outline.md
```
