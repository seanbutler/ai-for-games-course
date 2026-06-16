---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 8022e93b9e3b31a9
generated_at: 2026-06-16T14:31:04+00:00
---

# Unit 09 — AI at Scale: Crowds, Economies, and Level of Detail

**One-line summary:** Techniques for maintaining interactive performance and coherent behaviour when a game world contains hundreds to thousands of AI agents simultaneously.

---

## 1. Timed Session Plan (Lecture — 60 minutes total)

| # | Segment | Minutes |
|---|---------|---------|
| 1 | The Scaling Problem | 8 |
| 2 | AI Level of Detail (LOD) | 14 |
| 3 | Crowd Simulation and Flow Fields | 14 |
| 4 | Group, Squad, and Hierarchical AI | 12 |
| 5 | Influence Maps and Agent-Based Economies | 8 |
| 6 | Spatial Partitioning and Performance Budgeting | 4 |

**Total: 60 minutes**

---

## 2. Segment Detail

---

### Segment 1 — The Scaling Problem (8 min)

**Subtopics**
- Why per-agent full simulation breaks down: O(n) update cost, O(n²) perception queries
- Concrete numbers: frame-time budget at 60 fps (≈16 ms), realistic agent counts in shipped titles
- The design contract: players cannot perceive every agent simultaneously — exploit this
- Forward map to the rest of the lecture: LOD → crowds → hierarchy → economies → spatial structures

**Worked examples used**
- None (motivating framing only); numbers drawn from the flow-field vs A* example introduced in Segment 3

**Learning outcomes served**
- *"Apply level-of-detail strategies to AI update scheduling to maintain performance under large agent counts."* [lo1, lo3]
- *"Describe crowd and flow-field techniques and explain when they outperform per-agent pathfinding."* [lo1, lo2]

---

### Segment 2 — AI Level of Detail (LOD) (14 min)

**Subtopics**
- Three-tier LOD model: full simulation / abstract simulation / dormant
  - Full: pathfinding, perception, decision tree/BT running every frame
  - Abstract: statistical state updates, scripted schedules, no spatial queries
  - Dormant: agent exists in data only; no update cost
- Transition triggers: distance-based, importance-based (quest relevance, faction significance), visibility
- Time-slicing: spreading full-simulation agents across multiple frames; priority queues for update scheduling
- Re-hydration: reconstructing plausible concrete state (position, inventory, health) from abstract state when player approaches
- Fixed per-frame AI time budget: early-exit when budget exhausted, deferring lower-priority agents

**Worked examples used**
- **City LOD scheme (10 000 citizens):** specify each tier's simulation fidelity, transition triggers, and re-hydration logic — introduced here, worked through in full

**Learning outcomes served**
- *"Apply level-of-detail strategies to AI update scheduling to maintain performance under large agent counts."* [lo1, lo3]

---

### Segment 3 — Crowd Simulation and Flow Fields (14 min)

**Subtopics**
- Reynolds boids: three rules (separation, alignment, cohesion); emergent flocking from local rules; cost per agent
- Limitations of boids for directed navigation: no global goal awareness
- Flow fields: precompute a vector-per-cell directing agents toward a goal; all agents sample the same field
  - Construction: Dijkstra/BFS from goal outward; cost layer integration
  - Runtime: O(1) per agent per frame for steering; O(map cells) precomputation
  - Invalidation and incremental update on dynamic obstacles
- Continuum crowd models: density-based flow; brief conceptual description only
- Hybrid approach: flow field for global routing, local boids-style rules for separation and collision avoidance
- When flow fields win vs per-agent A*: many agents, shared destination, static or slowly changing maps

**Worked examples used**
- **Per-agent A* vs flow field for 500 RTS units:** implementation cost, runtime cost, path quality — worked through in full here

**Learning outcomes served**
- *"Describe crowd and flow-field techniques and explain when they outperform per-agent pathfinding."* [lo1, lo2]

---

### Segment 4 — Group, Squad, and Hierarchical AI (12 min)

**Subtopics**
- Separating group intent from individual execution: the squad as a first-class entity
- Formation movement: slot assignment, maintaining formation under pathfinding, re-slotting on member loss
- Coordinated flanking: squad-level goal decomposition → individual waypoint assignment
- Three-level hierarchy:
  - Individual agent: perception, local steering, animation state
  - Squad AI: formation, fire-and-move, target prioritisation
  - Commander / faction AI: resource allocation, objective selection, strategic timing
- Time granularity per level: individual updates every frame; squad every N frames; faction every M seconds
- Communication patterns: blackboard, direct message, shared influence map

**Worked examples used**
- None dedicated; formation and flanking illustrated with brief diagrammatic walkthrough (inline)

**Learning outcomes served**
- *"Design a hierarchical AI architecture that coordinates individual agents, squads, and faction-level reasoning."* [lo2, lo3]

---

### Segment 5 — Influence Maps and Agent-Based Economies (8 min)

**Subtopics**

**Influence maps**
- Encoding faction presence, threat level, and resource value as scalar fields over the map
- Propagation: simple diffusion / falloff from source cells
- Tactical queries: "find weakest enemy zone", "identify safe retreat corridor", "locate contested resource"
- Update frequency: full rebuild vs incremental; decoupled from agent update rate

**Agent-based economic simulation**
- Agents as economic actors: needs, roles, resource production and consumption
- Supply/demand emergence: price signals from scarcity without explicit market code
- Role assignment and resource routing: agents self-select tasks based on local utility
- Case studies: Dwarf Fortress (job queue + need satisfaction), RimWorld (colonist mood + work priorities), Mount & Blade (village prosperity model)
- Trade-offs: emergent richness vs authorial control; debugging opacity; scale limits

