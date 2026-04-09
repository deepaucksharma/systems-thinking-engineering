---
title: "41 — Metrics by Block"
type: concept
tags: [v2.1-canonical, measurement, metrics, indicators, telemetry]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/20-diagnostic-sequence.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Metrics by Block

This table defines the formal signals for diagnosing the health of the 5 canonical blocks. It is intended to cover every first-class variable named in the canonical [Master Equation](02-master-equation.md).

> [!NOTE]
> The abstract indicators grouped below are formally mapped to concrete software engineering databases (e.g., translating "Safety" to Workday telemetry and "Quality" to GitHub escaped defects) in the **[Telemetry Engine Schema (Digital Twin)](telemetry-engine-schema.md)**.

## Value Alignment (Block V)
*Are we building the right thing for our domain?*

| Variable | Leading Indicator | Lagging Indicator |
|----------|-------------------|-------------------|
| **Strategic Fit (SF)** | OKRs cascading cleanly | Mission-level revenue/goals met |
| **Customer Value (CV)** | Weekly active users (WAU) | User retention, NPS metrics |
| **Resource Alignment (RA)** | Staffing and budget match the stated priority | Strategic work repeatedly starved by urgent work |
| **Domain Assessment (DA)** | Matching constraints to Cynefin | "Best practices" fail or succeed |
| **Strategic Decision Rights ($A_{strat}$)** | Leaders rewarded for validated learning and prevention | Promotions favor launches over durable value |

## People System (Block P)
*Measured via the SPACE framework instead of pure output.*

| Variable | Leading Indicator | Lagging Indicator |
|----------|-------------------|-------------------|
| **Safety (PS)** | Dissent observed in meetings | Honest postmortems without blame |
| **Sustainability (Su)** | Work-after-hours trend | Sick leave spike; attrition rate |
| **Motivation & Autonomy (M)** | Engineers initiate improvements without permission theater | Quiet quitting; low discretionary effort |
| **Fairness & Trust (FT)** | Decisions explained clearly and perceived as just | Cynicism, coalition-building, political gaming |
| **Lived Culture (Cu)** | Local norms match stated values in meetings and reviews | What gets rewarded diverges from stated principles |
| **Extraneous Load (EL)** | Percent of time in broken pipelines or process friction | Low Germane Capacity ($GC$) |
| **Germane Capacity ($GC$)** | Protected time for learning, deep work, and reflection | No improvement bandwidth; same mistakes repeated |

## Execution System (Block E)
*Includes queuing-physics additions such as batch size and tail-risk interpretation.*

| Variable | Leading Indicator | Lagging Indicator |
|----------|-------------------|-------------------|
| **Clarity (C)** | Goal recall consistency (>80%) | Priority reversals per sprint |
| **Focus (F)** | WIP limits holding | Unplanned work percentage |
| **Skill (S)** | Inverse problem-resolution time improving | Chronic dependence on heroics or external rescue |
| **Coordination (Co)** | Ownership is explicit and blocker aging is low | Handoff failures; cross-team collisions |
| **Quality (Q)** | Test coverage, PR review depth | Escaped defects; tech debt growth |
| **Batch Size (BS)** | P90 item size < 5 days | Cycle time spikes at high utilization |
| **Tail Risk (TR)** | P95/P99 cycle time diverges from mean | Obesity Index indicates fat-tail behavior |

## Org Alignment (Block A)
*Does the org structure permit execution?*

| Variable | Leading Indicator | Lagging Indicator |
|----------|-------------------|-------------------|
| **Incentives (IA)** | Promotions reward prevention | Hero culture entrenched |
| **Decision Rights (DR)** | Clear DACI / RAPID ownership assigned | Deadlocked launch gates |
| **Team Composition (TC)** | Seniority mix and role coverage fit current complexity | Bus factor collapse; onboarding drag |
| **Cross-Team Architecture (XT)** | Cross-team blocker frequency | High MTTR across silos; dependency thrash |
| **Team Topology Health (TT)** | Teams have coherent charter and correct team type | Persistent boundary confusion and dependency overload |
| **Interaction Modes (IM)** | Collaboration / X-as-a-service / facilitation modes are explicit | Endless meetings, implicit handoffs, service confusion |

## Learning & Adaptation (Block L)
*Do we get better with time?*

| Variable | Leading Indicator | Lagging Indicator |
|----------|-------------------|-------------------|
| **Feedback Speed (FS)** | Time to deploy staging; time to signal | Delayed defect or user feedback |
| **Learning Practices (LP)** | Action items completed from retros | Same mistakes repeated |
| **Knowledge Retention (KR)** | Documentation current and onboarding path clear | Repeated relearning after attrition |
| **Change Absorption (CA)** | Number of concurrent initiatives remains within capacity | Change fatigue; falling velocity |
| **Experimentation Rate (ER)** | Safe-to-fail probes run with explicit hypotheses | Strategy remains opinion-driven for long periods |

## Measurement Use Rules

- **Do not average across blocks.** A strong Execution signal cannot cancel a weak People or Value signal.
- **Use leading indicators to judge intervention direction.** Use lagging indicators to confirm the new baseline later.
- **Partition by domain and lane where necessary.** Mixed states and heavy-tailed delivery make rolled-up averages misleading.
- **Treat measurement reliability as a prerequisite, not a footnote.** If $PS$ is low, downgrade confidence in all quantitative telemetry.

> **IMPORTANT:** Refer to the [Measurement Reliability Theorem](02-master-equation.md). If Psychological Safety ($PS$) is low, all quantitative execution metrics are suspect. A system without trust cannot produce honest telemetry.

## Historical Comparison

- Earlier measurement summary: [Metrics Framework](../legacy/metrics-framework.md)
- Measurement construction: [Measurement Theory](measurement-theory.md)
- Ethical constraints: [Ethical Measurement](ethical-measurement.md)
