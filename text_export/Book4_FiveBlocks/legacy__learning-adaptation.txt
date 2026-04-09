---
title: "Learning and Adaptation"
type: concept
tags: [v2-framework, system-block, block-l, learning, loops]
sources: [raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/legacy/master-equation.md, wiki/concepts/strategic-drift-loop.md, wiki/legacy/people-system.md, wiki/concepts/feedback-speed.md, wiki/concepts/fear-amplification-loop.md, wiki/legacy/execution-system.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/14-block-L.md]
---

# Learning & Adaptation (Block L - Legacy V2)

> [!WARNING]
> This page summarizes the earlier V2 formulation. For the canonical V2.1 definition, use **[14 — Block L (Learning & Adaptation)]()**.

**Core question:** *Does the system improve over time, or does it repeat the same patterns indefinitely?*

The Learning block captures the organization's ability to mutate based on environmental stressors, shifting from the $E(t)$ mechanics directly into structural growth. 

In the [Master Equation](../legacy/master-equation.md), the formulation is:
$$L(t) = FS(t) \cdot \prod_{m \in \{LP, KR, CA\}} \left(w_m \cdot l_m(t) + (1-w_m)\right)$$

*Note: In the V1 framework, [Feedback Speed]() (FS) was a direct multiplier on Execution. It is conceptually relocated here as the primary term of $L$.*

## Sub-variables & Measurement

| Sub-variable | Definition | Zero state | Observable signal |
|-------------|------------|------------|------------------|
| **[Feedback Speed]() (FS)** | Time from action to consequential signal. | Bugs discovered months later. | CI/CD cycle time; time to user signal. |
| **Learning Practices (LP)** | Retros, postmortems, experiments work. | Postmortems blame individuals. | Action item completion rate. |
| **Knowledge Retention (KR)** | Memory survives personnel changes. | Repeated mistakes; bus factor = 1. | Onboarding time trend. |
| **Change Absorption (CA)** | Rate of change vs. system's integration capacity. | Constant thrash; NYQUIST violations. | Simultaneous initiatives count. |

## Learning is Gated by Safety
$L_{\text{eff}}(t) = L(t) \cdot PS(t)$

Fast feedback loops without Psychological Safety ($PS$) do not accelerate learning; they accelerate distortion. Retrospectives become theater, signal is hidden, and failure is weaponized.

## Nyquist Constraint
The Change Absorption ($CA$) limit asserts you **must not intervene faster than feedback propagates**. Wait 2 full cycles before judging an intervention. Managers who change the state faster than this are the primary source of entropy.

**Time constant:** Medium (weeks to months) provided P and A blocks are stable.

## What Changed In V2.1

- **Experimentation Rate ($ER$) is now explicit.** V2.1 treats safe-to-fail experimentation as a first-class learning variable instead of an implied practice.
- **Learning is tied more tightly to diagnostic sequencing.** The canonical flow delays Learning optimization until the system is minimally stable.
- **Time-constant handling is more specific.** V2.1 connects Learning directly to the detailed Nyquist/J-curve treatment in [06 — Time Constants]().
