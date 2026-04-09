---
title: "14 — Block L (Learning & Adaptation)"
type: concept
tags: [v2.1-canonical, macro-blocks, learning, feedback-loops, adaptation]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/02-master-equation.md]
created: 2026-04-09
updated: 2026-04-09
status: active
historical_lineage: [wiki/legacy/learning-adaptation.md]
---

# Block L: Learning & Adaptation

## Core Question

*Do we actually improve based on reality, or do we just repeat our history?*

## What This Block Is

The Learning block ($L$) functions as the meta-multiplier across the entire system. It defines how quickly the organization can integrate new information and change its own structure. 

Crucially, **Learning is gated by Psychological Safety**. Fast feedback loops into a frightened system do not result in learning—they result in sophisticated gaming and distortion.

$$L(t) = FS \cdot LP \cdot KR \cdot CA \cdot ER$$

## Core Variables

### 1. Feedback Speed ($FS$)
**Definition:** The lead time from taking an action to receiving a consequential signal.
**Zero State:** Discovering architectural flaws three months after the code was written. Discovering a feature has zero users two quarters after launch. 

### 2. Learning Practices ($LP$)
**Definition:** The mechanisms by which the organization extracts signal from noise (e.g., retrospectives, postmortems).
**Zero State:** Ritualistic retrospectives that yield no structural changes. "Blame-free" postmortems that still secretly punish individuals.

### 3. Knowledge Retention ($KR$)
**Definition:** Organizational memory that survives individual attrition.
**Zero State:** Re-learning the same fatal mistake every time a senior engineer leaves. "Tribal knowledge" as the only form of documentation.

### 4. Change Absorption ($CA$)
**Definition:** The rate of change the system can physically integrate without collapsing.
**Zero State:** Launching a new "Agile Transformation" before the previous re-org has settled. Implementing three new tools simultaneously while $Su$ (Sustainability) is low. Constant thrash.
**Note:** Always respect the [Time Constants](06-time-constants.md) before pushing a new phase of change.

### 5. Experimentation Rate ($ER$)
**Definition:** The volume of safe-to-fail experiments running in the system per period.
**Zero State:** Every decision must be perfectly planned because failure is heavily penalized. Only "Big Bang" releases are permitted.

## The Safety Gate

Learning only produces value when the measurement instruments are honest. Because suppression triggers cascades, this operates as a highly non-linear [transfer function](transfer-functions.md):

$$L_{\text{eff}}(t) = L_{\text{raw}}(t) \cdot \left[ \frac{1}{1 + e^{-k(PS(t) - PS_{\text{crit}})}} \right]$$

If Psychological Safety ($PS$) is near zero, fast Feedback Speed ($FS$) doesn't help you learn. In a low-safety environment, teams will intuitively hide failures, manipulate data, and tell leadership what they want to hear. **You cannot diagnose a system that is lying to you.** Before optimizing $L$, you must stabilize $P$.

## Evolutionary Lineage
*Supersedes earlier V2 definition: [Learning & Adaptation](../legacy/learning-adaptation.md)*
