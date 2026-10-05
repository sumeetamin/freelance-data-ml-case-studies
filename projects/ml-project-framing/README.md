# ML Project Framing

## Problem

Before selecting an algorithm, define the decision the model should support, the prediction target, and how success will be measured. A freelance ML engagement included scoping target and scoring choices and preparing technical presentation material. This case study is generalized; no client dataset, clinical information, slides, or results are included.

## Reusable workflow

1. Translate the stakeholder question into a prediction unit and decision point.
2. Specify target, label window, inclusion rules, and data availability at prediction time.
3. Select a baseline and metric aligned to the use case (for example, MAE for a continuous target or precision/recall for an imbalanced classification task).
4. Choose a split that matches deployment conditions; use time- or group-based splits when random splitting would leak information.
5. Define calibration, subgroup, and error analyses before looking at test results.
6. Record assumptions, limitations, and the next data validation step.

## Guardrails

Metric names are examples, not claims about the freelance project's final evaluation. Clinical or otherwise sensitive datasets require authorization, privacy controls, and domain review; none are present in this repository.
