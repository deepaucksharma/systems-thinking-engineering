---
title: "P1 — Crisis"
type: concept
tags: [team-state, crisis, losing-loop, playbook]
sources: [raw/1.md, raw/2.md]
backlinks: [wiki/concepts/losing-loop.md, wiki/concepts/nyquist-constraint.md, wiki/sources/diagram-set-1.md, wiki/sources/diagram-set-2.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# P1 — Crisis

## Definition

The team is deep in the [Losing Loop](losing-loop.md). Characterized by confusion, overload, panic, and zero slack.

## Symptoms

- No one can restate the goal
- WIP is uncapped and growing
- Context switching is constant
- Quality bypasses are routine
- The team is reactive, not proactive

## Intervention (from Playbook)

1. **Stop adding work** — no new requests
2. **Choose ONE goal** — Direction lever, priority 5/5
3. **Cut WIP hard** — Protection lever, priority 5/5
4. **Ship one small win** — restore focus and morale

## Review Cadence

2×/week (per [Nyquist Constraint](nyquist-constraint.md))

## Transitions

- → [P2-Stabilizing](p2-stabilizing.md): One priority holds ≥1 cycle, WIP under control, visible panic drops
- → [P6-Mixed](p6-mixed-state.md): One team lane stabilizes while another is still burning

## Regression Triggers (from other states)

- From [P3-Functional](p3-functional.md): Stakeholder panic, surprise work injected, manager becomes bottleneck
- From [P4-Thriving](p4-thriving.md): Rapid growth without structure, key person leaves without transfer
- From [P6-Mixed](p6-mixed-state.md): Crisis in one lane consumes all improvement capacity

## Mathematical Threshold
In the [Extended Framework](../sources/3-extended-framework.md), P1 occurs when the [Order Parameter ($\Phi$)](order-parameter.md) drops below 0.3. This represents a supercritical, chaotic state where exponential degradation takes hold.

## Phase Space and Transitions (Diagram 7 & 8)
P1 sits in the lower-left quadrant of the Phase Space (Low Focus, Low Quality). 
- **Upward transition** (to [P2-Stabilizing](p2-stabilizing.md)) requires raising $\Phi > 0.35$ (Hysteresis gap).
- **Sudden collapse** into P1 can occur from [P3-Functional](p3-functional.md) via [Self-Organized Criticality](self-organized-criticality.md) (sandpile avalanches) when technical debt crosses a critical threshold.

## Related

- [Losing Loop](losing-loop.md) — the dynamic driving P1
- [Zero-Override Rule](zero-override-rule.md) — likely needed at P1
