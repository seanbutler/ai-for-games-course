---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 9124b2f3052cf3d7
generated_at: 2026-06-16T14:24:16+00:00
---

# Unit 03 — Decision Making Systems for Game Agents

**One-line summary:** Build, compare, and critically evaluate the three dominant hand-authored decision-making paradigms — FSMs, behaviour trees, and utility AI — and position them against learned policies.

---

## 1. Timed Session Plan (120 minutes total)

| # | Segment | Minutes |
|---|---------|---------|
| 1 | Framing: what decision making means for a game agent | 10 |
| 2 | Finite State Machines | 25 |
| 3 | Hierarchical FSMs | 10 |
| 4 | Behaviour Trees | 35 |
| 5 | Blackboards | 10 |
| 6 | Utility AI | 15 |
| 7 | Comparative analysis and ML bridge | 15 |
| | **Total** | **120** |

---

## 2. Segment Detail

### Segment 1 — Framing: what decision making means for a game agent (10 min)

**Subtopics**
- Recap: agent loop from Unit 02 (sense → decide → act)
- Decision making as the "decide" layer: mapping perceived world state to a chosen action
- Authoring contract: designer intent vs. runtime autonomy
- Three paradigms to be covered; evaluation criteria introduced upfront (authoring cost, scalability, debuggability, predictability)

**Worked examples:** none (framing only)

**Learning outcomes served:**
- *"Model agent behaviour as a finite state machine and articulate its limitations."* [lo1, lo3] — establishes the problem context
- *"Compare FSMs, behaviour trees, and utility AI on authoring cost and scalability."* [lo2] — introduces the comparison frame

---

### Segment 2 — Finite State Machines (25 min)

**Subtopics**
- FSM definition: states, transitions, entry/exit actions, transition guards
- Implementation patterns: enum + switch, state-object / State pattern, transition table
- Trace through the guard FSM: patrol → alert → chase → search → return
- State-explosion problem: adding a second objective (e.g., "low health → retreat") and counting new transitions
- Practical limits: combinatorial growth, hidden coupling between states, testing burden

**Worked example 1 (primary):**
- *Guard FSM (patrol → alert → chase → search → return)*
  - Draw the state diagram; label every transition condition
  - Add "low health → retreat" objective; enumerate the new transitions required
  - Count: N states × M objectives ≈ O(N·M) transitions — the explosion is made concrete

**Learning outcomes served:**
- *"Model agent behaviour as a finite state machine and articulate its limitations."* [lo1, lo3]
- *"Compare FSMs, behaviour trees, and utility AI on authoring cost and scalability."* [lo2] — FSM baseline established

---

### Segment 3 — Hierarchical FSMs (10 min)

**Subtopics**
- HSM motivation: grouping states into super-states to share transitions
- Entry/exit semantics for super-states; history pseudo-states
- How HSMs reduce (but do not eliminate) transition explosion
- Remaining limitations: still requires explicit enumeration of states; difficult to reuse sub-machines across agents

**Worked example 1 (continued):**
- Refactor the guard FSM into an HSM: "combat" super-state containing chase/search; show which transitions collapse
- Identify what HSMs still cannot cleanly express (concurrent concerns, priority interrupts)

**Learning outcomes served:**
- *"Model agent behaviour as a finite state machine and articulate its limitations."* [lo1, lo3]

---

### Segment 4 — Behaviour Trees (35 min)

**Subtopics**
- Motivation: replace explicit transitions with a hierarchical control flow evaluated each tick
- Tick semantics: every node returns SUCCESS, FAILURE, or RUNNING
- Composite nodes:
  - Sequence (AND): ticks children left-to-right; fails on first child failure
  - Selector (OR): ticks children left-to-right; succeeds on first child success
  - Parallel: ticks multiple children simultaneously; configurable success/failure policy
- Leaf nodes:
  - Condition: tests world state; instant SUCCESS or FAILURE
  - Action: executes behaviour; may return RUNNING across ticks
- Decorator nodes: inverter, repeater, timeout, cooldown
- Tree structure as implicit priority: left-to-right ordering encodes fallback logic
- Reactive vs. non-reactive trees; re-evaluation of conditions
- Authoring benefits: modularity, reuse of sub-trees, no explicit transition graph

