---
title: "Zero-Override Rule"
type: concept
tags: [rule, foundation, diagnostics, fix-order]
sources: [raw/1.md, raw/2.md]
backlinks: [wiki/entities/master-equation.md, wiki/entities/table-2-diagnostics.md, wiki/sources/diagram-set-1.md, wiki/sources/diagram-set-2.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Zero-Override Rule

## Definition

If any condition in the [Master Equation](../entities/master-equation.md) is near zero, **fix it first** — regardless of the default [fix-order](fix-order.md) hierarchy.

## Rationale

Because the equation is multiplicative, a single near-zero condition collapses the entire output. No amount of improvement in other conditions compensates. Arithmetic makes this non-negotiable.

## Operational Rule

> Do not average. Do not defer. Fix the zero FIRST.

## Application in Diagnostics

In the [Table 2](../entities/table-2-diagnostics.md) decision tree, the zero-override check is the **first gate** — before entering the normal fix-order hierarchy (Clarity → Focus → Skill/Coordination → Quality).

## Related

- [Master Equation](../entities/master-equation.md) — the multiplicative structure that creates this rule
- [Fix-Order](fix-order.md) — the default diagnostic hierarchy that this rule overrides
- [Losing Loop](losing-loop.md) — the dynamic that often drives conditions to zero
