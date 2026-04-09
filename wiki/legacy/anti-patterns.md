---
title: "Anti-Patterns (Fallacies)"
type: concept
tags: [anti-pattern, executive, management, failure-mode]
sources: [raw/4.md]
backlinks: [wiki/concepts/temporal-integration-loop.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/51-anti-patterns.md]
---

# Anti-Patterns (Legacy)

> [!WARNING]
> This page captures the earlier visual anti-pattern map. For the canonical V2.1 reference, use **[51 — Canonical Anti-Patterns]()**.

## Definition

Executive Anti-Patterns are logical fallacies that attempt to solve systemic failures with behavioral demands. Their root causes can always be mapped to thermodynamic constraints within the framework.

## Diagram 11: The Anti-Pattern Map

| Anti-Pattern | Root System Failure |
|---|---|
| **1. Command focus through pressure** <br> *"Just focus—stop getting distracted"* | Context switching is forced by structure, not choice. |
| **2. Label poor performance as a people failure** | A smart person in a chaotic system looks incompetent (Cascade Rule). |
| **3. Add detail to clarify a bad goal** <br> *"Write longer PRDs"* | More detail on a wrong goal just means building the wrong thing faster. |
| **4. Add process to fix coordination** <br> *"We need a new meeting"* | Process without ownership is bureaucracy. Fix structure first. |
| **5. Relax quality under pressure** <br> *"Skip review just this once"* | The rework loop is infinitely more expensive than the review. |
| **6. Change strategy weekly** <br> *"We need to be agile"* | Violates the [Nyquist Constraint](../legacy/nyquist-constraint.md); manager induces thrash. |
| **7. Run surveys without changes** | Telemetry without action breaks the control loop and erodes trust. |
| **8. Assume stable systems persist** | Entropy guarantees condition decay without active maintenance. |
| **9. Manager writes code to unblock** | Managerial heroics mask system failures and prevent true scaling. |
| **10. Grant one quality exception** | One exception establishes a lower permanent standard floor. |

## Application

Check the Anti-Pattern map before acting. If your proposed solution matches one of the 10 fallacies, redirect your focus to the systemic root cause defined in Table 2.

## What Changed In V2.1

- The canonical page groups anti-patterns around the newer block and gating model instead of the older diagram set.
- Tail-risk, measurement-reliability, and org-gating failures are now described with more explicit mathematical framing.
- This page remains useful as a compact legacy checklist, but it is no longer the canonical anti-pattern reference.

## Related
- [Table 2 — Diagnostics](../entities/table-2-diagnostics.md)
