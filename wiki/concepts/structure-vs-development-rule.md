---
title: "Structure-vs-Development Rule"
type: concept
tags: [rule, diagnostics, skill, coordination, disambiguation]
sources: [raw/1.md, raw/2.md]
backlinks: [wiki/entities/table-2-diagnostics.md, wiki/sources/diagram-set-1.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Structure-vs-Development Rule

## Definition

When you cannot tell whether a problem is caused by a **skill gap** or a **coordination failure**, **fix Structure first.**

## Rationale

Coordination failures mask skill levels. When ownership is unclear and work collides, even skilled engineers appear to struggle — not because they lack ability, but because they're fighting structural friction. Clarifying structure reveals true skill levels.

## Application

In the [Table 2](../entities/table-2-diagnostics.md) diagnostic decision tree:
1. If the symptom suggests capability or coordination failure...
2. And you can't tell which...
3. Fix Structure (assign clear owners, define interfaces, simplify dependencies)
4. Then re-assess — if problems persist with clear ownership, the issue is genuinely skill

## Related

- [Table 2](../entities/table-2-diagnostics.md) — the diagnostic table embedding this rule
- [Coordination](coordination.md) — the condition improved by Structure
- [Skill](skill.md) — the condition revealed once Structure is fixed
- [Fix-Order](fix-order.md) — where this rule sits in the hierarchy
