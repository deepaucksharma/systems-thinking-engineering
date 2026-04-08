---
title: "Measurement Theory"
type: concept
tags: [metrics, latent-variable, pca, reliability, measurement-theory]
sources: [raw/3.md]
backlinks: [wiki/entities/master-equation.md, wiki/concepts/metrics-framework.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Measurement Theory

## Definition

The engineering framework requires operationalizing abstract social constructs (like [Clarity](clarity.md) or [Skill](skill.md)) so they can be managed scientifically. You cannot manage what you cannot measure. Because these conditions are abstract, they are treated as **latent variables**.

## The Latent Variable Model

Each condition $c_i$ is a latent variable estimated from a vector of observable indicators $\mathbf{x}_i(t)$ and learned weights $\mathbf{\beta}_i$:

$$c_i(t) = f(\mathbf{x}_i(t), \mathbf{\beta}_i)$$

### Example: Clarity (Direction) Measurement

Observable indicators vector ($x$):
- $x_1$: Goal recall rate (% of team who can restate the goal verbatim)
- $x_2$: Priority churn (number of priority changes per week)
- $x_3$: Requirement volatility (% of accepted work later discarded)
- $x_4$: "Done" agreement (% of team who agree on acceptance criteria)

Using dimensional analysis, where Clarity is framed as **Information Entropy Reduction**:

$$C(t) = \frac{1}{4}\left(\frac{x_1}{100} + \left(1 - \frac{x_2}{x_{2,max}}\right) + \left(1 - \frac{x_3}{100}\right) + \frac{x_4}{100}\right)$$

## Statistical Validation Requirements

To guarantee these metrics are validly mapping to the physics of the system, they must pass three statistical tests:

1. **Principal Component Analysis (PCA):** If the framework is correct, the multiple observable indicators for a single condition must exhibit high covariance. PCA should yield a first principal component explaining >60% of variance.
2. **Test-Retest Reliability:** Measuring the exact same team twice within one week (assuming no massive disruptions) should yield similar condition values ($r > 0.8$).
3. **Convergent Validity:** Leading indicator scores (like Clarity score) must correlate strongly with the eventual lagging outcomes (like rework %).

## Related
- [Master Equation](../entities/master-equation.md) — the mathematical foundation incorporating these measurements.
- [Metrics Framework](metrics-framework.md) — the leading/lagging implementation of measurement.
- [Ethical Measurement](ethical-measurement.md) — limitations and dangers of operationalizing metrics.
