---
title: "12 - Block E (Execution System)"
type: concept
tags: [v2.1-canonical, macro-blocks, execution, physics, flow]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/02-master-equation.md]
created: 2026-04-09
updated: 2026-04-09
status: active
historical_lineage: [wiki/legacy/execution-system.md]
---

# Block E: Execution System

## Core Question

*Can work actually flow from intention to delivered value through this team?*

## What This Block Is

Block E is the execution core of the framework: the original five operating conditions plus an explicit treatment of batch size. It answers the mechanical question of delivery:

given that the direction is worthwhile, the people system is viable, and the surrounding structure is not blocking the team, can the work move?

**Block E is necessary but not sufficient.** A team can look busy, disciplined, and even highly skilled while still failing because strategy, people, or structure are the real constraint.

## The Block Equation

$$E(t) = C \cdot F \cdot S \cdot Co \cdot Q \cdot g_{\text{batch}}(BS)$$

Tail risk is diagnosed alongside Block E because it shows up vividly in delivery data, but it is modeled separately as the broader variability penalty `g_tail(Var)`. That separation matters: unpredictable delivery is often partly an execution issue and partly a structural or systemic issue.

## The Five Conditions

### Clarity (C) - OM1

**Definition:** Shared understanding of goals, priorities, and success criteria across the team.

**Failure pattern:** Team members answer the same question differently, start work without a shared definition of done, or discover basic disagreement late.

**Distinction from Value Alignment:** Clarity asks whether the team knows what it is trying to do. Value Alignment asks whether the thing it is trying to do is worth doing.

| Signal | Green | Yellow | Red |
|--------|-------|--------|-----|
| Goal recall consistency | > 80% consistent | 60-80% | < 60% |
| Priority reversals per sprint | 0-1 | 2-3 | > 3 |
| "Done" defined before start | Always | Usually | Rarely |

**Before diagnosing Clarity failure, verify:**
- Is this actually a Strategic Fit problem?
- Is safety low enough that people know the truth but will not say it?

**Intervention:** Define one goal per sprint in 25 words or fewer. Force-rank priorities. Kill ambiguous work before it starts.

### Focus (F) - OM2

**Definition:** Protected attention, controlled work in progress, and enough slack to absorb variation.

**Failure pattern:** Constant context switching, too many concurrent items, and no real capacity to finish.

**Queuing point:** Focus is not just a WIP count. It is the interaction of WIP, batch size, utilization, and arrival variability.

| Signal | Green | Yellow | Red |
|--------|-------|--------|-----|
| WIP / capacity ratio | < 0.8 | 0.8-1.0 | > 1.0 |
| Unplanned work % | < 20% | 20-35% | > 35% |
| Context switches per engineer per day | < 2 | 2-4 | > 4 |
| Mean batch size vs team capacity | < 1 week | 1-4 weeks | > 4 weeks |

**Before diagnosing Focus failure, verify:**
- Are incentives rewarding responsiveness over completion?
- Can the team actually refuse new work, or are WIP limits symbolic?

**Intervention:** Set explicit WIP caps, reduce batch size, make interrupts visible, and clarify who can authorize new work.

### Skill (S) - OM3

**Definition:** Capability to solve the actual problems the team faces, not generic prestige or pedigree.

**Failure pattern:** Ordinary problems require heroics, learning curves are too steep, and routine work repeatedly needs rescue.

**Interpretive caution:** A skill problem can be partly structural. A team with poor composition, high friction, or chaotic coordination often looks less capable than it really is.

| Signal | Green | Yellow | Red |
|--------|-------|--------|-----|
| Inverse problem resolution time | Improving | Stable | Degrading |
| Problems requiring external help | < 10% | 10-25% | > 25% |
| Bus factor | > 3 | 2-3 | 1 |
| Onboarding time to productivity | Stable/declining | Slowly increasing | Rapidly increasing |

