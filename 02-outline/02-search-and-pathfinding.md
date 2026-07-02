# Unit 02 — Search and Pathfinding

**One-line summary:** Build the graph-search intuition from BFS through to A*, then extend it to the representations actually used in shipped games.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — Search Graph Representations (20 min)

**Subtopics**
- Tile/grid graphs: uniform cost, 4- and 8-connected, pros and cons
- Waypoint graphs: manual placement, connectivity, memory cost
- Navigation meshes: convex polygons, corridor funnelling, why they dominate in 3D games
- When to choose each: map size, agent size, dynamic obstacles

**Outcomes served**
- *lo1*: Critically analyse principles of traditional game AI including pathfinding

---

### Segment 2 — Uninformed Search (20 min)

**Subtopics**
- BFS: frontier expansion, completeness, optimality on uniform graphs
- DFS: memory advantage, lack of optimality
- Uniform-cost search (Dijkstra): priority queue, cost accumulation, optimality proof sketch
- Why uninformed search is too slow for large game worlds

**Outcomes served**
- *lo1*, *lo3*: Analyse and implement classical game AI algorithms

---

### Segment 3 — Informed Search and A* (30 min)

**Subtopics**
- Greedy best-first: heuristic only, fast but suboptimal
- A*: f(n) = g(n) + h(n); open and closed sets
- Admissibility: h(n) ≤ true cost → optimality guarantee
- Consistency (monotonicity): triangle inequality, avoids re-expansion
- Heuristics for grids: Manhattan (4-dir), Euclidean, octile (8-dir)
- Tie-breaking: small perturbation to h(n) reduces node expansions

**Worked example 1:** Trace A* on an 8×8 grid — show open/closed sets at each step, demonstrate how octile distance prunes nodes that Manhattan misses.

**Outcomes served**
- *lo1*, *lo3*: Analyse and implement pathfinding algorithms

---

### Segment 4 — Practical Concerns (20 min)

**Subtopics**
- Path smoothing: string-pulling / funnel algorithm on navmeshes
- Dynamic obstacles: partial replanning, D* Lite concept
- Hierarchical pathfinding (HPA*): cluster abstraction, inter-cluster edges, two-phase query
- Jump Point Search: grid-specific pruning, symmetry breaking
- Any-angle paths: Theta* and line-of-sight post-processing

**Outcomes served**
- *lo2*: Evaluate and compare approaches; justify suitability for specific problems

---

### Segment 5 — NavMesh in Practice (10 min)

**Subtopics**
- Recast/Detour pipeline overview: voxelisation → region → polygon mesh → pathfinding
- Dynamic tile rebaking for moving obstacles
- Agent radius and height as NavMesh parameters

**Worked example 2:** Compare node-expansion counts for Dijkstra vs A* on the same map — show the heuristic's pruning effect in a concrete table.

**Outcomes served**
- *lo1*, *lo2*

---

### ML Bridge (20 min)

**Subtopics**
- Learned heuristics: neural networks predicting h(n), reducing expansions further
- Neural path planning: end-to-end learned navigation policies
- Why classical A* + good heuristic still dominates shipped titles: determinism, debuggability, no training data required
- Forward reference to Unit 06 (AI Agents and Learning)

**Outcomes served**
- *lo2*: Evaluate and compare classical vs ML approaches

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — Graph setup | 20 min | Tile grid loaded from supplied map file; nodes and edges constructed |
| 2 — Dijkstra | 25 min | Working Dijkstra implementation; instrument node-expansion counter |
| 3 — A* with pluggable heuristic | 35 min | A* with interface accepting Manhattan, Euclidean, or octile heuristic; run on three supplied maps |
| 4 — Results and analysis | 20 min | Table: map × algorithm × expansions × path cost; written paragraph justifying heuristic choice per map |

**Deliverable:** Working A* implementation; results table; written paragraph justifying heuristic choices.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| Dijkstra produces correct shortest paths | lo1, lo3 | Foundation — pathfinding baseline | 20% |
| A* produces correct optimal paths | lo1, lo3 | Foundation — pathfinding (A*) | 35% |
| Pluggable heuristic interface works for all three variants | lo3 | Foundation — pathfinding | 20% |
| Results table with correct expansion counts | lo2 | Report — design justification | 15% |
| Written paragraph with reasoned heuristic justification | lo2 | Report — design justification | 10% |

---

## References Used

**Gaps — references needed**
- Hart, P. E., Nilsson, N. J. & Raphael, B. (1968). Original A* paper — confirm on approved list.
- Millington, I. & Funge, J. *Artificial Intelligence for Games* (2nd ed.) — pathfinding chapters.
- Patel, A. *Introduction to A** (Red Blob Games) — interactive implementation reference; confirm on approved list.
- Monkkonen, M. *Recast Navigation* — NavMesh pipeline; confirm on approved list.
