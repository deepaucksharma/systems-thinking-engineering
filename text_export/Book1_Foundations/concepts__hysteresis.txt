---
title: "Hysteresis"
type: concept
tags: [thermodynamics, state-machine, dynamics, memory]
sources: [raw/3.md]
backlinks: [wiki/concepts/order-parameter.md, wiki/concepts/p2-stabilizing.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Hysteresis

## Definition

State transitions in engineering teams exhibit **hysteresis** — the system does not transition back and forth at the exact same threshold. The system has "memory".

## The Hysteresis Gap

- Upward Transition ([Crisis](p1-crisis.md) → [Stabilizing](p2-stabilizing.md)) requires $\Phi > 0.35$
- Downward Transition (Stabilizing → Crisis) occurs at $\Phi < 0.25$

This gap (0.25–0.35) explains why:
- "One bad week" doesn't immediately destroy a stabilizing team.
- "One good week" doesn't pull a crisis team out of a crisis.

## Formal Proof

The energy landscape of the stabilizing system is a **double-well potential**:

$$ E(\Phi) = -\frac{a}{2}\Phi^2 + \frac{b}{4}\Phi^4 $$

A team in P2 (Stabilizing) sits in a shallow well. A small shock can push them back into the deep well of Crisis or forward into Functional. This mathematical property is the formal definition of "fragility."

## Related
- [Order Parameter ($\Phi$)](order-parameter.md) — The metric that defines hysteresis thresholds.
