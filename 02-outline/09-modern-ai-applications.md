# Unit 08 — Modern AI Applications in Games

**One-line summary:** Survey the frontier — neural rendering enhancement, physics approximation, LLM-driven NPCs — and critically assess what each delivers and what it costs.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — Neural Rendering Enhancement (25 min)

**Subtopics**
- The rendering budget problem: ray tracing and 4K are expensive; upscaling buys resolution cheaply
- DLSS (Deep Learning Super Sampling): CNN trained to upscale low-res frames using temporal data
- Temporal anti-aliasing as a prior; motion vectors as input features
- FSR (AMD) and XeSS (Intel) — alternative approaches; brief comparison
- Denoising: neural networks for real-time ray-traced shadow/GI denoising (OIDN)
- Critical assessment: latency introduced, ghosting artefacts, input resolution trade-off

**Worked example 1:** Walk through the DLSS 2.0 inference pipeline — input features (low-res frame, motion vectors, depth), network architecture (CNN), output (upscaled frame); identify where temporal information is integrated.

**Outcomes served**
- *lo4*, *lo6*: Conceptual understanding; critically assess role of modern AI in game development

---

### Segment 2 — Physics Approximation with ML (20 min)

**Subtopics**
- The physics simulation bottleneck: rigid body, cloth, fluid, destruction — CPU cost
- Neural surrogates: train a network to predict simulation output given initial conditions
- Cloth simulation with NNs: position-based dynamics replaced by learned regression
- Fluid and smoke: CNN predicting next-frame velocity field
- Limitations: out-of-distribution failure, lack of physical guarantees, training data requirements
- Where it makes sense: background effects where exact physics is not gameplay-critical

**Outcomes served**
- *lo4*, *lo6*

---

### Segment 3 — Large Language Models in Games (35 min)

**Subtopics**
- What LLMs are: transformer decoder trained on text; next-token prediction at scale
- Capabilities relevant to games: natural language dialogue, quest generation, NPC memory, player instruction parsing
- Prompt engineering: system prompt, few-shot examples, chain-of-thought — no fine-tuning required
- Fine-tuning: adapting a base LLM to a game's lore and character voices
- Retrieval-Augmented Generation (RAG): grounding responses in a game knowledge base
- Limitations: hallucination, latency (cloud API), cost per token, lack of guaranteed consistency
- Current shipped examples: AI Dungeon, Inworld AI NPC middleware, Ubisoft NEO NPC project

**Worked example 2:** Design a prompt stack for a quest-giver NPC — system prompt (character voice, lore constraints), player utterance, response format; show how a RAG lookup injects world-state context.

**Outcomes served**
- *lo4*, *lo6*

---

### Segment 4 — AI-Assisted Game Development (20 min)

**Subtopics**
- Code generation for gameplay scripting: GitHub Copilot, model-assisted shader writing
- AI-assisted art asset creation: diffusion models for concept art, texture variation
- Automated playtesting: RL agents as stress-testers and bug finders
- Ethical considerations: authorship, labour displacement, IP/copyright in training data
- Critical framing: augmentation vs replacement; where human judgement remains essential

**Outcomes served**
- *lo6*

---

### Segment 5 — Module Synthesis and Assessment Guidance (20 min)

**Subtopics**
- Full taxonomy revisited: classical (units 01–03) → ML foundations (04–05) → agents/learning (06) → content (07) → modern applications (08)
- Assessment requirements recap: mandatory foundation + one advanced-learning + one advanced-generative
- Report structure guidance: how to frame the classical vs ML comparison section
- What markers are looking for: depth of reasoning, not breadth of techniques
- Q&A and gap-filling

**Outcomes served**
- All LOs — synthesis

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — DLSS analysis | 25 min | Read the DLSS 2.0 technical blog; annotate architecture diagram; answer three structured questions on input features and temporal integration |
| 2 — LLM NPC prompt design | 40 min | Design a prompt stack for a supplied NPC archetype (knight, merchant, villain); test via API or local model; iterate on two failure cases |
| 3 — Critical evaluation | 30 min | Table comparing three approaches (scripted dialogue, BT-driven dialogue, LLM): controllability, cost, latency, consistency |
| 4 — Write-up | 25 min | ~400-word critical assessment of the LLM approach: what it achieves, where it fails, whether you would use it in your project and why |

**Deliverable:** Annotated DLSS diagram; prompt stack with two iterated versions; comparison table; critical assessment paragraph.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| DLSS analysis answers correct and show architectural understanding | lo4, lo6 | Report — modern AI component | 20% |
| Prompt stack produces coherent, in-character NPC responses | lo6, lo5 | Advanced generative component | 30% |
| Comparison table addresses controllability, cost, latency, consistency | lo2, lo6 | Report — critical comparison | 25% |
| Critical assessment paragraph is specific, honest, and technically grounded | lo2, lo6 | Report — evaluation and reflection | 25% |

---

## References Used

**Gaps — references needed**
- Liu, J. & Takehara, J. (2020). DLSS 2.0: Deep Learning Super Sampling. NVIDIA Developer Blog — confirm on approved list.
- Vaswani, A. et al. (2017). Attention Is All You Need — transformer architecture underpinning LLMs.
- A primary source on in-game LLM integration (Inworld AI, Ubisoft NEO NPC, or similar) — not yet on approved list; flag for author to supply.
- A source on neural physics surrogates — not yet on approved list.
