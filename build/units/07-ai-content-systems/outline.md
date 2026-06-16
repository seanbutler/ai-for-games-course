---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 913d43ac42faa956
generated_at: 2026-06-16T14:28:45+00:00
---

# Unit 07 — AI for Game Content and Systems

**One-line summary:** Surveys procedural and generative AI techniques for game content creation, from classical grammar-based methods to GANs, VAEs, and diffusion models, and evaluates their place in a real production pipeline.

---

## 1. Timed Session Plan (120 minutes)

| # | Segment | Minutes | Cumulative |
|---|---------|---------|------------|
| 1 | Framing: What is Content Generation? | 10 | 10 |
| 2 | Classical PCG: Constructive and Grammar-Based Methods | 25 | 35 |
| 3 | Search-Based PCG | 10 | 45 |
| 4 | Generative Neural Networks — GANs and VAEs | 30 | 75 |
| 5 | Diffusion Models and Modern Asset Pipelines | 20 | 95 |
| 6 | Neural Physics Approximation | 10 | 105 |
| 7 | Production Considerations and Critical Evaluation | 15 | 120 |

---

## 2. Segment Detail

---

### Segment 1 — Framing: What is Content Generation? (10 min)

**Subtopics**
- The content bottleneck in game development: cost, scale, variety
- Taxonomy overview: constructive → search-based → ML-based (three families, not a hierarchy)
- The PCG evaluation triangle: quality, diversity, controllability — introduced here, revisited throughout
- Forward-reference to Units 01–06: where classical AI ends and generative AI begins

**Worked examples**
- None (framing only)

**Learning outcomes served**
- *"Describe the main families of procedural content generation and their trade-offs."* [lo6]

---

### Segment 2 — Classical PCG: Constructive and Grammar-Based Methods (25 min)

**Subtopics**
- Constructive generation: noise functions (Perlin/Simplex), random walks, BSP trees for level layout
- L-systems: rewriting rules, parametric L-systems, application to vegetation and dungeon corridors
- Wave Function Collapse (WFC): constraint propagation, adjacency rules, entropy-guided tile selection
- Strengths and limits: determinism, artist control, scalability, failure modes (contradiction states in WFC)
- Brief comparison: classical PCG vs ML-based PCG on controllability axis

**Worked examples**
- **WFC dungeon tile map (primary):** Walk through constraint propagation step by step on a small grid — initial entropy state, lowest-entropy cell selection, collapse, neighbour propagation, backtrack on contradiction. Annotated diagram at each step.

**Learning outcomes served**
- *"Describe the main families of procedural content generation and their trade-offs."* [lo6]
- *"Assess the practical pipeline for integrating generative AI into a game production workflow."* [lo2, lo6] *(partial — classical baseline)*

---

### Segment 3 — Search-Based PCG (10 min)

**Subtopics**
- Framing content generation as optimisation: fitness functions over content spaces
- Evolutionary algorithms applied to level design (map layouts, difficulty curves)
- Quality-diversity algorithms (MAP-Elites): generating a diverse archive rather than a single optimum
- Trade-offs: computational cost, fitness function design difficulty, interpretability
- Forward-reference: RL-based content generation (Unit 06 connection)

**Worked examples**
- None (conceptual; builds on WFC example for contrast)

**Learning outcomes served**
- *"Describe the main families of procedural content generation and their trade-offs."* [lo6]
- *"Critically evaluate the role of ML-based physics approximation in interactive systems."* [lo4, lo6] *(framing contrast only)*

---

### Segment 4 — Generative Neural Networks: GANs and VAEs (30 min)

**Subtopics**

*GANs (15 min)*
- Generator/discriminator architecture: adversarial training loop
- Loss dynamics: minimax objective, why training is unstable
- Mode collapse: definition, visual intuition, mitigation strategies (Wasserstein GAN, minibatch discrimination)
- Game applications: texture synthesis, sprite generation, level image generation

