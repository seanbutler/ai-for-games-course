---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: 28c846bf5a370eb3
generated_at: 2026-06-16T14:26:32+00:00
---

# Unit 05 — Neural Network Architectures

**One-line summary:** A systematic tour of MLP, CNN, RNN/LSTM, and Transformer architectures, grounded in games-relevant input modalities, equipping students to select and apply the right network for a given problem.

---

## 1. Timed Session Plan (Lecture — 120 minutes)

| # | Segment | Minutes | Cumulative |
|---|---------|---------|------------|
| 1 | Framing & recap | 5 | 5 |
| 2 | From perceptron to MLP | 20 | 25 |
| 3 | Convolutional Neural Networks | 25 | 50 |
| 4 | Worked Example A — CNN forward pass on a tile map | 15 | 65 |
| 5 | Recurrent Networks & LSTMs | 20 | 85 |
| 6 | Worked Example B — RNN vs LSTM on game-event sequences | 10 | 95 |
| 7 | Transformer architecture | 15 | 110 |
| 8 | Practical regularisation & optimisers | 7 | 117 |
| 9 | Architecture selection & forward bridge | 3 | 120 |

---

## 2. Segment Detail

### Segment 1 — Framing & Recap (5 min)

**Subtopics**
- Recap Unit 04: gradient descent, backpropagation, the learning loop
- Motivating question: *why does architecture matter?* — same data, different inductive biases
- Roadmap of the four architecture families covered today

**Worked examples:** none

**Learning outcomes served:**
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

### Segment 2 — From Perceptron to MLP (20 min)

**Subtopics**
- Single perceptron: weights, bias, linear threshold
- Stacking layers: hidden layers, depth vs width intuition
- Activation functions: ReLU (default choice), sigmoid, tanh — shapes, saturation, dead-neuron risk
- Forward pass algebra: matrix–vector notation; shape tracking
- Universal approximation: what it promises and what it does not
- Games context: flat feature vectors (e.g., agent health, ammo, distance-to-target) as natural MLP inputs

**Worked examples:** none (inline arithmetic trace on a 3-layer toy network)

**Learning outcomes served:**
- *"Describe the structure and forward pass of a multilayer perceptron."* [lo4]

---

### Segment 3 — Convolutional Neural Networks (25 min)

**Subtopics**
- Motivation: why fully-connected layers are wasteful on spatial data
- Convolution operation: kernel, stride, padding; output dimension formula
- Feature maps and filter banks
- Pooling: max-pool, average-pool; spatial downsampling
- Translation invariance / equivariance — why it matters for game grids and sprite sheets
- Typical CNN stack: Conv → ReLU → Pool → … → Flatten → FC
- Games applications:
  - Processing pixel frames (Atari-style RL input)
  - Tile-map classification / terrain recognition
  - Game-state grids (fog-of-war masks, occupancy maps)
- Parameter count comparison: CNN vs equivalent FC layer

**Worked examples:** sets up Worked Example A (next segment)

**Learning outcomes served:**
- *"Explain how convolutional layers exploit spatial locality for image and grid inputs."* [lo4]
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

### Segment 4 — Worked Example A: CNN Forward Pass on a Tile Map (15 min)

**Setup**
- Input: 16 × 16 single-channel tile-map excerpt (values 0–3 encoding terrain type)
- Architecture: Conv(8 filters, 3×3, stride 1, padding 0) → ReLU → MaxPool(2×2) → Conv(16 filters, 3×3) → ReLU → MaxPool(2×2) → Flatten → FC(4)

**Steps traced**
1. Compute output spatial dimensions after each Conv and Pool layer (show formula)
2. Count parameters at each layer
3. Trace a single feature-map activation value through the first convolution by hand
4. Identify where spatial information is discarded vs preserved
5. Discuss: what would change if input were RGB (3-channel)?

**Learning outcomes served:**
- *"Explain how convolutional layers exploit spatial locality for image and grid inputs."* [lo4]
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

### Segment 5 — Recurrent Networks & LSTMs (20 min)

