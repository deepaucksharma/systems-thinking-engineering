---
title: "Org Alignment"
type: concept
tags: [v2-framework, system-block, block-a, org-design, incentives]
sources: [raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/legacy/master-equation.md, wiki/legacy/skill.md, wiki/legacy/quality.md, wiki/concepts/incentive-death-spiral.md, wiki/legacy/focus.md, wiki/legacy/execution-system.md, wiki/legacy/coordination.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/13-block-A.md]
---

# Org Alignment (Block A - Legacy V2)

> [!WARNING]
> This page summarizes the earlier V2 formulation. For the canonical V2.1 definition, use **[13 — Block A (Org Alignment)](../concepts/13-block-A.md)**.

**Core question:** *Does the organizational system permit effective work, or does it structurally prevent it?*

Most "team performance" problems that resist team-level interventions are actually top-down organizational (A) problems.

In the [Master Equation](../legacy/master-equation.md), the formulation is:
$$A(t) = \prod_{l \in \{IA, DR, TC, XT\}} \left(w_l \cdot a_l(t) + (1-w_l)\right)$$

## Sub-variables & Measurement

| Sub-variable | Definition | Zero state | Observable signal |
|-------------|------------|------------|------------------|
| **Incentive Alignment (IA)** | Rewards match sustainable value creation. | Heroics celebrated; prevention invisible. | Who gets promoted for what. |
| **Decision Rights & Power (DR)** | Decisions made at the right contextual level. | Everything escalates; HiPPO culture. | Decision latency; reversal rate. |
| **Team Composition & Roles (TC)** | Seniority mix, role clarity, boundaries. | Bus factor = 1; role collisions. | Bus factor, role ambiguity survey. |
| **Cross-Team Architecture (XT)** | Team boundaries match technical architecture. | Conway's Law violations; blocked by dependencies. | Cross-team blocker frequency. |

## Structural Gating

### Execution is gated by Org Alignment
$E_{\text{eff}}(t) = E(t) \cdot A(t)$

A team that is penalized for saying no, rewarded for heroics over prevention, and blocked by cross-team dependencies cannot sustainably execute—even if their internal processes ($E$) are impeccable. 

### Inverse Conway Maneuver ($XT$)
When $XT$ is low, the org chart clashes with the architecture. Technical architecture cannot sustainably mandate dependencies that contradict the org structure. 

**Time constant:** Years. Reorgs and incentive revamps are the slowest levers in the system.

## What Changed In V2.1

- **Block A is more fully decomposed.** V2.1 treats Team Topology Health ($TT$) and Interaction Modes ($IM$) as explicit canonical variables rather than folding everything into broader structure concerns.
- **Org diagnosis is staged more carefully.** The newer diagnostic flow distinguishes hard org no-win conditions from deeper A-block inspection after failed local interventions.
- **The page now sits in a clearer migration path.** V2.1 numbered pages hold the active definitions, while this page remains useful for tracing the earlier framing.
