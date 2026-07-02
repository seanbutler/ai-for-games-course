# Assessment Brief

**Module code:** WM9SL-15  
**Module title:** AI and Games  
**Assessment title:** Game AI Implementation  
**Weight:** 100%  
**Length:** 4000 words (report component)  
**Submission format:** Project -- Individual  
**Submission deadline:** 31st May 2026  
**Self-certification eligible:** Yes (extension only)

---

## Overview

You will design and implement artificial intelligence techniques within an interactive game environment, then write a 4000-word technical report documenting your design decisions, implementation, and critical evaluation. The project is designed to demonstrate both your practical ability to implement game AI systems and your capacity to analyse and justify the approaches you have chosen. Code alone is not sufficient evidence of learning: the report is the primary vehicle through which you demonstrate achievement of the module learning outcomes.

---

## Deliverables

### Deliverable 1 -- Code

A working implementation of AI techniques within a game or interactive environment. The codebase must be submitted as a zip archive containing all source files and a README describing how to build and run the project.

Your implementation must include all Foundation requirements listed below, plus at least the minimum number of Advanced requirements for your chosen tier.

### Deliverable 2 -- Report (4000 words)

The report documents your implementation and provides the critical analysis through which learning outcomes are assessed. Structure it using the following sections.

**Introduction**  
Briefly describe your game or interactive environment and the AI problem(s) you are addressing. State which Foundation and Advanced techniques you have implemented and why you selected them.

**Design and Architecture**  
Explain the overall structure of your AI system. Describe how the components fit together and how your design decisions follow from the constraints and goals of your chosen environment. Reference relevant literature to justify your design choices.

**Implementation**  
Describe the key algorithmic choices you made during implementation. Where you deviated from a textbook approach, explain why. Include pseudocode or short code excerpts where they aid explanation; do not reproduce large blocks of source code.

**Evaluation**  
Critically evaluate the AI behaviour you implemented. Discuss what works well, what fails under which conditions, and how your chosen approach compares to alternatives. Quantitative results (timing, path quality, decision accuracy) are expected where measurable.

**Reflection**  
Reflect on the relationship between classical and modern AI approaches in your implementation. Where could a machine learning technique replace or augment a classical one? What would be gained and what would be lost?

**References**  
Full bibliography in a consistent citation format (Harvard preferred).

---

## Requirements

### Foundation -- all required

Every submission must include a working implementation of each of the following:

- A pathfinding system using A* or an equivalent informed search algorithm on a graph representation suitable for your environment (tile grid, waypoint graph, or navigation mesh)
- A decision system for at least one agent using a finite state machine, behaviour tree, or equivalent hierarchical decision structure
- A spatial sensing or perception component (range detection, line-of-sight, or field-of-view sensor) that feeds into the agent decision system

### Advanced: Classical AI -- choose at least one

- Hierarchical pathfinding (cluster abstraction or equivalent) with measurable improvement in query time or path quality
- Navigation mesh generation or integration with dynamic obstacle avoidance
- Behaviour tree with blackboard architecture, reusable subtrees, and at least one decorator node type
- Utility AI scoring system with response curves applied to at least two competing agent objectives
- Goal-Oriented Action Planning (GOAP) or STRIPS-style planner producing runtime action sequences for at least one agent

### Advanced: Machine Learning -- choose at least one

- Trained neural network (any architecture) solving a game-relevant classification or regression task, with training and evaluation results reported
- Reinforcement learning agent trained in your game environment, with learning curves and policy analysis
- Convolutional, recurrent, or transformer architecture applied to a game-relevant problem, with architecture choice justified
- Procedural content generation using a neural generative model, with generated output evaluated against a baseline


---

## Notes

The report is the primary evidence for your learning outcomes. Markers cannot infer understanding from code alone: every design decision, algorithmic choice, and evaluation finding must be articulated in the report. A functioning implementation with a weak report will not achieve a high mark; a strong report with a non-functional implementation will not pass.

The reference platform constraint is firm: your submission must build and run without modification on the platform specified in the lab setup (see Unit 01). Submissions that cannot be built will be marked on the report only.

Feedback will be provided in writing following marking. In-class tutor demonstrations of solution approaches will also be provided after the submission deadline.
