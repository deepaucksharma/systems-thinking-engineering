---
title: "Nyquist Constraint"
type: concept
tags: [control-theory, timing, measurement, feedback, v2-framework]
sources: [raw/1.md, raw/2.md, raw/4.md, raw/5.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/4-visual-architecture.md, wiki/concepts/temporal-integration-loop.md, wiki/concepts/multi-scale-dynamics.md, wiki/legacy/metrics-framework.md, wiki/concepts/v2-theorems.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/06-time-constants.md]
---

# Nyquist Constraint (Legacy)

> [!WARNING]
> For the Canonical V2.1 J-Curve and specific feedback windows per-variable, refer to **[06 — Time Constants]()**.

## Definition

A principle from signal processing applied to management: **You must sample (measure) at twice the frequency of the system's baseline cycle, and you must not intervene faster than feedback propagates.**

## V2 Block Time Constants

A fatal anti-pattern is applying a universal "2 week" wait time across the model. In **Canonical V2**, every Block ($V$, $P$, $E$, $A$, $L$) has a distinct Time Constant. The Nyquist constraint must scale against the specific Block's temporal frequency:

| System Block | Time Constant | Minimum Nyquist Wait Period |
|---|---|---|
| **Execution ($E$)** | Sprints | 2-4 weeks (2 sprints) |
| **Learning ($L$)** | Months | 4-8 weeks (Time for new tooling to integrate) |
| **People ($P$)** | Quarters | 3-6 months (Trust rebuilds slowly) |
| **Value ($V$)** | Quarters/Years | 6-12 months (Market feedback cycling) |
| **Org Alignment ($A$)** | Years | 1-2 years (Re-org/Incentive shockwaves) |

If a manager changes strategy or re-orgs the company ($V$/$A$ block) and expects to see results in 2 sprints, they are acting on heavily aliased data, concluding falsely that "the reorg failed." 

## Continuous Anti-Pattern: Manager Oscillation

Changing strategy faster than feedback propagates induces **Manager Oscillation**. The manager becomes the primary source of instability in the system. 

## Related
- [Metrics Framework](../legacy/metrics-framework.md) — The leading and lagging indicators measured.
- [Temporal Integration Loop]() — Where the Nyquist constraint is executed.
- [V2 Theorems]() — Specifically the Escaping Feedback delays.
