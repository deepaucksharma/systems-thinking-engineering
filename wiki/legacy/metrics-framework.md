---
title: "Metrics Framework"
type: concept
tags: [metrics, leading-indicators, lagging-indicators, measurement, telemetry, v2-framework]
sources: [raw/2.md, raw/5.md]
backlinks: [wiki/legacy/nyquist-constraint.md, wiki/concepts/p6-mixed-state.md, wiki/legacy/quality.md, wiki/sources/diagram-set-2.md, wiki/sources/canonical-v2-consolidated-model.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/41-metrics-by-block.md]
---

# Metrics Framework (Legacy)

> [!WARNING]
> This framework has been explicitly replaced by the Canonical V2.1 Measurement architecture (incorporating the SPACE frame and Tail-Risk metrics). See **[41 — Metrics by Block]()**.

## Definition

The V2 framework maps **leading** and **lagging** indicators across all five causal blocks ($V$, $P$, $E$, $A$, $L$). Leading indicators predict future state; lagging indicators confirm past state. 

*Crucial Systemic Rule:* A system cannot be managed by observing lagging indicators alone, as the [Feedback Speed]() delay will cause heavy [Nyquist Constraint](../legacy/nyquist-constraint.md) violations, steering the team into oscillation.

## Metrics by Block

### Value Alignment (Block V)
| Sub-variable / Concept | Leading Indicators | Lagging Indicators |
|---|---|---|
| **Strategic Fit (SF)** | Priority churn rate, conflicting mandates | "Strategy du jour" complaints, objective abandonment |
| **Market/Problem Fit (CV)** | Hypothesis testing cycle rate, customer interviews/wk | Usage metrics, retention rate, feature adoption |
| **Resource Alignment (RA)** | Dedicated budget vs urgent interruptions | Roadmap completion rate, actual vs planned allocation |

### People System (Block P)
| Sub-variable / Concept | Leading Indicators | Lagging Indicators |
|---|---|---|
| **Psychological Safety (PS)** | Time between error and reporting, dissenting voices in review | Hidden incidents, "water melon" status reports |
| **Sustainability (Su)** | Workload vs capacity, weekend commits, vacation backlog | Sick leave trends, burnout classifications |
| **Motivation/Trust (M/FT)** | Voluntary extra-role behavior, meeting engagement | Quiet quitting, voluntary attrition of high performers |

### Execution System (Block E)
| Sub-variable / Concept | Leading Indicators | Lagging Indicators |
|---|---|---|
| **[Clarity](../legacy/clarity.md) (C)** | Goal recall rate, stable priority list | Rework %, discarded work, missed expectations |
| **[Focus](../legacy/focus.md) (F)** | WIP within cap, fewer interrupts, maker hours | Cycle time, task aging, throughput |
| **[Skill](../legacy/skill.md) (S)** | Pairing frequency, review depth, skill coverage | Time to solve, repeated failures, bus factor |
| **[Coordination](../legacy/coordination.md) (Co)** | Dependency age, clear ownership boundaries | Cross-team slips, handoff failures, integration blocks |
| **[Quality](../legacy/quality.md) (Q)** | Test execution rate, review completion, static passes | Escaped defects, rollback rate, incident frequency |

### Org Alignment (Block A)
| Sub-variable / Concept | Leading Indicators | Lagging Indicators |
|---|---|---|
| **Incentive Alignment (IA)** | Reward ratio (heroics vs prevention) | Tactical work burying strategic work |
| **Decision Rights (DR)** | Decision latency, number of required sign-offs | Escalation frequency, high reversal rate |
| **Cross-Team Arch (XT)** | Boundary interface complexity | Conway's Law violations, blocked-by-other-team time |

### Learning & Adaptation (Block L)
| Sub-variable / Concept | Leading Indicators | Lagging Indicators |
|---|---|---|
| **[Feedback Speed]() (FS)** | Time to detect, review turnaround, deploy frequency | Recurring incidents, untested long-running branches |
| **Learning Practices (LP)** | Action item completion rate post-incident | Same incident occurs repeatedly |
| **Change Absorption (CA)** | Number of simultaneous top-down changes | System thrash, fatigue, failure to adopt tooling |

## Dashboard Design Principle

- Watch **leading indicators weekly**.
- Track **lagging indicators monthly**.
- If leading moves but lagging doesn't → **hold course** (system is propagating).
- If neither moves in 2 cycles → **re-diagnose** (wrong lever or blocked by a higher-order Gating Theorem).

## Multi-Dimensional Limits & Mixed States

In [P6-Mixed State](), averaging metrics across lanes or blocks is technically invalid. Averaging an excellent Execution metric with a fatal People metric ($\Phi_E = 0.9, \Phi_P = 0.2$) yields a false signal. Partition metrics strictly by domain and block constraint.

## Related

- [Nyquist Constraint](../legacy/nyquist-constraint.md) — timing rules for interpreting metrics
- [P6-Mixed State]() — when averages are dangerous
- [Measurement Theory]() — mathematical rules for latent variables
- [Table 2 Diagnostics](../entities/table-2-diagnostics.md) — acting on the metrics