**Subtopics**
- Motivation: inputs that are sequences, not fixed-size vectors (event logs, dialogue history, time-series of game state)
- Vanilla RNN: hidden state, unrolling through time, shared weights
- Backpropagation through time (BPTT): brief recap
- Vanishing gradient problem: why long-range dependencies fail in vanilla RNNs
- LSTM architecture:
  - Cell state as long-term memory
  - Forget gate, input gate, output gate — purpose of each
  - How gating mitigates vanishing gradients
- GRU: simplified gating, when to prefer it
- Games contexts:
  - NPC dialogue state tracking
  - Sequence of player actions as input to an adaptive AI
  - Temporal smoothing of noisy sensor data

**Worked examples:** sets up Worked Example B (next segment)

**Learning outcomes served:**
- *"Describe recurrent networks and LSTMs as mechanisms for sequential state."* [lo4]

---

### Segment 6 — Worked Example B: RNN vs LSTM on Game-Event Sequences (10 min)

**Setup**
- Input sequence: 6 game events (e.g., MOVE, SHOOT, RELOAD, MOVE, MOVE, SHOOT) encoded as one-hot vectors
- Task: predict next action (toy classification)
- Hidden size: 4 units

**Steps traced**
1. Vanilla RNN: unroll 6 steps; show hidden state update equation; highlight where gradient magnitude shrinks across early timesteps
2. LSTM: show cell-state update at step 3 (forget gate near 1, input gate active); contrast gradient flow
3. Side-by-side: which architecture retains the RELOAD event's influence by step 6?
4. Takeaway: rule of thumb for sequence length vs architecture choice

**Learning outcomes served:**
- *"Describe recurrent networks and LSTMs as mechanisms for sequential state."* [lo4]
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

### Segment 7 — Transformer Architecture (15 min)

**Subtopics**
- Motivation: parallelism over sequences; attention as soft lookup
- Self-attention mechanism:
  - Query, Key, Value projections
  - Scaled dot-product attention formula
  - Intuition: each token attends to all others simultaneously
- Multi-head attention: multiple attention subspaces, concatenation
- Positional encoding: why order must be injected explicitly
- Encoder vs decoder roles (conceptual only — no full derivation)
- Games relevance:
  - LLM-driven NPC dialogue (forward reference to Unit 08)
  - Sequence-to-sequence level generation (forward reference to Unit 07)
  - Decision transformers for offline RL (forward reference to Unit 06)
- Honest limitations: data-hungry, compute-heavy — when *not* to reach for a transformer in a game context

**Worked examples:** none (conceptual diagram walkthrough)

**Learning outcomes served:**
- *"Explain the transformer self-attention mechanism at a conceptual level."* [lo4]
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

### Segment 8 — Practical: Regularisation & Optimisers (7 min)

**Subtopics**
- Dropout: training vs inference mode; typical rates
- Batch normalisation: normalising activations; training stability
- Adam optimiser: adaptive learning rates; why it is the practical default over SGD for most game-AI experiments
- Brief mention: weight decay, gradient clipping (relevant for RNNs)
- When these matter: small datasets (dropout), deep networks (batch norm), noisy gradients (Adam + clipping)

**Worked examples:** none

**Learning outcomes served:**
- *"Describe the structure and forward pass of a multilayer perceptron."* [lo4] (completion — training-time behaviour)
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

### Segment 9 — Architecture Selection & Forward Bridge (3 min)

**Subtopics**
- Decision heuristic summary (one slide):
  - Flat feature vector → MLP
  - Spatial / image / grid input → CNN
  - Variable-length sequence / temporal context → LSTM or GRU
  - Long-range dependencies, large-scale sequence modelling → Transformer
- Forward bridge:
  - Unit 06: CNNs feed visual state to RL agents; LSTMs encode partial observability
  - Unit 07: Transformers and RNNs underpin generative content systems
  - Unit 08: LLM-driven dialogue builds on transformer encoder/decoder understanding

**Worked examples:** none

**Learning outcomes served:**
- *"Select an appropriate architecture for a given games-relevant input modality."* [lo2, lo5]

