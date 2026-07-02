# Marking Guidance -- Staff

**Module:** WM9SL-15 AI and Games  
**Assessment:** Game AI Implementation  
**Weight:** 100% | **Length:** 4000 words report + code  
**Deadline:** 31st May 2026  
**Audience:** Markers and moderators only -- do not distribute to students

---

## Marking Principles

This is a single-component, 100% project assessment at Level 7 (M-level). All six learning outcomes are assessed. The report is the primary evidence vehicle: code demonstrates capability, but understanding is evidenced in writing. Markers must read the report and run the code; neither alone is sufficient.

Students are on Warwick WMG MSc Games Engineering -- they are competent C++ programmers. Expectations for implementation quality and technical precision in the report are high. Vague or imprecise language in the report should be penalised under the design and evaluation criteria.

---

## Learning Outcome Mapping

| LO | Description | Primary criterion |
|---|---|---|
| lo1 | Critically analyse traditional game AI including pathfinding, decision systems, behaviour modelling | Foundation correctness; Design and analysis |
| lo2 | Evaluate and compare AI approaches; justify suitability | Design and analysis; Evaluation and reflection |
| lo3 | Design and implement classical game AI algorithms | Foundation correctness; Advanced quality |
| lo4 | Demonstrate conceptual understanding of modern ML | Advanced quality (ML option); Evaluation and reflection |
| lo5 | Develop and apply neural network-based solutions | Advanced quality (ML option) |
| lo6 | Critically assess role of modern AI in game development | Evaluation and reflection |

---

## Criterion 1 -- Foundation Implementation Correctness (30%)

Markers must build and run the submission. Note in comments if the build failed.

**What to look for:**

- **Pathfinding:** A* or equivalent. Check: correct open/closed set management, admissible heuristic, produces optimal or near-optimal paths on supplied test cases. Accept tile grid, waypoint graph, or navmesh. Partial credit if algorithm is present but not integrated into the game environment.
- **Decision system:** FSM, BT, or equivalent. Check: states/nodes correctly implemented, transitions or tick semantics correct, system responds appropriately to world state changes. A BT must use the tick protocol (SUCCESS/FAILURE/RUNNING). An FSM must have explicit transitions.
- **Sensing/perception:** At minimum a range check feeding into the decision system. Full marks require the sensor output to visibly drive agent behaviour. A range sensor in isolation with no connection to decisions is partial credit.

**Descriptor guidance:**

| Band | Mark range | Description |
|---|---|---|
| High distinction | 85-100% | All three components correct, integrated, and cleanly architected. Code is readable and structured. |
| Distinction | 70-84% | All three present and correct. Minor integration issues or code quality concerns. |
| Merit | 60-69% | All three present; one has a functional defect that does not prevent demonstration of the technique. |
| Pass | 50-59% | All three present; one or two have functional defects. Or two present and fully correct. |
| Marginal fail | 40-49% | One Foundation component absent or the submission does not build. |
| Fail | 0-39% | Two or more Foundation components absent or non-functional. |

---

## Criterion 2 -- Advanced Implementation Quality (25%)

Students choose at least one Classical AI and at least one ML Advanced technique. Reward ambition: a student who attempts two Advanced techniques and succeeds at one should score higher than a student who attempts one and barely meets the minimum bar.

**Classical AI options -- what to look for:**

- *Hierarchical pathfinding:* Must demonstrate measurable improvement (query time or expansion count) with results reported. Implementation without results is partial credit.
- *Navigation mesh:* Must be usable for pathfinding, not just displayed. Dynamic obstacle handling requires evidence it works.
- *Behaviour tree with blackboard:* Must demonstrate blackboard read/write decoupling perception from decision logic. Subtree reuse must be demonstrated with at least two agents or contexts sharing a subtree.
- *Utility AI:* Response curves must be non-trivial (not just linear). Multi-attribute scoring and normalisation expected. Agent behaviour must visibly reflect the continuous trade-off.
- *GOAP/STRIPS:* Planner must compute sequences at runtime, not pre-authored. Demonstrate at least two different start states producing different plans.

**ML options -- what to look for:**

- *Trained network:* Training data, loss curve, and test accuracy must be reported. Architecture must be justified for the problem (not just "I used a neural network").
- *RL agent:* Learning curve required. Policy analysis must describe what the agent learned to do and where it fails.
- *CNN/RNN/Transformer:* Architecture choice must be argued: why this type for this problem? Results compared to a simpler baseline.
- *Neural PCG:* Generated output must be evaluated against a baseline (random, rule-based, or human-authored). Quality metric must be defined and argued.

