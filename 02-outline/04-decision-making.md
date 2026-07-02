# Unit 03 — Decision Making Systems for Game Agents

**One-line summary:** Progress from finite state machines through behaviour trees to utility AI, understanding what each buys you and what it costs.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — Finite State Machines (20 min)

**Subtopics**
- States, transitions, entry/exit actions
- Implementation patterns: enum switch, state objects, transition tables
- The state-explosion problem: guard with two objectives demonstrates combinatorial blowup

**Worked example 1:** Design an FSM for a guard (patrol → alert → chase → search → return); trace the transition explosion when a second objective (low health → retreat) is added. Count states and transitions before and after.

**Outcomes served**
- *lo1*: Critically analyse decision systems in traditional game AI
- *lo3*: Design and implement classical game AI algorithms

---

### Segment 2 — Hierarchical FSMs (15 min)

**Subtopics**
- Motivation: flat FSM transition count grows as O(n²); nesting reduces this by grouping related states under a parent
- HSM mechanics: substates inherit parent transitions; entry/exit actions at each level; history states (resume last substate on re-entry)
- UML statechart notation: nested state diagrams, default entry points, history pseudo-states
- Example: refactor the guard FSM — Combat superstate contains chase/attack/retreat; any transition to flee fires from the superstate level, not duplicated on every substate
- Limitation: HSMs still require hand-authored transitions; deep nesting becomes hard to read and debug
- HSMs as a stepping stone: hierarchy is the right idea, but encoding it as nested transitions is still brittle — sets up the motivation for behaviour trees

**Worked example 2:** Refactor the guard FSM from Segment 1 into an HSM — show the Combat superstate grouping chase/attack/retreat; count how many transitions are eliminated; identify where the remaining complexity lives.

**Outcomes served**
- *lo1*, *lo2*: Analyse and compare decision system approaches

---

### Segment 3 — Behaviour Trees (35 min)

**Subtopics**
- Motivation: HSMs showed hierarchy helps, but transitions are still hand-coded; BTs encode priority and sequence structurally
- Tick semantics: every node returns SUCCESS, FAILURE, or RUNNING
- Composite nodes: Sequence (AND), Selector (OR), Parallel
- Decorator nodes: Inverter, Repeater, Limiter, Timeout
- Leaf nodes: Condition (query world state), Action (do something)
- Blackboards: shared read/write store for perception and world state — decouples sensing from decision logic
- Execution model: tick from root each frame; stateless vs stateful nodes

**Worked example 3:** Refactor the guard HSM from Segment 2 as a behaviour tree — show how Sequence and Selector nodes replace hand-coded transitions entirely; compare node count and authoring effort across all three representations (flat FSM → HSM → BT).

**Outcomes served**
- *lo1*, *lo3*

---

### Segment 4 — Utility AI (20 min)

**Subtopics**
- Motivation: discrete transitions poor fit for continuous trade-offs (how hungry? how threatened?)
- Scoring candidate actions: utility function per action, normalisation, selection
- Response curves: linear, exponential, logistic — tuning agent personality
- Multi-attribute utility: weighted sum of sub-scores
- Cost: harder to author and debug than BTs; not guaranteed predictable priority order

**Outcomes served**
- *lo1*, *lo2*: Evaluate and compare approaches

---

### Segment 5 — Planning: STRIPS and GOAP (20 min)

**Subtopics**
- Motivation: BTs and Utility AI still require the designer to specify structure or scores; planning asks only "what actions exist and what do they require/produce?" — the sequence is computed at runtime
- STRIPS representation: world state as a set of boolean predicates; actions defined by preconditions and effects
- Forward search planning: start state → apply valid actions → goal state; A* over the plan-space
- GOAP (Goal-Oriented Action Planning): Jeff Orkin's game-practical formulation used in F.E.A.R. (2005); action costs enable least-cost plan selection; actions expose preconditions and effects to the planner at runtime
- F.E.A.R. example: squad AI selects cover, suppression, flanking actions dynamically — designer writes actions, not sequences
- Limitations: planning is expensive; state space must be kept small; replanning on world change is costly; debugging "why did the agent choose that plan?" is hard
- When to use: rich action spaces where sequence cannot be pre-authored; emergent behaviour is desirable and acceptable latency exists

**Worked example 4:** Define a small GOAP world for a guard — predicates: `playerVisible`, `inCover`, `hasAmmo`; actions: `takeCover` (pre: ~inCover, post: inCover), `shoot` (pre: playerVisible ∧ hasAmmo), `reload` (pre: ~hasAmmo, post: hasAmmo), `flank` (pre: inCover ∧ playerVisible); show the planner finding the least-cost plan to reach goal `~playerVisible` from two different start states.

**Outcomes served**
- *lo1*, *lo2*: Analyse and compare decision system approaches

---

### Segment 6 — Comparison and Selection Guide (15 min)

**Subtopics**
- FSM: few-state agents; fast, predictable, hard to scale
- HSM: reduces transition count; still hand-coded structure
- BT: hierarchical, reusable, dominant in shipped AAA titles; good tooling
- Utility AI: continuous trade-offs; emergent feel; used in The Sims, Halo
- GOAP/Planning: rich emergent behaviour; runtime sequence computation; used in F.E.A.R., Tomb Raider (2013)
- Selection guide: state count, authoring cost, debuggability, designer control requirements
- Authoring and runtime visualisation requirements for each

**Outcomes served**
- *lo2*: Evaluate and compare approaches; justify suitability

---

### ML Bridge (25 min)

**Subtopics**
- STRIPS/GOAP → model-based RL: classical planning uses an explicit world model; model-based RL learns that model from experience
- Utility AI → learned value functions in RL: scoring functions become Q-values
- Hierarchical RL: learned sub-goals mirror the HSM/BT hierarchy
- LLM-driven planning: language models as planners — generate action sequences in natural language, ground to game actions
- Why authored systems still dominate shipped titles: control, predictability, no training data, interpretable failure
- Forward reference to Unit 07 (AI Agents and Learning)

**Outcomes served**
- *lo2*, *lo6*

**Outcomes served**
- *lo2*, *lo6*

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — FSM guard | 25 min | Working FSM for patrol/alert/chase/search/return using supplied state-machine base class |
| 2 — BT refactor | 50 min | Same guard behaviour reimplemented as a behaviour tree using supplied node interfaces; blackboard for perception state |
| 3 — Reflection | 20 min | ~300-word written comparison of FSM vs BT: authoring effort, state explosion, debuggability |
| 4 — Extension (if time) | 25 min | Add a second agent objective (low health → retreat) to both implementations; compare effort |

**Deliverable:** Working FSM and BT implementations; written reflection.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| FSM guard correct (all transitions functional) | lo1, lo3 | Foundation — decision system | 25% |
| BT guard correct (blackboard used for perception) | lo1, lo3 | Foundation — decision system | 35% |
| Written reflection addresses authoring effort and state explosion | lo2 | Report — design justification | 25% |
| Extension: second objective added to both | lo3 | Foundation — behaviour modelling | 15% |

---

## References Used

**Gaps — references needed**
- Millington, I. & Funge, J. *Artificial Intelligence for Games* (2nd ed.) — FSM and BT chapters.
- Buckland, M. *Programming Game AI by Example* — FSM implementation in C++.
- Champandard, A. J. *Behavior Trees for Next-Gen Game AI* (AiGameDev) — BT authoring rationale.
