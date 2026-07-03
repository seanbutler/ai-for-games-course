# Unit 03 — Collision Detection, Response, and Spatial Perception

**One-line summary:** Build the geometric layer that lets agents know what they are touching and what they can see, from primitive overlap tests through to a working field-of-view sensor.

---

## Lecture Session Plan — 120 minutes

---

### Segment 1 — Geometry Primitives and the Two-Phase Architecture (20 min)

**Subtopics**
- Why game objects need collision geometry separate from render geometry
- Primitive types: AABB, sphere, capsule, OBB — construction, memory cost, test cost
- Agent vs physics-body trade-offs: capsule for characters (cheap vertical sweep, smooth sliding); AABB for projectiles and triggers; OBB for oriented crates and vehicles
- The two-phase argument: O(n²) naive pair-testing is untenable; broad phase culls candidate pairs cheaply so narrow phase only runs on likely hits

**Outcomes served**
- *lo1*: Critically analyse principles and techniques used in traditional game AI

---

### Segment 2 — Broad-Phase Structures (20 min)

**Subtopics**
- Sweep-and-prune (sort-and-sweep): one axis, incremental update, when it wins
- Uniform grid: cell sizing heuristics, multi-cell objects, query by radius
- Bounding-volume hierarchy (BVH): top-down construction, AABB tree, traversal cost
- Decision guide: uniform grid for uniformly sized dynamic agents; BVH for static scene geometry; sweep-and-prune for slow-moving large objects

**Outcomes served**
- *lo1*, *lo2*: Evaluate and compare approaches; justify suitability for specific problems

---

### Segment 3 — Narrow-Phase Algorithms (25 min)

**Subtopics**
- AABB vs AABB: axis-overlap test, minimum translation vector (MTV) derivation
- Sphere vs sphere: distance vs sum-of-radii
- Sphere vs AABB: nearest-point clamp, distance check
- Separating Axis Theorem (SAT) for OBBs: axes to test, early-out on first separation

**Worked example 1:** AABB overlap test and MTV response — trace the maths on a concrete pair of boxes, then show the same function used for both physics separation and agent-avoidance push-out.

**Outcomes served**
- *lo1*, *lo3*: Design and implement classical game AI algorithms

---

### Segment 4 — Collision Response (15 min)

**Subtopics**
- Position correction (overlap separation): move-out along MTV, split correction between bodies by inverse mass ratio
- Impulse-based velocity response: relative velocity along collision normal, restitution coefficient, impulse magnitude derivation
- Friction: tangential impulse, static vs kinetic coefficient
- Where AI agents diverge from rigid-body physics: agents often want kinematic control, so they take position correction but ignore velocity impulse

**Outcomes served**
- *lo1*, *lo3*

---

### Segment 5 — Ray Casting and Shape Casts (20 min)

**Subtopics**
- Parametric ray: origin + t·direction, valid t range
- Ray vs AABB: slab method, per-axis entry/exit t, intersection interval
- Ray vs sphere: quadratic formulation, discriminant test, nearest hit
- Ray vs triangle: Möller–Trumbore, barycentric coordinates
- Shape casts (swept volumes): capsule cast for agent step validation, sphere sweep for projectiles — reduce to ray cast against expanded geometry

**Worked example 2:** Trace a ray through a uniform grid for line-of-sight — step cell-by-cell using DDA, early-out on the first occupied cell. Show the code and walk a concrete example on a small grid.

**Outcomes served**
- *lo1*, *lo3*

---

### Segment 6 — AI Perception Systems (15 min)

**Subtopics**
- Line-of-sight: ray cast from eye point to target, check against scene geometry only (not other agents)
- Range detection: sphere overlap query against broad-phase grid, returns candidate list
- Field-of-view cone: three-stage filter — range check (broad), dot-product angle check (cheap narrow), ray-cast occlusion (expensive, last)
- Designing sensors as components: sensor emits a list of perceived entities; decision system consumes that list — clean separation

**Worked example 3:** Build the full FoV sensor — combine the three stages, show the C++ struct and query function, trace it on an example scene with two visible and one occluded target.

**Outcomes served**
- *lo1*, *lo2*, *lo3*

---

### Segment 7 — Optimisations and Practical Concerns (5 min)

**Subtopics**
- Early-out ordering: cheapest test first (range before angle before ray)
- Layer/channel masking: tag geometry as "opaque to AI" vs "opaque to physics" vs "trigger only"
- Per-frame query budgeting: not every agent needs a full FoV scan every frame; stagger updates, prioritise by distance to player

**Outcomes served**
- *lo2*: Evaluate and justify suitability for specific technical problems

---

## Lab Plan — 120 minutes

**Premise:** Extend the A* tile-grid project from Unit 02 with a spatial perception layer. Students do not yet wire the sensor into a decision system — that is Unit 04's job.

| Stage | Duration | What students produce |
|---|---|---|
| 1 — AABB collision grid | 30 min | Static obstacle AABB array + uniform grid broad phase; query returns list of overlapping obstacles for a given agent AABB |
| 2 — Ray-cast LOS | 30 min | DDA grid traversal for line-of-sight; tested against the obstacle grid from Stage 1 |
| 3 — FoV sensor | 40 min | Full three-stage FoV sensor (range → angle → LOS ray); returns `vector<AgentId>` of visible targets |
| 4 — Timing comparison | 20 min | Run FoV queries with and without the broad-phase grid; record query counts and wall-clock time in a results table |

**Deliverable:** Working C++ implementation of all three systems; results table (with/without broad-phase, query counts, timings); one paragraph explaining which optimisation had the largest impact and why.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| AABB collision grid compiles and correctly detects overlaps | lo1, lo3 | Foundation — sensing/collision | 25% |
| Ray-cast LOS returns correct true/false for occluded/clear pairs | lo1, lo3 | Foundation — sensing/rays | 25% |
| FoV sensor returns correct visible-agent list on the provided test scene | lo1, lo3 | Foundation — visual cones | 30% |
| Results table with analysis paragraph | lo2 | Report — design justification | 20% |

---

## References Used

- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

**Gaps — references needed**

- A dedicated collision detection reference would strengthen Segments 3–5. Suggest adding: Ericson, C. (2004). *Real-Time Collision Detection*. Morgan Kaufmann. — it is the standard practitioner source for all narrow-phase algorithms and ray/shape casts covered here.