**Descriptor guidance:**

| Band | Mark range | Description |
|---|---|---|
| High distinction | 85-100% | At least one Classical and one ML technique, both correct and well-integrated. Results reported and analysed. |
| Distinction | 70-84% | At least one Classical and one ML technique, both functional. Results present. Minor gaps in analysis. |
| Merit | 60-69% | One Classical and one ML technique present. One is fully functional; the other has a defect but demonstrates the core idea. |
| Pass | 50-59% | One Advanced technique (of either type) present and functional. Minimum bar met but only just. |
| Marginal fail | 40-49% | Advanced technique attempted but not functional, or results not reported. |
| Fail | 0-39% | No Advanced technique present. |

---

## Criterion 3 -- Report: Design Justification and Analysis (25%)

This criterion assesses lo1 and lo2 most directly. Look for evidence that the student understands why they made the choices they made, not just what they did.

**Positive indicators:**
- Explicit consideration of at least one alternative approach with reasoned rejection
- Design decisions derived from stated constraints of the game environment (not just "A* is good for pathfinding")
- References to lecture content or external literature that are used to support an argument, not just cited in passing
- Architectural diagrams or pseudocode that illuminate structure (not reproduced source code)

**Negative indicators:**
- Purely descriptive writing ("I implemented A*, which works by...")
- References cited but not engaged with
- No comparison to alternatives
- Design choices presented as obvious or default without justification

**Descriptor guidance:**

| Band | Mark range | Description |
|---|---|---|
| High distinction | 85-100% | Every major design choice is motivated by problem constraints and supported by literature or empirical evidence. Alternatives are genuinely considered. Writing is precise and technically confident. |
| Distinction | 70-84% | Most design choices are justified. Some alternatives mentioned. Literature engaged with, not just listed. |
| Merit | 60-69% | Some justification present. Alternatives mentioned but not developed. Literature cited. |
| Pass | 50-59% | Design described with minimal justification. Descriptive rather than analytical. |
| Marginal fail | 40-49% | Report describes what was built but offers no analysis. Reads as a lab notebook, not a critical report. |
| Fail | 0-39% | Report absent, too short to assess, or does not describe the implementation. |

---

## Criterion 4 -- Report: Evaluation and Reflection (20%)

This criterion assesses lo2, lo4, lo6. Look for honest, specific evaluation rather than self-congratulation. Reflection on classical vs ML trade-offs must be substantive.

**Positive indicators:**
- Quantitative results (timings, path costs, expansion counts, classification accuracy, reward curves)
- Specific failure modes identified: under what conditions does the AI break?
- Reflection proposes a concrete ML alternative to at least one classical component with specific benefits and costs articulated
- Reference to industry practice (shipped titles, published techniques) to contextualise results

**Negative indicators:**
- "The AI worked well" without evidence
- Reflection says "ML could make this better" without specifying how or at what cost
- No failure modes identified
- Evaluation is qualitative only when quantitative evidence was feasible

**Descriptor guidance:**

| Band | Mark range | Description |
|---|---|---|
| High distinction | 85-100% | Quantitative evaluation with honest analysis of limitations. Reflection is specific, grounded, and demonstrates understanding of both classical and ML trade-offs at an industry level. |
| Distinction | 70-84% | Evaluation includes some quantitative results. Reflection is substantive and specific. |
| Merit | 60-69% | Evaluation present. Some quantitative data. Reflection is present but general. |
| Pass | 50-59% | Some evaluation of behaviour. Reflection present but superficial. |
| Marginal fail | 40-49% | Evaluation is anecdotal. Reflection is one or two sentences with no substance. |
| Fail | 0-39% | No evaluation. Reflection absent. |

---

## Moderation and Consistency Notes

- The Foundation component accounts for 30%. A submission with all three Foundation components working correctly but no Advanced work and a weak report cannot exceed approximately 45% overall -- which is a fail. Communicate this to students if asked.
- Do not reward length. A focused 3500-word report that addresses all criteria is preferable to a padded 5000-word submission.
- Code comments do not substitute for report analysis. Students who annotate their code extensively but write a thin report should not receive credit in the report criteria on the basis of the code.
- If the submission does not build: mark the report on its own merits, cap the Foundation and Advanced scores at 40% (marginal fail), note clearly in feedback.
- Second marking is required for any submission below 50% (fail boundary) or above 70% (distinction boundary).
