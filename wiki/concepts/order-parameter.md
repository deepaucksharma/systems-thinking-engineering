---
title: "Order Parameter (Phi)"
type: concept
tags: [thermodynamics, state-machine, measurement, physics, v2-framework]
sources: [raw/3.md, raw/5.md]
backlinks: [wiki/concepts/hysteresis.md, wiki/legacy/master-equation.md, wiki/concepts/p1-crisis.md, wiki/concepts/v2-extended-states.md]
created: 2026-04-08
updated: 2026-04-09
status: active
---

# Order Parameter (Phi)

## Definition

The order parameter `Phi` is the framework's way of talking about overall system state. It is useful as a **state-summary device**, not as a claim that complex organizations can be reduced perfectly to one number.

In the earlier execution-only framing, `Phi` was treated more like a composite score over execution conditions. In the broader V2 framing, it becomes multi-dimensional:

$$\Phi(t) = [\Phi_V, \Phi_P, \Phi_E, \Phi_A, \Phi_L]$$

The key idea is not the notation. The key idea is that the *shape* of the system matters as much as the average score. A team with strong execution and collapsing people health is not "middling." It is unstable in a very specific way.

## How State Is Interpreted

Each sub-score is a normalized composite of block-level conditions. The overall state is usually driven by the weakest block, while the pattern across blocks helps explain what intervention will or will not work.

That is why the order parameter is more useful for:
- naming broad system states;
- spotting mismatch patterns;
- deciding where to look next;

than for ranking teams numerically.

## State Transitions (P1-P5)

| State | Pattern | Characteristics | Primary Risk |
|-------|---------|-----------------|-------------|
| **[P1 Crisis](p1-crisis.md)** | Any `Phi < 0.3` | Losing loop active; visible instability everywhere | Irreversible attrition and debt |
| **[P2 Stabilizing](p2-stabilizing.md)** | Worst `Phi`: `0.3-0.5` | Fragile improvement; fires are reducing | Regression when load rises |
| **[P3 Functional](p3-functional.md)** | All `Phi`: `0.5-0.7` | Delivery works; improvement is limited | Slow decay without reinvestment |
| **[P4 Thriving](p4-thriving.md)** | All `Phi > 0.7` | Winning loop engaged; calm and adaptive | Complacency and invisible decay |
| **[P5 Scaling](p5-scaling.md)** | `Phi_E` high while `Phi_A` or `Phi_P` falls | Growth stresses structure and people | Execution outruns system capacity |

These thresholds are best treated as heuristic state bands, not universal constants.

## Mismatch States

Because `Phi` is multi-dimensional, the framework can describe mismatch states such as:
- high execution with poor value alignment;
- high execution with collapsing people health;
- strong learning in a structurally blocked organization.

See [V2 Extended States](v2-extended-states.md) for the named legacy mismatch patterns.

## Mixed-State Rule

See [P6 - Mixed State](p6-mixed-state.md).

The practical rule is simple: do not average away the weakest block. A system with `Phi_P = 0.2` and `Phi_E = 0.9` is not safely in the middle. It is a high-output system sitting on a human failure mode.

## Related

- [Hysteresis](hysteresis.md) - why upward and downward transitions are asymmetric
- [P1 - Crisis](p1-crisis.md) - the most unstable state band
- [P6 - Mixed State](p6-mixed-state.md) - when different subsystems occupy different states
- [V2 Extended States](v2-extended-states.md) - legacy mismatch-state taxonomy
