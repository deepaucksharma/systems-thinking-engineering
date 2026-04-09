---
title: "Feedback Speed"
type: concept
tags: [condition, feedback, om6, learning-rate, cycle-time, telemetry, v2-framework]
sources: [raw/1.md, raw/2.md, raw/3.md, raw/4.md, raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/concepts/littles-law.md, wiki/legacy/learning-adaptation.md, wiki/concepts/fear-amplification-loop.md, wiki/legacy/master-equation.md, wiki/legacy/fix-order.md, wiki/legacy/nyquist-constraint.md, wiki/concepts/winning-loop.md, wiki/concepts/losing-loop.md]
created: 2026-04-08
updated: 2026-04-09
status: active
---

# Feedback Speed (OM6)

## Definition

Feedback Speed began as OM6 in the earlier execution model and later became part of the broader Learning block. It refers to the time between action and consequential signal:

- how fast defects are discovered;
- how fast customer impact becomes visible;
- how fast the system can tell whether a change helped or harmed.

Fast feedback is useful because it shortens learning loops. It is not automatically good in all circumstances, because a frightened or overloaded system can turn fast feedback into faster gaming.

## Useful Measurement Proxies

One simple framing is:

$$FS(t) = \frac{\text{baseline cycle}}{\text{current cycle}}$$

But the exact formula matters less than the operational question: how long does it take for the system to tell you something meaningful?

Useful proxies include:
- time to defect detection;
- time to user signal;
- CI/CD latency;
- review turnaround time;
- time from incident to diagnosis.

## Why It Matters

When feedback is slow:
- rework becomes more expensive;
- uncertainty compounds before correction happens;
- managers steer with stale information;
- teams repeat the same mistakes longer than necessary.

When feedback is fast and trustworthy:
- mistakes are caught earlier;
- smaller experiments become possible;
- the cost of learning drops.

## Diagnostic Context

Feedback Speed is now best understood as part of Learning and Adaptation rather than as a standalone master multiplier.

It should be interpreted together with:
- [06 - Time Constants](06-time-constants.md)
- [14 - Block L (Learning & Adaptation)](14-block-L.md)
- [11 - Block P (People System)](11-block-P.md)

The most important caution is this:

**fast feedback without psychological safety can accelerate distortion rather than learning.**

If safety is low, teams may optimize for the visibility of the signal rather than for the reality behind it. That is why Feedback Speed should never be read independently from the measurement-reliability and safety discussions elsewhere in the wiki.

## If Feedback Speed Is Near Zero

Typical signs:
- bugs discovered months after introduction;
- user behavior only understood long after release;
- review or deployment loops so slow that iteration is effectively blocked;
- retrospectives that arrive after context and energy are already gone.

At that point, the system is often steering with stale data.

## Practical Levers

- reduce batch size;
- improve instrumentation;
- shorten CI/CD latency;
- reduce waiting and handoff time in the path to signal;
- tighten the loop between user pain and corrective action.

## Related

- [14 - Block L (Learning & Adaptation)](14-block-L.md) - current home of feedback inside the broader learning model
- [06 - Time Constants](06-time-constants.md) - observation windows and intervention timing
- [11 - Block P (People System)](11-block-P.md) - safety and sustainability shape whether feedback is usable
- [Little's Law](littles-law.md) - rework becomes more expensive when detection is slow