*VAEs (10 min)*
- Encoder → latent space → decoder structure
- Reconstruction loss vs KL divergence: the ELBO objective, what each term enforces
- Latent space interpolation: controllable generation by walking the latent space
- Game applications: character variation, tile-set generation, style blending

*Comparison (5 min)*
- GAN vs VAE: sample sharpness vs latent structure; which to reach for and when
- Revisit PCG evaluation triangle: where GANs and VAEs sit on quality/diversity/controllability axes

**Worked examples**
- **1D GAN mode collapse (primary):** Generator trained to match a bimodal Gaussian. Show training curves and sample distributions at three checkpoints: early (random), mid (one mode captured), collapsed (one mode ignored). Illustrate what the discriminator gradient looks like in each case.

**Learning outcomes served**
- *"Explain how generative neural networks (GANs, VAEs, diffusion) produce game assets."* [lo4, lo6]
- *"Describe the main families of procedural content generation and their trade-offs."* [lo6]

---

### Segment 5 — Diffusion Models and Modern Asset Pipelines (20 min)

**Subtopics**
- Denoising diffusion: forward (noise addition) and reverse (denoising) processes; intuition without full score-matching derivation
- Conditioning mechanisms: text prompts, class labels, image inpainting — how conditioning steers generation
- Text-to-image in practice: Stable Diffusion as a case study for texture and concept-art generation
- 3D asset generation: NeRF and diffusion-based mesh generation (brief survey)
- AI-generated dialogue and narrative: language model integration (forward-reference to Unit 08)
- Practical pipeline: prompt engineering, inpainting for tiling textures, artist-in-the-loop iteration

**Worked examples**
- None (pipeline walkthrough via annotated diagram: prompt → latent diffusion → post-process → engine import)

**Learning outcomes served**
- *"Explain how generative neural networks (GANs, VAEs, diffusion) produce game assets."* [lo4, lo6]
- *"Assess the practical pipeline for integrating generative AI into a game production workflow."* [lo2, lo6]

---

### Segment 6 — Neural Physics Approximation (10 min)

**Subtopics**
- Motivation: expensive simulation (fluid, cloth, destruction) vs real-time budget
- Learned surrogates: training a network to replicate simulator outputs given state inputs
- Architecture choices: MLPs for low-DOF systems, CNNs for spatial fields
- Accuracy vs speed trade-off; failure modes when inputs leave the training distribution
- Industry examples: neural cloth simulation, fluid upscaling, destruction preview

**Worked examples**
- None (conceptual; brief annotated diagram of surrogate pipeline)

**Learning outcomes served**
- *"Critically evaluate the role of ML-based physics approximation in interactive systems."* [lo4, lo6]

---

### Segment 7 — Production Considerations and Critical Evaluation (15 min)

**Subtopics**
- Artist-in-the-loop workflows: curation, post-processing, style guides, human override
- IP and copyright: training data provenance, generated asset ownership (current legal landscape, briefly)
- Bias in training data: demographic representation in character generation, cultural homogenisation
- Quality assurance: automated metrics (FID, LPIPS) vs playtester evaluation
- When *not* to use generative AI: cases where hand-authored content is preferable (narrative coherence, brand consistency)
- Synthesis: mapping all three PCG families back to the evaluation triangle; which family fits which production context

**Worked examples**
- None (discussion-driven; revisits WFC and GAN examples for contrast)

**Learning outcomes served**
- *"Assess the practical pipeline for integrating generative AI into a game production workflow."* [lo2, lo6]
- *"Describe the main families of procedural content generation and their trade-offs."* [lo6]
- *"Critically evaluate the role of ML-based physics approximation in interactive systems."* [lo4, lo6] *(ethical/production dimension)*

---

## 3. Lab Plan (120 minutes)

### Overview
Students work with a supplied pre-trained generative model (GAN or VAE) for 2D tile generation. The lab moves through four staged tasks, each with an explicit deliverable.

---

### Stage 1 — Environment Setup and Baseline Inspection (15 min)

