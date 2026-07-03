# Unit 07 — AI for Game Content and Systems

**One-line summary:** Procedural and generative AI for creating game content — from grammar-based and search-based PCG through to neural generative models.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — Why Procedural Content Generation? (15 min)

**Subtopics**
- The content problem: hand-authored content is expensive; PCG scales content at low marginal cost
- PCG taxonomy: constructive vs search-based; offline vs runtime; deterministic vs stochastic
- Examples in shipped titles: Minecraft terrain, Spelunky levels, No Man's Sky biomes, Diablo loot
- Trade-offs: controllability, quality, reproducibility (seed-based vs truly random)

**Outcomes served**
- *lo6*: Critically assess role and impact of modern AI in game development

---

### Segment 2 — Grammar-Based and Rule-Based Generation (20 min)

**Subtopics**
- L-systems: production rules for plant/dungeon growth; parametric L-systems
- Context-free grammars for level generation: room types as non-terminals, connections as rules
- Wave Function Collapse (WFC): constraint propagation on tile grids; adjacency rules
- Designer control knobs: rule weights, constraint tightening, guaranteed connectivity

**Worked example 1:** Apply a simple grammar to generate a dungeon: start symbol → rooms → corridors; show three derivations with different random seeds; identify where designer constraints are encoded.

**Outcomes served**
- *lo6*, *lo3*: Design and implement an AI technique

---

### Segment 3 — Search-Based PCG (20 min)

**Subtopics**
- Framing content as an optimisation problem: solution space = possible content; fitness = quality metric
- Evolutionary algorithms: representation, fitness function, selection, crossover, mutation
- Genetic algorithms for level design: encoding a level as a chromosome, fitness = fun proxy
- Monte Carlo approaches: random playouts to evaluate content quality
- Pitfalls: fitness function defines what "good" means — Goodhart's Law in PCG

**Outcomes served**
- *lo6*, *lo2*

---

### Segment 4 — Neural Generative Models (35 min)

**Subtopics**
- Autoencoders: encoder-decoder; latent space interpolation for content variation
- Variational autoencoders (VAEs): probabilistic latent space; sampling new content
- Generative Adversarial Networks (GANs): generator vs discriminator; training instability
- Diffusion models: denoising process; state of the art for image/texture generation
- Games applications: texture synthesis, character model generation, level image generation
- Practical limitations: mode collapse, training cost, controllability vs quality trade-off

**Worked example 2:** Describe a VAE pipeline for generating 2D dungeon layouts — latent space encodes "dungeon style"; sample and decode to produce novel layouts; show interpolation between two styles.

**Outcomes served**
- *lo4*, *lo5*, *lo6*

---

### Segment 5 — Evaluation of Generated Content (10 min)

**Subtopics**
- Playability metrics: is the level completable? reachable? balanced?
- Diversity metrics: coverage of design space; novelty vs quality
- Player experience models: mapping content properties to predicted player response
- Human evaluation vs automated metrics

**Outcomes served**
- *lo2*, *lo6*

---

### ML Bridge / Forward Reference (20 min)

**Subtopics**
- LLMs for narrative and dialogue generation (full treatment Unit 08)
- Learned playtesting: RL agent as automated quality evaluator for PCG
- Hybrid: PCG generates structure; neural model fills in detail

**Outcomes served**
- *lo6*

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — WFC tile generator | 40 min | Wave Function Collapse implementation on a supplied tile set; generate three dungeon floor plans |
| 2 — Fitness-based PCG | 35 min | Simple genetic algorithm varying room count and connectivity; fitness = path length from start to exit |
| 3 — Evaluation | 25 min | Automated playability check (is exit reachable?); diversity metric (average pairwise tile difference) |
| 4 — Write-up | 20 min | Paragraph comparing WFC and GA approaches: controllability, quality, runtime cost |

**Deliverable:** WFC and GA implementations; evaluation results; written comparison paragraph.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| WFC generates valid (constraint-satisfying) floor plans | lo6, lo3 | Advanced generative component | 30% |
| GA produces measurably improving fitness over generations | lo6, lo5 | Advanced generative component | 25% |
| Playability and diversity metrics computed correctly | lo2 | Report — evaluation | 20% |
| Written comparison paragraph | lo2, lo6 | Report — critical comparison | 25% |

---

## References Used

**Gaps — references needed**
- Shaker, N., Togelius, J. & Nelson, M. J. *Procedural Content Generation in Games* (Springer, 2016) — taxonomy, grammar-based, search-based PCG.
- Liu, R. et al. (2021). Deep Learning for Procedural Content Generation. *Neural Computing and Applications*, 33 — neural generative approaches.
- Goodfellow, I. et al. *Deep Learning* — VAE and GAN chapters.
- A primary source on Wave Function Collapse (Gumin, 2016, GitHub) — confirm availability and citation form.
