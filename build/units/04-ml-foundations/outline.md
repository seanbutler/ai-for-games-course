---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: d1d43083b3a83685
generated_at: 2026-06-16T14:25:24+00:00
---

# Unit 04 — Foundations of Machine Learning

**One-line summary:** Establishes the vocabulary, mental models, and failure-mode awareness that underpin every ML technique in Units 05–08, grounded in game-relevant problem framings.

---

## 1. Timed Session Plan (Lecture — 120 minutes)

| # | Segment | Minutes |
|---|---------|---------|
| 1 | Scene-setting: where ML sits in the module | 10 |
| 2 | ML paradigms: supervised, unsupervised, reinforcement learning | 20 |
| 3 | The learning loop: data → model → loss → optimisation | 20 |
| 4 | **Worked Example A** — enemy move prediction as supervised classification | 15 |
| 5 | Gradient descent: batch, SGD, mini-batch; learning rate intuition | 20 |
| 6 | Backpropagation: chain rule on computation graphs (conceptual) | 15 |
| 7 | **Worked Example B** — one gradient descent step on a toy loss surface | 10 |
| 8 | Overfitting, underfitting, bias-variance trade-off; regularisation overview | 15 |
| 9 | Train / validation / test splits and held-out evaluation | 10 |
| 10 | Wrap-up: when *not* to use ML — classical methods still win | 5 |
| | **Total** | **120** |

---

## 2. Segment Detail

### Segment 1 — Scene-setting: where ML sits in the module (10 min)

**Subtopics**
- Recap of Units 01–03: hand-authored, deterministic, interpretable
- The gap ML fills: learning from data rather than explicit rules
- Module roadmap: this unit → vocabulary; Units 05–08 → specific architectures and applications
- Forward-reference: every subsequent ML unit is an instance of the learning loop introduced here

**Worked examples:** none

**Learning outcomes served**
- *"Identify appropriate ML problem framings for given game-development tasks."* [lo2, lo4]

---

### Segment 2 — ML paradigms: supervised, unsupervised, reinforcement learning (20 min)

**Subtopics**
- Supervised learning: labelled data, input–output mapping, classification vs regression
- Unsupervised learning: structure discovery, clustering, dimensionality reduction; game uses (player segmentation, asset clustering)
- Reinforcement learning: agent, environment, reward signal, policy; contrast with supervised
- Decision boundary between paradigms: what determines which to reach for
- Game-relevant use-case examples for each paradigm (brief; full treatment in later units)

**Worked examples:** none (examples embedded as brief illustrations within the taxonomy)

**Learning outcomes served**
- *"Describe the supervised, unsupervised, and reinforcement learning paradigms and their game-relevant use cases."* [lo4]

---

### Segment 3 — The learning loop: data → model → loss → optimisation (20 min)

**Subtopics**
- Four components of the loop and their roles
- Data: representation, features, labels; garbage-in/garbage-out
- Model: hypothesis class (linear, non-linear); capacity
- Loss function: what it measures; examples — cross-entropy, MSE; why choice matters
- Optimisation: minimising loss as the engine of learning
- How the loop closes: iterative parameter update

**Worked examples:** none (loop introduced abstractly here; instantiated in Worked Example A)

**Learning outcomes served**
- *"Explain gradient descent and backpropagation at a conceptual level."* [lo4]
- *"Identify appropriate ML problem framings for given game-development tasks."* [lo2, lo4]

---

### Segment 4 — Worked Example A: enemy move prediction as supervised classification (15 min)

**Worked example**
- *"Frame predicting an enemy's next move as a supervised classification problem: features, labels, loss function, and evaluation metric."*
- Step-by-step walkthrough:
  - Define the game scenario (e.g. turn-based tactical game)
  - Choose features: player position delta, health ratio, cover boolean, etc.
  - Define labels: discrete action classes (attack, retreat, flank, hold)
  - Select loss: categorical cross-entropy; explain why
  - Choose evaluation metric: accuracy, then motivate confusion matrix
  - Identify what "training data" means here (recorded game logs)
  - Note: same problem could be solved with a decision tree or FSM — why might ML be preferred or not?

**Learning outcomes served**
- *"Identify appropriate ML problem framings for given game-development tasks."* [lo2, lo4]
- *"Describe the supervised, unsupervised, and reinforcement learning paradigms and their game-relevant use cases."* [lo4]

---

### Segment 5 — Gradient descent: batch, SGD, mini-batch; learning rate intuition (20 min)

