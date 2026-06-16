---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 75fb2935d3fcbcd0
generated_at: 2026-06-16T14:29:57+00:00
---

# Unit 08 — Modern AI Applications in Games

**One-line summary:** A synthesis unit surveying neural rendering, LLM integration, AI-assisted development, and ethics, culminating in a principled decision framework for choosing between classical and ML techniques in the project.

---

## 1. Timed Session Plan — Lecture (120 min total)

| # | Segment | Duration |
|---|---------|----------|
| 1 | Framing: where we are in the module arc | 5 min |
| 2 | Neural rendering: super-resolution and denoising | 25 min |
| 3 | Physics approximation via neural surrogates | 15 min |
| 4 | LLMs in games: dialogue, quests, narrative | 25 min |
| 5 | AI-assisted development tools | 15 min |
| 6 | Ethics, risk, and responsible deployment | 15 min |
| 7 | Classical-vs-ML synthesis: a decision framework | 15 min |
| 8 | Assessment consolidation and Q&A | 5 min |

**Total: 120 min**

---

## 2. Segment Detail

### Segment 1 — Framing: where we are in the module arc (5 min)

**Subtopics**
- Recap of the classical-first arc: Units 01–07 in one slide
- This unit as the integration point: every prior technique is now a candidate in a design decision
- Signpost to the project brief

**Worked examples**
- None (orientation only)

**Learning outcomes served**
- *"Synthesise learning from across the module to justify AI technique choices for the project."* [lo2, lo6]

---

### Segment 2 — Neural rendering: super-resolution and denoising (25 min)

**Subtopics**
- The rendering pipeline bottleneck: why resolution and ray-count are expensive
- Traditional temporal anti-aliasing (TAA): how it works, its artefacts
- Super-resolution: upscaling from a lower internal resolution
  - DLSS 2.0 architecture: where the CNN sits in the pipeline, input buffers (colour, motion vectors, depth)
  - AMD FSR: spatial vs temporal approaches, no training data requirement
  - Quality/performance trade-off: latency, ghosting, sharpness
- Real-time denoising: Monte Carlo noise in path tracing; neural denoisers vs accumulation buffers
- Neural radiance fields (NeRF): brief conceptual overview; current impracticality for real-time; forward reference to research trajectory

**Worked examples**
- **WE1 (full):** Compare a traditional TAA pipeline with DLSS 2.0 — diagram showing where the neural network replaces the resolve pass, what inputs it consumes, and the quality/performance trade-off at 1080p→4K upscale.

**Learning outcomes served**
- *"Explain neural super-resolution and denoising and their impact on rendering pipelines."* [lo4, lo6]

---

### Segment 3 — Physics approximation via neural surrogates (15 min)

**Subtopics**
- Why real-time physics is constrained: CPU/GPU budget, determinism requirements
- Classical approximations: pre-baked animations, simplified collision proxies
- Neural surrogates: training a small network to approximate cloth, fluid, or destruction outputs
  - Inputs/outputs of a surrogate model
  - Training data generation from offline simulation
  - Accuracy vs speed trade-off; failure modes (out-of-distribution inputs)
- Industry examples: ML cloth in character systems, fluid surface approximation
- When to use: latency budget, authorial control, and content variability considerations

**Worked examples**
- Brief illustrative comparison: pre-baked cloth animation vs neural surrogate — parameter table (memory, CPU cost, flexibility)

**Learning outcomes served**
- *"Critically assess the role and impact of modern AI technologies in game development."* [lo6]
- *"Synthesise learning from across the module to justify AI technique choices for the project."* [lo2, lo6]

---

### Segment 4 — LLMs in games: dialogue, quests, and narrative (25 min)

**Subtopics**
- What an LLM is (brief recap from Unit 05 transformer coverage): token prediction, context window
- Use cases in games
  - NPC dialogue: open-ended conversation vs scripted dialogue trees
  - Dynamic quest generation: prompt engineering for structured output
  - Procedural narrative: LLM as a story manager vs classical drama manager
- Practical constraints
  - Latency: local inference vs API call; token generation speed
  - Cost: per-token pricing at scale; offline vs online deployment
  - Authorial control: guardrails, content filtering, consistency with lore
  - Determinism: same input ≠ same output; implications for QA and reproducibility
