---
title: "10 — Block V (Value Alignment)"
type: concept
tags: [v2.1-canonical, macro-blocks, strategy, domain-calibration, value]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/02-master-equation.md]
created: 2026-04-09
updated: 2026-04-09
status: active
historical_lineage: [wiki/legacy/value-alignment.md]
---

# Block V: Value Alignment

## Core Question

*Are we building the right thing for the right domain?*

## What This Block Is

Value Alignment ($V$) is the ultimate gating condition of the entire framework. Perfect Execution ($E$) applied to the wrong strategy results in perfect waste. It dictates that strategic decisions must be calibrated to the actual complexity of the domain they operate in.

**Execution cannot outrun a bad strategy.** If the $V$ block is zero, all subsequent effort in $P$, $E$, $A$, and $L$ multiplies out to zero return on investment.

$$V(t) = f(SF, CV, RA, DA) \cdot A_{\text{strat}}$$

## Core Variables

### 1. Strategic Fit ($SF$)
**Definition:** A coherent, non-contradictory strategy that aligns market opportunity with organizational capabilities.
**Zero State:** Conflicting mandates (e.g., "Max Quality" vs "Ship by Friday" without acknowledging the tradeoff). Strategy is reduced to a list of unrelated goals.

### 2. Customer / Problem Value ($CV$)
**Definition:** Evidence of a real user need or problem that is actively solved by the output.
**Zero State:** Building solutions in search of a problem.

### 3. Resource Alignment ($RA$)
**Definition:** Investment reality matches the stated strategic priority.
**Zero State:** The "most critical initiative" is perpetually starved of staffing while legacy cash-cows consume all capacity.

### 4. Domain Assessment ($DA$) — Cynefin Calibration
**Definition:** Correctly identifying the system domain (Clear, Complicated, Complex, Chaotic) and applying the appropriate constraints.
**Zero State:** Treating a Complex domain (software product development) like a Clear domain (assembly line). Applying "best practices" where "emergent practices" (experimentation) are required.
**Why it matters:** Applying the wrong domain constraints guarantees failure, regardless of how well the constraints are managed.

### 5. Strategic Decision Rights ($A_{strat}$)
**Definition:** Leaders and executives are appropriately rewarded for sustainable value creation, not just short-term outputs.
**Zero State:** Rewarding the launch of features over the validation of customer value.

## The Learning Gate

Strategic Value is continuously gated by Learning (Block L).

$$V_{\text{eff}}(t) \approx V(t) \cdot L(t) \cdot f(DA)$$

In Complex domains (most product work), strategy without experimentation is merely prior belief. The quality of strategic decisions decays rapidly without fast feedback from reality. If you are not learning ($L$), your strategy ($V$) is silently depreciating in value.

## Evolutionary Lineage
*Supersedes earlier V2 definition: [Value Alignment](../legacy/value-alignment.md)*
