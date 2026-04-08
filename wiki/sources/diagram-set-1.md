---
title: "Diagram Architecture for Systems EM Framework (Set 1)"
type: source
tags: [diagrams, master-equation, causal-loops, stock-flow, control-theory, decision-tree, state-machine, phase-space, lever-access]
sources: [raw/1.md]
backlinks: []
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Diagram Architecture for Systems EM Framework (Set 1)

**Source file:** `raw/1.md`

## Summary

This source presents a complete set of **nine diagrams** that visually encode every dimension of the Engineering Management Control Theory framework. Each diagram covers a distinct explanatory layer with no overlap and no gaps.

## Key Diagrams

1. **Master Equation Visual** (Diagram 1) — Visualizes the multiplicative structure `OUTPUT = (C × F × S × Co × Q) × FS` and the zero-override rule. See: [Master Equation](../entities/master-equation.md)
2. **Full Causal Loop Diagram** (Diagram 2) — Shows the [Losing Loop](../concepts/losing-loop.md) (R1) and [Winning Loop](../concepts/winning-loop.md) (R2), manager levers as balancing forces, and [Condition Decay](../concepts/condition-decay.md).
3. **Stock and Flow / Queuing Physics** (Diagram 3) — Operationalizes [Little's Law](../concepts/littles-law.md): Cycle Time = WIP ÷ Throughput. Shows the rework loop and queue dynamics.
4. **Closed-Loop Control System** (Diagram 4) — Control-engineering view of the manager's loop, including the [Nyquist Constraint](../concepts/nyquist-constraint.md): don't intervene faster than feedback propagates.
5. **Fix-Order Decision Tree** (Diagram 5) — Executable diagnostic from [Table 2](../entities/table-2-diagnostics.md), integrating the [Zero-Override Rule](../concepts/zero-override-rule.md) and [Structure-vs-Development Rule](../concepts/structure-vs-development-rule.md).
6. **Team State Machine** (Diagram 6) — State transitions across [P1-Crisis](../concepts/p1-crisis.md) through [P5-Scaling](../concepts/p5-scaling.md) and [P6-Mixed](../concepts/p6-mixed-state.md), with regression triggers.
7. **Phase Space Diagram** (Diagram 7) — Plots team movement through Focus-Quality space. Identifies the [Hero Culture Trap](../concepts/hero-culture-trap.md) and [Rushing Trap](../concepts/rushing-trap.md).
8. **Lever Access and Escalation Map** (Diagram 8) — Operationalizes the [Lever-Access Rule](../concepts/lever-access-rule.md) with escalation paths for each blocked lever.
9. **Complete Temporal Loop** (Diagram 9) — Meta-diagram showing Observe → Diagnose → Act → Measure cycle connecting all eight preceding diagrams.

## Core Insights

- **Multiplicative structure is arithmetic, not advice.** A zero in any condition kills output regardless of strength elsewhere.
- **Two self-reinforcing loops** compete: the Losing Loop (workload → context switching → quality drop → rework → more workload) and the Winning Loop (slack → investment → skill/coordination → throughput → more slack).
- **Condition decay** means the Winning Loop isn't self-sustaining without maintenance.
- **The Nyquist constraint** formally justifies waiting 2 full cycles before judging an intervention.
- **The lever-access check** is an explicit decision gate — many managers pull levers they cannot actually move.
