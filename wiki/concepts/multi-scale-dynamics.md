---
title: "Multi-Scale Dynamics"
type: concept
tags: [scale, temporal-decoupling, coupling, feedback]
sources: [raw/3.md]
backlinks: [wiki/concepts/fractal-scaling.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Multi-Scale Dynamics

## Definition

Engineering organizations operate simultaneously across three scales: Micro (Team), Meso (Department), and Macro (Organization).  

The output of a department is not a simple sum of team outputs due to complex **upward, downward, and lateral coupling**.

## Formal Multi-Scale Model

The scales are bound by differential equations representing internal dynamics, external noise $\xi$, and the top-down ($\alpha$) or bottom-up ($\beta$) coupling coefficients:

$$ \frac{d\Phi_{\text{team}}}{dt} = f_{\text{team}}(\Phi_{\text{team}}) + \alpha \cdot (\Phi_{\text{dept}} - \Phi_{\text{team}}) + \xi_{\text{team}}(t) $$
$$ \frac{d\Phi_{\text{dept}}}{dt} = f_{\text{dept}}(\Phi_{\text{dept}}) + \beta \cdot \langle \Phi_{\text{team}} \rangle + \xi_{\text{dept}}(t) $$

## Resonance and Anti-Resonance

Destructive interference occurs when layers operate on different natural frequencies but are tightly coupled. 
*Example:* A department changes strategy mid-quarter while teams are mid-sprint. Work is discarded and throughput collapses.

## Solution: Temporal Decoupling

To prevent anti-resonance, organizations must temporally decouple the scales:
- The Department sets **invariant goals** for the full quarter.
- Teams have autonomy to adapt **tactics** within discrete sprints.
- Synchronization occurs only at quarter boundaries.

## Scale-Free Chaos

A zero at the Macro level (e.g., CEO pivots strategy constantly) cascades down, creating zeros at the Meso and Micro levels. A team cannot "local optimize" its way out of macro-level systemic failure.

## Related
- [Fractal Scaling](fractal-scaling.md) — How the same physics apply at all scales.
- [Nyquist Constraint](nyquist-constraint.md) — Temporal rules for changing strategy.
