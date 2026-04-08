---
title: "Resource Allocation Game"
type: concept
tags: [political-economy, game-theory, slack, utilization]
sources: [raw/3.md]
backlinks: [wiki/concepts/lever-access-rule.md, wiki/concepts/focus.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# The Resource Allocation Game

## Definition

The engineering framework assumes managers have unilateral control over levers. In reality, organizations are multi-agent systems with competing interests and asymmetric information, requiring game-theoretic solutions.

## The Central Conflict: Slack vs. Utilization

- **Executive Leadership (EL)** wants maximum utilization (Output/Capacity → 100%).
- **Engineering Managers (EM)** want strategic slack (Utilization ≈ 80%) to preserve flow and resilience.

These goals are fundamentally incompatible. High utilization causes cycle time to approach infinity, leading to the [Losing Loop](losing-loop.md). 

## Principal-Agent Problem

Executive Leadership cannot directly observe system conditions (Clarity, Focus, Quality). They observe lagging metrics like quarterly delivery or optics ("busyness"). When EL sets aggressive goals, the EM often overcommits to appear cooperative, resulting in systemic overload and delayed delivery.

## Nash Equilibrium: Suboptimal Overcommitment

Without mechanism design, the stable equilibrium is destructive:
1. EL assumes EM is sandbagging.
2. EM overcommits.
3. Team burns out; quality degrades.
4. Delivery slips.
5. EL increases pressure.

## Mechanism Design: Credible Signaling

To break the equilibrium, the EM must use **costly signals** to reveal true system state:
- Public WIP boards.
- Automated telemetry (removing info asymmetry).
- Explicit refusal accompanied by alternatives ("X or Y, but not both").

## Related
- [Utilization Curve](utilization-curve.md) — The physics behind why EM needs slack.
- [Lever-Access Rule](lever-access-rule.md) — The political costs of moving levers.
