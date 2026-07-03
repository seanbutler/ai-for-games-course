# Unit 01 — Introduction to Artificial Intelligence in Games

**One-line summary:** Orient students to what game AI is, where it came from, and how the module is structured — classical foundations first, modern ML second.

---

## Lecture Session Plan — 60 minutes

### Segment 1 — What Game AI Is (and Is Not) (15 min)

**Subtopics**
- General AI vs game AI: optimality vs believability, computational budget constraints
- Bounded rationality: good enough, fast enough, debuggable enough
- The role of AI in a real-time game loop (alongside rendering, physics, audio)

**Outcomes served**
- *lo1*: Critically analyse the principles and techniques used in traditional game AI

---

### Segment 2 — Historical Milestones (20 min)

**Subtopics**
- Pac-Man ghosts (1980): four simple finite state rules producing emergent challenge
- Super Mario 64 (1996): FSM-driven enemies with spatial detection — step toward 3D agent AI
- Quake bots (1996): navigation meshes and reactive AI
- Halo (2001): squad-level combat AI and cover systems
- AlphaGo (2016): deep RL defeating world champion — shift from hand-authored to learned
- Modern generative AI in games: NPC dialogue, procedural content, DLSS

**Worked example 1:** Dissect the Pac-Man ghost AI — map each ghost's rule to its perceived personality (Blinky chases, Pinky ambushes, Inky flanks, Clyde retreats); show how emergence arises from four independent deterministic rules with no communication between ghosts and no ML.

**Worked example 2:** Dissect the Super Mario 64 enemy AI — enemies use simple FSMs with radius-based detection and facing-direction checks. Reference: [The AI of Super Mario 64 | AI and Games #64](https://www.youtube.com/watch?v=3fmVyXBr1Z8) (Dr Tommy Thompson):
- Goomba: idle patrol state → on Mario entering detection radius, switch to chase; lose Mario if he exits a larger radius; no memory of where Mario went
- Boo: tracks Mario's facing direction via dot product; moves toward Mario when dot product < 0 (back turned); freezes and recoils when dot product > 0 (Mario looking at it) — a perception-gated FSM with one condition
- Chain Chomp: rotates around stake anchor; lunges toward Mario if he enters lunge radius; returns to orbit — FSM with spatial constraint
- Bob-omb: patrol → charge toward Mario on detection → explode after timeout
- Key observations: each enemy has 2–4 states; detection uses distance and angle checks (range sphere + dot product); no pathfinding — movement is direct or scripted; show how this is a step up in sophistication from Pac-Man's flat rules

**Outcomes served**
- *lo1*: Critically analyse principles of traditional game AI
- *lo6*: Critically assess the role of modern AI in game development

---

### Segment 3 — Taxonomy and Module Arc (15 min)

**Subtopics**
- Taxonomy: search/pathfinding → perception/collision → decision making → learning → generative
- The two-theme structure: classical hand-authored techniques (Units 01–04) vs modern ML (Units 05–08)
- Why classical-first: determinism, debuggability, production dominance; ML builds on the same problems
- Assessment walkthrough: what the project requires, how the report evidences learning outcomes

**Outcomes served**
- *lo2*: Evaluate and compare different AI approaches; justify suitability
- *lo6*: Critically assess role of modern AI in game development

---

### Segment 4 — Environment Setup (10 min)

**Subtopics**
- Module starter codebase: structure overview (game state / agent logic / rendering layers)
- Build system and toolchain
- Where to find lab starters for each unit

**Outcomes served**
- *lo3*: Design and implement classical game AI algorithms (prerequisite setup)

---

## Lab Plan — 60 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — Build and run | 20 min | Starter project compiling and running; identify the three code layers (state, agent, render) |
| 2 — Enemy AI dissection | 25 min | Read supplied implementations of a Mario 64-style Boo (dot-product perception gate) and a Pac-Man ghost; annotate each state and condition in comments; identify what world state each reads |
| 3 — Written reflection | 15 min | One paragraph: the Boo uses a single dot-product check yet feels intelligent — why? What would you need to change to make it less exploitable, and would that be classical or ML? |

**Deliverable:** Running starter environment; annotated enemy code (Boo + ghost); one-paragraph reflection.

**Marking rubric**

| Task | LO | Marks |
|---|---|---|
| Starter project runs without modification | lo3 | 30% |
| Boo states and dot-product condition correctly identified and annotated | lo1 | 40% |
| Reflection distinguishes classical from ML approach | lo2 | 30% |

---

## References Used

**Gaps — references needed**
- A primary source on Pac-Man ghost AI (Iwatani / original design documentation) is not on the approved list — flag for author to supply or cite as common knowledge.
- Millington, I. & Funge, J. *Artificial Intelligence for Games* (2nd ed.) would cover the historical framing — confirm it is on the approved list before citing.