- Classical comparisons
  - Dialogue trees (Unit 03) vs LLM dialogue: control, cost, expressiveness
  - Grammar-based narrative (Unit 07) vs LLM narrative: structure vs fluency
- Forward reference: Unit 09 (AI at scale) for deployment architecture

**Worked examples**
- **WE2 (full):** Design a decision tree for selecting between a hand-authored behaviour tree and an LLM-backed NPC, given constraints of latency, budget, and authorial control — walk through each branch with concrete threshold values.

**Learning outcomes served**
- *"Critically assess LLM integration in games: capabilities, limitations, and player-experience implications."* [lo6]
- *"Evaluate and compare different AI approaches… and justify their suitability for specific design or technical problems."* [lo2]

---

### Segment 5 — AI-assisted development tools (15 min)

**Subtopics**
- Code generation: Copilot-style tools in game development workflows; strengths (boilerplate, API lookup) and failure modes (hallucinated APIs, subtle logic errors)
- Asset creation: text-to-texture, text-to-3D, style-transfer tools; pipeline integration and IP/licensing concerns
- QA and playtesting: automated agents for coverage testing; RL agents as stress-testers; limitations vs human playtesters
- Prompt-driven level design: LLM + PCG pipeline (link back to Unit 07)
- Dependency risk: reliance on third-party model providers; versioning and deprecation

**Worked examples**
- None (illustrative examples embedded in bullet discussion)

**Learning outcomes served**
- *"Critically assess the role and impact of modern AI technologies in game development, including… content generation."* [lo6]

---

### Segment 6 — Ethics, risk, and responsible deployment (15 min)

**Subtopics**
- Bias in training data: representation in generated characters, dialogue tone, world content
- Player manipulation: personalised difficulty, monetisation targeting, dark patterns enabled by player-behaviour models
- Environmental cost: inference energy at scale; model size vs deployment frequency
- Dependency on third-party models: data privacy, API availability, terms of service
- Regulatory landscape: EU AI Act categories relevant to games; age-rating implications of generative content
- Mitigation strategies: content filtering, human-in-the-loop authoring, transparency with players

**Worked examples**
- None (discussion-driven; instructor poses scenario questions)

**Learning outcomes served**
- *"Evaluate ethical and practical considerations when deploying modern AI in game products."* [lo6]

---

### Segment 7 — Classical-vs-ML synthesis: a decision framework (15 min)

**Subtopics**
- The core question: for a given in-game problem, which technique class is appropriate?
- Decision dimensions
  - Runtime constraints (latency, memory, platform)
  - Authorial control requirements (predictability, debuggability)
  - Data availability (training data cost, collection feasibility)
  - Team capability and toolchain maturity
  - Player-experience requirements (consistency vs variety)
- Framework structure: a two-axis map (control ↔ flexibility; cost ↔ capability)
- Applying the framework to project scenarios: pathfinding, NPC behaviour, content generation
- Explicit link to project report requirement: justifying technique choices with reference to this framework

**Worked examples**
- Rapid application of the framework to three project-relevant scenarios (pathfinding, NPC dialogue, level generation) — instructor-led, students call out answers

**Learning outcomes served**
- *"Synthesise learning from across the module to justify AI technique choices for the project."* [lo2, lo6]
- *"Evaluate and compare different AI approaches… and justify their suitability for specific design or technical problems."* [lo2]

---

### Segment 8 — Assessment consolidation and Q&A (5 min)

**Subtopics**
- Map project deliverables to module learning outcomes (one slide)
- Remind students: report must make reasoning visible, not just describe code
- Signpost: Unit 09 (AI at scale), Unit 10 (tooling and pipeline) as report-justification resources
- Open Q&A

**Worked examples**
- None

**Learning outcomes served**
- *"Synthesise learning from across the module to justify AI technique choices for the project."* [lo2, lo6]

---

## 3. Lab Plan — Tutorial (120 min total)

### Overview

Open-ended critical analysis exercise. Students select one modern AI application from games and produce a structured written evaluation, then discuss in groups of three.

---

### Stage 1 — Topic selection and framing (15 min)

**Activity**
- Instructor presents four candidate topics with one-paragraph context for each:
  1. DLSS 2.0 / neural super-resolution
  2. An LLM-backed NPC dialogue system (e.g. a published or prototype system)
  3. A generative asset tool (e.g. text-to-texture in a game pipeline)
  4. A reinforcement-learning game agent (e.g. OpenAI Five, AlphaStar, or a published indie example)
