---
title: "Coordination"
type: concept
tags: [condition, structure, om4, dependencies, ownership, v2-framework]
sources: [raw/1.md, raw/2.md, raw/5.md]
backlinks: [wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/concepts/structure-vs-development-rule.md, wiki/legacy/skill.md, wiki/concepts/p5-scaling.md, wiki/legacy/execution-system.md]
created: 2026-04-08
updated: 2026-04-08
status: stale
superseded_by: [wiki/concepts/12-block-E.md]
---

# Coordination (OM4 - Legacy)

> [!WARNING]
> This is a fragmented legacy metric page. For the complete V2.1 unified Execution layer and the updated Team Topologies heuristics, see **[12 — Block E (Execution System)]()** and **[13 — Block A (Org Alignment)]()**.

## Definition

The fourth condition in the Execution System (`E`) block of the [Master Equation](../legacy/master-equation.md). Measures whether work flows without collisions, duplications, or gaps. Moved by the **Structure** lever.

## Leading Indicators

- Clear ownership map
- Lower dependency age
- Blocker duration/total work

## Lagging Indicators

- Cross-team slips
- Handoff failures
- Constant rework from misalignment

## If Near Zero

Work collides. Teams duplicate effort or leave gaps. Integration is painful and unpredictable. Ownership disputes are rampant.

## Lever: Structure

- Assign clear owners for every surface
- Define interfaces between components/teams
- Simplify dependencies
- Fix intra-team structure before attempting cross-team fixes

## V2 Context & Gating

When experiencing persistent Coordination failures that cross team boundaries, escalate to [Org Alignment (Block A)](../legacy/org-alignment.md). Specifically, check **Cross-Team Architecture (XT)**. This is often a Conway's Law violation where team-level fixes cannot overcome structural dependency failures. You cannot fix Coordination by improving team processes if the architecture requires constant cross-team negotiation.

## Related

- [Skill](../legacy/skill.md) — the parallel condition
- [Structure-vs-Development Rule]() — fix coordination first when ambiguous
- [P5-Scaling]() — scaling stresses coordination most
- [Execution System](../legacy/execution-system.md) — Coordination belongs to Block E
