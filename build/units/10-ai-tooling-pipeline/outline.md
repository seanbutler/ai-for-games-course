---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 1d3c009efa830779
generated_at: 2026-06-16T14:32:03+00:00
---

# Unit 10 — AI Tooling and Pipelines

**One-line summary:** Practical production skills for building, configuring, debugging, and validating game AI systems using industry-standard pipelines and tooling.

---

## 1. Timed Session Plan — Lecture (60 min total)

| # | Segment | Minutes |
|---|---------|---------|
| 1 | Navigation Mesh Pipelines | 18 |
| 2 | Blackboard Architecture and Perception Pipelines | 14 |
| 3 | Visual Authoring Tools for BT and FSM | 10 |
| 4 | Data-Driven AI Configuration | 8 |
| 5 | AI Debugging, Visualisation, and Testing | 10 |

---

## 2. Segment Detail

---

### Segment 1 — Navigation Mesh Pipelines (18 min)

**Subtopics:**
- What a NavMesh is and why it supersedes waypoint graphs at production scale
- Recast/Detour pipeline: voxelisation → region segmentation → polygon mesh → Detour runtime
- Key bake parameters: agent radius, agent height, max slope, step height, cell size; how each affects traversable surface
- Tile-based incremental updates: when and why to rebake at runtime (destructible geometry, doors, dynamic obstacles)
- Off-mesh links: jump connections, ladders, teleporters — authored vs auto-generated
- Dynamic obstacle avoidance: RVO/ORCA principles; local vs global navigation separation
- NavMesh in Unreal Engine and Unity: editor exposure of Recast parameters, runtime API surface

**Worked example:**
- *Unreal Engine NavMesh bake pipeline walk-through:* compare parameter sets for a platformer (tight agent radius, high step height, small cell size) vs an open-world RPG (larger cell size, tile streaming, runtime tile invalidation on geometry change); trace the sequence of events that triggers a tile rebake

**Learning outcomes served:**
- *"Describe the asset pipeline for navigation data and explain how NavMesh generation parameters affect agent behaviour. [lo1, lo3]"*

---

### Segment 2 — Blackboard Architecture and Perception Pipelines (14 min)

**Subtopics:**
- Motivation: why a monolithic NPC update function breaks down at scale
- Blackboard as shared agent knowledge store: typed keys, read/write access patterns, lifetime of entries
- Reader/writer separation: sensors write, reasoners read, actuators consume — decoupling benefits
- Perception pipeline: sight cone query (dot-product + range check), hearing range query, sensory event queue, filtering (line-of-sight raycasts, occlusion)
- Connecting world state to decisions: how BT service nodes poll the blackboard; event-driven vs polling update models
- Comparison: blackboard vs direct sensing (coupling, testability, replay)

**Worked example:**
- *Refactor a monolithic NPC update function:* show the before (single function reading world state, running logic, issuing movement commands) and the after (perception component writes to blackboard; BT service reads blackboard; decorator gates action nodes); annotate what moved where and why each boundary exists

**Learning outcomes served:**
- *"Implement a blackboard system and explain how it decouples sensing, reasoning, and action in a production AI architecture. [lo3]"*

---

### Segment 3 — Visual Authoring Tools for BT and FSM (10 min)

**Subtopics:**
- Unreal Engine Behaviour Tree editor: node graph, task/service/decorator separation, blackboard key binding in the editor
- Unity Animator as FSM authoring tool: states, transitions, conditions, blend trees; limitations for complex game logic
- Third-party node-graph tools: general pattern, designer-facing affordances
- Trade-offs for team workflows:
  - Programmer vs designer ownership of logic
  - Version-control friction (binary vs text asset formats)
  - Debugging support (live node highlighting, breakpoints)
  - Scalability: when visual tools become unwieldy (deep nesting, large graphs)
- Forward reference: same visual paradigm reappears in ML training dashboards and agent policy inspection tools

**Worked example:** *(integrated into segment — no standalone example; uses Unreal BT editor screenshots/live demo as illustration)*

**Learning outcomes served:**
- *"Evaluate visual authoring tools for behaviour trees and finite state machines and assess their trade-offs for team workflows. [lo2, lo3]"*

---

### Segment 4 — Data-Driven AI Configuration (8 min)

**Subtopics:**
- Motivation: separating tunable parameters from compiled code; designer iteration without programmer involvement
- Externalisation patterns: JSON/YAML config files, Unreal DataTables, Unity ScriptableObjects
- Hot-reload workflow: file-watcher → reload callback → agent re-initialisation without restart
- What to externalise: perception radii, patrol waypoint lists, reaction times, BT task parameters
- Risks and discipline: schema validation, default fallbacks, version-controlled data files
- ML bridge note: same pattern applies to hyperparameter files and training configuration — forward reference to Units 04–06

**Worked example:** *(feeds directly into tutorial — students implement this pattern; no separate lecture example)*

**Learning outcomes served:**
- *"Apply AI debugging and visualisation techniques to identify and fix incorrect agent behaviour. [lo3]"* (enabling context)
- *"Describe the asset pipeline for navigation data and explain how NavMesh generation parameters affect agent behaviour. [lo1, lo3]"* (data-driven parameter management as part of the asset pipeline)

