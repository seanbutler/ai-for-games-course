# Unit 03 — Perception: Sensing the World

**One-line summary:** Build the geometric layer that lets agents know what they are touching and what they can see — from collision primitives and overlap tests through raycasting to a complete field-of-view sensor.

---

## Lecture Session Plan — 60 minutes

### Segment 1 — Why Perception is a Separate Problem (10 min)

**Subtopics**
- The sensing problem: agents need to query the world, not just act in it
- Inputs vs outputs: sensing (this unit) feeds decision making (Unit 04)
- The cost problem: naively checking every object against every agent is O(n²) — not viable at game scale
- Separation of concerns: sensor component emits a list of perceived entities; decision system consumes it — clean interface

**Outcomes served**
- *lo1*: Critically analyse principles and techniques used in traditional game AI

---

### Segment 2 — Collision Geometry and Overlap Tests (15 min)

**Subtopics**
- Collision primitives for sensing: sphere (range check), AABB (trigger volumes), capsule (character occupancy)
- Why sensing uses simpler geometry than physics: speed over precision
- Sphere overlap test: distance² vs radius² — no square root needed
- AABB overlap test: axis-separation check on x, y, z independently
- Broad-phase first: spatial grid or BVH to cull candidates before running overlap tests
- Use cases: range detection ("enemies within 10m"), trigger zones ("player entered room"), proximity alerts

**Worked example 1:** Implement a range sensor — given an agent position and a list of candidates, use a sphere overlap test to return all candidates within radius r; show the broad-phase grid reducing the candidate list from 200 to 4 before the overlap test runs.

**Outcomes served**
- *lo1*, *lo3*: Design and implement classical game AI algorithms

---

### Segment 3 — Raycasting for Line-of-Sight (20 min)

**Subtopics**
- Parametric ray: origin + t·direction; valid t range [t_min, t_max]
- Ray vs AABB: slab method — per-axis entry/exit t, take max entry and min exit
- Ray vs sphere: quadratic formulation, discriminant test
- Ray vs triangle: Möller–Trumbore algorithm (brief; used for mesh-accurate LOS)
- Grid traversal for LOS: DDA algorithm — step cell by cell, early-out on first occupied cell; cheap and sufficient for tile-based games
- Shape casts (swept volumes): capsule cast for movement validation, sphere sweep for projectile prediction — reduce to ray cast against expanded geometry
- Layer masking: tag geometry as "blocks vision" vs "blocks movement" vs "trigger only" — allows ray to ignore non-relevant objects

**Worked example 2:** Trace a line-of-sight ray using DDA on an 8×8 tile grid between two agents — step through each cell, show the early-out when an opaque tile is hit; compare to brute-force segment-vs-all-tiles.

**Outcomes served**
- *lo1*, *lo3*

---

### Segment 4 — Field-of-View Sensors and Practical Optimisation (15 min)

**Subtopics**
- Three-stage FoV filter (cheap to expensive, early-out at each stage):
  1. Range check — sphere overlap, discard candidates outside radius
  2. Angle check — dot product of forward vector and direction-to-candidate; discard if outside cone half-angle
  3. Occlusion check — ray cast from eye point to candidate; discard if blocked
- Why this order: range and angle are O(1) arithmetic; ray cast is the expensive step — only run it on survivors
- Per-frame budgeting: stagger sensor updates across frames; prioritise agents near the player
- Sensor output: `vector<EntityId>` of visible targets — handed to decision system

**Outcomes served**
- *lo1*, *lo2*: Evaluate and compare approaches; justify optimisation choices

---

## Lab Plan — 60 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — Range sensor | 15 min | Sphere overlap test returning all agents within radius; tested against a supplied scene of 50 agents |
| 2 — Line-of-sight | 20 min | DDA ray cast for LOS against the tile grid from Unit 02; returns true/false |
| 3 — FoV sensor | 15 min | Three-stage filter combining range, dot-product angle, and LOS ray; returns visible agent list |
| 4 — Timing and write-up | 10 min | Record query times with and without broad-phase culling; one paragraph on which stage eliminated the most candidates |

**Deliverable:** Working C++ implementations of range sensor, LOS ray cast, and FoV sensor; timing results; one-paragraph analysis.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| Range sensor returns correct results | lo1, lo3 | Foundation — sensing/ranges | 25% |
| LOS ray cast correct on supplied test cases (clear and occluded pairs) | lo1, lo3 | Foundation — sensing/rays | 30% |
| FoV sensor returns correct visible-agent list | lo1, lo3 | Foundation — visual cones | 30% |
| Timing paragraph with reasoned analysis | lo2 | Report — design justification | 15% |

---

## References Used

**Gaps — references needed**
- Millington, I. & Funge, J. *Artificial Intelligence for Games* (2nd ed.) — sensing and perception chapters.
- A dedicated collision/geometry reference (e.g. Ericson, C. *Real-Time Collision Detection*, Morgan Kaufmann, 2004) would strengthen Segments 2–3 — not currently on approved list; flag for author to add.