**Subtopics**
- Loss surface as a landscape; parameters as position on that surface
- Gradient: direction of steepest ascent; negative gradient for descent
- Batch gradient descent: full dataset per update; stable but slow
- Stochastic gradient descent (SGD): one sample per update; noisy but fast
- Mini-batch: practical compromise; typical batch sizes in games contexts
- Learning rate: too large → divergence; too small → slow convergence; intuition via loss curve shapes
- Brief mention of adaptive optimisers (Adam) as forward-reference to Unit 05

**Worked examples:** feeds directly into Worked Example B

**Learning outcomes served**
- *"Explain gradient descent and backpropagation at a conceptual level."* [lo4]

---

### Segment 6 — Backpropagation: chain rule on computation graphs (conceptual) (15 min)

**Subtopics**
- Computation graph: nodes as operations, edges as data flow
- Forward pass: computing the loss
- Backward pass: propagating gradients from loss back to parameters
- Chain rule: how gradients compose through the graph
- Emphasis: conceptual understanding, not full symbolic derivation
- Why this matters: every deep learning framework (PyTorch, TensorFlow) implements this automatically
- Common misconception: backprop is not "the learning" — it is gradient *computation*; gradient descent is the update

**Worked examples:** none (conceptual; Worked Example B follows immediately)

**Learning outcomes served**
- *"Explain gradient descent and backpropagation at a conceptual level."* [lo4]

---

### Segment 7 — Worked Example B: one gradient descent step on a toy loss surface (10 min)

**Worked example**
- *"Walk through one gradient descent step on a toy loss surface, showing how the learning rate affects convergence."*
- Step-by-step walkthrough:
  - Toy problem: single parameter θ, loss L(θ) = (θ − 3)²
  - Compute gradient analytically: dL/dθ = 2(θ − 3)
  - Starting point θ₀ = 0; compute gradient value
  - Apply update rule: θ₁ = θ₀ − η · dL/dθ
  - Show result for η = 0.1 (converging), η = 1.0 (oscillating), η = 1.5 (diverging)
  - Sketch loss curves for each; connect to practical advice on learning rate selection
  - Bridge: in a neural network, this same step happens for thousands of parameters simultaneously via backprop

**Learning outcomes served**
- *"Explain gradient descent and backpropagation at a conceptual level."* [lo4]

---

### Segment 8 — Overfitting, underfitting, bias-variance trade-off; regularisation overview (15 min)

**Subtopics**
- Underfitting (high bias): model too simple; fails on training data
- Overfitting (high variance): model memorises training data; fails on new data
- Bias-variance trade-off: the fundamental tension in model capacity
- Diagnosing via training vs validation loss curves
- Regularisation overview:
  - L2 (weight decay): penalises large weights
  - L1: promotes sparsity
  - Dropout: forward-reference to Unit 05
  - Early stopping: practical and widely used
- Game-specific framing: overfitting to a particular player's behaviour; generalisation to new players

**Worked examples:** none (concepts illustrated with loss-curve sketches)

**Learning outcomes served**
- *"Articulate bias-variance trade-off and common failure modes (overfitting, underfitting)."* [lo4]

---

### Segment 9 — Train / validation / test splits and held-out evaluation (10 min)

**Subtopics**
- Why a single dataset is insufficient: the evaluation contamination problem
- Three-way split: roles of train, validation, and test sets
- Validation set: hyperparameter tuning (e.g. regularisation strength, learning rate)
- Test set: final, untouched evaluation; report this number only once
- Cross-validation: brief mention; when it is worth the cost
- Game context: temporal splits for trajectory data (train on early sessions, test on later)
- Direct link to tutorial task: students will implement this split

**Worked examples:** none

**Learning outcomes served**
- *"Articulate bias-variance trade-off and common failure modes (overfitting, underfitting)."* [lo4]
- *"Identify appropriate ML problem framings for given game-development tasks."* [lo2, lo4]

---

### Segment 10 — Wrap-up: when not to use ML — classical methods still win (5 min)

**Subtopics**
- Checklist: data availability, interpretability requirements, latency constraints, determinism needs
- Cases where FSMs, BTs, or A* remain the right answer
- ML as a complement, not a replacement, for classical game AI
- Forward-reference: Units 05–08 will revisit this comparison for each technique
- One-sentence preview of Unit 05 (neural networks)

**Worked examples:** none

**Learning outcomes served**
- *"Identify appropriate ML problem framings for given game-development tasks."* [lo2, lo4]

