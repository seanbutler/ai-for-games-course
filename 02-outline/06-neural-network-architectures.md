# Unit 05 — Neural Network Architectures

**One-line summary:** From perceptron to transformer — understand the building blocks that underpin every modern ML application in games.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — Multilayer Perceptrons (20 min)

**Subtopics**
- Single perceptron: weighted sum + activation; geometric interpretation as a hyperplane
- MLP: stacking layers; universal approximation theorem (intuition only)
- Activation functions: sigmoid (vanishing gradient problem), tanh, ReLU, Leaky ReLU — why ReLU dominates
- Weight initialisation: why zero-init fails; Xavier / He initialisation
- Forward pass walkthrough on a small network (2 inputs → 4 hidden → 1 output)

**Worked example 1:** Trace a forward pass through a small MLP classifying game state (player health, enemy distance, ammo count) → action choice; compute output by hand.

**Outcomes served**
- *lo4*: Demonstrate conceptual understanding of neural networks

---

### Segment 2 — Convolutional Neural Networks (30 min)

**Subtopics**
- Motivation: fully connected layers for images are prohibitively large; local structure and translation invariance
- Convolution operation: kernel, stride, padding; output dimension formula
- Pooling: max and average; spatial downsampling
- Feature maps: what different filters learn at different depths
- CNN architecture pattern: Conv → ReLU → Pool → ... → Flatten → FC
- Games applications: processing pixel frames for RL agents; tile-map classification; minimap analysis

**Worked example 2:** Trace a forward pass through a small CNN processing a 16×16 tile-map excerpt — compute spatial dimensions at each layer (Conv 3×3 s1 → Pool 2×2).

**Outcomes served**
- *lo4*, *lo5*: Apply understanding to games-relevant problems

---

### Segment 3 — Recurrent Networks and LSTMs (25 min)

**Subtopics**
- Motivation: sequential data — game event logs, dialogue history, time-series sensor input
- Vanilla RNN: hidden state unrolled through time; vanishing gradient in long sequences
- LSTM: cell state (long-term memory) + hidden state; input, forget, output gates
- GRU: simplified gating, fewer parameters, similar performance
- Games applications: sequence-aware NPC memory, trajectory prediction, anomaly detection in player behaviour

**Worked example 3:** Contrast a vanilla RNN and an LSTM processing a short sequence of game events (see enemy, take cover, shoot, retreat) — show where the LSTM forget gate prevents irrelevant early events from dominating.

**Outcomes served**
- *lo4*

---

### Segment 4 — Transformers and Attention (25 min)

**Subtopics**
- Motivation: RNNs process sequentially; attention allows parallel computation and global dependencies
- Self-attention: query, key, value; attention score computation; softmax normalisation
- Multi-head attention: parallel attention heads capture different relationships
- Positional encoding: injecting sequence order without recurrence
- Encoder vs decoder roles; encoder-only models (BERT-style) vs decoder-only (GPT-style)
- Games relevance: LLM-driven NPC dialogue (Unit 08), decision transformers for offline RL

**Outcomes served**
- *lo4*

---

### Segment 5 — Practical Training Techniques (20 min)

**Subtopics**
- Batch normalisation: normalise per-layer activations; accelerates training, reduces sensitivity to init
- Dropout: randomly zero activations during training; regularisation effect
- Modern optimisers: Adam (adaptive learning rates per parameter) vs SGD with momentum
- Learning rate schedules: warmup, cosine annealing
- Selecting architecture for input modality: grid/image → CNN; sequence → RNN/Transformer; tabular → MLP

**Outcomes served**
- *lo4*, *lo2*: Justify architecture choice for specific problems

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — Dataset inspection | 15 min | Load supplied terrain screenshot dataset; inspect class balance and image dimensions |
| 2 — CNN implementation | 45 min | PyTorch CNN to classify four terrain types; Conv → ReLU → Pool × 2 → FC → Softmax |
| 3 — Train and evaluate | 25 min | Train for fixed epochs; plot training and validation loss; confusion matrix on test set |
| 4 — Architectural experiment | 20 min | Change one architectural parameter (add layer, change kernel size, change pooling); rerun and compare |
| 5 — Write-up | 15 min | Paragraph explaining the effect of the architectural change on accuracy and training dynamics |

**Deliverable:** Training script; loss/accuracy plots; confusion matrix; written paragraph on architectural change.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| CNN architecture correct and compiles | lo4, lo5 | Advanced learning component | 25% |
| Training produces improving loss curves (no obvious bug) | lo5 | Advanced learning component | 25% |
| Confusion matrix computed and correct | lo4 | Report — ML component | 20% |
| Architectural experiment run with correct comparison | lo4, lo2 | Report — critical comparison | 15% |
| Written paragraph with reasoned explanation | lo2 | Report — evaluation | 15% |

---

## References Used

**Gaps — references needed**
- Goodfellow, I., Bengio, Y. & Courville, A. *Deep Learning* (MIT Press, 2016) — MLP, CNN, RNN chapters.
- LeCun, Y. et al. (1998). Gradient-based learning applied to document recognition — CNN seminal paper.
- Vaswani, A. et al. (2017). Attention Is All You Need — transformer architecture.
