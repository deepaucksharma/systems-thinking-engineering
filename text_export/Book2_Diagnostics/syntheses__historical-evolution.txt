---
title: "Historical Evolution"
type: synthesis
tags: [lineage, history, v1-framework, v2-framework, evolution]
sources: []
backlinks: [wiki/_indexes/root.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Historical Evolution Matrix

The Systems EM framework has evolved through three distinct paradigms. This page serves as the permanent lineage matrix documenting how early constraints mature into explicit physical formulations.

> [!NOTE]
> All linked legacy files are preserved for historical context in the `legacy/` directory. They are `status: stale` and should not be used for current diagnostic operations.

## V1 $\rightarrow$ V2: The Jump to 5 Blocks
The original V1 framework was exclusively an *Execution Model* based on 5 Operational Metrics (OM1-OM5) and OM6 (Feedback Speed). It failed to account for macro-environmental constraints that routinely crushed local team execution. 

V2 solved this by embedding Execution inside 4 external gating blocks.

| V1 Condition (Legacy) | V2 Framework Relocation |
|-----------------------|-------------------------|
| [Clarity (OM1)](../legacy/clarity.md) | Nested into Execution ($E$). Differentiated from Value. |
| [Focus (OM2)](../legacy/focus.md) | Nested into Execution ($E$). Coupled with batch size. |
| [Skill (OM3)](../legacy/skill.md) | Nested into Execution ($E$). Cross-loaded with Team Comp. |
| [Coordination (OM4)](../legacy/coordination.md) | Nested into Execution ($E$). Bounded by Org Structure ($A$). |
| [Quality (OM5)](../legacy/quality.md) | Nested into Execution ($E$). |
| [Feedback Speed (OM6)](../concepts/feedback-speed.md) | Promoted to become Block L (Learning & Adaptation). |

## V2 $\rightarrow$ V2.1: Formalizing the Physics
V2 established the 5 blocks ($V, P, E, A, L$) but lacked strict mathematical parameterization. V2.1 canonicalized the equations, explicitly injected queuing physics ($M[X]/M/1/\infty$), and merged cognitive load directly into the People System.

### The Canonical Mapping
| Legacy V2 Formulation (Stale) | Canonical V2.1 Definition (Active) |
|-------------------------------|------------------------------------|
| [Value Alignment](../legacy/value-alignment.md) | [10 — Block V (Value Alignment)](../concepts/10-block-V.md) |
| [People System](../legacy/people-system.md) | [11 — Block P (People System)](../concepts/11-block-P.md) |
| [Execution System](../legacy/execution-system.md) | [12 — Block E (Execution System)](../concepts/12-block-E.md) |
| [Org Alignment](../legacy/org-alignment.md) | [13 — Block A (Org Alignment)](../concepts/13-block-A.md) |
| [Learning & Adaptation](../legacy/learning-adaptation.md) | [14 — Block L (Learning & Adaptation)](../concepts/14-block-L.md) |
| [Master Equation](../legacy/master-equation.md) | [02 — Master Equation](../concepts/02-master-equation.md) |

### Deprecated and Subsumed Rules
Certain standalone rules and constraint pages from V1/V2 were either generalized into broader V2.1 theorems or folded directly into the canonical block pages.
- [Zero-Override Rule](../legacy/zero-override-rule.md) (Subsumed by Diagnostic Sequence Step 0)
- [Nyquist Constraint](../legacy/nyquist-constraint.md) (Subsumed by Time Constants and Block L)
- [Metrics Framework](../legacy/metrics-framework.md) (Replaced by [41 - Metrics by Block](../concepts/41-metrics-by-block.md))
- [Fix-Order](../legacy/fix-order.md) (Replaced by [20 - Diagnostic Sequence](../concepts/20-diagnostic-sequence.md))
- [Anti-Patterns](../legacy/anti-patterns.md) (Replaced by [51 - Anti-Patterns](../concepts/51-anti-patterns.md))
