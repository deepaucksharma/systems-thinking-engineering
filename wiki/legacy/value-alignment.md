---
title: "Value Alignment"
type: concept
tags: [v2-framework, system-block, block-v, strategy]
sources: [raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/legacy/master-equation.md, wiki/concepts/winning-loop.md, wiki/concepts/strategic-drift-loop.md, wiki/legacy/clarity.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/10-block-V.md]
---

# Value Alignment (Block V - Legacy V2)

> [!WARNING]
> This page summarizes the earlier V2 formulation. For the canonical V2.1 definition, use **[10 — Block V (Value Alignment)](../concepts/10-block-V.md)**.

**Core question:** *If we executed this work perfectly, would it matter?*

Value Alignment represents the "Strategic hypothesis" of the team. A zero in Value Alignment means the team is perfectly executing the wrong goal—optimizing execution of waste.

In the [Master Equation](../legacy/master-equation.md), the mathematical formulation is:
$$V(t) = \prod_{i \in \{SF, CV, RA\}} \left(w_i \cdot v_i(t) + (1-w_i)\right) \cdot A_{\text{strat}}(t)$$

## Sub-variables & Measurement

| Sub-variable | Definition | Zero state | Observable signal |
|-------------|------------|------------|------------------|
| **Strategic Fit (SF)** | Work maps to coherent, non-contradictory strategic hypothesis. | Conflicting mandates, "strategy du jour." | Priority reversals per quarter. |
| **Market/Problem Fit (CV)** | Evidence that outputs solve real problems for real users. | Building features nobody uses. | Usage rates vs internal metrics divergence. |
| **Resource Alignment (RA)** | Investment actually matches stated strategy. | Strategic work starved by urgent work. | Roadmap vs actual allocation divergence. |
| **Strategic Decision Rights ($A_{strat}$)** | Leaders rewarded for sustainable value creation. | Promotions go to firefighters, prevention invisible. | Who got promoted for what in last 18 mo. |

## Important Distinctions

**Value vs. Clarity:** 
You can have perfect Clarity ($E_1$) around a bad objective. Clarity asks "does the team know what they're trying to do?" while Strategic Fit asks "is what they're trying to do worth doing?"

## Gating Mechanics
**Strategic Value is gated by Learning:**
$V_{\text{eff}}(t) = V(t) \cdot L(t)$

In high-uncertainty domains, strategy without experimentation is mostly prior belief. A plan that cannot be tested cannot be improved.

**Time constant:** Quarters to years. Strategy changes are expensive and slow to propagate.

## What Changed In V2.1

- **Domain Assessment ($DA$) is now explicit.** V2.1 treats Cynefin calibration as a first-class variable rather than an implied strategic concern.
- **Canonical authority moved to numbered block pages.** The wiki now separates canonical V2.1 definitions from earlier V2 block summaries so readers can compare without confusing the active source of truth.
- **Diagnostic use is more explicit.** V2.1 ties Value failures directly into the no-win checks before local Execution diagnosis.
