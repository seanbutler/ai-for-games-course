---
generated_by: generate.py
stage: outline
model: claude-sonnet-4-6
spec_sha: 7d26897
input_hash: efb68f3a20066e1e
generated_at: 2026-06-16T14:27:42+00:00
---

# Unit 06 — AI Agents and Learning in Games

**One-line summary:** Formalises game agent behaviour as Markov Decision Processes, builds from tabular Q-learning to Deep Q-Networks and policy gradients, and closes the classical-vs-ML comparison arc with a critical evaluation of RL in shipped titles.

---

## 1. Timed Session Plan (Lecture — 120 minutes)

| # | Segment | Minutes |
|---|---------|---------|
| 1 | Framing: from authored decisions to learned behaviour | 10 |
| 2 | Markov Decision Processes | 20 |
| 3 | Value functions and Q-learning | 25 |
| 4 | Deep Q-Networks (DQN) | 25 |
| 5 | Policy gradient methods | 15 |
| 6 | Case studies: AlphaGo/Zero, OpenAI Five | 15 |
| 7 | Practical limits and classical comparison | 10 |
| **Total** | | **120** |

---

## 2. Segment Detail

### Segment 1 — Framing: from authored decisions to learned behaviour (10 min)

**Subtopics**
- Recap Unit 03 FSM/BT: designer specifies every transition explicitly
- Motivation: what happens when the state space is too large or too dynamic to author by hand?
- Learning outcomes as a spectrum: hand-authored → search-based → learned policy
- Unit roadmap; where this fits in the classical-first arc

**Worked examples**
- None (framing only); brief callback to Unit 03 enemy FSM as the running comparison object

**Learning outcomes served**
- *"Compare RL agents with classical decision systems on the same game problem."* [lo2]
- *"Critically evaluate the practical limits of RL in shipped game titles."* [lo2, lo6]

---

### Segment 2 — Markov Decision Processes (20 min)

**Subtopics**
- Formal definition: tuple ⟨S, A, T, R, γ⟩
  - States S, actions A
  - Transition function T(s, a, s′) — stochastic vs deterministic
  - Reward function R(s, a, s′)
  - Discount factor γ: intuition and effect on agent horizon
- Markov property: why it matters and when it is violated in games (partial observability)
- Mapping a game scenario onto an MDP: grid world walkthrough
  - States = cells; actions = {N, S, E, W}; rewards = goal +1, pit −1, step −0.01
- Episode vs continuing tasks; terminal states

**Worked examples**
- Grid-world MDP instantiation (4-state toy used again in Segment 3)

**Learning outcomes served**
- *"Formalise a game scenario as a Markov Decision Process."* [lo4, lo5]

---

### Segment 3 — Value functions and Q-learning (25 min)

**Subtopics**
- State-value function V(s): expected discounted return from s under policy π
- Action-value function Q(s, a): expected return after taking a in s, then following π
- Bellman equations: recursive decomposition of V and Q
- Optimal Bellman equation; greedy policy extraction from Q*
- Tabular Q-learning update rule:
  - Q(s,a) ← Q(s,a) + α[r + γ max_{a′} Q(s′,a′) − Q(s,a)]
  - Parameters: learning rate α, exploration ε-greedy
- Convergence conditions (tabular, finite MDP, decaying ε and α)
- Limitations of tabular approach: state-space explosion in real games

**Worked examples**
- **Worked Example 1 (primary):** Trace Q-learning updates on the 4-state grid world
  - Show Q-table initialisation (all zeros)
  - Step through 3–4 episodes manually; show Q-values converging toward optimal
  - Highlight role of γ in propagating reward backwards

**Learning outcomes served**
- *"Explain Q-learning and the Deep Q-Network algorithm."* [lo4, lo5]
- *"Formalise a game scenario as a Markov Decision Process."* [lo4, lo5]

---

### Segment 4 — Deep Q-Networks (DQN) (25 min)

**Subtopics**
- Function approximation: replace Q-table with neural network Q(s, a; θ)
- Input representation for games: raw pixels vs feature vectors; frame stacking (4 frames)
- Two instabilities introduced by naïve deep Q-learning:
  1. Correlated consecutive samples → breaks i.i.d. assumption
  2. Moving target: Q-network and target both change each step
