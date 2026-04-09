---
title: "Skill"
type: concept
tags: [condition, development, om3, capability, v2-framework]
sources: [raw/1.md, raw/2.md, raw/5.md]
backlinks: [wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/concepts/structure-vs-development-rule.md, wiki/legacy/execution-system.md]
created: 2026-04-08
updated: 2026-04-08
status: stale
superseded_by: [wiki/concepts/12-block-E.md]
---

# Skill (OM3 - Legacy)

> [!WARNING]
> This is a fragmented legacy metric page. For the complete V2.1 unified Execution layer, see **[12 — Block E (Execution System)](../concepts/12-block-E.md)** and **[13 — Block A (Org Alignment)](../concepts/13-block-A.md)** for how Composition and Interactions limit pure capability.

## Definition

The third condition in the Execution System (`E`) block of the [Master Equation](../legacy/master-equation.md). Measures capability to solve the technical problems the team actually faces. Moved by the **Development** lever.

## Leading Indicators

- Pairing frequency
- Review depth
- Skill coverage breadth (bus factor)

## Lagging Indicators

- Inverse problem resolution time
- Repeated failures on similar issues
- Complexity-adjusted delivery rate

## If Near Zero

Engineers are stuck on every problem. Blockers accumulate. Solutions require heroics every time.

## Lever: Development

- Pair with a stronger engineer
- Narrow the problem scope
- Targeted coaching
- Show results from coaching before asking for budget

## V2 Context & Structural Gating

While Skill ($E_S$) sits in the Execution System (`E`), it is frequently governed tightly by **Team Composition & Roles ($TC$)** in the [Org Alignment (Block A)](../legacy/org-alignment.md) system.
- "We don't have the skills" may be a literal composition problem ($TC_{gap}$). In this case, pulling the local coaching/development lever will fail; you must escalate for hiring/restructuring via the [Lever-Access Rule](../concepts/lever-access-rule.md).
- Additionally, when $Skill$ drops systemically across seniors, check [Sustainability (Su)](../legacy/people-system.md). When $Su < 1.0$, advanced skills atrophy rapidly due to cognitive exhaustion.

## Disambiguation

See [Structure-vs-Development Rule](../concepts/structure-vs-development-rule.md): when you can't tell if the problem is Skill or [Coordination](../legacy/coordination.md), fix Structure first — coordination failures mask true skill levels.

## Related

- [Coordination](../legacy/coordination.md) — the parallel condition at the same fix-order level
- [Structure-vs-Development Rule](../concepts/structure-vs-development-rule.md) — disambiguation rule
- [Execution System](../legacy/execution-system.md) — Skill belongs to Block E
