---
title: "Hero Culture Trap"
type: concept
tags: [trap, failure-mode, phase-space, bus-factor]
sources: [raw/1.md, raw/4.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/4-visual-architecture.md, wiki/concepts/p6-mixed-state.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Hero Culture Trap

## Definition

A pathological team state: **high quality maintained by individual heroics, not by the system.** Focus is low because WIP is not capped — one hero absorbs the overflow.

## Diagram 8: Phase Space Diagram

```mermaid
quadrantChart
    title Phase Space — WIP Discipline vs. Defect Containment
    x-axis Low WIP Discipline (Chaos) --> High WIP Discipline (Focused Flow)
    y-axis Low Quality (Defects Escaping) --> High Quality (Defects Contained)
    quadrant-1 Hero Culture Trap
    quadrant-2 Thriving — P4
    quadrant-3 Crisis — P1
    quadrant-4 Rushing Trap (Debt Accumulating)
    Hero Culture: [0.18, 0.78]
    Thriving P4: [0.82, 0.85]
    Crisis P1: [0.08, 0.08]
    Deadline Rush: [0.72, 0.18]
```

## Phase Space Trajectory

Upper-left quadrant: High Quality, Low [Focus](focus.md).
Quality stays high while Focus stays low. Disastrously, this is sustainable only as long as the hero remains. It appears fine in metrics until it catastrophically isn't. Remove the hero and the team drops to [P1-Crisis](p1-crisis.md) instantly.

## Intervention

Fix [Structure](coordination.md) and [Protection](focus.md): establish ownership before heroics. The system must hold quality, not a person.

## Related

- [Rushing Trap](rushing-trap.md) — the other pathological quadrant (lower-right)
- [Focus](focus.md) — the degraded condition enabling hero culture
