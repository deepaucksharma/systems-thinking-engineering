---
title: "Nyquist Constraint"
type: concept
tags: [control-theory, timing, measurement, feedback]
sources: [raw/1.md, raw/2.md, raw/4.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/4-visual-architecture.md, wiki/concepts/temporal-integration-loop.md, wiki/concepts/multi-scale-dynamics.md, wiki/concepts/metrics-framework.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Nyquist Constraint

## Definition

A principle from signal processing applied to management: **You must sample (measure) at twice the frequency of the system's baseline cycle, and you must not intervene faster than feedback propagates.**

If a manager changes strategy every week but code takes two weeks to deploy, the manager is acting on aliased (lagged) data. 

## Diagram 5: Closed-Loop Control System

```mermaid
flowchart TD
    subgraph CONTROLLER["🧠 Controller — Engineering Manager"]
        OBS["Observe\nLeading Indicators"]
        COMP["Compare to\nTarget State"]
        DECIDE["Select Lever\n& Magnitude"]
        WAIT["Wait 2 Full\nReview Cycles\n(Nyquist Constraint)"]
    end

    subgraph ACTUATORS["🔧 Actuators — Five Levers"]
        L1["Direction"]
        L2["Protection"]
    end

    subgraph SENSORS["📡 Sensor — Feedback Speed"]
        LEAD["Leading Indicators\n(Days latency — fast, noisy)"]
        LAG["Lagging Indicators\n(Weeks latency — slow, reliable)"]
    end

    subgraph OSCILLATION["⚠️ Oscillation Failure Modes"]
        OSC1["Manager changes strategy\nfaster than feedback propagates\n= Manager is the instability source"]
        OSC2["Leading indicators move\nbut lagging do not\n⟹ Hold course\nSystem responding; not yet propagated"]
    end

    OBS --> COMP --> DECIDE --> L1
    L1 --> LEAD & LAG
    LEAD -->|"fast signal"| WAIT
    LAG -->|"slow signal"| WAIT
    WAIT -->|"strategy unchanged"| OBS
    WAIT -.->|"changed too fast"| OSC1
    WAIT -.->|"leading moved, lagging stable"| OSC2
```

## Anti-Pattern

Changing strategy faster than feedback propagates induces **Manager Oscillation**. The manager becomes the primary source of instability in the system.

## Related
- [Metrics Framework](metrics-framework.md) — The leading and lagging indicators measured.
- [Temporal Integration Loop](temporal-integration-loop.md) — Where the Nyquist constraint is executed.
