---
title: "11 — Block P (People System)"
type: concept
tags: [v2.1-canonical, macro-blocks, people, sustainability, safety, cognitive-load]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/02-master-equation.md]
created: 2026-04-09
updated: 2026-04-09
status: active
historical_lineage: [wiki/legacy/people-system.md]
---

# Block P: People System

## Core Question

*Can humans tell the truth, stay motivated, and sustain performance?*

## What This Block Is

The People System (Block P) represents the human capacity layer. It is arguably the most under-weighted block in practice, yet mathematically it governs two absolute system limits: The reliability of all telemetry, and the decay rate of all other blocks.

$$P(t) \approx Su \cdot PS \cdot M \cdot FT \cdot Cu \cdot (1 - EL) \cdot GC$$

*(Canonical form and gates: [02 — Master Equation](02-master-equation.md).)*

## Core Variables

### 1. Psychological Safety ($PS$)
**Definition:** Truth-telling capacity; freedom to surface bad news and dissent without retribution.
**Zero State:** The team knows the project is failing but reports green to executives. All metrics become political lies.
**Why it matters:** Fast feedback loops without safety do not accelerate learning; they accelerate distortion. For how **safety couples to learning** without double-counting \(PS\) in a scalar collapse, see Gate 1 in [02 — Master Equation](02-master-equation.md).
**Time Constant:** Days to destroy, months to rebuild.

### 2. Sustainability / Burnout ($Su$)
**Definition:** Balance of demands vs. resources; recovery rate vs. depletion rate.
**Zero State:** Systemic exhaustion. High sick leave. Loss of senior personnel.
**Why it matters:** When $Su < 1.0$, the system is consuming future capacity to produce present output. All other blocks decay at a rate proportional to $(1 - Su)$.

### 3. Motivation & Autonomy ($M$)
**Definition:** Based on Self-Determination Theory (Autonomy, Competence, Relatedness). Operates via intrinsic drive rather than controlled motivation.

### 4. Fairness & Trust ($FT$)
**Definition:** Perceived justice in decisions, rewards, and promotions. Lacking this, intrinsic motivation converts into transactional extraction.

### 5. Lived Culture ($Cu$)
**Definition:** What actually gets rewarded or punished, rather than what is written in the values statement. (Schein's deepest layer of underlying assumptions).

### 6. Cognitive Load Decomposition ($EL$ vs $GC$)
**Cognitive Load is not just "too much work". It is composed of:**
- **Intrinsic Load:** The actual difficulty of the problem. (Fix via Skill/Seniors).
- **Extraneous Load ($EL$):** Friction. Broken pipelines, noisy alerts, bureaucracy. *This directly subtracts from system capacity.*
- **Germane Capacity ($GC$):** Protected time and energy for learning, reflection, and mastery.

If Extraneous Load ($EL$) uses 90% of the budget, Germane Capacity ($GC$) is 0, which halts all organizational learning (Block L).

## Measurement Frame: SPACE

To measure Block P, use the **SPACE** framework instead of purely output-driven DORA metrics:
- **S**(atisfaction) → $Su$, $M$
- **P**(erformance) → Outcomes filtered from Block E
- **A**(ctivity) → Flow metrics (but do not over-weight)
- **C**(ommunication) → $PS$, $Cu$, Coordination
- **E**(fficiency) → Extraneous Load ($EL$), Focus, deep-work hours

## Evolutionary Lineage
*Supersedes earlier V2 definition: [People System](../legacy/people-system.md)*
