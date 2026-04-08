---
title: "Quality"
type: concept
tags: [condition, standards, om5, defects, gates]
sources: [raw/1.md, raw/2.md]
backlinks: [wiki/entities/master-equation.md, wiki/concepts/fix-order.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Quality (OM5)

## Definition

The fifth condition in the [Master Equation](../entities/master-equation.md). Measures whether output meets standards and doesn't break users. Moved by the **Standards** lever.

## Leading Indicators

- Test execution rate
- Review completion rate
- Observability coverage

## Lagging Indicators

- Escaped defects
- Rollback rate
- Incident frequency

## If Near Zero

Output breaks users. Rework dominates new work. The [Losing Loop](losing-loop.md) accelerates through the rework path.

## Lever: Standards

- Tighten test automation
- Enforce code review
- Stop bypassing gates under pressure
- Start with voluntary adoption on highest-risk code path, then expand

## Related

- [Losing Loop](losing-loop.md) — quality degradation feeds the rework cycle
- [Metrics Framework](metrics-framework.md) — quality metrics detail
