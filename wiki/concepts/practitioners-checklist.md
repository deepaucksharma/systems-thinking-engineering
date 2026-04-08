---
title: "Practitioner's Checklist"
type: concept
tags: [implementation, timeline, playbook, execution]
sources: [raw/3.md]
backlinks: [wiki/concepts/temporal-integration-loop.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Practitioner's Checklist

## Definition

A phased timeline for adopting and embedding the framework natively within a working engineering group, transitioning from baseline measurements to deep institutionalization.

## The Rollout Timeline

### Phase 1: Baseline Measurement (Week 1)
- [ ] Instrument basic core metrics (WIP counts, raw cycle time, defect escape rate).
- [ ] Survey goal clarity (can every contributor accurately state the specific top priority?)
- [ ] Explicitly map component ownership.

### Phase 2: Diagnosis (Weeks 2-4)
- [ ] Cross-index symptoms using [Table 2 Diagnostics](../entities/table-2-diagnostics.md) to identify the absolute weakest condition.
- [ ] Verify mathematically that the condition is near zero, avoiding [zero override rules](zero-override-rule.md).
- [ ] Run the [Lever Access Rule](lever-access-rule.md) matrix to verify structural permission to intervene. 

### Phase 3: Intervention (Months 2-3)
- [ ] Apply **exactly one** corrective lever from the tables. (Do not boil the ocean).
- [ ] Set up hardcore shielding against regression triggers (e.g. warding off scope creep).
- [ ] Hold course. Resist the urge to thrash for two complete cycles (referencing the [Nyquist Constraint](nyquist-constraint.md)).

### Phase 4: Validation (Months 4-6)
- [ ] Observe leading indicators shift (expected latency: 1-2 weeks).
- [ ] Observe lagging outcome indicators shift (expected latency: 4-6 weeks).
- [ ] If nothing moves, the diagnosis identified the wrong structural failing. Re-diagnose.

### Phase 5: Institutionalization (Months 7-12)
- [ ] Connect system metrics to live dashboards.
- [ ] Train entire constituent teams natively on the mental model framework to establish a shared dialect.
- [ ] Programmatically automate protection layers (Hard WIP caps in Jira logic; strict automated quality CI/CD gates).

## Related
- [Temporal Integration Loop](temporal-integration-loop.md) — The conceptual cycle summarizing this timeline.
- [Table 2 Diagnostics](../entities/table-2-diagnostics.md) — Operational execution phase manual.
