---
title: "Feedback Speed"
type: concept
tags: [condition, feedback, om6, learning-rate, cycle-time, telemetry, v2-framework]
sources: [raw/1.md, raw/2.md, raw/3.md, raw/4.md, raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/concepts/littles-law.md, wiki/legacy/learning-adaptation.md, wiki/concepts/fear-amplification-loop.md, wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/legacy/nyquist-constraint.md, wiki/concepts/winning-loop.md, wiki/concepts/losing-loop.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Feedback Speed (OM6)

## Definition

Now conceptually housed as the primary term of the **Learning & Adaptation (Block L)** (formerly the multiplier in V1's master execution equation). Measures the time from action to consequential signal (technical and product). It amplifies the impact of all other conditions.

## Measurement Proxy

$$FS(t) = \frac{\text{baseline\_cycle}}{\text{current\_cycle}}$$

Where baseline cycle is the reference review cycle length. Lead time to defect detection, time to user signal, CI/CD cycle time are all markers.

## Leading Indicators

- Time-to-detect (how quickly defects surface after introduction)
- Review turnaround time (PR latency)
- Deploy frequency
- Retrospective cadence

## Lagging Indicators

- Recurring incidents (same class of failure repeating)
- Slow improvement velocity 
- Morale erosion

## If Near Zero

Discovering bugs in production months after introduction. User behavior unknown until launch. 
The [Nyquist Constraint](../legacy/nyquist-constraint.md) is violated: the manager is acting on aliased, stale data. 

## V2 Context & Diagnostic Gating

**Feedback Speed ($FS$) is gated tightly by Psychological Safety ($PS$):**
Fast feedback loops without Safety do not accelerate learning; they accelerate distortion. 
- Retrospectives identify symptoms, not causes (honesty is unsafe).
- Fast metrics are gamed.
- Postmortems become blame rituals.

Because of the [Measurement Reliability Theorem](v2-theorems.md), the diagnostic flow demands a hard gate: **If Feedback Speed is low, the diagnostic MUST check: "Is $PS$ low?"** If yes, attempting to improve $FS$ (via tight CI/CD or PR metrics) will trigger the [Fear Amplification Loop](fear-amplification-loop.md), poisoning the telemetry entirely.

## Lever: Feedback Speed

- **Shrink batch size** — smaller deployments = faster feedback loops
- **Instrument telemetry** — automated detection of errors 
- **Customer feedback tight loops** — shorten the signal from user pain to fix
- **Improve CI/CD latency** 

## Rework Loop Speed

In the Stock-and-Flow model ([Little's Law](littles-law.md)), fast detection (Feedback Speed high) means rework enters cheaply; slow detection means rework is catastrophically expensive.

## Related

- [Learning & Adaptation](../legacy/learning-adaptation.md) — Feedback Speed belongs to Block L
- [People System](../legacy/people-system.md) — Psychological Safety gates feedback
- [Nyquist Constraint](../legacy/nyquist-constraint.md) — how fast feedback must arrive 
- [Little's Law](littles-law.md) — the two-speed rework loop