**Before diagnosing Skill failure, verify:**
- Is the real issue team composition rather than team capability?
- Is coordination so poor that skill is being misread?

**Intervention:** Identify the missing capability precisely, reduce extraneous load, pair on real work, and check composition before defaulting to hiring.

### Coordination (Co) - OM4

**Definition:** Work flows without collisions, duplication, ownership gaps, or chronic handoff failure.

**Failure pattern:** Rework from misalignment, unclear ownership, and recurring blockers between people or teams.

**Interpretive caution:** Many coordination problems are architectural or structural, not interpersonal. If boundaries and dependencies are wrong, local process fixes will have bounded effect.

| Signal | Green | Yellow | Red |
|--------|-------|--------|-----|
| Blocker duration / total work | < 10% | 10-20% | > 20% |
| Handoff failure rate | < 5% | 5-15% | > 15% |
| "Who owns X?" resolution time | < 1 day | 1-3 days | > 3 days |
| Cross-team blocker frequency | < 1/sprint | 1-3/sprint | > 3/sprint |

**Before diagnosing Coordination failure, verify:**
- Is this really a cross-team architecture problem?
- Is unclear ownership actually unclear authority?

**Intervention:** Map ownership before process. If the same coordination breakdown recurs, suspect structure before blaming habits.

### Quality (Q) - OM5

**Definition:** Output meets standards without excessive rework, and defects are found early enough to be affordable.

**Failure pattern:** Firefighting dominates, defects escape regularly, and debt accumulates faster than the team can service it.

**Interpretive caution:** Quality often degrades quietly when speed is rewarded and prevention is invisible. The visible metric can stay green while the underlying system worsens.

| Signal | Green | Yellow | Red |
|--------|-------|--------|-----|
| Escaped defect rate | < 1% | 1-3% | > 3% |
| Rework percentage | < 10% | 10-20% | > 20% |
| Technical debt accumulation rate | Declining | Stable | Growing |
| Time to detect defect after introduction | Hours | Days | Weeks |

**Before diagnosing Quality failure, verify:**
- Is burnout preventing sustainable standards?
- Are incentives rewarding speed while hiding the cost of rework?

**Intervention:** Make prevention visible, automate detection where possible, and stop granting exceptions that silently redefine the standard.

## Batch Size as a First-Class Lever

Batch size deserves its own treatment because teams often focus on WIP while ignoring work item size.

$$\text{Cycle Time} \approx \frac{\text{WIP} \cdot \overline{\text{Batch Size}}}{\text{Throughput}} \cdot f(\text{Utilization}, \text{Arrival Variance})$$

The exact queueing model will vary by context, but the practical lesson is stable:
- smaller stories are easier to estimate and review;
- smaller releases fail more safely;
- smaller batches reduce the damage caused by uncertainty.

**Heuristic:** If cycle time is high while WIP looks reasonable, inspect story-size distribution before assuming the answer is more discipline.

## Tail Risk as a Diagnostic Lens

Average cycle time is often too optimistic for software systems because the tail matters disproportionately.

$$Ob(X) = P(X_1 + X_4 > X_2 + X_3 \mid X_1 \le X_2 \le X_3 \le X_4)$$

You do not need the exact formula to use the idea well. The operational point is that two teams with similar averages can have very different reliability if one produces far worse outliers.

| Planning Context | Better Signal |
|-----------------|---------------|
| Daily team management | Mean or median cycle time |
| Sprint planning | P75 cycle time |
| Quarterly commitments | P90 cycle time |
| External promises | P95 or explicit uncertainty range |

**How this fits the model:**
- Block E contains the controllable execution mechanics.
- Tail risk is a lens on reliability, not just on speed.
- The cause of tail risk may sit in execution, org coupling, intake volatility, or weak learning loops.

A team with acceptable averages but a fat tail is less reliable than its dashboard suggests.

## Evolutionary Lineage
*Supersedes earlier V2 definition: [Execution System](../legacy/execution-system.md)*
