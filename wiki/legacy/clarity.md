---
title: "Clarity"
type: concept
tags: [condition, direction, om1, v2-framework]
sources: [raw/1.md, raw/2.md, raw/5.md]
backlinks: [wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/legacy/execution-system.md]
created: 2026-04-08
updated: 2026-04-08
status: stale
superseded_by: [wiki/concepts/12-block-E.md]
---

# Clarity (OM1 - Legacy)

> [!WARNING]
> This is a fragmented legacy metric page. For the complete V2.1 unified Execution layer (including queuing physics logic and macro-gate bounds), see **[12 — Block E (Execution System)](../concepts/12-block-E.md)**.

## Definition

The first condition in the Execution System (`E`) block of the [Master Equation](../legacy/master-equation.md). Measures whether the team has a **shared understanding of goals, priorities, and success criteria**. Moved by the **Direction** lever.

## Leading Indicators

- Goal recall rate (can team members restate the goal consistently?)
- Stable priority list
- Low scope and priority churn rate

## Lagging Indicators

- Rework percentage (building the wrong thing)
- Discarded work
- Missed stakeholder expectations

## If Near Zero

The team builds wrong things. All effort is wasted. [Zero-Override Rule](../legacy/zero-override-rule.md) applies — fix Direction immediately.

## Lever: Direction

- Rewrite the goal in one sentence
- Define "done" explicitly
- Lock the priority order
- Repeat until every team member can restate it

## V2 Context & Strategic Gating

Before concluding a Clarity failure is strictly an Execution problem, verify that [Value Alignment (Block V)](../legacy/value-alignment.md) is not failing explicitly through **Strategic Fit ($SF$)**. Many persistent Clarity failures are actually symptoms of the [Strategic Drift Loop](../concepts/strategic-drift-loop.md).

- **Clarity ($E_C$)** asks: "Does the local team know what they're trying to do?"
- **Strategic Fit ($V_{SF}$)** asks: "Is what they're trying to do actually coherent and worth doing?"

You can have perfect Execution-Clarity around an incoherent objective. Pulling the Direction lever when the root cause is $V \approx 0$ is a failure of [Structure-vs-Development macro-disambiguation](../concepts/structure-vs-development-rule.md). Validate strategy before rewriting the team's local charter.

## Related

- [Execution System](../legacy/execution-system.md) — Clarity belongs to Block E
- [Fix-Order](../legacy/fix-order.md) — Clarity is fix position 1 inside the E-block
