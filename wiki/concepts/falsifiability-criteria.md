---
title: "Falsifiability Criteria"
type: concept
tags: [science, validation, empirical-testing]
sources: [raw/3.md]
backlinks: [wiki/legacy/master-equation.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Falsifiability Criteria

## Definition

For the framework to be considered predictive science rather than management philosophy, its claims must be empirically falsifiable.

## Testable Hypotheses

1. **H1 (Multiplicative Zero):** Teams with any condition $c_i < 0.2$ will have output < 30% of capacity, regardless of other conditions.
2. **H2 (WIP/Cycle Time):** Reducing WIP by 50% will reduce cycle time by >30% within 2 sprints, assuming other conditions remain stable.
3. **H3 (State Persistence):** Teams in [P3 (Functional)](p3-functional.md) will remain there for >6 months in the absence of external growth shocks or reorgs.
4. **H4 (Intervention Latency):** Lever changes will move leading indicators within 1-2 weeks, but lagging indicators won't move for 4-6 weeks (Nyquist constraint).
5. **H5 (Hysteresis):** The transition threshold for Crisis → Stabilizing is mathematically higher than the regression threshold for Stabilizing → Crisis.

## Empirical Validation Protocol

Validating these claims requires a **Minimum Viable Dataset**:
- **N = 50 teams** across 10+ companies.
- **T = 12 months** of longitudinal data reporting weekly telemetry metrics and surveys.

**Analysis Plan constraints:**
- Construct validity requires a Principal Component Analysis (PCA) on dimension indicators; confirming a primary PC explains over 60% of the variance.
- Predictive Validation requires a proven $R^2 > 0.6$ showing $\Phi(t)$ correlates with $\text{Output}(t+1)$.

## Related
- [02 — Master Equation](02-master-equation.md) — Defines the blocks and multiplicative structure assumed by H1 and validation designs.
- [Utilization Curve](utilization-curve.md) — Provides the math for H2.
- [Hysteresis](hysteresis.md) — Provides the math for H5.
