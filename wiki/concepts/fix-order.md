---
title: "Fix-Order"
type: concept
tags: [diagnostics, hierarchy, fix-order, decision-tree]
sources: [raw/1.md, raw/2.md]
backlinks: [wiki/concepts/zero-override-rule.md, wiki/concepts/lever-access-rule.md, wiki/concepts/structure-vs-development-rule.md, wiki/entities/table-2-diagnostics.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Fix-Order (Default Diagnostic Hierarchy)

## Definition

The prescribed sequence for diagnosing and fixing conditions when multiple are degraded and none is at zero:

1. **[Clarity](clarity.md)** — Check Direction first. Can everyone restate the goal?
2. **[Focus](focus.md)** — Check Protection. Is WIP within cap? Are interruptions controlled?
3. **[Skill](skill.md) / [Coordination](coordination.md)** — Check Development and Structure. Apply [Structure-vs-Development Rule](structure-vs-development-rule.md) if ambiguous.
4. **[Quality](quality.md)** — Check Standards. Are they holding under pressure?
5. **Feedback Speed** — Check learning rate. Is time-to-detect shrinking?

## Override

The [Zero-Override Rule](zero-override-rule.md) supersedes this hierarchy: if any condition is near zero, fix it first regardless of position in the fix-order.

## Cascade Rule

Before diagnosing lower-order conditions (Skill, Coordination, Quality), verify that higher-order conditions (Clarity, Focus) are in place. Apparent capability problems may be artifacts of unclear direction or overloaded teams.

## Related

- [Table 2](../entities/table-2-diagnostics.md) — the diagnostic reference implementing this hierarchy
- [Zero-Override Rule](zero-override-rule.md) — overrides this hierarchy
