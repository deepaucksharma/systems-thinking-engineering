---
title: "06 — Time Constants"
type: concept
tags: [v2.1-canonical, control-theory, timing, j-curve, measurement]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/20-diagnostic-sequence.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Time Constants and the Nyquist Constraint

## The Core Principle

Every block operates at a different natural frequency. Intervening faster than a block's natural frequency — or measuring results before the feedback has propagated — makes the manager the source of instability.

**Nyquist Constraint:** Do not re-intervene until you have observed at least 2 full feedback cycles for that block.

## Time Constants by Block and Sub-Variable

| Block | Variable | Degradation Rate | Recovery Rate | Minimum Observation Window |
|-------|----------|-----------------|---------------|---------------------------|
| **V** | Strategic Fit (SF) | Months-quarters | Quarters-years | 1-2 quarters before judging |
| **V** | Customer Value (CV) | Weeks-months | Weeks-months (via experiments) | 4-8 weeks per experiment cycle |
| **V** | Domain Assessment (DA) | Fast (new info) | Fast (new info) | 2-4 weeks per learning cycle |
| **P** | Psychological Safety (PS) | **Days-weeks** | **Months** | 4-8 weeks to see early movement |
| **P** | Motivation (M) | Weeks-months | Weeks-months | 6-12 weeks |
| **P** | Sustainability/Burnout (Su) | Weeks-months | Equal to accumulation period | 4-8 weeks; recovery ≥ depletion time |
| **P** | Culture/Norms (Cu) | Years | **Years** | 12+ months; don't expect linear progress |
| **E** | Clarity (C) | Sprints | Sprints | 2-3 sprints |
| **E** | Focus (F) | Days-weeks | Weeks | 2-4 weeks |
| **E** | Skill (S) | Months | Months-quarters | 6-12 weeks |
| **E** | Quality (Q) | Weeks-months | Weeks-months | 4-8 weeks |
| **E** | Batch Size (BS) | Days-weeks | Days-weeks | 2-3 sprint cycles |
| **A** | Incentive Alignment (IA) | Months-years | **Months-years** | 6-18 months |
| **A** | Decision Rights (DR) | Months | Months-quarters | 3-6 months |
| **A** | Team Composition (TC) | Months | Quarters | 2-3 months per hire cycle |
| **A** | Cross-Team Architecture (XT) | Months-years | **Years** | 6-18 months |
| **L** | Feedback Speed (FS) | Weeks | Weeks | 2-4 weeks |
| **L** | Learning Practices (LP) | Weeks-months | Months | 6-10 weeks |
| **L** | Change Absorption (CA) | Days-weeks | Equal to overload period | Don't add new change during recovery |

## The Critical Asymmetry

**Safety (PS) has the most dangerous asymmetry:**
- Can be destroyed in days by a single high-visibility retaliatory event
- Requires months to rebuild even with consistent positive reinforcement
- This is why PS is treated as a hard zero requiring emergency response

**Culture (Cu) is the slowest:**
- Changes at the Schein "underlying assumptions" level take years
- Changes at the "artifacts" level take weeks and are often illusory
- Leaders systematically overestimate culture change speed

**Incentives (IA) lag behavior change:**
- Incentive policy can change overnight
- Behavior change follows at 3-6 months
- Culture internalization follows at 12-24 months
- Planning timelines must reflect this cascade

## The J-Curve: Transition Costs

Every significant intervention produces a temporary performance decrease before the new baseline is achieved.

```
Performance
    │
    │▓▓▓▓▓ Pre-intervention baseline
    │     ▓▓▓
    │        ▓ ← Transition dip (do not judge here)
    │         ▓▓
    │           ▓▓▓▓▓▓▓▓ Post-intervention baseline
    │
    └─────────────────────────────── Time
              ↑              ↑
         Intervention   Nyquist window
```

**Drivers of dip depth and duration:**

| Factor | Effect on Dip |
|--------|--------------|
| Change magnitude | Larger change = deeper dip |
| Extraneous cognitive load of new system | Higher friction = longer dip |
| Psychological Safety | Low PS = hidden confusion = extended dip |
| Change Absorption (CA) | Low CA = system overloaded = extended dip |

**J-Curve Protocol:**

Before implementing any significant intervention:
1. Predict the dip: estimate timing and depth based on change magnitude and CA
2. Communicate it: tell stakeholders explicitly "performance will temporarily decrease"
3. Set the Nyquist window: minimum observation period = J-curve duration + 1 feedback cycle
4. Define the abort signal: what pattern of leading indicators would indicate the dip is accelerating rather than recovering?

**The intervention failure pattern:**

Organizations measure during the dip, conclude the intervention failed, revert to baseline, and develop learned helplessness about change ("we tried that once"). This pattern is induced by:
- Not predicting the J-curve
- Not communicating it to stakeholders
- Not defining the abort signal in advance

## Framework Fit and Correctness Evaluation

> [!CAUTION]
> **Market Velocity Mismatch:** The Nyquist Constraint mathematically assumes that the organization's maximum safe observation frequency is faster than the market's mutation frequency.
>
> In hypersonically volatile environments (e.g., pre-Product-Market-Fit startups or highly disruptive AI sectors), the external market state may completely change before the 1-2 quarter Strategic Fit ($SF$) Nyquist window concludes. In this unique scenario, upholding the Nyquist limit internally guarantees failure because the organization becomes mathematically decoupled from market reality. The framework structurally struggles to model pure Chaos-domain speed without breaking its own rules for structural stability.
