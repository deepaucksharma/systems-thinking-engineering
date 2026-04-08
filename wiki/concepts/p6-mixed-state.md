---
title: "P6 — Mixed State"
type: concept
tags: [team-state, mixed-state, partitioning, playbook]
sources: [raw/1.md, raw/2.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/diagram-set-2.md, wiki/concepts/p1-crisis.md, wiki/concepts/p3-functional.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# P6 — Mixed State

## Definition

A genuinely distinct team configuration where **different subsystems are in different states simultaneously**. One lane may be in [P1-Crisis](p1-crisis.md) while another is [P3-Functional](p3-functional.md). The mixed-state rule exists because P6 is invisible to averaged metrics.

## Key Rule

> Use WORST state for stabilization. Use BEST state for investment. Do NOT average away a zero. Create separate cadences.

## Symptoms

- Averaged metrics say "functional" but one subsystem is burning
- Heroics in one area mask collapse in another
- Cross-domain context switching

## Intervention

- **Partition** the team into distinct domains for diagnosis and treatment
- Apply crisis protocols to the burning domain
- Protect investment time in the healthy domain
- Track separately: different cadences, different dashboards
- **Prevent spread**: don't let the crisis in one lane consume all improvement capacity

## Transitions

- → [P2-Stabilizing](p2-stabilizing.md): Burning lane stabilizes, local ownership holds
- → [P1-Crisis](p1-crisis.md): Crisis in one lane consumes all improvement capacity

## Phase Space Trajectory (Diagram 8)
In the Phase Space Diagram, P6 represents a split probability field:
- **P6a (Healthy Lane):** Sits in the Thriving or Functional quadrant.
- **P6b (Burning Lane):** Sits in the Crisis quadrant.

Because the system is mathematically split, evaluating the overall [Order Parameter ($\Phi$)](order-parameter.md) by averaging metrics will lie. The manager must partition the metrics by lane constraint.

## Related

- [Metrics Framework](metrics-framework.md) — why averages lie in mixed states
