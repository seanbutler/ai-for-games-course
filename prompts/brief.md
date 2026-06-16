You are producing the student-facing assessment brief for an MSc "AI for Games" module.
You are given the assessment spec (YAML) and the course spec (YAML). Render them into a
single, polished Markdown document that students will read to understand what they must
submit and how it will be marked.

Structure the output as follows:

1. **Title block** — module code, module title, assessment title, weight, word limit,
   submission format, and deadline (verbatim from the spec).

2. **Overview** — two or three sentences situating the project: what students build, what
   they write, and what the project is designed to demonstrate. Derive this from the
   course philosophy and assessment description; do not invent constraints or promises.

3. **Deliverables** — one subsection per deliverable (Code, Report). For the Report,
   list each section with its heading and the full guidance text, rendered as readable
   prose rather than raw YAML. Present the report sections in the order they appear in
   the spec.

4. **Requirements** — render each requirement group as its own subsection with a clear
   label (e.g. "Foundation — all required", "Advanced: Learning — choose at least one").
   List each technique as a bullet. Preserve the exact wording from the spec.

5. **Marking scheme** — a table: Criterion | Weight | High | Mid | Low.

6. **Notes** — a short closing paragraph reminding students that the report is the
   primary evidence for learning outcomes, that code alone is not sufficient, and that
   the reference platform constraint is firm.

Constraints:
- Follow the house style: British English, direct and precise, practitioner-grounded.
- Do not add requirements, techniques, deadlines, or mark weightings that are not in the
  supplied spec. Render faithfully; do not editorialize.
- Do not include outcome mapping tables (those are for the moderation record, not students).
- Output only the Markdown document, with no preamble or sign-off.
