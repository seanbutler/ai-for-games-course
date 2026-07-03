# Unit 04 — Foundations of Machine Learning

**One-line summary:** Establish the vocabulary and mental model — learning paradigms, the training loop, gradient descent — that every subsequent ML unit builds on.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — Why ML in Games? (15 min)

**Subtopics**
- Problems where classical hand-authoring breaks down: too many states, too much variation, data available
- Problems where classical is still better: determinism required, small state space, no training data
- The classical-to-ML spectrum: from hand-authored rules to fully learned policies
- Where ML appears in modern games: NPC behaviour, PCG, rendering enhancement, playtesting

**Outcomes served**
- *lo2*: Evaluate and compare different AI approaches; justify suitability
- *lo4*: Demonstrate conceptual understanding of modern ML

---

### Segment 2 — Learning Paradigms (20 min)

**Subtopics**
- Supervised learning: labelled input-output pairs; prediction and classification
- Unsupervised learning: finding structure without labels; clustering, dimensionality reduction
- Reinforcement learning: agent, environment, reward signal, policy
- Game-relevant use cases per paradigm: supervised for move prediction; unsupervised for player segmentation; RL for agent training
- Self-supervised and imitation learning — brief mention, forward reference to Unit 06

**Outcomes served**
- *lo4*: Demonstrate conceptual understanding of ML paradigms

---

### Segment 3 — The Learning Loop (25 min)

**Subtopics**
- Data: features, labels, dataset splits (train / validation / test) — why held-out evaluation matters
- Model: parameterised function mapping inputs to outputs
- Loss function: measuring prediction error (MSE, cross-entropy)
- Optimisation: minimising loss by adjusting parameters
- Gradient descent: intuition from loss surface; batch, stochastic, mini-batch variants
- Learning rate: too high (divergence) vs too low (slow convergence)

**Worked example 1:** Frame predicting an enemy's next move as supervised classification — define features (player position, enemy health, cover state), label (move direction), loss function, and evaluation metric.

**Outcomes served**
- *lo4*

---

### Segment 4 — Backpropagation (20 min)

**Subtopics**
- Computation graphs: operations as nodes, values flowing forward
- Chain rule applied to a graph: gradient flows backward
- Intuition only — no full derivation; goal is to understand why deep networks can be trained
- Vanishing and exploding gradients: brief mention, forward reference to Unit 05 (LSTMs, batch norm)

**Worked example 2:** Walk through one gradient descent step on a toy two-parameter loss surface — show how the partial derivatives point toward the minimum and how learning rate scales the step.

**Outcomes served**
- *lo4*

---

### Segment 5 — Overfitting, Generalisation, and Failure Modes (20 min)

**Subtopics**
- Bias-variance trade-off: high bias = underfitting; high variance = overfitting
- Regularisation overview: L1/L2 weight penalty, dropout (forward reference to Unit 05)
- Data augmentation as a regularisation strategy
- Evaluating a model: confusion matrix, precision/recall, why accuracy alone misleads
- Failure mode in games: model trained on one map fails on another — distribution shift

**Outcomes served**
- *lo4*, *lo2*

---

### Segment 6 — Where ML Fits in the Module Arc (20 min)

**Subtopics**
- Unit 05: neural architectures (the model)
- Unit 06: agents and RL (the loop applied to behaviour)
- Unit 07: generative models (the loop applied to content)
- Unit 08: modern applications (what all of this enables in production)
- Recap of classical vs ML comparison table built so far

**Outcomes served**
- *lo2*, *lo4*

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — Data exploration | 20 min | Load supplied dataset of recorded player trajectories; inspect feature distributions and class balance |
| 2 — Train logistic regression | 35 min | Scikit-learn logistic regression to predict turn direction at junctions; train/val/test split |
| 3 — Regularisation experiment | 25 min | Repeat with two different regularisation strengths (C=0.01 and C=100); record validation accuracy |
| 4 — Evaluation and write-up | 20 min | Confusion matrix on test set; written paragraph on what the matrix reveals about failure modes |
| 5 — Discussion | 20 min | Would a classical hand-authored rule do better here? When and why? |

**Deliverable:** Training script; results table (regularisation strength × accuracy); written paragraph on confusion matrix findings.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| Correct train/val/test split and no data leakage | lo4 | Report — ML component | 20% |
| Logistic regression trains and produces predictions | lo4, lo5 | Advanced learning component | 30% |
| Regularisation experiment with correct results | lo4 | Report — ML component | 20% |
| Confusion matrix computed and interpreted correctly | lo4, lo2 | Report — critical comparison | 15% |
| Written paragraph on failure modes | lo2 | Report — evaluation | 15% |

---

## References Used

**Gaps — references needed**
- Goodfellow, I., Bengio, Y. & Courville, A. *Deep Learning* (MIT Press, 2016) — gradient descent, backpropagation, regularisation.
- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach* (4th ed.) — ML foundations chapter.
