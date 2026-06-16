---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 484e4d835ce3711b
generated_at: 2026-06-16T14:23:05+00:00
---

# Unit 02 — Search and Pathfinding

**One-line summary:** Build and compare BFS, Dijkstra, and A* on game-world graph representations, then reason about heuristic design, optimality, and practical extensions.

---

## 1. Timed Session Plan (Lecture — 120 minutes total)

| # | Segment | Minutes | Cumulative |
|---|---------|---------|------------|
| 1 | Framing: why pathfinding matters in games | 10 | 10 |
| 2 | Search-graph representations | 20 | 30 |
| 3 | Uninformed search: BFS, DFS, Dijkstra | 20 | 50 |
| 4 | Informed search: greedy best-first and A* | 25 | 75 |
| 5 | Heuristic design: admissibility, consistency, distance metrics | 15 | 90 |
| 6 | Worked example: A* trace on an 8×8 grid | 15 | 105 |
| 7 | Practical concerns and extensions (signpost) | 10 | 115 |
| 8 | ML bridge and wrap-up | 5 | 120 |

---

## 2. Segment Detail

### Segment 1 — Framing: why pathfinding matters in games (10 min)

**Subtopics**
- Pathfinding as the most universally shipped AI subsystem
- Cost of getting it wrong: agent stuck-states, rubber-banding, frame-budget overruns
- Module context: classical-first — we solve this problem fully before asking whether ML can help

**Worked examples:** none

**Learning outcomes served:**
- *"Critically analyse the principles and techniques used in traditional game artificial intelligence, including pathfinding, decision systems, and behaviour modelling."* [lo1]

---

### Segment 2 — Search-graph representations (20 min)

**Subtopics**
- Tile grids: 4-connected vs 8-connected; uniform vs weighted cells; memory layout
- Waypoint graphs: hand-placed nodes, edge costs, suitability for open worlds
- Navigation meshes: polygon soup, convex decomposition, adjacency graph; why NavMesh is the production default
- Trade-offs table: granularity, memory, authoring cost, dynamic-obstacle handling
- Brief: Recast/Detour as the industry reference implementation

**Worked examples:** none (trade-offs table is the in-lecture artefact)

**Learning outcomes served:**
- *"Model a game world as a search graph (tile grid, waypoint graph, navmesh)."* [lo1, lo3]
- *"Critically analyse the principles and techniques used in traditional game artificial intelligence…"* [lo1]

---

### Segment 3 — Uninformed search: BFS, DFS, Dijkstra (20 min)

**Subtopics**
- BFS: FIFO frontier, completeness, optimality on unweighted graphs
- DFS: LIFO frontier, memory advantage, non-optimality; rarely used for pathfinding
- Uniform-cost search (Dijkstra): priority-queue frontier ordered by g(n); optimality proof sketch
- Complexity: time and space in terms of branching factor and depth
- Implementation note: open/closed set data structures and their cost

**Worked examples:**
- Side-by-side node-expansion comparison (Dijkstra vs A*) — introduced here for Dijkstra half; A* half delivered in Segment 6

**Learning outcomes served:**
- *"Implement and contrast BFS, Dijkstra, and A*."* [lo1, lo3]

---

### Segment 4 — Informed search: greedy best-first and A* (25 min)

**Subtopics**
- Greedy best-first: frontier ordered by h(n); fast but non-optimal; failure cases
- A*: f(n) = g(n) + h(n); combining path cost and heuristic estimate
- Algorithm walkthrough: open set, closed set, parent pointers, path reconstruction
- Optimality theorem: A* is optimal if h is admissible (and consistent for graph search)
- Tie-breaking strategies: nudging f, preferring higher g; effect on path aesthetics
- C++ data-structure choices: `std::priority_queue` vs indexed heap; lazy deletion

**Worked examples:**
- A* trace on 8×8 grid (setup — full step-by-step trace delivered in Segment 6)

