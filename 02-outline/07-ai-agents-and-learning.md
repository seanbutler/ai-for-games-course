# Unit 06 — AI Agents and Learning in Games

**One-line summary:** Apply the ML foundations to autonomous game agents — from Q-learning through deep RL to imitation learning — and compare directly against hand-authored decision systems.

---

## Lecture Session Plan — 120 minutes

### Segment 1 — The RL Framework (20 min)

**Subtopics**
- Agent, environment, state, action, reward, policy, value function
- Markov Decision Processes (MDPs): Markov property, transition function, discount factor γ
- Episode vs continuous tasks; sparse vs dense reward
- Why RL for games: environment is the game engine; reward is the score; policy is the AI
- Pitfalls: reward hacking, sim-to-real gap (training in engine ≠ playing with humans)

**Outcomes served**
- *lo4*, *lo5*: Conceptual understanding and application of ML to games

---

### Segment 2 — Tabular RL: Q-Learning (25 min)

**Subtopics**
- Value functions: V(s) and Q(s,a) — expected discounted future reward
- Bellman equation: recursive definition of optimal Q
- Q-learning update rule: temporal difference error; learning rate α
- Exploration vs exploitation: ε-greedy strategy; ε decay schedules
- Limitations of tabular Q: state space must be small and discrete; impractical for most game states

**Worked example 1:** Run Q-learning on a small grid-world (5×5, goal in corner, wall penalty) — trace three update steps manually; show Q-table convergence after many episodes.

**Outcomes served**
- *lo4*, *lo5*

---

### Segment 3 — Deep Q-Networks (DQN) (25 min)

**Subtopics**
- DQN: replace Q-table with a neural network; input = state, output = Q(s,a) for all actions
- Key innovations: experience replay (breaks temporal correlation); target network (stabilises training)
- Atari benchmark: DQN achieving human-level play from raw pixels — significance and limitations
- Extensions: Double DQN, Duelling DQN, Prioritised Experience Replay — brief
- Practical considerations: frame stacking, reward clipping, action repeat

**Worked example 2:** Describe the DQN pipeline for a simple shooter: state (enemy positions, ammo), action space (move/shoot/reload), reward shaping choices; discuss what reward function leads to camping behaviour.

**Outcomes served**
- *lo4*, *lo5*

---

### Segment 4 — Policy Gradient and Actor-Critic (20 min)

**Subtopics**
- Limitation of value-based methods: continuous action spaces
- Policy gradient: directly optimise policy π(a|s;θ); REINFORCE algorithm
- Actor-critic: combine value function (critic) with policy (actor); reduces variance
- Proximal Policy Optimisation (PPO): clipped surrogate objective; stability advantage
- When to use: continuous control (character movement, steering) vs discrete action games

**Outcomes served**
- *lo4*, *lo5*

---

### Segment 5 — Imitation Learning (15 min)

**Subtopics**
- Behavioural cloning: supervised learning on expert demonstrations; distribution shift problem
- DAgger: iterative data collection to correct compounding errors
- Games use case: training NPCs to mimic playtester or designer behaviour
- Comparison to hand-authored BTs: less authoring effort, less predictability, needs data

**Outcomes served**
- *lo4*, *lo2*: Compare classical and ML approaches on same problem

---

### Segment 6 — Classical vs RL Comparison (15 min)

**Subtopics**
- Direct comparison: hand-authored BT guard vs RL-trained agent on same task
- Authoring effort, training cost, interpretability, robustness to level changes
- Hybrid approaches: BT structure with RL leaf nodes; curriculum learning
- Current practice in shipped titles: RL used for specific sub-problems (e.g. movement tuning), not full agent behaviour

**Outcomes served**
- *lo2*: Evaluate and compare; justify suitability for specific problems

---

## Lab Plan — 120 minutes

| Stage | Duration | What students produce |
|---|---|---|
| 1 — Q-learning grid world | 35 min | Tabular Q-learning agent navigating a supplied grid world; plot episode reward over training |
| 2 — Extend to DQN | 45 min | Replace Q-table with a small PyTorch MLP; add experience replay buffer; retrain on same grid world |
| 3 — Comparison | 20 min | Table: tabular Q vs DQN on convergence speed, final reward, sensitivity to hyperparameters |
| 4 — Write-up | 20 min | Paragraph comparing RL agent to the Unit 03 BT guard: what did RL get right/wrong? |

**Deliverable:** Q-learning and DQN implementations; results table; written comparison paragraph.

**Marking rubric**

| Task | LO | Project requirement | Marks |
|---|---|---|---|
| Tabular Q-learning converges on supplied grid world | lo4, lo5 | Advanced learning component | 25% |
| DQN with experience replay trains correctly | lo5 | Advanced learning component | 30% |
| Results table with valid comparison | lo4, lo2 | Report — critical comparison | 20% |
| Written paragraph comparing RL to BT | lo2 | Report — critical comparison | 25% |

---

## References Used

**Gaps — references needed**
- Sutton, R. S. & Barto, A. G. *Reinforcement Learning: An Introduction* (2nd ed., MIT Press, 2018) — MDPs, Q-learning, policy gradient, actor-critic.
- Mnih, V. et al. (2015). Human-level control through deep reinforcement learning. *Nature*, 518 — DQN paper.
- Silver, D. et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529 — AlphaGo.
