---
title: "Fix-Order"
type: concept
tags: [diagnostics, hierarchy, fix-order, decision-tree, v2-framework]
sources: [raw/1.md, raw/2.md, raw/5.md, raw/6.md]
backlinks: [wiki/legacy/zero-override-rule.md, wiki/concepts/lever-access-rule.md, wiki/concepts/structure-vs-development-rule.md, wiki/entities/table-2-diagnostics.md, wiki/legacy/clarity.md, wiki/concepts/feedback-speed.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/20-diagnostic-sequence.md]
---

# Fix-Order (Legacy)

> [!WARNING]
> This logic tree has been formally replaced by the V2.1 rules. For the Canonical diagnostic flow, refer to **[20 — Diagnostic Sequence](../concepts/20-diagnostic-sequence.md)**.

## Definition

The prescribed sequence for diagnosing and fixing conditions when the system is failing. Because of the V2 Gating Theorems, diagnosing Execution without securing the macro-environment will fail. The fix-order is split into **Macro** and **Micro** sequences.

## The Canonical Sequence

The V2.1 flow is best read as four stages rather than a single linear ladder:

1. **Check no-win conditions first**: Verify there is no near-zero failure in Strategic Fit / Customer Value ($V$), Psychological Safety / Sustainability ($P$), or hard Org blockers like Incentive Alignment / Cross-Team Architecture ($A$). If one is near zero, stop and apply zero-override.
2. **Verify People integrity**: Confirm the measurement system is trustworthy before relying on metrics. Low $PS$ means the rest of the diagnostic stack is politically distorted.
3. **Diagnose local Execution ($E$)**: Apply the classical internal sequence only after the environment is at least minimally viable.
4. **Inspect Org Alignment more deeply if E keeps relapsing**: Persistent execution failures after local intervention are usually suppressed by $A$, even when there was no obvious step-0 org collapse.

## The Micro Sequence (Execution Block E)

Once the macro blocks are stable, apply the classical internal Execution sequence:

1. **[Clarity](../legacy/clarity.md)** — Check Direction first. Can everyone restate the local goal?
2. **[Focus](../legacy/focus.md)** — Check Protection. Is WIP within cap? Are interruptions controlled?
3. **[Skill](../legacy/skill.md) / [Coordination](../legacy/coordination.md)** — Check Development and Structure. Apply [Structure-vs-Development Rule](../concepts/structure-vs-development-rule.md) if ambiguous.
4. **[Quality](../legacy/quality.md)** — Check Standards. Are they holding under pressure?

## The Learning Layer (Block L)

- **[Feedback Speed](../concepts/feedback-speed.md)** — Is the time-to-detect signal shrinking? Optimize Learning after the system is stable enough to benefit from faster feedback.

## Override

The [Zero-Override Rule](../legacy/zero-override-rule.md) supersedes this hierarchy: if any critical systemic condition drops to near zero across ANY block, it must be addressed immediately to prevent a total phase collapse.

## Related

- [Table 2](../entities/table-2-diagnostics.md) — the diagnostic reference implementing this hierarchy
- [Zero-Override Rule](../legacy/zero-override-rule.md) — overrides this hierarchy
- [Gating Theorems](../concepts/v2-theorems.md) — the mathematical rationale for why environment checks precede local optimization