**Tasks**
- Install dependencies; load the supplied pre-trained model checkpoint
- Run the provided baseline noise generator; visualise 10 outputs
- Inspect the model architecture (layer count, latent dimension) in the supplied notebook

**Produces**
- 10 baseline noise-generated level images (saved to disk)
- Brief notes on architecture (filled-in template)

**Assessment mapping**
- Establishes the comparison baseline required by the written evaluation deliverable

---

### Stage 2 — Sampling from the Generative Model (25 min)

**Tasks**
- Write a Python sampling function: draw *N* latent vectors, decode to tile grids, save outputs
- Visualise 10 generated levels side by side with the baseline outputs
- Experiment with latent space interpolation between two samples (VAE track) or truncation trick (GAN track)

**Produces**
- `sample.py` script (or equivalent notebook cells)
- Grid visualisation of 10 generated levels

**Assessment mapping**
- Directly satisfies the "sampling script" and "visualisation of 10 generated levels" deliverable components
- Supports LO5 (applying a neural network solution to a practical problem)

---

### Stage 3 — Diversity Metric Implementation (35 min)

**Tasks**
- Implement pairwise Hamming distance between flattened tile grids
- Compute mean pairwise distance over a sample of 50 generated levels
- Repeat for the baseline noise generator
- Tabulate results; plot distribution of pairwise distances for both generators

**Produces**
- `diversity.py` (or equivalent) implementing the metric
- Results table and distance distribution plot

**Assessment mapping**
- Satisfies the "diversity metric results" deliverable component
- Grounds the written evaluation in quantitative evidence; supports LO2 (comparing approaches)

---

### Stage 4 — Written Evaluation (45 min)

**Tasks**
- Draft ~300-word evaluation covering:
  - What the diversity metric reveals about the generative model vs the baseline
  - Observed failure modes (mode collapse, implausible tile adjacencies, repetition)
  - One concrete suggestion for improving diversity or quality
  - One scenario where the classical WFC approach (from lecture) would be preferable and why

**Produces**
- Written evaluation (~300 words), submitted alongside the script and visualisations

**Assessment mapping**

| Deliverable component | Assessment criterion | LOs |
|---|---|---|
| Sampling script + visualisations | Working generative pipeline applied to a game problem | LO5 |
| Diversity metric implementation | Quantitative comparison of AI approaches | LO2 |
| Written evaluation | Critical assessment of generative AI strengths/failure modes; classical vs ML comparison | LO2, LO6 |

- Feeds directly into the project report requirement: *"critically compare the classical and ML/generative components on the same in-game problem"*
- Provides practice evidence for LO6: *"critically assess the role and impact of modern AI technologies in game development"*

---

## 4. References Used

- Shaker, N., Togelius, J. & Nelson, M. J. (2016). *Procedural Content Generation in Games.* Springer.
- Liu, R. et al. (2021). Deep Learning for Procedural Content Generation. *Neural Computing and Applications,* 33, 19–37.
- Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning.* MIT Press.

---

## 5. Gaps — References Needed

- **Wave Function Collapse:** No canonical paper on the approved list. The original algorithm is described in Gumin, M. (2016). *WaveFunctionCollapse* (GitHub repository). Author should confirm whether this should be added to `refs.yaml`.
- **Diffusion models:** No approved reference covers denoising diffusion probabilistic models (e.g., Ho et al., 2020, *Denoising Diffusion Probabilistic Models*, NeurIPS). A citation is needed for Segment 5. Author should supply and add to `refs.yaml`.
- **Quality-diversity / MAP-Elites:** No approved reference covers MAP-Elites (Mouret & Clune, 2015) or quality-diversity algorithms. Needed for Segment 3. Author should supply.
- **Neural physics surrogates:** No approved reference covers learned simulation surrogates specifically. A survey or industry paper is needed for Segment 6. Author should supply.
- **FID / LPIPS metrics:** No approved reference covers standard generative model evaluation metrics. Needed for Segment 7. Author should supply.