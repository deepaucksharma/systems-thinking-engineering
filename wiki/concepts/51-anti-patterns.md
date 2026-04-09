---
title: "51 — Canonical Anti-Patterns"
type: concept
tags: [v2.1-canonical, reference, failures, anti-patterns, executive]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/20-diagnostic-sequence.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Canonical System Anti-Patterns

Organizations fail in predictable ways when trying to optimize output without respecting the V2.1 Control Theory constraints. These are the most common executive fallacies.

## 1. Manager Oscillation (Nyquist Violation)
**The Error:** An executive makes a major change to Block A (like a re-org or strategy shift) and evaluates the result 2 weeks later. Because they see a drop in performance, they immediately intervene again.
**The Reality:** The [J-Curve](06-time-constants.md) usually implies a temporary dip. Because Block A has a time constant of months/years, a 2-week measurement is totally aliased. The manager becomes the primary source of instability in the system.

## 2. The Incentive Death Spiral
**The Error:** Pulling the "Standards/Quality" lever on a team that is actively burning out, while simultaneously rewarding executives for shipping fast.
**The Reality:** A [People System](11-block-P.md) failure ($Su < 1.0$) means quality is structurally suppressed. If Incentives ($IA$) reward speed over prevention, the team will simply game the new quality metrics (e.g., writing tautological tests).

## 3. Fear Amplification via Fast Feedback
**The Error:** Installing sophisticated DORA metrics, PR cycle-time tracking, and automated CI/CD dashboards in an environment with low Psychological Safety ($PS \approx 0$).
**The Reality:** The framework's measurement-reliability gate ([02 - Master Equation](02-master-equation.md), Gate 1) treats fast feedback without psychological safety as distortion-accelerating, not learning-accelerating. Engineers will optimize for the metric (gaming batch sizes, hiding failures) rather than the outcome.

## 4. Unbounded Utilization
**The Error:** Running the engineering team at 100% capacity to ensure "no one has free time", assuming this maximizes ROI.
**The Reality:** Software development represents an $M^X/M/1/\infty$ queue. Due to queuing physics, cycle time goes nonlinear at 85% utilization and infinite at 100%. Operating at 100% capacity is a guarantee of infinite queue growth, not maximum productivity.

## 5. The Mean-Masked Tail Risk
**The Error:** Making quarterly commitments based on the team's *average* (mean) cycle time.
**The Reality:** Software delivery is extremely heavy-tailed. A team with a mean cycle time of 3 days might have a P95 cycle time of 35 days (a high [Obesity Index](12-block-E.md)). In V2.1 this shows up in the separate variability penalty, even though you usually detect it first in execution data. If you plan based on means, you systematically underestimate catastrophic delays. Use P95 for quarterly commitments.

## 6. The Local-Optima Trap (Macro-Blindness)
**The Error:** Launching an "Agile Transformation" at the team level (Block E) to fix a Cross-Team Architecture (Block A) failure.
**The Reality:** [Org Alignment gates Execution](02-master-equation.md). If four teams are forced to coordinate on a monolith due to a Conway's Law violation, no amount of Scrum coaching will speed them up. Apply the Inverse Conway maneuver to redesign the structure instead.

## Historical Comparison

- Earlier anti-pattern catalog: [Anti-Patterns](../legacy/anti-patterns.md)
- Diagnostic context: [20 - Diagnostic Sequence](20-diagnostic-sequence.md)
