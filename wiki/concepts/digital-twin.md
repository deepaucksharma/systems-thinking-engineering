---
title: "Digital Twin (Discrete-Event Simulation)"
type: concept
tags: [simulation, data, telemetry, modeling]
sources: [raw/3.md]
backlinks: [wiki/concepts/order-parameter.md, wiki/concepts/temporal-integration-loop.md]
created: 2026-04-08
updated: 2026-04-09
status: active
---

# Digital Twin (Organizational Simulation)

## Definition

In this framework, a digital twin means a continuously updated operational model of the engineering system. It is not a perfect replica of the organization. It is a **decision-support model** that combines telemetry, system assumptions, and scenario analysis to help operators reason about likely future behavior.

The most useful form of the twin is usually:
- descriptive first;
- diagnostic second;
- predictive only where the signals are stable enough to support prediction.

## What the Twin Is For

A digital twin can help answer questions like:
- is the system drifting toward overload or instability?
- which block appears to be deteriorating first?
- what is likely to happen if WIP, batch size, staffing mix, or intake volatility changes?

This is much more valuable than pretending the twin can forecast exact delivery outcomes with high confidence.

## Inputs

The twin draws on telemetry described in [Telemetry Engine Schema](telemetry-engine-schema.md), typically from:
- issue-tracking systems for flow and blocker data;
- version-control and CI/CD systems for delivery and review signals;
- survey or people data for safety, sustainability, and trust signals.

The twin is only as good as the measurement environment. If safety is low or incentives encourage gaming, the model should lower confidence in its own outputs.

## Typical Outputs

Useful outputs include:
- estimated block-level health trends;
- warnings about rising variability, overload, or coordination drag;
- scenario comparisons rather than single-point predictions;
- confidence bands showing how uncertain the estimate is.

Example:

> Focus appears to be degrading, with rising arrival volatility and batch size. If current intake continues, the team is more likely to move from functional to unstable than to recover naturally.

That kind of output is often more honest than a precise-looking forecast like "P3 to P2 in 21 days."

## Counterfactual Use

The digital twin is especially valuable for "what if" reasoning:
- what if we reduce batch size instead of adding headcount?
- what if we stop starting new work for two weeks?
- what if the dependency path across teams is cut in half?

Counterfactuals are usually safer than direct prediction because they help compare interventions even when the absolute forecast is noisy.

## Practical Warnings

- Do not confuse the twin with reality.
- Do not automate management decisions directly from the twin.
- Do not trust precision that the underlying data cannot justify.
- Do not treat people metrics as neutral if the organization is using them coercively.

## Related

- [Discrete-Event Simulation (DES)](discrete-event-simulation.md) - one computational approach for implementing the twin
- [Telemetry Engine Schema](telemetry-engine-schema.md) - operational mapping from raw signals to modeled variables
- [Order Parameter (Phi)](order-parameter.md) - one way of summarizing system state inside the model
