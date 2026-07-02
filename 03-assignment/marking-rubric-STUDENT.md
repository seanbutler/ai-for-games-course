# Marking Rubric

**Module:** WM9SL-15 AI and Games  
**Assessment:** Game AI Implementation  
**Weight:** 100% | **Submission deadline:** 31st May 2026

Use this rubric to check your submission before you submit. Markers will use the same criteria.

---

## How marks are distributed

| Criterion | Weight |
|---|---|
| Foundation implementation correctness | 30% |
| Advanced implementation quality | 25% |
| Report: design justification and analysis | 25% |
| Report: evaluation and reflection | 20% |

---

## Criterion 1 -- Foundation Implementation Correctness (30%)

All three Foundation components are required. Absence of any one component will result in a fail on this criterion.

| Mark | What this looks like |
|---|---|
| 85-100% | All three components (pathfinding, decision system, sensing) are correct, integrated with each other, and cleanly implemented. The marker can build and run your project without modification. |
| 70-84% | All three components present and functionally correct. Minor code quality issues or small integration gaps. |
| 60-69% | All three present. One has a defect that does not prevent it demonstrating the technique. |
| 50-59% | All three present with defects, or two components fully correct and one absent. |
| 40-49% | One Foundation component absent or the project does not build. |
| 0-39% | Two or more Foundation components absent or non-functional. |

**Checklist:**
- [ ] A* (or equivalent informed search) runs correctly on your graph representation
- [ ] Decision system (FSM or behaviour tree) responds correctly to world state changes
- [ ] Sensing component (range, LOS, or FoV) feeds into the decision system
- [ ] Project builds and runs on the reference platform without modification

---

## Criterion 2 -- Advanced Implementation Quality (25%)

You must include at least one Classical AI technique and at least one ML technique from the lists in the assessment brief. Attempting more than the minimum and succeeding at it will earn a higher mark.

| Mark | What this looks like |
|---|---|
| 85-100% | At least one Classical and one ML technique, both correctly implemented and integrated. Results measured and reported in the report. |
| 70-84% | At least one of each, both functional. Results present. Minor gaps in analysis or integration. |
| 60-69% | One of each attempted. One is fully functional; the other demonstrates the core idea despite a defect. |
| 50-59% | One Advanced technique (of either type) present and functional. Minimum met. |
| 40-49% | Advanced technique attempted but not functional, or implemented without reporting results. |
| 0-39% | No Advanced technique present. |

**Checklist:**
- [ ] At least one Classical AI Advanced technique implemented and functional
- [ ] At least one ML Advanced technique implemented and functional
- [ ] Results (timings, accuracy, learning curves, or equivalent) reported in the report
- [ ] Architecture or algorithm choice explained and justified in the report

---

## Criterion 3 -- Report: Design Justification and Analysis (25%)

This criterion assesses whether you understand why you made the choices you made, not just what you built. Descriptive writing scores in the pass band at best.

| Mark | What this looks like |
|---|---|
| 85-100% | Every major design decision is motivated by the specific constraints of your game environment. You consider at least one alternative approach per major decision and reject it with reasoned argument supported by literature or evidence. Writing is precise and technically confident. |
| 70-84% | Most design choices are justified with reference to problem constraints. Alternatives mentioned and briefly assessed. Literature engaged with, not just listed. |
| 60-69% | Some justification present. Alternatives mentioned but not developed into comparative argument. |
| 50-59% | Design described but justification is thin ("A* is a standard pathfinding algorithm"). No meaningful comparison to alternatives. |
| 40-49% | Report describes what was built but does not explain why those choices were made. Reads as a lab notebook. |
| 0-39% | Report absent, too short, or does not describe the implementation. |

**Checklist:**
- [ ] Each major design choice is explained in terms of your specific game environment, not just in general terms
- [ ] At least one alternative is considered and rejected with a reason for each major component
- [ ] References are cited and the argument engages with them (not just listed in the bibliography)
- [ ] No large blocks of source code reproduced in the report -- use pseudocode or short excerpts to illustrate a specific point

---

## Criterion 4 -- Report: Evaluation and Reflection (20%)

Markers want to see honest, specific evaluation backed by evidence, and genuine engagement with the classical vs ML trade-off.

| Mark | What this looks like |
|---|---|
| 85-100% | Quantitative evaluation of AI behaviour (timings, path costs, expansion counts, accuracy, reward curves -- whatever is measurable for your project). Specific failure modes identified with conditions. Reflection proposes a concrete ML alternative to at least one classical component, with specific benefits and costs articulated. |
| 70-84% | Some quantitative results. Failure modes identified. Reflection is substantive and specific to your implementation. |
| 60-69% | Evaluation present with some data. Reflection is present but stays at a general level. |
| 50-59% | Behaviour evaluated informally. Reflection is present but brief and generic. |
| 40-49% | Evaluation is anecdotal ("it seemed to work well"). Reflection is one or two sentences. |
| 0-39% | No evaluation. Reflection absent. |

**Checklist:**
- [ ] At least one quantitative result reported and discussed (not just stated)
- [ ] At least one failure mode or limitation described with specific conditions
- [ ] Reflection names a specific ML technique that could replace or augment a classical component and explains what would be gained and lost
- [ ] No unsupported claims that the AI "worked well" without evidence

---

## Submission checklist

- [ ] Source code as a zip archive with a README explaining how to build and run
- [ ] Report as a PDF, 4000 words maximum (references and figure captions excluded from the count)
- [ ] Submitted via the module submission portal before 23:59 on 31st May 2026
- [ ] Self-certification (extension) claimed in advance if needed -- not retrospectively
