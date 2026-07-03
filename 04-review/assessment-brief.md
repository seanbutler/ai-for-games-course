# External Marker Review -- Assessment Brief (Revision 5)

**Document reviewed:** `03-assessment/assessment-brief.md`  
**Module:** WM9SL-15 AI and Games, Warwick WMG  
**Reviewer role:** External examiner  
**Review date:** 2026-07-03

---

## Overall judgement

The brief is in good shape. The section labelling (A, B, C) is now consistent throughout, "from Section B" is correctly used in Section C, and the inference speed requirement has been sensibly reframed as a descriptive and evaluative task. The document reads clearly and the three-section structure is well-motivated.

One must-fix item remains outstanding. Two minor points are noted below.

---

## Outstanding must-fix

### 1. No marking scheme

There is no marking scheme. This has been flagged in every review and is still absent. A student-facing brief at Warwick must state how marks are distributed. Without it, students cannot make informed decisions about where to invest effort, and markers have no published criteria to defend their judgements against.

The module team must confirm the weights and add a table before this brief is released. Example structure:

| Criterion | Weight |
|---|---|
| Section A -- Traditional Game AI implementation | 30% |
| Section B -- Neural Architecture implementation and justification | 25% |
| Section C -- Neural Generative Model implementation and evaluation | 20% |
| Report -- design analysis, evaluation, and reflection | 25% |

---

## Minor points

### 2. Commented-out navmesh option still present

**Location:** Line 37.

```
<!-- ~2. Navigation mesh generation or integration with dynamic obstacle avoidance~ -->
```

This has been in the file since Revision 3. It is invisible in rendered Markdown but visible in any raw file view. It signals an unresolved editorial decision. Remove it before distribution -- if the option has been dropped, delete the line; if it may be reinstated, track the decision elsewhere.

### 3. Overview run-on sentence

**Location:** Line 14.

The sentence runs from the shell description all the way through to "then write a 4000-word technical report" without a break. Suggested split:

> "You will architect and implement artificial intelligence techniques in C++ using the game engineering shell (game loop, renderer, input, basic drawing) provided, producing a single interactive system within a modern development environment. You will then write a 4000-word technical report documenting your design decisions, implementation, and critical evaluation."

---

## Summary

| Priority | Issue | Status |
|---|---|---|
| Must fix | No marking scheme | Not yet addressed |
| Should fix | Commented-out navmesh line in raw file | Not yet addressed |
| Polish | Overview run-on sentence | Not yet addressed |
