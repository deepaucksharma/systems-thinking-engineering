---
title: "Telemetry Engine Schema"
type: concept
tags: [v2.1-canonical, measurement, telemetry, digital-twin, data-schema]
sources: []
backlinks: [wiki/_indexes/concepts.md, wiki/concepts/digital-twin.md, wiki/concepts/41-metrics-by-block.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Telemetry Engine Schema

This page describes how the framework's abstract variables can be grounded in observable telemetry. It is best treated as a **schema for measurement design**, not as a rigid universal ETL specification.

The goal is not to force every organization into the same data model. The goal is to show how raw operational signals might be translated into block-level estimates.

## Core Measurement Sources

Three source families usually matter most:

1. **Issue-tracking systems**
   Examples: Jira, Linear, Asana
   Useful for: WIP, blocker duration, queue age, batch size, intake volatility

2. **Version-control and delivery systems**
   Examples: GitHub, GitLab, CI/CD tooling
   Useful for: review latency, deploy cadence, defect escape proxies, integration friction

3. **People and survey systems**
   Examples: pulse surveys, HRIS, engagement tooling
   Useful for: safety, sustainability, trust, fairness, burnout signals

No single source should be treated as sufficient on its own.

## Translation Logic by Block

### Block V: Value Alignment

Possible signals:
- proportion of work mapped to explicit priorities or strategic themes;
- evidence that important work receives actual staffing and budget;
- evidence that reward and promotion logic tracks durable value rather than visible output.

Value is usually the hardest block to infer from telemetry alone. It often requires qualitative judgment and explicit strategy review.

### Block P: People System

Possible signals:
- survey items related to safety, trust, and perceived fairness;
- after-hours work and overload indicators;
- sick leave, attrition, or other strain proxies;
- signs of reduced improvement effort or growing cynicism.

This block has the highest measurement-risk. If telemetry collection itself feels coercive, the measurement system can damage the thing it is trying to observe.

### Block E: Execution System

Possible signals:
- WIP, queue age, and batch size;
- review latency and handoff delay;
- defect escape and rework load;
- cycle-time distribution and tail behavior.

This is usually the easiest block to instrument, but it is also the block most likely to be over-trusted because the data feels concrete.

### Block A: Org Alignment

Possible signals:
- cross-team blocker patterns;
- dependency hops required to complete common work;
- evidence that decision rights are unclear or fragmented;
- mismatch between stated priorities and actual reward structures.

Much of Block A has to be inferred from patterns in multiple systems rather than from one explicit dashboard.

### Block L: Learning and Adaptation

Possible signals:
- time from action to signal;
- whether retrospective actions are actually completed;
- persistence of repeated failure modes;
- documentation freshness and onboarding friction;
- change load relative to absorption capacity.

Learning is especially easy to mis-measure if teams are performing the rituals without changing behavior.

## Distillation and Interpretation

A telemetry engine may combine dozens of raw signals. The key design challenge is not data collection; it is signal interpretation.

Useful practices include:
- combining multiple weak indicators instead of trusting one proxy;
- distinguishing leading from lagging indicators;
- segmenting by team, workflow, or dependency lane instead of averaging everything together;
- lowering confidence when the measurement environment itself is compromised.

Statistical techniques like PCA or latent-variable modeling can help, but they are aids to interpretation, not substitutes for judgment.

## Practical Warnings

- Do not infer trust from systems that people know are punitive.
- Do not treat data availability as proof of data importance.
- Do not let the schema become more rigid than the organization it is trying to observe.
- Do not automate sensitive management actions directly from raw telemetry.

## Related

- [41 - Metrics by Block](41-metrics-by-block.md) - block-level metric reference
- [Measurement Theory](measurement-theory.md) - latent-variable construction and validation
- [Ethical Measurement](ethical-measurement.md) - safeguards and side effects
- [Digital Twin](digital-twin.md) - operational model using telemetry as input
