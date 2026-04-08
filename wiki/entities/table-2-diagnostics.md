---
title: "Table 2 — Diagnostics"
type: entity
tags: [table, diagnostics, decision-tree, fix-order, flowchart]
sources: [raw/1.md, raw/2.md, raw/4.md]
backlinks: [wiki/sources/diagram-set-1.md, wiki/sources/4-visual-architecture.md, wiki/concepts/zero-override-rule.md, wiki/concepts/structure-vs-development-rule.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Table 2 — Diagnostics

## Purpose

Table 2 is the diagnostic engine of the framework. It maps **observed symptoms** to **root cause diagnoses** and prescribes the correct **lever** to pull, in what order.

## Diagram 6: The Complete Diagnostic Decision Tree

This diagram encodes the executable logic of Table 2:

```mermaid
flowchart TD
    START(["🔍 Symptom Observed\nBegin Diagnosis"])
    ZERO{"⚠️ ZERO CHECK FIRST\nIs any single condition\nnear zero?"}
    START --> ZERO
    ZERO -->|"YES"| WHICHZERO{"Which condition\nis near zero?"}

    WHICHZERO -->|"Clarity"| FD1["Pull Direction Lever\nRewrite goal in one sentence"]
    WHICHZERO -->|"Focus"| FD2["Pull Protection Lever\nCut WIP immediately"]
    WHICHZERO -->|"Quality"| FD5["Pull Standards Lever\nTighten test gates"]
    WHICHZERO -->|"Learning Rate"| FD6["Pull Feedback Speed Lever\nShrink batch size"]
    WHICHZERO -->|"Skill or Coordination"| SVSD{"Structure vs\nDevelopment Rule"}

    SVSD -->|"Cannot tell"| FIXSTR["Fix Structure First"]
    SVSD -->|"Skill gap confirmed"| FIXDEV["Fix Development"]

    ZERO -->|"NO — Apply default\norder"| C1{"Layer 1: Clarity\nFix Order 1"}
    C1 -->|"NO"| FC1["Pull Direction Lever"]
    C1 -->|"YES"| C2{"Layer 2: Focus\nFix Order 2"}
    C2 -->|"NO"| FC2["Pull Protection Lever"]
    C2 -->|"YES"| C3{"Layer 3: Skill/Coordination"}
    
    C3 --> SVSD2{"Distinguish skill\nfrom ownership?"}
    SVSD2 -->|"NO or Coordination"| FS2["Pull Structure Lever"]
    SVSD2 -->|"Skill confirmed"| FD3["Pull Development Lever"]

    FS2 --> C4
    FD3 --> C4

    C4{"Layer 4: Quality\nFix Order 5"}
    C4 -->|"NO"| FC4["Pull Standards Lever"]
    C4 -->|"YES"| C5{"Layer 5: Feedback Speed"}
    
    C5 -->|"NO"| FC5["Pull Feedback Speed Lever"]
    C5 -->|"YES"| HEALTHY(["✅ Enter Manager Loop"])

    FC1 & FC2 & FC4 & FC5 & FD1 & FD2 & FD5 & FD6 & FIXSTR & FIXDEV --> LOOP
    LOOP(["🔄 Wait 2 full cycles\nObserve leading indicators"])
```

## Diagnostic Rows (Reference)

| ID | Symptom | Root Cause | Lever | Fix Order |
|---|---|---|---|---|
| D1 | People confused about what to build | Direction failure (Clarity ≈ 0) | Direction | 1 |
| D3 | Lots started, little finished | Flow failure (Focus ≈ 0) | Protection | 2 |
| D5 | Engineers stuck on technical problems | Capability failure (Skill ≈ 0) | Development | 3 |
| D6 | Work collides, duplicates, or has gaps | Coordination failure | Structure | 4 |
| D7 | Bugs reaching users, unstable releases | Quality failure (Standards ≈ 0) | Standards | 5 |

## Embedded Rules

- **[Zero-Override Rule](../concepts/zero-override-rule.md):** If any condition is near zero, fix it first regardless of the fix-order hierarchy.
- **[Structure-vs-Development Rule](../concepts/structure-vs-development-rule.md):** When you can't tell if a problem is skill or coordination, fix Structure first.

## Related

- [Fix-Order Decision Tree](../concepts/fix-order.md) — visual flowchart of Table 2 logic
- [Master Equation](master-equation.md) — the equation whose terms Table 2 diagnoses
