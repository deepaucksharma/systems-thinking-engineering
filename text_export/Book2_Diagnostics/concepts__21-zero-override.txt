---
title: "21 — Zero-Override Protocol"
type: concept
tags: [v2.1-canonical, rules, zero-states, escalation]
sources: [raw/6.md]
backlinks: [wiki/concepts/20-diagnostic-sequence.md, wiki/concepts/00-model-identity.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Zero-Override Protocol (V2.1)

## Definition

In a multiplicative formula ($OUTCOME = V \cdot P \cdot E \cdot A \cdot L$), a zero in any variable collapses the entire product to zero. The **Zero-Override Rule** states that if you encounter a "Hard Zero" in any Block, you must abandon standard diagnostic sequences (like optimizing Sprints) and fix the zero immediately to prevent total system collapse.

## The Canonical "Hard Zeros"

If any of these conditions are true, treat them as a Hard Zero requiring escalation above the team layer:

### $V \approx 0$: Strategy Collapse
- No credible strategy or real user problem to solve. 
- *Intervention:* Stop building features. Pivot immediately or shut down the project.

### $PS \approx 0$: Safety Collapse
- People cannot surface bad news without retribution.
- *Intervention:* Halt all metric-driven performance management. The data is compromised. Rely on 1:1s and anonymous channels until trust is restored.

### $Su \approx 0$: Systemic Burnout
- Balance of demands vs recovery is totally broken.
- *Intervention:* Immediately cut Scope and WIP. Do not implement new process improvements; the system has zero Change Absorption capacity.

### $IA \approx 0$: Inverse Incentives
- The organization visibly promotes behavior that destroys long-term value (e.g., rewarding rushed shipments that cause outages).
- *Intervention:* The manager must escalate structurally. Do not ask the team to "work smarter".

### $XT/TT \approx 0$: Deep Architectural Deadlock
- Deep Conway's Law violation. Teams cannot deploy without 5-way negotiations.
- *Intervention:* Stop optimizing local cross-team sync meetings. Apply the Inverse Conway maneuver to merge or reorganize the teams.

## Execution Rules During a Zero-Override

1. **Do not treat these as local execution problems.**
2. **Document as an Org-Level Constraint.** Name the tradeoff explicitly to executives.
3. **Escalate immediately.** 
4. **Apply minimal local mitigation.** (e.g., If Burnout is real, cancel all non-essential meetings immediately to stop the bleeding while you negotiate scope with the business).

## Historical Comparison

- Earlier rule page: [Zero-Override Rule](../legacy/zero-override-rule.md)
- Broader operator flow: [20 - Diagnostic Sequence](20-diagnostic-sequence.md)
