---
title: "Ethical Measurement"
type: concept
tags: [ethics, goodharts-law, psychology, telemetry, metrics]
sources: [raw/3.md]
backlinks: [wiki/concepts/measurement-theory.md, wiki/concepts/goodharts-law.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Ethical Measurement

## Definition

Operationalizing the systems engineering framework requires pervasive measurement (commits, PR latency, WIP counts) to inform the [Digital Twin](digital-twin.md). This directly creates immense ethical tensions and systemic failure risks if applied coercively.

## The Panopticon Risk

When engineers know every micro-action (PR review time, task completion) is tracked and bound to individual "performance scores," it creates a surveillance state. This destroys psychological safety.

Psychological safety acts as a critical hidden variable; when it collapses, all telemetry becomes immediately corrupted as actors mask behaviors.

**Mitigation Principles:**
1. **Aggregate, don't individualize:** Report team-level conditions, not individual rankings.
2. **No surprise metrics:** Telemetry visibility must be symmetrical (visible to everyone).
3. **Learning, not punishment:** Metrics inform structural design; they are completely divorced from performance reviews.
4. **Opt-in for individuals:** Coaching data is volunteered, never surveiled.

## The Automation Paradox

As measurement becomes sophisticated, the temptation is to automate the manager entirely.

> *Fallacy:* "If $\Phi < 0.3$, write a script to automatically reduce the team's WIP limit in Jira to 10."

This removes human judgment and forces immediate gaming of the system ([Goodhart's Law](goodharts-law.md)). Engineers will simply split their Jira tasks artificially to improve "completion rates" without achieving real throughput.

**Resolution:**
Metrics **inform** management; they do not **replace** it. The human manager is the designated controller in the loop, required to parse ambiguous symptoms.

## Related
- [Goodhart's Law](goodharts-law.md) — the mathematical outcome of attempting coercive metric measurement.
- [Measurement Theory](measurement-theory.md) — how to construct valid metrics in the first place.
