---
title: "Order Parameter (Φ)"
type: concept
tags: [thermodynamics, state-machine, measurement, physics]
sources: [raw/3.md]
backlinks: [wiki/concepts/hysteresis.md, wiki/entities/master-equation.md, wiki/concepts/p1-crisis.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Order Parameter ($\Phi$)

## Definition

In the [Extended Framework](../sources/3-extended-framework.md), the system's overall state is defined by its **order parameter** ($\Phi$), a concept borrowed from statistical mechanics.

It is computed as the weighted sum of all conditions:

$$ \Phi(t) = \sum_{i} w_i \cdot c_i(t) $$

## State Transitions at Critical Thresholds

State transitions in the [Team State Machine](p1-crisis.md) occur at specific critical thresholds of $\Phi$:

| State | Order Parameter Range | System Behavior | Physical Analogy |
|-------|----------------------|-----------------|------------------|
| [P1: Crisis](p1-crisis.md) | $\Phi < 0.3$ | Deep losing loop | Supercritical fluid |
| [P2: Stabilizing](p2-stabilizing.md) | $0.3 \leq \Phi < 0.5$ | Fragile equilibrium; bistable | Phase transition |
| [P3: Functional](p3-functional.md) | $0.5 \leq \Phi < 0.7$ | Stable flow | Liquid (laminar) |
| [P4: Thriving](p4-thriving.md) | $0.7 \leq \Phi < 0.85$ | Compound growth | Ferromagnetic |
| [P5: Scaling](p5-scaling.md) | $0.85 \leq \Phi$, $d\Phi/dt < 0$ | Structural stress | Supercooled liquid |

## Predictive Power

The probability of entering a crisis in the near future can be predicted by mathematically observing $\Phi(t)$ and its exact rate of change $\frac{d\Phi}{dt}$.

Using the logistic function $\sigma$, the probability of entering a Crisis State down the road (where time step $\Delta t$ is calculated in weeks format) is modeled as:

$$ P(\text{Crisis in } t+\Delta t) = \sigma\left(\frac{0.3 - \Phi(t)}{\frac{d\Phi}{dt} \cdot \Delta t}\right) $$

## Related
- [Hysteresis](hysteresis.md) — The gap between threshold values for upward vs downward transitions.
- [Digital Twin](digital-twin.md) — How $\Phi$ is estimated in real-time.