**Worked example 2 (primary):**
- *Refactor the guard as a behaviour tree*
  - Root selector: [Combat sub-tree | Patrol sub-tree]
  - Combat sub-tree (sequence): [CanSeePlayer? → ChasePlayer → AttackPlayer]
  - Patrol sub-tree (sequence): [MoveToWaypoint → Wait]
  - Add "low health → retreat" as a higher-priority selector branch — show zero new transitions required
  - Trace a full tick cycle: player visible → combat branch; player not visible → patrol branch
  - Contrast with Worked Example 1: same behaviour, structurally cleaner, no transition explosion

**Learning outcomes served:**
- *"Implement a behaviour tree with composite, decorator, and leaf nodes."* [lo1, lo3]
- *"Compare FSMs, behaviour trees, and utility AI on authoring cost and scalability."* [lo2]

---

### Segment 5 — Blackboards (10 min)

**Subtopics**
- Blackboard as a shared, keyed data store for perception and world state
- Decoupling sensors from decision logic: sensors write, BT nodes read
- Key design decisions: typed vs. untyped entries; scoping (agent-local vs. team-shared)
- Debuggability benefit: entire agent state visible in one place at runtime
- Common pitfalls: stale data, write conflicts in parallel nodes

**Worked example 2 (continued):**
- Show the guard BT's blackboard schema: `player_visible: bool`, `last_seen_position: vec3`, `health: float`
- Trace how a sensor writes `player_visible = true` and the BT's condition leaf reads it

**Learning outcomes served:**
- *"Implement a behaviour tree with composite, decorator, and leaf nodes."* [lo1, lo3] — blackboard is part of the BT implementation
- *"Compare FSMs, behaviour trees, and utility AI on authoring cost and scalability."* [lo2] — debuggability dimension

---

### Segment 6 — Utility AI (15 min)

**Subtopics**
- Motivation: discrete transitions and priority trees struggle with continuous, multi-factor trade-offs
- Core idea: score every candidate action against the current world state; execute the highest scorer
- Scoring functions: linear, exponential, logistic curves; normalisation
- Composing multiple considerations per action (product or weighted sum)
- Authoring workflow: tuning curves vs. writing transition logic
- Limitations: harder to reason about worst-case behaviour; emergent interactions between scores; debugging requires visualisation tools
- When to prefer utility AI: large action spaces, continuous resource trade-offs (e.g., RPG combat, RTS unit behaviour)

**Worked example (brief, illustrative — no new character):**
- Guard action set: {Patrol, Chase, Retreat, CallForHelp}
- Show two considerations for "Retreat": `health_curve(health)` × `enemy_proximity_curve(distance)`
- Sketch how the score changes as health drops and enemy closes — transition emerges from scoring, not an explicit rule

**Learning outcomes served:**
- *"Compare FSMs, behaviour trees, and utility AI on authoring cost and scalability."* [lo2]

---

### Segment 7 — Comparative analysis and ML bridge (15 min)

**Subtopics**
- Side-by-side comparison table: FSM / HSM / BT / Utility AI across:
  - Authoring cost (initial and maintenance)
  - Scalability to complex behaviour
  - Debuggability and predictability
  - Designer control
  - Runtime cost
