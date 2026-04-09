---
title: "20 - Diagnostic Sequence"
type: concept
tags: [v2.1-canonical, diagnostics, fix-order, flowchart]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/12-block-E.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# The Diagnostic Sequence

## Philosophy

Diagnosis should move from the largest constraints toward the most local mechanics. Fixing a local symptom while a larger constraint remains active often produces brief improvement followed by relapse.

The sequence below is not sacred, but it encodes a useful bias:
- do not optimize execution around the wrong goal;
- do not trust dashboards from a system that cannot tell the truth;
- do not demand team discipline when structure is doing the damage;
- do not add learning loops to a system that is too strained to absorb change.

## Decision Flow

### Step 0: Check for no-win conditions

Ask these first:

1. Is there a coherent, non-contradictory strategy?
2. Is the work plausibly valuable to real users or customers?
3. Can people surface bad news without disproportionate penalty?
4. Is the system already showing burnout, overload, or visible breakage?
5. Are incentives actively rewarding harmful behavior?
6. Is there cross-team deadlock with no feasible local path around it?

If one of these is clearly broken:
- document it as a primary constraint;
- stop promising large gains from local optimization alone;
- apply only the minimum local mitigation needed to prevent further damage;
- escalate the root issue explicitly.

### Step 1: Verify the People System before trusting measurement

Before using metrics as a steering instrument, check whether the signal source is trustworthy.

**Psychological Safety**
- Are survey and interview responses candid or filtered?
- Do skip-level conversations match the official story?
- Do problems surface quickly or only after damage is obvious?

If safety is low, downgrade confidence in quantitative metrics and rely more on interviews, anonymous channels, and direct observation.

**Sustainability**
- Is energy holding week over week?
- Is after-hours work normalizing or accumulating?
- Is meeting quality degrading?

If sustainability is low, reduce load before adding improvement work. An overloaded team is rarely a good experimental platform.

**Motivation and Fairness**
- Are people still initiating improvements?
- Is cynicism becoming the dominant tone?

These matter, but they usually follow behind safety and sustainability in urgency.

### Step 2: Diagnose Execution with structural awareness

Apply the classic execution checks, but resist treating every execution symptom as a purely local problem.

**Clarity**
- Are people aligned on the goal and success criteria?
- Or is the disagreement caused by conflicting upstream mandates?

**Focus**
- Is work in progress actually under control?
- Or is the deeper problem batch size, interrupts, or inability to refuse intake?

**Skill vs Coordination**
- Is the team truly under-capable?
- Or is the system structured in a way that makes competent people look ineffective?

**Quality**
- Is rework coming from poor discipline?
- Or from overload, hidden debt, or incentives that punish prevention?

**Tail Risk**
- Are averages acceptable while commitments remain unreliable?
- If so, switch from mean-only thinking to percentile-based analysis.

### Step 3: Inspect Org Alignment when execution fixes keep washing out

When the same execution problems recur after sincere local intervention, inspect the surrounding structure.

Look for:
- incentive systems that reward heroics, urgency, or local throughput over system health;
- decision rights that leave teams unable to protect focus or clarify priorities;
- team composition or topology mismatched to the work;
- architectural dependency patterns that make coordination failure structurally likely.

At this stage, the right answer is often not "coach the team harder." It is "change the environment the team is operating in."

### Step 4: Improve Learning only after the system can absorb it

Learning work is valuable, but it is easy to romanticize. More retrospectives, experiments, or process changes can destabilize an already overloaded system.

Check:
- feedback speed;
- whether retros and postmortems change behavior;
- whether knowledge survives turnover;
- whether the organization is already carrying too many simultaneous changes.

A useful question here is not just "can we learn faster?" but "can this system digest another change without thrashing?"

## What to Record

After diagnosis, document:

1. Which block is the current primary constraint.
2. Which intervention is being attempted.
3. What time horizon is realistic.
4. Which leading signals would indicate movement.
5. What would trigger a re-diagnosis.

## Historical Comparison

- Earlier shorthand: [Fix-Order](../legacy/fix-order.md)
- Companion routing table: [Table 2 - Diagnostics](../entities/table-2-diagnostics.md)