**Learning outcomes served:**
- *"Implement and contrast BFS, Dijkstra, and A*."* [lo1, lo3]
- *"Design admissible heuristics and reason about optimality."* [lo1]

---

### Segment 5 — Heuristic design: admissibility, consistency, distance metrics (15 min)

**Subtopics**
- Admissibility: h(n) ≤ true cost to goal — never overestimates
- Consistency (monotonicity): h(n) ≤ cost(n→n') + h(n'); implies admissibility; avoids reopening nodes
- Manhattan distance: 4-connected grids; formula; when it is exact
- Euclidean distance: 8-connected or continuous; admissible but weaker than octile
- Octile distance: correct for 8-connected uniform grids; derivation
- Inadmissible heuristics: weighted A* (ε-suboptimal but faster); when the trade-off is acceptable in games
- Heuristic selection guide: grid type → recommended metric

**Worked examples:**
- Heuristic value table computed at each node during the 8×8 trace (feeds Segment 6)

**Learning outcomes served:**
- *"Design admissible heuristics and reason about optimality."* [lo1]
- *"Evaluate when hierarchical or any-angle extensions are warranted."* [lo2]

---

### Segment 6 — Worked example: A* trace on an 8×8 grid (15 min)

**Subtopics**
- Full step-by-step A* trace with octile heuristic on a prepared 8×8 grid with obstacles
  - Show open set (priority queue contents), closed set, and f/g/h values at each iteration
  - Highlight node-expansion order vs Dijkstra on the same map
- Node-expansion count comparison: Dijkstra vs A* — quantify the heuristic's pruning effect
- Common student errors: re-expanding closed nodes, incorrect parent updates

**Worked examples:**
- **WE-1:** A* step-by-step on 8×8 grid with octile heuristic (open/closed sets at each iteration)
- **WE-2:** Node-expansion count comparison: Dijkstra vs A* on the same map

**Learning outcomes served:**
- *"Implement and contrast BFS, Dijkstra, and A*."* [lo1, lo3]
- *"Design admissible heuristics and reason about optimality."* [lo1]

---

### Segment 7 — Practical concerns and extensions (10 min)

**Subtopics**
- Path smoothing: string-pulling, funnel algorithm on NavMesh
- Dynamic obstacles and partial replanning: D* Lite concept; incremental repair vs full replan
- Hierarchical Pathfinding A* (HPA*): cluster abstraction, two-level search, when to use
- Jump Point Search: symmetry breaking on uniform grids; expansion savings
- Theta*: any-angle paths; line-of-sight checks; smoother results than post-processing
- Decision guide: which extension fits which game type (RTS, FPS, open-world)

**Worked examples:** none (signpost only — no full derivations)

**Learning outcomes served:**
- *"Evaluate when hierarchical or any-angle extensions are warranted."* [lo2]
- *"Critically analyse the principles and techniques used in traditional game artificial intelligence…"* [lo1]

---

### Segment 8 — ML bridge and wrap-up (5 min)

**Subtopics**
- Forward-reference: learned heuristics; neural A* guidance; end-to-end neural planners
- Why classical A* remains the production default: determinism, debuggability, frame-budget predictability
- Full ML treatment deferred to Unit 06
- Recap of session outcomes; preview of tutorial task

**Worked examples:** none

**Learning outcomes served:**
- *"Evaluate and compare different AI approaches used in games, including rule-based systems and machine learning methods, and justify their suitability for specific design or technical problems."* [lo2]

---

## 3. Lab Plan (Tutorial — 120 minutes total)

### Overview
Students implement A* over a tile grid using the supplied starter project (C++ or Python), instrument it, and compare it against a provided Dijkstra baseline across three maps.

---

### Stage 1 — Familiarise with the starter project (15 min)

**What students do**
- Read the starter-project structure: `Grid`, `Node`, `Pathfinder` interface, `DijkstraBaseline` reference implementation
- Confirm build and run on the reference platform
- Inspect the instrumentation hook: `onNodeExpanded()` callback that increments an expansion counter

