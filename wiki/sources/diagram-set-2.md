---
title: "Comprehensive Diagram Set for EM Control Theory (Set 2)"
type: source
tags: [diagrams, multiplicative-system, causal-loops, condition-dependency, stock-flow, diagnostics, state-transitions, control-loop, metrics, zero-propagation, mixed-state, lever-access]
sources: [raw/2.md]
backlinks: []
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Comprehensive Diagram Set for EM Control Theory (Set 2)

**Source file:** `raw/2.md`

## Summary

This source presents **eleven diagrams** organized across four layers: Strategic (Why), Structural (What), Tactical (How), and Operational (Now). It provides an alternative and expanded visualization of the same Engineering Management Control Theory framework as [Set 1](diagram-set-1.md).

## Layer Architecture

### Strategic Layer (Why)
1. **Multiplicative System Architecture** — [Master Equation](../entities/master-equation.md) with zero propagation rules and manager lever mappings.
2. **Enhanced Causal Loop Diagram** — Distinguishes loop-breaking interventions (Direction, Protection, Ship one thing) from loop-feeding interventions (Development, Standards, Structure).
9. **Zero Propagation Analysis** — Quantitative demonstration: healthy state (product = 0.28), one zero (0.04, 7× worse), two zeros (0.006, 47× worse). See: [Zero-Override Rule](../concepts/zero-override-rule.md).

### Structural Layer (What)
3. **Condition Dependency DAG** — Fix-order hierarchy as a directed acyclic graph with override for near-zero conditions. Color-coded by condition.
4. **Stock & Flow with Rework Loop** — Queuing physics with explicit rework path and [Little's Law](../concepts/littles-law.md) annotation.
8. **Metrics Constellation** — Maps leading and lagging indicators to each of the six conditions. See: [Metrics Framework](../concepts/metrics-framework.md).

### Tactical Layer (How)
5. **Diagnostic Decision Tree** — Eight-question flowchart mapping symptoms to root causes: direction failure, flow failure, capability failure, coordination failure, quality failure, learning failure, system failure, scaling failure. Includes the cascade rule.
6. **State Transition Map** — [P1](../concepts/p1-crisis.md) through [P5](../concepts/p5-scaling.md) with transition conditions, regression triggers, and intervention notes.
7. **Control Loop with Time Delays** — Manager OODA cycle with timing rules: 2-cycle wait, review cadence by state, oscillation risk.

### Operational Layer (Now)
10. **Mixed-State Partition View** — Handles teams where subsystems are in different states. Key rule: use worst state for stabilization, best for investment, never average away a zero. See: [P6-Mixed State](../concepts/p6-mixed-state.md).
11. **Lever Access Decision Tree** — Expanded escalation paths with free/low-cost substitutes for each blocked lever.

## Usage Guides (from source)

| Context | Recommended Diagram Sequence |
|---|---|
| **Teaching/Onboarding** | 1 → 9 → 3 → 5 |
| **Daily Operations** | 5 → 11 → 7 → 8 |
| **Strategic Planning** | 6 → 2 → 10 → 4 |
| **Crisis Response** | 9 → 3 → 2 → 7 |

## Cross-Reference with Set 1

Both sets cover the same framework. Set 1 uses 9 diagrams emphasizing the temporal/meta-loop; Set 2 uses 11 diagrams with a clearer four-layer separation and adds the Metrics Constellation and Zero Propagation Analysis as standalone diagrams.