---

### Segment 5 — AI Debugging, Visualisation, and Testing (10 min)

**Subtopics:**
- In-game debug overlays: path corridor rendering, perception radii, active BT node highlight, current FSM state label, blackboard value display
- Logging strategies: structured per-agent event logs, timestamped state transitions, decision rationale traces
- Replay tools: recording agent state streams for post-mortem analysis
- Scripted scenario tests: deterministic seed + scripted stimulus → assert expected state transition or path
- Automated regression: catching behaviour regressions when BT or parameter changes are made
- Stress-testing: high agent counts, frame-budget profiling, LOD strategies for AI update rate
- Connecting to assessment: debug evidence (screenshots, logs) as report artefacts

**Worked example:** *(feeds directly into tutorial — broken NPC diagnosis; no separate lecture example)*

**Learning outcomes served:**
- *"Apply AI debugging and visualisation techniques to identify and fix incorrect agent behaviour. [lo3]"*

---

## 3. Lab Plan — Tutorial (60 min total)

**Brief:** Students receive a pre-built project containing a broken NPC. Three faults are seeded: incorrect patrol (wrong waypoint order), stuck pathfinding (NavMesh parameter mismatch causing agent to fail to reach a destination), and wrong state transitions (FSM guard condition logic error). A second task requires externalising parameters to a data file with hot-reload.

---

### Stage 1 — Fault Diagnosis (25 min)

| Step | Activity | Student Produces |
|------|----------|-----------------|
| 1a | Enable debug overlays (path corridor, FSM state label, perception radius) and observe each fault in motion | Annotated screenshots or notes identifying visible symptoms |
| 1b | Read structured log output; correlate log events to observed behaviour | Identification of which log entries correspond to each fault |
| 1c | Trace each fault to root cause: NavMesh parameter, waypoint array index, FSM condition expression | Fault log entries (part of written deliverable) |

---

### Stage 2 — Fault Repair (20 min)

| Step | Activity | Student Produces |
|------|----------|-----------------|
| 2a | Fix NavMesh bake parameter causing stuck pathfinding; rebake and verify path corridor overlay | Corrected NavMesh config / editor parameter change |
| 2b | Fix waypoint order bug in patrol logic | Corrected source code |
| 2c | Fix FSM guard condition logic error | Corrected source code |

---

### Stage 3 — Data-Driven Externalisation (15 min)

| Step | Activity | Student Produces |
|------|----------|-----------------|
| 3a | Identify three agent parameters suitable for externalisation (e.g. patrol speed, perception radius, reaction delay) | Selection with brief justification |
| 3b | Move parameters to a JSON or YAML config file; implement or wire up the provided hot-reload callback | Modified source code + config file |
| 3c | Demonstrate hot-reload: change a value in the file at runtime and observe the agent update without restart | Working demo (verified by tutor or captured in deliverable) |

---

### Deliverable

- **Fixed NPC source code** with three parameters externalised to a data file (submitted to module repository)
- **Fault log** (~150 words): for each of the three bugs — name of the fault, root cause as revealed by the debug tooling, and the fix applied

---

### Assessment Mapping

| Deliverable component | Maps to assessment requirement | Outcome evidence |
|-----------------------|-------------------------------|-----------------|
| Fixed pathfinding (NavMesh parameter) | Foundation: pathfinding technique (Units 01–03 mandatory) | lo3 — working classical algorithm in interactive environment |
| Fixed FSM transitions | Foundation: decision system (Units 01–03 mandatory) | lo1, lo3 — analysis and implementation of classical AI |
| Externalised config + hot-reload | Applied context: design and architecture documentation | lo2 — justifying technique choices; lo6 — toolchain trade-offs |
| Fault log | Report evidence: debug methodology, root-cause reasoning | lo1, lo2 — critical analysis; supports report sections (a) and (d) |

*This tutorial directly exercises the skills students need to document their project's AI architecture and debugging process in the 4000-word report.*

---

## 4. References Used

- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.
- Buckland, M. (2005). *Programming Game AI by Example*. Wordware Publishing.
- Champandard, A. J. *Behavior Trees for Next-Gen Game AI* (AiGameDev).
- Monkkonen, M. *Recast Navigation* (open source). github.com/recastnavigation/recastnavigation.

---

## 5. Gaps — References Needed

- **RVO/ORCA dynamic obstacle avoidance:** A primary or survey source for Reciprocal Velocity Obstacles (van den Berg et al.) and ORCA is needed for Segment 1. Not present in the approved reference list.
- **Unreal Engine NavMesh / Behaviour Tree documentation:** Official Epic Games documentation or a citable Unreal Engine source for the editor pipeline walk-through. Not present in the approved reference list.
- **Unity Animator / state machine authoring:** Official Unity documentation or a citable practitioner source. Not present in the approved reference list.
- **Hot-reload / data-driven game configuration patterns:** A practitioner or academic source covering externalised configuration and live-reload workflows in game engines. Not present in the approved reference list.
- **AI testing and automated regression in games:** A source covering scripted scenario testing or behaviour regression testing for game agents. Not present in the approved reference list.