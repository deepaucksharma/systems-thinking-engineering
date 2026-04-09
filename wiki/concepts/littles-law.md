---
title: "Little's Law"
type: concept
tags: [queuing-theory, throughput, flow, wip, cycle-time, physics]
sources: [raw/1.md, raw/2.md, raw/4.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/diagram-set-2.md, wiki/sources/4-visual-architecture.md, wiki/concepts/utilization-curve.md, wiki/concepts/feedback-speed.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Little's Law

## Definition

```
Cycle Time = WIP ÷ Throughput
```

A fundamental result from queuing theory applied to engineering workflow: the time any work item spends in the system equals the amount of work in progress divided by the rate at which work completes.

## Diagram 3: Stock and Flow Physics

This diagram operationalizes Little's Law into a physical model of throughput:

```mermaid
flowchart LR
    subgraph SOURCE["📥 Inflow — Arrival Rate λ"]
        FE["Feature Requests"]
        BU["Bug Reports"]
        MT["Maintenance &\nKTLO Obligations\n(20–30% of capacity)"]
        EX["Executive\nAd-hoc Requests"]
    end

    subgraph GATE1["🎯 Direction Filter (V-Block)"]
        PRI["Priority &\nScope Decision\nOne Goal Rule"]
        DEF2["Explicit Parking Lot\nDeferred or Declined\n(Backpressure Signal)"]
    end

    subgraph STOCK["📦 Queue Stock"]
        BL["Committed\nBacklog"]
        IP["⚠️ Work In Progress\nWIP Cap Enforced\n(Focus — F)"]
        HW["Hidden Work\n(Invisible WIP\nBreaks all caps)"]
    end

    subgraph PROCESS["⚙️ Processing Rate μ (Block E)"]
        CAP["Effective Team\nCapacity"]
        BLOCK["Blockers &\nDependency Friction\n(Coordination loss)"]
        HERO["Hero Concentration\n(Skill bottleneck)"]
    end

    subgraph QGATE["✅ Quality Gate (Q)"]
        REV["Automated Tests\nCode Review\nRelease Gates"]
        DONE["Verified Done\n& Shipped"]
    end

    subgraph REWORK["🔄 Rework Loop — Feedback Speed (FS)"]
        ESC["Escaped Defects"]
        INC["Incidents &\nUser Pain"]
        LATE["⚠️ Late Detection\n= Expensive Rework"]
    end

    FE & BU & EX -->|"arrive into"| PRI
    MT -->|"non-negotiable allocation\ndeducted first"| CAP
    PRI -->|"accepted & ranked"| BL
    PRI -->|"rejected or deferred"| DEF2
    BL -->|"pulled when WIP < cap"| IP
    HW -->|"bypasses cap — inflates real WIP"| IP
    IP -->|"processed by"| CAP
    BLOCK -->|"reduces effective"| CAP
    HERO -->|"concentrates risk in"| CAP
    CAP -->|"completes work"| REV
    REV -->|"passes all gates"| DONE
    REV -->|"fails gate — recycles"| IP
    DONE -->|"ships"| USERS["👥 Users & Production"]
    USERS -->|"defect discovered"| ESC
    ESC -->|"if fast feedback"| INC
    ESC -->|"if slow feedback"| LATE
    INC -->|"re-enters as unplanned"| BL
    LATE -->|"re-enters as expensive unplanned"| BL
```

## Hidden Destroyers in the System

As shown in Diagram 3, three hidden elements destroy throughput:
1. **Hidden Work:** Bypasses WIP caps, inflating real WIP and multiplying cycle time.
2. **Unbudgeted Maintenance:** Acts as an invisible tax on the processing rate ($\mu$).
3. **Late Detection:** Rework loops have two speeds — fast detection is cheap, slow detection is catastrophic.

## Critical Threshold

When utilization exceeds ~85%, queuing theory predicts **non-linear cycle time growth** — the queue explodes disproportionately. This is why the framework emphasizes slack: operating at 100% utilization is a mathematical guarantee of infinite queue growth. See the [Utilization Curve](utilization-curve.md).

## Framework Fit and Correctness Evaluation

> [!CAUTION]
> **Theoretical Divergence:** Classical queuing theory mathematical models fundamentally fail when applied to human engineering teams without heavy modification.

In classical manufacturing or compute networks, the Processing Rate ($\mu$) is independent of the queue size or utilization (a server processes a packet at a static clock speed regardless of how long the packet waited). 

In the Systems EM framework, **$\mu$ decays as a function of the queue size**. If a team is pushed to 100% utilization, the resulting systemic stress ($Su < 1$) triggers an exponential decay of processing capacity (as defined in the [Transfer Functions](transfer-functions.md)). Human cycles are state-dependent. Therefore, while Little's Law is observationally useful to prove that high WIP equals slow cycle times, it *under-predicts* the severity of the collapse, because it fails to account for the catastrophic burnout of the processing engine itself.

## Related

- [Block E: Focus (F)](12-block-E.md) — the condition that controls WIP
- [Feedback Speed](14-block-L.md) — governs which rework path (fast vs. slow) is triggered
- [Utilization Curve](utilization-curve.md) — The 85% physics limit.
