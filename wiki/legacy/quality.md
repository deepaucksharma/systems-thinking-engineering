---
title: "Quality"
type: concept
tags: [condition, standards, om5, defects, gates, v2-framework]
sources: [raw/1.md, raw/2.md, raw/5.md]
backlinks: [wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/legacy/execution-system.md]
created: 2026-04-08
updated: 2026-04-08
status: stale
superseded_by: [wiki/concepts/12-block-E.md]
---

# Quality (OM5 - Legacy)

> [!WARNING]
> This is a fragmented legacy metric page. For the complete V2.1 unified Execution layer, taking into account new Heavy-Tail and self-organized criticality features, see **[12 — Block E (Execution System)](../concepts/12-block-E.md)**.

## Definition

The fifth condition in the Execution System (`E`) block of the [Master Equation](../legacy/master-equation.md). Measures whether output meets standards without rework (escaped defects). Moved by the **Standards** lever.

## Leading Indicators

- Test execution rate
- Review completion rate
- Observability coverage

## Lagging Indicators

- Escaped defect rate
- Rework percentage
- Incident frequency

## If Near Zero

Output breaks users. Defect avalanches and perpetual firefighting. The [Losing Loop](../concepts/losing-loop.md) accelerates through the rework path.

## Lever: Standards

- Tighten test automation
- Enforce code review
- Stop bypassing gates under pressure
- Start with voluntary adoption on highest-risk code path, then expand

## V2 Context & Burnout Gating

When Quality consistently drops, it is critically important to perform a macro-block check before assuming low Execution Standards ($E_Q$):
- **Check [People System (Block P)](../legacy/people-system.md)** for Sustainability ($Su$) failures. Quality degradation is the primary trailing symptom of burnout. Pulling the Execution *Standards* lever on a burned-out team is catastrophic—it triggers the [Incentive Death Spiral](../concepts/incentive-death-spiral.md) by applying more pressure to an exhausted system.
- **Check [Org Alignment (Block A)](../legacy/org-alignment.md)** for Incentive Alignment ($IA$). If the organization visibly rewards heroic firefighting over steady prevention, Quality standards will always be bypassed. You cannot enforce $E_Q$ locally if $A_{IA}$ destroys it systemically.

## Related

- [Losing Loop](../concepts/losing-loop.md) — quality degradation feeds the rework cycle
- [Metrics Framework](../legacy/metrics-framework.md) — quality metrics detail
- [Execution System](../legacy/execution-system.md) — Quality belongs to Block E
