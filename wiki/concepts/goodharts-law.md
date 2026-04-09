---
title: "Goodhart's Law"
type: concept
tags: [metrics, ethics, measurement, anti-pattern]
sources: [raw/3.md]
backlinks: [wiki/concepts/digital-twin.md, wiki/concepts/51-anti-patterns.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Goodhart's Law & The Automation Paradox

## Definition

> "When a measure becomes a target, it ceases to be a good measure." — Charles Goodhart

## The Automation Paradox

Operationalizing the framework requires pervasive measurement (cycle times, commit frequencies, review latencies). This creates a dangerous temptation: automating management decisions completely (e.g., "If $\Phi < 0.3$, instantly freeze deployments").

Removing human judgment triggers Goodhart's Law. If metrics define automated punishment, engineers will game the metrics. They will artificially split tasks to improve "completion rate," or rubber-stamp code reviews to improve "latency."

## The Panopticon Risk 

If individuals know their personal metrics feed a score, it creates a surveillance state, destroying psychological safety—the unmeasured bedrock of all systems.

## Mitigation Principles

1. Aggregate metrics to the team level, never the individual.
2. Metrics inform system design; they never replace management judgment.
3. No surprise metrics—all dashboards must be public.
4. Individuals may opt-in to advanced metrics for coaching.

## Framework Fit and Correctness Evaluation

> [!NOTE]
> **Theoretical Convergence:** Goodhart's Law is explicitly modeled in the V2.1 framework via the [Measurement Theory](measurement-theory.md) premise of "Latent Variables" and the [Mechanism Design](incentive-mechanism-design.md) tension matrices.

The framework mathematically assumes that you cannot measure the actual outcome ($V_{eff}$) directly in real-time. If you substitute a proxy metric (like tickets closed) and tie it to the Incentive Architecture ($IA$), Game Theory dictates that Psychological Safety ($PS$) will instantly invert to protect the agents, destroying Learning ($L$). The Master Equation requires the use of orthogonal, non-punitive *latent* indicators (e.g., measuring $Su$ via eNPS rather than lines of code) specifically to mathematically neutralize Goodhart's Law.

## Related
- [Digital Twin](digital-twin.md) — The system most likely to trigger these ethical risks.
- [Measurement Theory](measurement-theory.md) — The mathematical defense against Goodhart's Law.
- [41 - Metrics by Block](41-metrics-by-block.md) — Gathering the data responsibly without targeting.
