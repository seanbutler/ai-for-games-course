# Benchmark Module Research

## Georgia Tech — CS 7632 Game AI (OMSCS)

**Source:** https://omscs.gatech.edu/cs-7632-game-ai  
**Schedule:** https://faculty.cc.gatech.edu/~surban6/2019fa-gameAI/schedule.html  
**Level:** Graduate (MSc)  
**Tools:** Unity + C#  
**Assessment:** 8 assignments (70%), 2 exams (15% each)

**Weekly topic schedule (Fall 2019):**

| Week | Topics |
|---|---|
| 1 | Course intro; path planning — grids |
| 2 | Path planning — path networks, expanded geometry, navmeshes |
| 3–4 | Path planning — search (A* etc.) |
| 4–5 | Kinematic movement, steering, flocking, formations |
| 6–8 | Decision making — FSMs, decision trees, behaviour trees, rules |
| 9 | Planning (STRIPS-style) |
| 11–13 | Procedural content generation — search, optimisation, genetic algorithms, player models |
| 13–14 | Reinforcement learning, N-gram prediction, MCTS, case-based reasoning |

**Topic coverage:** movement/steering heavily weighted; no explicit ML foundations or neural architecture units; RL and PCG present but light; no rendering AI, LLMs, or modern generative AI.

---

## Falmouth University — Artificial Intelligence for Games MSc

**Source:** https://www.falmouth.ac.uk/study/postgraduate/artificial-intelligence-games  
**Level:** MSc (full programme, not a single module)  
**Structure:** Three study blocks

| Block | Module | Credits |
|---|---|---|
| 1 | Development Practice (C++, git, interdisciplinary teamwork) | 30 |
| 1 | Classical Artificial Intelligence | 30 |
| 2 | Machine Learning | 30 |
| 2 | Game Development Project | 30 |
| 3 | Major Project | 60 |

**Classical AI module covers:** decision-making techniques, classical algorithms used in industry. Topics include genetic programming, fuzzy logic, Monte Carlo Tree Search.  
**Machine Learning module covers:** current ML frameworks, data-rich problem spaces.  
**Assessment:** 100% coursework.

**Comparison to WM9SL-15:** Falmouth splits classical and ML into two full 30-credit modules; WM9SL-15 covers both within a single 15-credit module but goes deeper on specific game-relevant sub-topics (navmesh, rendering AI, LLMs, procedural content). Falmouth does not appear to have equivalent depth on modern AI applications (DLSS, LLM-driven NPCs).

---

## Abertay University — MAT501 Applied Mathematics and Artificial Intelligence

**Source:** https://www.abertay.ac.uk/course-search/postgraduate-taught/applied-artificial-intelligence-and-user-experience/ (module detail page returned 502 — content retrieved via search)  
**Level:** MSc component module  
**Focus:** Mathematics underpinning AI for games

**Topics covered:**
- Fuzzy logic and fuzzy state machines
- Case-based reasoning
- Genetic algorithms
- Reinforcement learning (value iteration, policy iteration, Q-learning, learning automata)
- Probabilistic methods
- Artificial neural networks
- Clustering / unsupervised learning (SVD, k-means)
- Gradient descent and backpropagation

**Assessment:** not publicly detailed  
**Comparison to WM9SL-15:** Abertay is heavier on mathematical foundations (fuzzy logic, probabilistic methods, SVD); WM9SL-15 is heavier on practical implementation, classical game-specific techniques (pathfinding, BTs, steering), and modern applications (generative AI, rendering).

---

## Key differentiators of WM9SL-15

- Only module of the three to explicitly cover collision detection and spatial perception as a standalone topic
- Only one to cover rendering AI (DLSS-style upscaling, denoising)
- Only one to explicitly cover LLM integration in games
- Only one to cover AI at scale (spatial indexing, LOD AI, crowds) and tooling/pipeline
- Tightest scope (15 credits, 4 weeks) — requires careful time budgeting per unit
