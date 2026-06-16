---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 3c2409ead85f56d2
generated_at: 2026-06-16T14:22:02+00:00
---

# Unit 01 — Introduction to Artificial Intelligence in Games

**One-line summary:** Orients students to the field, establishes the classical-first module arc, and grounds every subsequent technique in a concrete taxonomy of game-AI problems.

---

## Timed Session Plan — Lecture (60 min total)

| # | Segment | Duration |
|---|---------|----------|
| 1 | What Game AI Is (and Is Not) | 10 min |
| 2 | Historical Milestones | 15 min |
| 3 | Taxonomy of Techniques | 12 min |
| 4 | Worked Examples: Pac-Man Ghosts → LLM NPC | 13 min |
| 5 | Module Arc and Assessment Brief | 10 min |

---

### Segment 1 — What Game AI Is (and Is Not) (10 min)

**Subtopics**
- Game AI vs academic/research AI: different success criteria
- Bounded rationality: agents that are *good enough*, not optimal
- Believability over optimality: the player-experience contract
- Real-time constraints: CPU budgets, determinism, predictability
- Common misconceptions to dispel (e.g. "AI = machine learning")

**Worked examples:** None (framing segment; examples arrive in Segment 4)

**Learning outcomes served**
- *"Describe the historical role of AI in shaping game design and player experience."* [lo1]
- *"Distinguish between classical/hand-authored AI and modern ML-based approaches."* [lo2]

---

### Segment 2 — Historical Milestones (15 min)

**Subtopics**
- Pac-Man ghost personalities (1980): emergent behaviour from four simple rules
- *Space Invaders* and early deterministic AI patterns
- *Halo* (2001) combat AI: utility, cover, squad coordination — hand-authored but sophisticated
- STRIPS planners and goal-oriented action planning (GOAP) in *F.E.A.R.* (2005)
- AlphaGo (2016): first time deep RL surpassed human experts in a complex game
- Generative AI wave (2022–present): LLMs, diffusion models entering game pipelines
- Throughline: each era's AI reflects the hardware budget and design goals of its time

**Worked examples:** Pac-Man ghost AI (introduced here; dissected fully in Segment 4)

**Learning outcomes served**
- *"Describe the historical role of AI in shaping game design and player experience."* [lo1]
- *"Critically assess the role and impact of modern AI technologies in game development."* [lo6]

---

### Segment 3 — Taxonomy of Techniques (12 min)

**Subtopics**
- Four families:
  1. **Search & pathfinding** — A\*, NavMesh, MCTS
  2. **Decision making** — FSM, behaviour trees, utility AI, GOAP
  3. **Learning** — supervised, reinforcement, imitation learning
  4. **Generative** — PCG, neural generative models, LLM integration
- Mapping families to game-development problems (navigation, NPC behaviour, content creation, dialogue)
- Where each family sits in the module schedule (Units 01–10 preview)
- Classical vs ML axis: same problem, two solution families — the module's recurring comparison

**Worked examples:** None (taxonomy is structural; examples anchor in Segment 4)

**Learning outcomes served**
- *"Distinguish between classical/hand-authored AI and modern ML-based approaches."* [lo2]
- *"Identify which module topics map to which game-development problems."* [lo6]

---

### Segment 4 — Worked Examples: Pac-Man Ghosts → LLM NPC (13 min)

**Worked Example A — Pac-Man Ghost AI (8 min)**
- The four ghosts: Blinky (chase), Pinky (intercept), Inky (flank), Clyde (scatter)
- Each ghost = one rule; combined = emergent, varied challenge
- No ML, no search tree — pure hand-authored state logic
- Key insight: *simplicity + composition = believable complexity*
- Discussion prompt: what would break if you replaced the rules with a neural net?

**Worked Example B — LLM-Driven NPC Contrast (5 min)**
- Sketch: NPC dialogue and behaviour driven by a large language model
- What is gained: open-ended response, apparent depth, authoring flexibility
- What is lost: determinism, CPU budget predictability, designer control, testability
- Forward-reference: Units 07–08 will treat generative AI in full
- Framing payoff: establishes the classical-vs-ML comparison that recurs throughout the module