- Experience replay buffer
  - Store transitions (s, a, r, s′, done) in circular buffer
  - Sample random mini-batches; breaks temporal correlation
- Target network
  - Separate network θ⁻ updated every C steps (hard copy) or via soft update
  - Stabilises the regression target y = r + γ max_{a′} Q(s′,a′; θ⁻)
- DQN training loop overview (collect → store → sample → update → sync)
- Extensions worth naming (Double DQN, Dueling DQN, Prioritised Replay) — forward references only

**Worked examples**
- **Worked Example 2 (primary):** Replay buffer mechanics
  - Concrete illustration: buffer of capacity 5, show what happens to temporal correlation with sequential vs random sampling
  - Diagram: training loop with replay buffer and target network annotated

**Learning outcomes served**
- *"Explain Q-learning and the Deep Q-Network algorithm."* [lo4, lo5]
- *"Formalise a game scenario as a Markov Decision Process."* [lo4, lo5]

---

### Segment 5 — Policy gradient methods (15 min)

**Subtopics**
- Value-based vs policy-based distinction: Q-learning outputs values; policy gradient directly parameterises π(a|s; θ)
- REINFORCE algorithm: gradient estimate ∇θ log π(a|s; θ) · G_t
  - Intuition: increase probability of actions that led to high return
  - Variance problem; baseline subtraction
- Actor-critic overview: actor = policy network, critic = value network; reduces variance
- When to prefer policy gradient over DQN
  - Continuous action spaces (steering, aiming)
  - Stochastic policies (bluffing, mixed strategies)
- Forward reference: Proximal Policy Optimisation (PPO) used in OpenAI Five (Segment 6)

**Worked examples**
- Conceptual walkthrough: single REINFORCE update step on a 2-action game choice (no full trace — time-limited)

**Learning outcomes served**
- *"Describe policy gradient methods and contrast them with value-based approaches."* [lo4]

---

### Segment 6 — Case studies: AlphaGo/AlphaZero and OpenAI Five (15 min)

**Subtopics**
- **AlphaGo / AlphaZero**
  - Why Go defeated classical search (branching factor ~250, positional evaluation hard)
  - AlphaGo pipeline: supervised learning from human games → RL self-play → MCTS guided by policy + value networks
  - AlphaZero: removes human data; pure self-play; generalises to Chess and Shogi
  - Key insight: MCTS + learned evaluation function; neither alone is sufficient
- **OpenAI Five (Dota 2)**
  - Scale: 180 years of self-play per day; PPO; team reward
  - Curriculum learning: start with shorter game horizons, gradually extend
  - Multi-agent non-stationarity: opponents change as all agents learn simultaneously
  - Emergent strategies vs designed behaviours
- **Game-playing benchmarks overview**
  - Atari (DQN baseline), StarCraft II (AlphaStar), NetHack — brief
  - What these benchmarks do and do not tell us about game AI in production

**Worked examples**
- Diagram: AlphaGo MCTS rollout annotated with policy network (prior) and value network (leaf evaluation)

**Learning outcomes served**
- *"Explain Q-learning and the Deep Q-Network algorithm."* [lo4, lo5] (DQN Atari context)
- *"Describe policy gradient methods and contrast them with value-based approaches."* [lo4] (PPO in OpenAI Five)
- *"Critically evaluate the practical limits of RL in shipped game titles."* [lo2, lo6]

---

### Segment 7 — Practical limits and classical comparison (10 min)

**Subtopics**
- Sample inefficiency: millions of frames to match human-level; cost in compute and wall-clock time
- Reward shaping: difficulty of specifying what "good play" means; reward hacking examples
- Non-stationarity in multi-agent settings
- Designer control and explainability: RL agent behaviour is opaque; FSM/BT is auditable
- Deployment realities: most shipped titles still use classical AI; RL used in training tools, not runtime agents (exceptions: AlphaStar, some NPC research prototypes)
- Decision framework: when to choose RL over FSM/BT
  - Large state space, no good hand-authored heuristic, offline training budget available
- Closing the arc: Unit 03 FSM vs Unit 06 RL agent on the same enemy scenario — summary comparison table

**Worked examples**
- Comparison table: FSM vs Q-learning/DQN on axes of design effort, sample cost, explainability, runtime cost, designer control

