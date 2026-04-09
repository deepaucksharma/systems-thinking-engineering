---
title: "Execution System"
type: concept
tags: [v2-framework, system-block, block-e, flow, mechanics]
sources: [raw/5.md]
backlinks: [wiki/_indexes/concepts.md, wiki/legacy/master-equation.md, wiki/concepts/winning-loop.md, wiki/concepts/sustainability-drain-loop.md, wiki/legacy/skill.md, wiki/legacy/quality.md, wiki/legacy/people-system.md, wiki/concepts/losing-loop.md, wiki/legacy/focus.md, wiki/legacy/coordination.md, wiki/legacy/clarity.md]
created: 2026-04-08
updated: 2026-04-09
status: stale
superseded_by: [wiki/concepts/12-block-E.md]
---

# Execution System (Block E - Legacy V2)

> [!WARNING]
> This page summarizes the earlier V2 formulation. For the canonical V2.1 definition, use **[12 — Block E (Execution System)](../concepts/12-block-E.md)**.

**Core question:** *Can work actually flow through this team from intention to delivered value?*

The Execution block encapsulates the core mechanics modeled by the original V1 (Master Equation) of this framework. It is necessary but mathematically insufficient to ensure actual system success without alignment across other blocks. 

In the [Master Equation](../legacy/master-equation.md), the formulation is:
$$E(t) = \prod_{k \in \{C, F, S, Co, Q\}} \left(w_k \cdot e_k(t) + (1-w_k)\right) \cdot g_{\text{var}}(\text{Var}(t))$$

## Sub-variables & Measurement
The Execution variables map to the classic Operations Model points (OM1-OM5):

| Sub-variable | Definition | Zero state | Observable signal |
|-------------|------------|------------|------------------|
| **[Clarity](./clarity.md) (C)** | Shared understanding of goals/criteria. | Teams give different goal answers. | Goal recall variance. |
| **[Focus](./focus.md) (F)** | Protected attention; WIP limited. | Everyone doing everything. | WIP/capacity ratio. |
| **[Skill](./skill.md) (S)** | Capability to solve the technical problems. | Stuck on every problem. | Complexity-adjusted delivery rate. |
| **[Coordination](./coordination.md) (Co)** | Work flows without collisions. | Constant rework, handoff failures. | Blocker duration/total work. |
| **[Quality](./quality.md) (Q)** | Output meets standards. | Defect avalanche, perpetual firefighting. | Escaped defect rate. |

*(Note: In V2, Feedback Speed is part of the [Learning & Adaptation](./learning-adaptation.md) block, not Execution.)*

## Key Dynamics
- **Fix Order within E:** C → F → S/Co (check A first) → Q → FS.
- **Conway's Check:** Before concluding an E problem is strictly Execution, verify that Org Alignment [Block A](./org-alignment.md) is not suppressing it. Persistent Focus failures are frequently top-down $IA$ (Incentive) failures.
- **Execution is gated by Org Alignment:** $E_{\text{eff}}(t) = E(t) \cdot A(t)$. The org game overrides the team game.

**Time constant:** Sprints to months.

## What Changed In V2.1

- **Queuing physics became first-class.** V2.1 expands Block E beyond the five OM variables by making Batch Size and tail-risk reasoning explicit in the canonical execution model.
- **Execution is now more sharply bounded by macro-gates.** The newer page is stricter about checking Value, People, and Org conditions before calling something an Execution failure.
- **Condition-level diagnostics are richer.** V2.1 adds more concrete green/yellow/red signals and stronger disambiguation rules for Clarity, Focus, Skill, Coordination, and Quality.