**Produces:** nothing submitted; mental model of the codebase confirmed

---

### Stage 2 — Implement the pluggable heuristic interface (20 min)

**What students do**
- Implement the `Heuristic` abstract class / function-pointer interface
- Write three concrete heuristics: Manhattan, Euclidean, Octile
- Unit-test each heuristic against hand-computed values for known node pairs

**Produces:** `heuristics.cpp` / `heuristics.h` with three implementations and passing unit tests

---

### Stage 3 — Implement A* (35 min)

**What students do**
- Implement `AStarPathfinder` using an indexed priority queue (or `std::priority_queue` with lazy deletion)
- Handle: open set, closed set, parent-pointer map, path reconstruction
- Wire in the `onNodeExpanded()` instrumentation
- Verify correctness: path cost matches Dijkstra on unweighted map; path is visually sensible

**Produces:** `astar.cpp` / `astar.h`; correctness confirmed against baseline on Map 1

---

### Stage 4 — Run experiments across three maps (30 min)

**What students do**
- Run Dijkstra and A* (with each heuristic) on the three supplied maps:
  - Map 1: open grid, few obstacles
  - Map 2: maze-like corridors
  - Map 3: large open area with a central obstacle cluster
- Record: algorithm × heuristic × node expansions × path cost × runtime (ms)
- Populate the results table template provided

**Produces:** completed results table (map × algorithm × expansions × path cost)

---

### Stage 5 — Written justification (20 min)

**What students do**
- Write one paragraph per map justifying the heuristic choice:
  - Which heuristic minimised expansions without sacrificing optimality?
  - Did any map expose a case where Manhattan was inadmissible (diagonal movement)?
  - Any tie-breaking observations?

**Produces:** three short paragraphs (one per map) — the primary written deliverable

---

### Assessment Mapping

| Lab deliverable | Assessment requirement | Learning outcome |
|---|---|---|
| Working A* implementation in C++ | Mandatory foundation: pathfinding (e.g. A*) | lo3 |
| Pluggable heuristic interface | Design and implement classical game AI algorithms | lo3 |
| Results table (expansions, path cost) | Report section comparing classical AI components | lo1, lo2 |
| Written heuristic justification paragraphs | Justify technique choices with reference to module theory | lo1, lo2 |

The lab deliverable maps directly to the **foundation** requirement of the project assessment (all foundation techniques from Units 01–03 must appear in the submitted code) and provides the empirical data students will cite in their report's classical-AI analysis section.

---

## 4. References Used

- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- Hart, P. E., Nilsson, N. J. & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths. *IEEE Transactions on Systems Science and Cybernetics*, 4(2), 100–107.
- Patel, A. Introduction to A* (Red Blob Games). redblobgames.com.
- Monkkonen, M. Recast Navigation (open source). github.com/recastnavigation/recastnavigation.

---

## 5. Gaps — References Needed

- **HPA\* primary source:** Botea, A., Müller, M. & Schaeffer, J. (2004). Near Optimal Hierarchical Path-Finding. *Journal of Game Development*, 1(1). — not on the approved list; needed for Segment 7 HPA* treatment.
- **Jump Point Search primary source:** Harabor, D. & Grastien, A. (2011). Online Graph Pruning for Pathfinding on Grid Maps. *AAAI*. — not on the approved list; needed for Segment 7 JPS treatment.
- **Theta\* primary source:** Nash, A., Daniel, K., Koenig, S. & Felner, A. (2007). Theta*: Any-Angle Path Planning on Grids. *AAAI*. — not on the approved list; needed for Segment 7 Theta* treatment.
- **D\* Lite primary source:** Koenig, S. & Likhachev, M. (2002). D\* Lite. *AAAI*. — not on the approved list; needed for Segment 7 dynamic-replanning treatment.