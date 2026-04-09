---
title: "Nyquist Constraint"
type: concept
tags: [control-theory, timing, measurement, feedback, v2-framework]
sources: [raw/1.md, raw/2.md, raw/4.md, raw/5.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/4-visual-architecture.md, wiki/concepts/temporal-integration-loop.md, wiki/concepts/multi-scale-dynamics.md, wiki/legacy/metrics-framework.md, wiki/concepts/v2-theorems.md]
created: 2026-04-08
updated: 2026-04-10
status: stale
superseded_by: [wiki/concepts/06-time-constants.md]
---

# Nyquist Constraint (Legacy)

> [!WARNING]
> For the current timing reference, use [06 - Time Constants](../concepts/06-time-constants.md). This page preserves the earlier analogy and its limits.

## Definition

This page uses a signal-processing analogy to make a management point: if you measure too slowly or intervene too quickly relative to how the system actually changes, you will misread what is happening.

That is a useful idea. It is not a claim that organizational systems literally satisfy the formal assumptions of Nyquist-Shannon sampling theory.

## V2 Block Time Constants

A persistent anti-pattern is applying one universal wait time across the model. In earlier V2 framing, each block had a distinct time constant:

| System Block | Time Constant | Minimum Wait Window |
|---|---|---|
| **Execution (`E`)** | Sprints | 2-4 weeks |
| **Learning (`L`)** | Months | 4-8 weeks |
| **People (`P`)** | Quarters | 3-6 months |
| **Value (`V`)** | Quarters to years | 6-12 months |
| **Org Alignment (`A`)** | Years | 1-2 years |

If a manager changes strategy or re-orgs the company (`V` or `A`) and expects to see results in two sprints, they are likely acting on aliased or premature data and may conclude falsely that the change failed.

## What This Explains Well

The analogy is helpful for explaining:
- why some interventions are judged too early;
- why different layers of the system move at different speeds;
- why repeated changes can create instability rather than clarity.

## What It Does Not Establish

This page does not establish that management systems can be analyzed with the same mathematical precision as sampled electronic signals. The analogy is directionally useful, but the exact thresholds and transfer properties are not derived here.

## Continuous Anti-Pattern: Manager Oscillation

Changing strategy faster than feedback propagates can induce manager oscillation. In that sense, the manager becomes a source of instability in the system.

## Related

- [Metrics Framework](../legacy/metrics-framework.md) - the earlier measurement reference
- [Temporal Integration Loop](../concepts/temporal-integration-loop.md) - where timing discipline appears operationally
- [V2 Theorems](../concepts/v2-theorems.md) - the broader older model context