**Learning outcomes served**
- *"Compare RL agents with classical decision systems on the same game problem."* [lo2]
- *"Critically evaluate the practical limits of RL in shipped game titles."* [lo2, lo6]

---

## 3. Lab Plan (Tutorial — 120 minutes)

### Overview
Students train a DQN agent on a supplied minimal 2D game environment using a provided PyTorch scaffold, then compare the learned agent's behaviour with a hand-authored FSM.

---

### Stage 1 — Environment familiarisation (15 min)

**What students do**
- Run the supplied grid-world / simple arcade environment
- Inspect the observation space, action space, and reward signal
- Confirm the MDP mapping: identify S, A, R, γ in the code

**What students produce**
- Annotated MDP diagram (handwritten or digital) submitted as part of the lab record

**Assessment mapping**
- Grounds *"Formalise a game scenario as a Markov Decision Process"* [lo4, lo5]; provides evidence for report section on ML technique design

---

### Stage 2 — Baseline DQN run (25 min)

**What students do**
- Run the provided training scaffold with default hyperparameters
- Observe learning curve (episode reward vs training step)
- Inspect replay buffer size and target-network update frequency in the config

**What students produce**
- Baseline learning-curve plot (saved as PNG/CSV)

**Assessment mapping**
- Demonstrates correct application of DQN [lo5]; plot feeds directly into the written comparison deliverable

---

### Stage 3 — Hyperparameter experiment (35 min)

**What students do**
- Select **one** hyperparameter to vary: replay buffer size OR target-network update frequency
- Run two additional training runs (low setting vs high setting)
- Record learning curves for all three runs on the same axes

**What students produce**
- Two additional learning-curve plots; brief inline notes on observed differences

**Assessment mapping**
- Develops ability to *"Evaluate and compare different AI approaches"* [lo2]; supports report section (c): critical comparison

---

### Stage 4 — FSM comparison and written reflection (45 min)

**What students do**
- Load (or recall from Unit 03 lab) the equivalent hand-authored FSM for the same game scenario
- Observe both agents playing in the environment side by side (or sequentially)
- Write approx. 300-word comparison covering:
  - Emergent vs authored behaviour: what the RL agent does that the FSM does not (and vice versa)
  - Sample cost and training time vs FSM authoring time
  - Designer control and predictability
  - Which approach is preferable for this specific scenario, and why

**What students produce**
- Written comparison (~300 words) + all learning-curve plots

**Assessment mapping**

| Deliverable | Project report section | Learning outcome |
|---|---|---|
| MDP diagram | Report (a): architecture of each AI component | lo4 |
| Learning-curve plots | Report (c): classical vs ML comparison | lo2, lo5 |
| Written comparison | Report (b) & (c): technique justification and comparison | lo2, lo6 |
| Trained agent weights | Code deliverable: working RL component | lo5 |

---

## 4. References Used

- Sutton, R. S. & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
- Mnih, V. et al. (2015). Human-level control through deep reinforcement learning. *Nature*, 518, 529–533.
- Silver, D. et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529, 484–489.
- Millington, I. & Funge, J. (2009). *Artificial Intelligence for Games* (2nd ed.). Morgan Kaufmann.

---

## 5. Gaps — References Needed

| Gap | Where needed | Notes for author |
|---|---|---|
| OpenAI Five / Dota 2 technical report | Segment 6 | The OpenAI Five paper (Berner et al., 2019, arXiv:1912.06680) is the canonical source; not on the approved list. |
| AlphaStar (StarCraft II) | Segment 6 (benchmarks) | Vinyals et al. (2019), *Nature* 575, 350–354; not on the approved list. |
| REINFORCE / policy gradient foundations | Segment 5 | Williams (1992) is the original REINFORCE paper; Sutton & Barto (2018) covers it but a direct citation to Williams may be preferred for academic rigour. Confirm whether Sutton & Barto alone is sufficient. |
| PPO (Proximal Policy Optimisation) | Segment 5 forward-reference, Segment 6 | Schulman et al. (2017), arXiv:1707.06347; not on the approved list. |
| Curriculum learning in RL | Segment 6 (OpenAI Five) | Bengio et al. (2009) is the standard reference; not on the approved list. |