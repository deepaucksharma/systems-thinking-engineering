---
title: "Focus"
type: concept
tags: [condition, protection, om2, wip, slack, v2-framework]
sources: [raw/1.md, raw/2.md, raw/5.md]
backlinks: [wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/concepts/littles-law.md, wiki/concepts/winning-loop.md, wiki/legacy/execution-system.md]
created: 2026-04-08
updated: 2026-04-08
status: stale
superseded_by: [wiki/concepts/12-block-E.md]
---

# Focus (OM2 - Legacy)

> [!WARNING]
> This is a fragmented legacy metric page. For the complete V2.1 unified Execution layer, see **[12 — Block E (Execution System)](../concepts/12-block-E.md)**, which specifically addresses the queuing physics updates to Batch Size and Utilization limits.

## Definition

The second condition in the Execution System (`E`) block of the [Master Equation](../legacy/master-equation.md). Measures protected attention and whether work-in-progress is kept within capacity. Moved by the **Protection** lever.

## Leading Indicators

- WIP within cap
- Fewer interruptions
- Maker hours (uninterrupted blocks)
- Unplanned work percentage

## Lagging Indicators

- Cycle time
- Task aging (how long items sit in progress)
- Throughput

## If Near Zero

Everyone doing everything simultaneously. WIP piles up. The team context-switches constantly. This triggers the [Losing Loop](../concepts/losing-loop.md).

## Lever: Protection

- Cut WIP immediately
- Cancel noise (unnecessary meetings, low-priority requests)
- Batch requests instead of streaming them
- Protect maker time

## V2 Context & Gating

Before treating Focus as a pure Execution problem, verify [Org Alignment (Block A)](../legacy/org-alignment.md). Many persistent Focus failures are actually Incentive Alignment ($IA$) failures top-down. 
If the org rewards responsiveness to urgent tasks over completing strategic work, a team cannot mathematically maintain Focus. You cannot fix Focus by telling a team to focus if their manager's manager rewards heroics. 

## Connection to Slack

Focus > 0 creates **slack** — the surplus capacity that enables the [Winning Loop](../concepts/winning-loop.md). Without focus, there is no slack, and the winning loop cannot engage.

## Related

- [Little's Law](../concepts/littles-law.md) — why WIP control matters
- [Losing Loop](../concepts/losing-loop.md) — overloaded focus drives this loop
- [Winning Loop](../concepts/winning-loop.md) — focus surplus enables this loop
- [Execution System](../legacy/execution-system.md) — Focus belongs to Block E