- Students individually select one topic
- Students spend 5 min noting: what they already know; what they need to look up

**Student produces**
- A topic choice and a brief prior-knowledge inventory (bullet notes, not assessed)

---

### Stage 2 — Structured analysis (50 min)

**Activity**
- Students work individually using a provided scaffold with four required sections:
  1. **How it works** — mechanism, architecture, key components (≈100 words)
  2. **Classical comparison** — what technique (if any) it replaces or augments; trade-offs (≈100 words)
  3. **Limitations** — technical, practical, ethical (≈100 words)
  4. **Player-experience impact** — what changes for the player; positive and negative (≈100 words)
- Instructor circulates; prompts students to be specific and critical rather than descriptive

**Student produces**
- Draft structured evaluation (~400 words) against the four-section scaffold

**Assessment mapping**
- Directly seeds the report's critical assessment section (project deliverable, lo6)
- Practises the classical-vs-ML comparison required in the report (lo2)

---

### Stage 3 — Group discussion (40 min)

**Activity**
- Groups of three formed (mixed topics where possible)
- Each student presents their evaluation in ~3 min; group discusses for ~2 min
  - Prompts: Do you agree with the limitations identified? Would you use this technique in your project? What would change your answer?
- Final 10 min: whole-class debrief; instructor draws out two or three cross-cutting themes (e.g. the control/flexibility trade-off, the cost of inference at scale)

**Student produces**
- Participation in structured peer discussion
- Optional: one or two revision notes added to their written evaluation after hearing peers

---

### Stage 4 — Reflection and project link (15 min)

**Activity**
- Students individually write two sentences:
  1. How the technique they analysed relates to a component they plan to implement in their project
  2. One limitation they will need to address or acknowledge in their project report
- Instructor closes by explicitly linking the four scaffold sections to the project report requirements (a)–(d) from the assessment spec

**Student produces**
- Two-sentence project link note (not assessed; retained for personal use)

---

### Lab Deliverable

| Item | Format | Word count | Assessed? |
|------|--------|-----------|-----------|
| Structured written evaluation | Four-section scaffold | ~400 words | Formative only — seeds the project report reflective section |
| Group discussion participation | In-person | — | Formative only |

**Assessment mapping summary**

| Lab output | Project report section | Learning outcome |
|------------|----------------------|-----------------|
| "How it works" section | Report section (a): design and architecture | lo4 |
| "Classical comparison" section | Report section (c): classical vs ML comparison | lo2 |
| "Limitations" section | Report section (d): limitations and improvements | lo6 |
| "Player-experience impact" section | Report section (b): technique justification | lo2, lo6 |

---

## 4. References Used

- Liu, J. & Takehara, J. (2020). DLSS 2.0: Deep Learning Super Sampling. NVIDIA Developer Blog.
- Vaswani, A. et al. (2017). Attention Is All You Need. Advances in Neural Information Processing Systems, 30.
- Shaker, N., Togelius, J. & Nelson, M. J. (2016). Procedural Content Generation in Games. Springer.
- Millington, I. & Funge, J. (2009). Artificial Intelligence for Games (2nd ed.). Morgan Kaufmann.

---

## 5. Gaps — References Needed

| Gap | Where needed | Notes for author |
|-----|-------------|-----------------|
| Neural surrogate physics (cloth/fluid/destruction) | Segment 3 | A survey or industry paper on learned physics approximation in real-time systems; no approved reference covers this. |
| LLM integration in games (NPC dialogue / dynamic narrative) | Segment 4 | A published paper or practitioner report on LLM-backed NPC systems (e.g. a GDC talk, an academic paper on dialogue generation); not covered by any approved reference. |
| AI-assisted development tools (code generation, asset creation, QA agents) | Segment 5 | A practitioner or academic source on Copilot-style tools or ML-based QA in game development pipelines. |
| EU AI Act / regulatory landscape for games | Segment 6 | A primary or secondary source on AI regulation relevant to interactive entertainment. |
| Environmental cost of ML inference at scale | Segment 6 | A source quantifying energy cost of large-model inference (e.g. Strubell et al. or equivalent). |
| NeRF overview | Segment 2 | Mildenhall et al. (2020) NeRF paper would be the canonical source; not on the approved list. |