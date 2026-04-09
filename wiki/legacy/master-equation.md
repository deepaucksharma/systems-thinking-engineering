---
title: "Master Equation"
type: concept
tags: [equation, foundation, multiplicative-system, v2-framework, output, legacy-reference]
sources: [raw/1.md, raw/2.md, raw/3.md, raw/4.md, raw/5.md]
backlinks: [wiki/sources/canonical-v2-consolidated-model.md, wiki/legacy/zero-override-rule.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/02-master-equation.md]
---

# Master Equation (Legacy)

> [!WARNING]
> This page is retained for historical comparison. For the most detailed current version of the model in this wiki, use **[02 - Master Equation](../concepts/02-master-equation.md)**.

The Master Equation models engineering output as a multiplicative set of interdependent constraints. First introduced as a single execution-focused equation (V1), it later expanded into the V2 block model. This page exists to show that evolution without implying that the earlier forms are the best standalone reference.

## What This Page Is For

- Compare the original V1 execution-only model to the later V2 block model.
- Preserve historical framing used by earlier wiki pages and source ingests.
- Redirect readers to the expanded modern formulation when they need the most complete version.

## Legacy V2 Identity

```text
OUTCOME(t) = theta * V(t) * P(t) * E(t) * A(t) * L(t) * exp(-lambda * Debt(t)) * g(Var(t))
```

This is the older V2 block identity as captured before the later cleanup and expansion work. For the fuller version, use [02 - Master Equation](../concepts/02-master-equation.md), which is more explicit about block variables, gating, and heavy-tail variability treatment.

Where:
- `theta` = team capacity baseline
- `V(t)` = Value Alignment block
- `P(t)` = People System block
- `E(t)` = Execution System block
- `A(t)` = Org Alignment block
- `L(t)` = Learning and Adaptation block
- `exp(-lambda * Debt(t))` = debt drag term
- `g(Var(t))` = legacy shorthand for a variability penalty

## Original V1 Identity (Now Nested Inside E)

Historically, the framework only modeled the execution layer:

```text
OUTPUT = (Clarity * Focus * Skill * Coordination * Quality) * Feedback Speed
```

This later became the core of Block E, while Feedback Speed moved into the Learning block.

## Why It Still Matters

The multiplicative structure is still the key insight:

- severe weakness in one major condition can dominate the whole system;
- strong local execution does not compensate for weak strategy, people health, or org design;
- the historical equation makes it easier to see how the framework widened from team mechanics to a broader sociotechnical model.

## Related

- [Master Equation (entity index)](../entities/master-equation.md) - how this topic is cataloged alongside other named framework objects
- [02 - Master Equation](../concepts/02-master-equation.md) - fuller current formulation
- [10 - Block V (Value Alignment)](../concepts/10-block-V.md) - value-side constraints
- [11 - Block P (People System)](../concepts/11-block-P.md) - human-system constraints
- [12 - Block E (Execution System)](../concepts/12-block-E.md) - execution-side constraints
- [13 - Block A (Org Alignment)](../concepts/13-block-A.md) - structural constraints
- [14 - Block L (Learning & Adaptation)](../concepts/14-block-L.md) - adaptation constraints
- [Zero-Override Rule](../legacy/zero-override-rule.md) - operational consequence of multiplicative structure