**Learning outcomes served**
- *"Describe the historical role of AI in shaping game design and player experience."* [lo1]
- *"Distinguish between classical/hand-authored AI and modern ML-based approaches."* [lo2]
- *"Critically assess the role and impact of modern AI technologies in game development."* [lo6]

---

### Segment 5 — Module Arc and Assessment Brief (10 min)

**Subtopics**
- Classical-first rationale: build intuition before adding ML complexity
- Unit-by-unit roadmap: foundations (01–03) → ML (04–06) → generative (07–08) → applied (09–10)
- Assessment overview:
  - Mandatory: pathfinding, decision system, behaviour modelling (Units 01–03)
  - Advanced learning: at least one trained/RL component (Units 04–06)
  - Advanced generative: at least one PCG/neural/LLM component (Units 07–08)
  - Report: 4 000 words; design rationale, technique comparison, critical reflection
- Advice on starting early: foundation code from labs feeds directly into the project
- Development environment: reference platform, starter repo, language expectations (C++)

**Worked examples:** None

**Learning outcomes served**
- *"Identify which module topics map to which game-development problems."* [lo6]
- *"Distinguish between classical/hand-authored AI and modern ML-based approaches."* [lo2]

---

## Lab / Tutorial Plan — 60 min

### Overview
Environment setup and codebase orientation. Students leave with a running starter environment and a concrete mental model of how game-AI code is structured.

---

### Stage 1 — Environment Setup (15 min)

**What students do**
- Clone the module starter repository
- Install dependencies (Python or C++ toolchain per platform instructions)
- Build and run the pre-built A\* demo successfully

**Deliverable at this stage:** Demo window opens and agent navigates a grid without errors.

**Common failure points to flag in lab notes**
- Path/compiler version mismatches
- Missing build tools on Windows vs Linux

---

### Stage 2 — Guided Code Exploration (25 min)

**What students do**
- Read through the starter codebase with a provided worksheet
- Identify and label three architectural layers:
  1. **Game state** — grid representation, obstacle map, agent position
  2. **Agent logic** — the A\* search, decision of next move
  3. **Rendering** — drawing the grid, path, and agent
- Locate the boundary between each layer (specific files/functions)
- Note: *where* would you add a new AI behaviour without touching the renderer?

**Deliverable at this stage:** Annotated worksheet (or brief written notes) naming the files/functions that implement each layer.

---

### Stage 3 — Reflection and Discussion (20 min)

**What students do**
- Small-group (or whole-class) discussion: how does the three-layer separation relate to the Pac-Man ghost example from the lecture?
- Written response (5–8 sentences): identify one design decision in the starter code they would change and why
- Preview: next week's lab will extend the agent logic layer with a full A\* implementation

**Deliverable at this stage:** Written identification of the three layers + one justified design observation.

---

### Combined Lab Deliverable (submitted or checked off)

> A brief written document (no length minimum; quality over quantity) that:
> 1. Confirms the environment runs (screenshot or tutor sign-off).
> 2. Names the files/classes responsible for game state, agent logic, and rendering.
> 3. States one design decision in the starter code and a reasoned alternative.

**Assessment mapping**
- This lab is formative; it is not directly marked.
- The three-layer architecture identified here is the scaffold students will extend for the mandatory foundation components (pathfinding, decision system, behaviour modelling) that constitute the assessed project's mandatory requirements.
- Habit of separating concerns established here is explicitly rewarded in the project report's design and architecture section.

---

## References Used

- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

---

## Gaps — References Needed

- **Pac-Man ghost AI primary source:** A citable primary or authoritative secondary source describing the original Pac-Man ghost behaviour rules (e.g. Toru Iwatani interviews, or Jamey Pittman's "The Pac-Man Dossier"). No entry on the approved list covers this specifically.
- **Halo combat AI:** A citable source for the *Halo* (2001) AI design (e.g. the GDC talk by Damian Isla or the *AI Game Programming Wisdom* chapter). Not present on the approved list.
- **F.E.A.R. GOAP:** A citable source for the *F.E.A.R.* GOAP system (e.g. Jeff Orkin's GDC 2006 paper "Three States and a Plan"). Not present on the approved list.