---

## 3. Lab Plan (Tutorial — 120 minutes)

### Overview

Students apply the learning loop end-to-end on a concrete game-data task using logistic regression — the simplest instantiation of supervised learning — before neural networks are introduced in Unit 05.

---

### Stage 1 — Data exploration (20 min)

**What students do**
- Load the supplied dataset of recorded player trajectories (CSV format; columns: position delta x/y, speed, junction type, turn label)
- Inspect class balance, feature distributions, missing values
- Produce a brief summary: number of samples, feature ranges, class ratio

**What students produce**
- Printed summary statistics and at least one visualisation (e.g. scatter plot of features coloured by class label)

**Assessment mapping**
- Grounds the evaluation discussion required in the project report (LO2, LO4)

---

### Stage 2 — Train / validation / test split and baseline (15 min)

**What students do**
- Implement an 80/10/10 train/validation/test split (random seed fixed for reproducibility)
- Establish a majority-class baseline accuracy
- Record baseline; motivate why a model must beat this

**What students produce**
- Split indices saved; baseline accuracy printed

**Assessment mapping**
- Demonstrates understanding of held-out evaluation (LO4)

---

### Stage 3 — Train logistic regression with two regularisation strengths (30 min)

**What students do**
- Train two logistic regression models using scikit-learn (or equivalent):
  - Model A: weak regularisation (e.g. C = 10.0 in sklearn convention)
  - Model B: strong regularisation (e.g. C = 0.01)
- Evaluate both on the validation set
- Record accuracy for each

**What students produce**
- Training script (Python)
- Results table: regularisation strength × validation accuracy

**Assessment mapping**
- Directly exercises bias-variance trade-off understanding (LO4); results table feeds into the written paragraph deliverable

---

### Stage 4 — Confusion matrix analysis (20 min)

**What students do**
- Generate confusion matrices for both models on the validation set
- Identify which class is most often misclassified and in which direction
- Hypothesise why (link back to feature distributions from Stage 1)

**What students produce**
- Two confusion matrix plots (or printed tables)
- Annotations identifying the dominant error type

**Assessment mapping**
- Practises evaluation and failure-mode analysis required in the project report (LO2, LO4)

---

### Stage 5 — Final evaluation and written paragraph (25 min)

**What students do**
- Select the better model based on validation accuracy
- Evaluate it once on the held-out test set
- Write one paragraph (≈150 words) explaining:
  - What the confusion matrix reveals about the model's failure mode
  - Whether the failure mode matters in a game context (e.g. is a false left worse than a false right?)
  - Which regularisation strength performed better and why

**What students produce**
- Test-set accuracy figure
- Written paragraph (submitted alongside the script)

**Assessment mapping**
- Written justification mirrors the report requirement to explain technique choices and failure modes (LO2, LO4, LO6)

---

### Stage 6 — Reflection and discussion (10 min)

**What students do**
- Group discussion (tutor-led): could this problem have been solved with a decision tree or hand-authored rules? What would be lost or gained?
- Forward-reference: how would replacing logistic regression with a neural network change the workflow?

**What students produce**
- No formal deliverable; verbal participation

**Assessment mapping**
- Reinforces the classical-vs-ML comparison expected in the project report (LO2)

---

### Lab Deliverable Summary

| Item | Format | Maps to assessment |
|------|--------|--------------------|
| Training script | `.py` file | LO3 (implementation), LO5 (applied ML) |
| Results table | In script output or notebook | LO4 (bias-variance understanding) |
| Confusion matrix plots/tables | Inline or saved figures | LO4 (failure-mode analysis) |
| Written paragraph | Plain text or PDF | LO2 (comparison and justification), LO4, LO6 |

---

## 4. References Used

- Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*. MIT Press.
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

---

## 5. Gaps — References Needed

- **Scikit-learn documentation** — the tutorial relies on scikit-learn's `LogisticRegression` API; a citable reference (e.g. Pedregosa et al., 2011, JMLR) is needed for the lab handout. Not present in the approved reference list.
- **Bias-variance trade-off primary source** — Geman et al. (1992) or Hastie, Tibshirani & Friedman (*The Elements of Statistical Learning*) would be the canonical citation for the formal bias-variance decomposition. Neither is on the approved list.
- **Supplied dataset** — the tutorial brief references "a supplied dataset of recorded player trajectories"; the author needs to confirm this dataset exists, is accessible on the module platform, and has a citable or describable provenance.