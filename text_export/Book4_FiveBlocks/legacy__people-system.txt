---
title: "People System"
type: concept
tags: [v2-framework, system-block, block-p, culture, psychology]
sources: [raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/legacy/master-equation.md, wiki/concepts/sustainability-drain-loop.md, wiki/legacy/skill.md, wiki/legacy/quality.md, wiki/concepts/feedback-speed.md, wiki/concepts/fear-amplification-loop.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/11-block-P.md]
---

# People System (Block P - Legacy V2)

> [!WARNING]
> This page summarizes the earlier V2 formulation. For the canonical V2.1 definition, use **[11 — Block P (People System)]()**.

**Core question:** *Can the humans in this system tell the truth, sustain performance, and actually want to do the work?*

The People System provides the human substrate that enables the [Execution System](./execution-system.md) and [Learning & Adaptation](./learning-adaptation.md) blocks to function.

In the [Master Equation](../legacy/master-equation.md), the formulation is:
$$P(t) = Su(t) \cdot \prod_{j \in \{PS, M, FT, Cu\}} \left(w_j \cdot p_j(t) + (1-w_j)\right)$$

## Sub-variables & Measurement

| Sub-variable | Definition | Zero state | Observable signal |
|-------------|------------|------------|------------------|
| **Psychological Safety (PS)** | Safety to surface bad news, uncertainty, disagreement, mistakes. | Retaliation, filtered upward reporting. | Time between problem occurring and being raised. |
| **Motivation & Autonomy (M)** | Intrinsic drive; agency, mastery, purpose. | Learned helplessness, quiet quitting. | Voluntary attrition of high performers. |
| **Fairness & Trust (FT)** | Perceived justice in decisions and info flow. | Gaming, cynicism, coalition-building. | Political behavior as primary career strategy. |
| **Sustainability (Su)** | Recovery rate ≥ depletion rate. | Burnout, emotional flatness. | Energy surveys, sick leave trends. |
| **Lived Culture/Norms (Cu)** | Day-to-day norms align with stated values. | Hypocrisy in rewards and values. | What actually gets praised in team meetings. |

## Core Dynamics

### The Safety Substrate
When Psychological Safety ($PS$) nears zero, **all other measurements become unreliable**. The mathematical framework dictates: $L_{\text{eff}}(t) = L(t) \cdot PS(t)$. Fear distorts signal, making Retrospectives and surveys pointless.

### The Sustainability Clock (Su)
Sustainability ($Su$) sits outside the P product term as a direct multiplier. When $Su < 1.0$, ALL conditions decay over time—not just People conditions. It is the system's active clock-speed modifier.

**Time constants:**
- Safety: Collapses in days, builds over months.
- Burnout: Accumulates slowly, recovery takes longer.
- Culture: Takes years to change in either direction.

## What Changed In V2.1

- **Cognitive load is decomposed more explicitly.** V2.1 elevates Extraneous Load ($EL$) and Germane Capacity ($GC$) into the canonical People model instead of leaving them implicit.
- **Measurement moved toward SPACE framing.** The newer page makes the measurement model part of the block definition, not just an interpretive note.
- **Telemetry reliability is treated as a formal gate.** V2.1 integrates the diagnostic consequence directly: low psychological safety invalidates downstream quantitative metrics.
