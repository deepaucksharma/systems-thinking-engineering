---
title: "Metrics Framework"
type: concept
tags: [metrics, leading-indicators, lagging-indicators, measurement, telemetry]
sources: [raw/2.md]
backlinks: [wiki/concepts/nyquist-constraint.md, wiki/concepts/p6-mixed-state.md, wiki/concepts/quality.md, wiki/sources/diagram-set-2.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Metrics Framework

## Definition

The framework maps **leading** and **lagging** indicators to each of the six conditions. Leading indicators predict future state; lagging indicators confirm past state.

## Metrics by Condition

| Condition | Leading Indicators | Lagging Indicators |
|---|---|---|
| [Clarity](clarity.md) | Goal recall rate, stable priority list, low scope churn | Rework %, discarded work, missed expectations |
| [Focus](focus.md) | WIP within cap, fewer interrupts, maker hours | Cycle time, task aging, throughput |
| [Skill](skill.md) | Pairing frequency, review depth, skill coverage | Time to solve, repeated failures, bus factor |
| [Coordination](coordination.md) | Clear ownership map, lower dependency age, fewer blockers | Cross-team slips, handoff failures, integration surprises |
| [Quality](quality.md) | Test execution rate, review completion, observability coverage | Escaped defects, rollback rate, incident frequency |
| Feedback Speed | Time to detect, review turnaround, deploy frequency | Recurring incidents, slow improvement, morale erosion |

## Dashboard Design Principle

- Watch **leading indicators weekly**
- Track **lagging indicators monthly**
- If leading moves but lagging doesn't → **hold course** (system is propagating)
- If neither moves in 2 cycles → **re-diagnose** (wrong lever or blocked)

## Mixed-State Warning

In [P6-Mixed State](p6-mixed-state.md), averaged metrics lie. Always partition metrics by subsystem/domain before interpreting.

## Related

- [Nyquist Constraint](nyquist-constraint.md) — timing rules for interpreting metrics
- [P6-Mixed State](p6-mixed-state.md) — when averages are dangerous
