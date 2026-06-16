---
generated_by: generate.py
stage: brief
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: bea3798bb9c9a08b
generated_at: 2026-06-16T19:33:24+00:00
---

# WM9SL-15 — AI and Games
## Game AI Implementation Project

| | |
|---|---|
| **Module** | WM9SL-15 — AI and Games |
| **Assessment title** | Game AI Implementation Project |
| **Weight** | 100% |
| **Word limit** | 4,000 words (±10%; references and figure captions excluded) |
| **Submission format** | Code archive + PDF report via Tabula |
| **Deadline** | End of Week 4 (exact date confirmed on Tabula) |

---

## Overview

This project asks you to design, build, and document a working, interactive game AI system in C++. You will implement classical AI techniques — pathfinding, decision-making, and behaviour modelling — alongside at least one machine-learning component, one generative or modern AI component, and one piece of architectural or pipeline work that makes the system viable at scale. The accompanying technical report is where you make your reasoning visible: explaining design choices, grounding them in module theory and literature, and critically comparing the approaches you used. Together, the code and report are designed to demonstrate that you can both build game AI and think rigorously about it.

---

## Deliverables

### Code

Submit a working, interactive game AI system written in C++. The codebase must build from source using the provided configuration and **must run without modification on the module reference platform**. If you deviate from the default build setup, include a README describing the steps required. The system must demonstrate all required techniques (see Requirements below).

### Report

Submit a PDF of no more than 4,000 words (±10%; references and figure captions are excluded from the count). The report must cover the following sections in order.

#### Introduction

State the game context you chose and why. Identify the AI problems your project addresses and give a one-paragraph roadmap of the report.

#### Classical AI Components

Explain the design and implementation of your foundation techniques (sensing, pathfinding, decision system, behaviour modelling). Justify your algorithmic choices with reference to module theory and relevant literature. Include complexity, speed, and size analysis where it informs your choice.

#### Machine Learning Component

Describe the ML technique you implemented, how it was trained, and how it integrates with the rest of the system. Compare its behaviour and trade-offs against the classical equivalent on the same in-game problem where applicable.

#### Generative / Modern AI Component

Describe the generative technique you implemented (PCG, neural generative model, or LLM integration). Critically assess its impact on gameplay or content quality and discuss limitations.

#### AI at Scale and Architecture / Pipeline

Describe the architectural or pipeline work you undertook to make your AI system viable at scale or maintainable in production. This may cover one or more of: large-scale agent management (spatial indexing, LOD AI, crowds); a per-frame AI budget or time-sliced update scheduler; a data-driven authoring pipeline with external config or hot-reload; NavMesh generation and dynamic maintenance; or async / job-based offloading of expensive queries. Explain the design decisions you made, the performance impact you measured or estimated, and how this work integrates with the rest of the system. Where relevant, reference the constraints of real-time interactive software and compare your approach against simpler alternatives you considered.

#### Evaluation and Reflection

Reflect on the overall system: what works, what doesn't, and why. Discuss limitations honestly and suggest concrete improvements. Compare your choices against alternatives you considered but did not implement.

#### Conclusion

Summarise the contributions of the project. One paragraph is usually enough; do not introduce new material here.

---

## Requirements

### Foundation — all required

These techniques must be present in every submission. They draw on Units 01–03.

- Inputs: Sensing, Ranges, Volumetric Collisions, Rays, Visual Cones
- Outputs: Movement, Actions
- Pathfinding algorithm (A* recommended; alternatives must be justified)
- Decision system (FSM or behaviour tree)
- At least one behaviour-modelling technique (steering, GOAP, utility AI, etc.)

### Advanced: Learning — choose at least one

Drawn from Units 04–06.

- Trained neural network applied to a meaningful in-game problem
- Reinforcement-learning agent
- Imitation-learning component

### Advanced: Generative — choose at least one

Drawn from Units 07–08.

- Procedural content generation (grammar-based, search-based, or noise-based)
- Neural generative model (VAE, GAN, diffusion) applied to game content
- LLM-driven component integrated into gameplay

### Advanced: Scale and Pipeline — choose at least one

Drawn from Units 09–10.

- Large-scale agent management: spatial indexing, LOD AI, or crowd simulation handling hundreds of agents at interactive frame rates
- AI performance budgeting system: time-sliced or prioritised update scheduling that keeps AI cost within a fixed per-frame budget
- Data-driven AI pipeline: external behaviour authoring (e.g. behaviour tree editor, data tables) with hot-reload or build-time validation
- NavMesh generation and maintenance pipeline, including dynamic obstacle handling or incremental re-bake
- Async / job-based AI computation: offloading sensing, pathfinding, or decision queries to worker threads with correct synchronisation

---

## Marking Scheme

| Criterion | Weight | High | Mid | Low |
|---|---|---|---|---|
| **Implementation quality** | 35% | All required techniques implemented correctly; code is clean, modular, and runs reliably. | Foundation techniques present and functional; advanced components partially working. | Missing required techniques or code does not run. |
| **Technical understanding (report)** | 30% | Report demonstrates deep understanding of every component; design decisions are well-reasoned and grounded in theory. | Adequate explanation of most components; some reasoning is superficial or unsupported. | Report is largely descriptive; little evidence of understanding why choices were made. |
| **Critical comparison** | 20% | Classical and ML/generative approaches compared rigorously on the same problem; trade-offs quantified or otherwise evidenced. | Some comparison present but limited to qualitative observations. | No meaningful comparison between approaches. |
| **Reflection and evaluation** | 15% | Honest, specific reflection on limitations; concrete and technically credible improvements proposed. | Reflection present but vague; improvements are generic. | Little or no reflection; limitations not acknowledged. |

---

## Notes

The report is the primary evidence markers use to assess your learning. Submitting working code is necessary but not sufficient: the report must make your reasoning visible — why you chose each technique, how the components relate to one another, and what you would do differently. A system that runs but is poorly explained will score poorly on the three report-based criteria, which together account for 65% of the mark. Finally, the reference platform constraint is firm: code that does not run on the module reference platform without modification cannot be assessed for implementation quality.