---

## 3. Lab Plan (Tutorial — 120 minutes)

**Overall brief:** Implement a small CNN in PyTorch to classify screenshots of four terrain types from a supplied dataset. Train, evaluate, and experiment with one architectural change.

---

### Stage 1 — Environment check & data loading (15 min)

**Student produces:**
- Verified PyTorch install; dataset loaded and visualised (sample grid of terrain images)
- Class distribution printed; train/validation/test split confirmed

**Assessment mapping:** Prerequisite hygiene; not directly marked, but broken setup prevents all later deliverables.

---

### Stage 2 — Baseline CNN implementation (30 min)

**Student produces:**
- A `nn.Module` subclass implementing: Conv → ReLU → MaxPool → Conv → ReLU → MaxPool → Flatten → FC → Softmax
- Forward pass verified on a single batch (shape checks pass)
- Parameter count printed

**Assessment mapping:**
- Directly exercises *"Design and implement … neural network-based solutions"* [lo5]
- Code forms part of the project's advanced-learning component (Units 04–06 requirement)

---

### Stage 3 — Training loop & logging (25 min)

**Student produces:**
- Training loop with Adam optimiser and cross-entropy loss
- Per-epoch training loss and validation loss logged
- Loss and accuracy curves plotted (matplotlib or equivalent)

**Assessment mapping:**
- Demonstrates understanding of the learning loop (Unit 04 prerequisite; reinforced here)
- Plots are a required deliverable; markers use them to assess [lo4] conceptual understanding

---

### Stage 4 — Evaluation on test set (15 min)

**Student produces:**
- Test-set accuracy figure
- Confusion matrix (4 × 4) with class labels
- Identification of the most-confused terrain pair

**Assessment mapping:**
- Confusion matrix is a required deliverable
- Supports report section justifying technique choices [lo2]

---

### Stage 5 — Architectural experiment (25 min)

**Student produces:**
- One architectural variant (e.g., add a third conv layer, change kernel size from 3×3 to 5×5, add dropout, remove one pooling layer)
- Comparative loss/accuracy plot: baseline vs variant
- Written paragraph (≈150 words) explaining the observed effect and linking it to lecture theory

**Assessment mapping:**
- Written paragraph is a required deliverable
- Directly maps to report requirement (d): *"reflect on limitations and potential improvements"*
- Supports [lo2]: *"Evaluate and compare different AI approaches … and justify their suitability"*

---

### Stage 6 — Wrap-up & peer discussion (10 min)

**Student produces:**
- Brief verbal or written note: which architecture change gave the best result in the room, and why
- Forward-looking question noted: *how would this CNN be used as the visual encoder for an RL agent?* (preview of Unit 06)

**Assessment mapping:** Consolidation; no separate deliverable.

---

### Lab Deliverable Summary

| Deliverable | Format | Maps to assessment requirement |
|---|---|---|
| Training script | `.py` file | Code submission — advanced-learning component |
| Loss & accuracy plots | Image files | Required plot deliverable |
| Confusion matrix | Image file | Required confusion-matrix deliverable |
| Architectural-change paragraph | Plain text / PDF | Report section on limitations & improvements |

---

## 4. References Used

- Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*. MIT Press.
- LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. (1998). Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 86(11), 2278–2324.
- Vaswani, A. et al. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems*, 30.

---

## 5. Gaps — References Needed

- **Dropout (Srivastava et al., 2014)** — the canonical dropout paper is not on the approved list; needed for Segment 8 when citing dropout as a regularisation technique.
- **Batch normalisation (Ioffe & Szegedy, 2015)** — not on the approved list; needed for Segment 8.
- **Adam optimiser (Kingma & Ba, 2015)** — not on the approved list; needed for Segment 8.
- **Decision Transformer (Chen et al., 2021)** — referenced in Segment 7 as a games-relevant transformer application; not on the approved list.
- A **terrain-type screenshot dataset** suitable for the lab (four classes, modest size, redistributable licence) is not specified anywhere in the course materials. The author should supply or identify this dataset before the lab is written.