- Industry context: BTs dominant in shipped titles (Halo, Unreal's built-in BT); utility AI in The Sims, Killzone
- ML bridge (forward-reference only):
  - Utility scoring ≈ value function in RL; hand-crafted curves replaced by learned Q-values
  - Imitation learning can bootstrap a BT-like policy from designer demonstrations
  - Authored trees still preferred where predictability and designer control are non-negotiable
  - Full treatment: Unit 06

**Worked examples:** none (synthesis and forward-reference)

**Learning outcomes served:**
- *"Compare FSMs, behaviour trees, and utility AI on authoring cost and scalability."* [lo2]
- *"Contrast hand-authored decision making with learned policies."* [lo2]

---

## 3. Lab Plan (120 minutes)

### Overview
Students extend the Unit 02 pathfinding agent with a behaviour tree decision layer. The lab is structured in four staged tasks; each task has a concrete deliverable that builds on the previous.

---

### Stage 1 — Inspect the node interfaces (15 min)

**What students do:**
- Read the supplied C++ base classes: `BTNode`, `BTComposite`, `BTLeaf`, `Blackboard`
- Trace the `tick()` virtual method and the `NodeStatus` enum (`SUCCESS`, `FAILURE`, `RUNNING`)
- Identify where the Unit 02 agent's perception data currently lives; plan the blackboard schema

**Produce:**
- Annotated diagram of the class hierarchy (on paper or in comments)
- Blackboard key list: at minimum `player_visible`, `last_seen_position`, `los_lost_timer`

**Assessment mapping:** Foundational understanding required before implementation; not directly marked but necessary for subsequent stages.

---

### Stage 2 — Implement leaf nodes and blackboard integration (30 min)

**What students do:**
- Implement condition leaves: `IsPlayerVisible`, `HasLOSTimedOut`
- Implement action leaves: `PatrolToNextWaypoint`, `ChasePlayer`, `GiveUp`
- Wire perception system to write `player_visible` and `last_seen_position` into the blackboard each frame
- Unit-test each leaf in isolation (stub blackboard values; verify returned status)

**Produce:**
- Compilable leaf node implementations
- Brief inline comments explaining the tick logic of each node

**Assessment mapping:** Directly supports the mandatory foundation requirement (behaviour-modelling technique); evidence for LO3.

---

### Stage 3 — Assemble the behaviour tree (40 min)

**What students do:**
- Construct the tree in code (or via the supplied builder DSL if provided):
  - Root selector → [Pursuit sub-tree | Patrol sub-tree]
  - Pursuit sub-tree (sequence): `IsPlayerVisible` → `ChasePlayer`
  - Search sub-tree (sequence): `NOT HasLOSTimedOut` → `MoveToLastKnownPosition`
  - Patrol sub-tree: `PatrolToNextWaypoint`
- Set the LOS-lost timeout via a blackboard entry (configurable, not hard-coded)
- Run the agent in the provided test scene; verify all three behavioural modes activate correctly

**Produce:**
- Working BT-driven agent that passes the three scenario checks:
  1. Agent patrols when player is absent
  2. Agent pursues when player is visible
  3. Agent searches last known position, then returns to patrol after timeout

**Assessment mapping:** Core deliverable; primary evidence for LO3 (working C++ implementation of classical algorithms in an interactive environment).

---

### Stage 4 — Written reflection (35 min)

**What students do:**
- Write approximately 300 words comparing the BT implementation to an equivalent FSM, addressing:
  - Authoring effort: how many transitions would the FSM require for the same behaviour?
  - State explosion: what happens when a new objective (e.g., "low ammo → seek cover") is added to each?
  - Debuggability: how does the blackboard help compared to inspecting FSM state variables?
- Optionally: note one limitation of the BT approach encountered during implementation

**Produce:**
- 300-word written reflection (submitted alongside code)

**Assessment mapping:**
- Directly maps to the project report requirement: *"critically compare the classical and ML/generative components on the same in-game problem"* (report criterion c)
- Evidence for LO1 (analysis of classical AI techniques) and LO2 (evaluation and comparison of approaches)

---

### Lab Marking Rubric Alignment

| Criterion | Marks (indicative) | Assessment evidence |
|-----------|-------------------|---------------------|
| Leaf nodes correct and blackboard-integrated | 30% | Code: Stage 2 |
| BT assembles and all three scenarios pass | 40% | Code: Stage 3 |
| Reflection addresses authoring effort, state explosion, debuggability | 30% | Written: Stage 4 |

---

## 4. References Used

- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.
- Buckland, M. (2005). *Programming Game AI by Example*. Wordware Publishing.
- Champandard, A. J. *Behavior Trees for Next-Gen Game AI* (AiGameDev).

---

## 5. Gaps — References Needed

- **Utility AI primary source:** No approved reference covers utility AI (The Sims / Killzone architecture, Dave Mark's work on utility theory). A practitioner source is needed to support Segment 6 — e.g., Mark, D. & Dill, K. (2012). *Improving AI Decision Modeling Through Utility Theory.* GDC Proceedings. **Author to supply or approve.**
- **HSM / Statechart formal treatment:** The approved list has no reference for hierarchical state machines (Harel statecharts). If formal treatment is required beyond the practitioner-level coverage in Millington, a source is needed — e.g., Harel, D. (1987). Statecharts: A visual formalism for complex systems. *Science of Computer Programming*, 8(3), 231–274. **Author to supply or approve.**