**Worked examples used**
- None dedicated; Dwarf Fortress / RimWorld used as brief illustrative cases (inline)

**Learning outcomes served**
- *"Evaluate agent-based economic simulation techniques used in games and assess their trade-offs for scale and authorial control."* [lo2, lo6]
- *"Design a hierarchical AI architecture that coordinates individual agents, squads, and faction-level reasoning."* [lo2, lo3] (influence maps as the shared data layer)

---

### Segment 6 — Spatial Partitioning and Performance Budgeting (4 min)

**Subtopics**
- Why naive neighbour lookup is O(n²): perception radius queries, collision checks
- Spatial structures for AI: uniform grid (fast insert/query, fixed cell size), quadtree (adaptive density), k-d tree (arbitrary dimensions)
- Choosing a structure: agent density, world size, update frequency of positions
- Performance budgeting summary:
  - Fixed frame-time budget → priority queue → early exit
  - Amortisation: spread expensive queries across frames
  - Profiling checkpoints: the tutorial task as a live example

**Worked examples used**
- Tutorial scenario (1 000 agents, LOD scheduler + flow field) referenced as the concrete application of these structures

**Learning outcomes served**
- *"Apply level-of-detail strategies to AI update scheduling to maintain performance under large agent counts."* [lo1, lo3]

---

## 3. Lab / Tutorial Plan (60 minutes)

**Brief:** Students extend the single working agent from the Unit 02 tutorial to handle 1 000 instances. Two interventions are required: (1) an LOD scheduler, and (2) replacement of per-agent A* calls with a shared flow field.

---

### Stage 1 — Baseline Profiling (10 min)

**What students do**
- Run the provided single-agent starter at 100, 500, and 1 000 instances with no modifications
- Record frame time and CPU time attributed to pathfinding using the supplied profiling hook

**What they produce**
- A baseline table: agent count → frame time (ms) → pathfinding share (%)

**Assessment mapping**
- Establishes the "before" evidence required by the profiling note deliverable

---

### Stage 2 — Implement the LOD Scheduler (20 min)

**What students do**
- Classify agents into three tiers based on distance from the camera/player position
- Full tier: run A* and decision update every frame
- Abstract tier: skip pathfinding; continue on last known heading; update every N frames
- Dormant tier: no update; position frozen
- Implement a fixed per-frame budget cap with a priority queue (full > abstract > dormant)

**What they produce**
- `LODScheduler` class (or equivalent) integrated into the agent update loop
- Frame-time reading at 100, 500, 1 000 agents post-LOD

**Assessment mapping**
- Directly exercises lo3 (implement classical AI algorithm in interactive environment)
- Provides evidence for report section on performance trade-offs (lo1, lo2)

---

### Stage 3 — Replace Per-Agent A* with a Shared Flow Field (20 min)

**What students do**
- Implement a BFS-based flow field from a single goal cell across the grid
- Replace per-agent `FindPath()` calls with a single `SampleFlowField(position)` lookup
- Combine flow-field steering with a simple separation force (boids separation rule only)

**What they produce**
- `FlowField` class with `Build(goal)` and `Query(cell) → direction` interface
- Updated agent steering that uses the flow field for full-tier and abstract-tier agents

**Assessment mapping**
- Exercises lo3 (pathfinding implementation)
- Provides the concrete comparison data for the worked example (per-agent A* vs flow field)

---

### Stage 4 — Post-Intervention Profiling and Written Note (10 min)

**What students do**
- Re-run at 100, 500, and 1 000 agents with both interventions active
- Write ≈150 words comparing frame time and behaviour fidelity before and after
- Note any visible behaviour degradation at the LOD tier boundaries

**What they produce**
- **Final deliverable:** modified source code (LOD scheduler + flow field) plus the 150-word profiling note with a before/after table

**Assessment mapping**

| Deliverable element | Assessment criterion | LO |
|---|---|---|
| LOD scheduler implementation | Foundation classical AI; performance reasoning | lo1, lo3 |
| Flow field implementation | Pathfinding technique; comparison with A* | lo1, lo2, lo3 |
| Profiling note | Justify technique choices; reflect on trade-offs | lo2 |
| Behaviour fidelity observation | Critical assessment of limitations | lo2, lo6 |

---

## 4. References Used

- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.
- Buckland, M. (2005). *Programming Game AI by Example*. Wordware Publishing.
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

---

## 5. Gaps — References Needed

The following sources are needed for this unit but are not present in the approved reference list. The author should supply or approve substitutes before content generation.

| Gap | Needed for | Notes |
|---|---|---|
| Reynolds, C. W. (1987). Flocks, herds and schools: A distributed behavioral model. *SIGGRAPH Computer Graphics*, 21(4), 25–34. | Segment 3 — boids rules; canonical primary source | Widely cited; verify page details |
| Treuille, A., Cooper, S. & Popović, Z. (2006). Continuum crowds. *ACM Transactions on Graphics*, 25(3), 1160–1168. | Segment 3 — continuum crowd model | ACM SIGGRAPH paper; verify details |
| A practitioner source on flow fields in RTS games (e.g. Elijah Emerson / Riot Games GDC talk on *League of Legends* pathfinding, or equivalent) | Segment 3 — industry grounding for flow fields | No GDC proceedings entry in approved list |
| A primary or practitioner source on influence maps (e.g. Tozour, P. in *AI Game Programming Wisdom* series) | Segment 5 — influence map construction and tactical querying | *AI Game Programming Wisdom* volumes not in approved list |
| A source on agent-based economic simulation in games (e.g. Adams, D. on Dwarf Fortress design, or academic treatment of emergent economies) | Segment 5 — economic simulation case studies | No Dwarf Fortress / RimWorld design documentation in approved list |