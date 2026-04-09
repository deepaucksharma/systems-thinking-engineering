---
title: "13 — Block A (Org Alignment)"
type: concept
tags: [v2.1-canonical, macro-blocks, org-design, topology, conway]
sources: [raw/6.md]
backlinks: [wiki/concepts/00-model-identity.md, wiki/concepts/02-master-equation.md]
created: 2026-04-09
updated: 2026-04-09
status: active
historical_lineage: [wiki/legacy/org-alignment.md]
---

# Block A: Org Alignment & Structure

## Core Question

*Does the org's structure, incentives, and architecture allow good execution to exist?*

## What This Block Is

Block A (Org Alignment) is the macro-environment that dictates whether local Execution (Block E) is even possible. The mathematical reality is that **Execution is gated by Org Alignment** ($E_{eff} \approx E \cdot A$). If the organizational game is designed poorly, the team-level game cannot be won. Persistent execution problems that resist agile/process fixes are almost always Block A failures.

$$A(t) = IA \cdot DR \cdot TC \cdot XT \cdot TT \cdot IM$$

## Core Variables

### 1. Incentive Alignment ($IA$)
**Definition:** What actually gets rewarded via promotion, praise, and compensation.
**Zero State:** Execs claim they want "Quality", but only promote engineers who rush features and then pull all-nighters to fix the resulting outages (Hero culture).
**Why it matters:** Engineers do not act maliciously; they are rational agents optimizing for a broken payoff matrix. See [Mechanism Design & Game Theory](incentive-mechanism-design.md) for how to mathematically structure Incentive Compatibility to reverse this gravity well.

### 2. Decision Rights ($DR$)
**Definition:** Who holds authority vs. accountability. Who can say "No."
**Zero State:** The team is accountable for delivery, but cannot reject incoming scope from external stakeholders.

### 3. Team Composition ($TC$)
**Definition:** Seniority mix, role clarity, bus factor.
**Zero State:** A team of all juniors handed a Complex domain. "We have a skill problem" ($E_S$) is often actually a Team Composition problem ($A_{TC}$).

### 4. Cross-Team Architecture ($XT$)
**Definition:** The degree to which organizational boundaries map to software boundaries (Conway's Law alignment).
**Zero State:** A single feature requires ticket-negotiation across 4 distinct teams. Coordination ($E_{Co}$) collapses.

### 5. Team Topology Health ($TT$) & Interaction Modes ($IM$)
**Definition:** Using the Team Topologies patterns correctly.
Instead of all teams looking identical, applying:
- Stream-aligned teams (end to end value)
- Enabling teams (upskilling)
- Complicated Subsystem teams (specialized math/physics)
- Platform teams (reducing cognitive load)

**Zero State:** A "Platform Team" that just mandates Jira workflows and imposes heavy compliance gates, *increasing* Extraneous Load ($EL$) rather than reducing it.

## Diagnostic Action

When local team interventions (fixing sprints, WIP limits, codebase rules) keep sliding backward after a few weeks, stop pulling Execution levers. Escalate to the Org Alignment level using the **Inverse Conway Maneuver**: redesign the organizational reporting lines to match the architecture you actually want.

## Evolutionary Lineage
*Supersedes earlier V2 definition: [Org Alignment](../legacy/org-alignment.md)*
