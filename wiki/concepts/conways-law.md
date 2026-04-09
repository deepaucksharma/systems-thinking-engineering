---
title: "Conway's Law"
type: concept
tags: [architecture, structure, coordination, scaling]
sources: [raw/3.md]
backlinks: [wiki/legacy/coordination.md, wiki/concepts/p5-scaling.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Conway's Law

## Definition

> "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." — Melvin Conway, 1967

## The Inviolable Constraint

You cannot fix [Coordination ($Co$)](12-block-E.md) through management directive alone. The org chart *is* the architecture. Attempts to impose a technical architecture that contradicts the organizational structure will fail.

## The Inverse Conway Maneuver

If you wish to change the architecture, you must reorganize the teams to match the desired architecture first. 

*Example:* To build microservices, you must structure small, autonomous teams with end-to-end ownership. You cannot build microservices with monolithic frontend and backend departments.

## Scaling Triggers

Communication overhead scales as a quadratic progression:
$$C_{\text{overhead}} \sim \frac{N(N-1)}{2} = O(N^2)$$

[P5 (Scaling)](p5-scaling.md) is triggered precisely when group size $N$ crosses the critical threshold where architectural coupling forces unmanageable overhead. The predictive formula for hitting that wall is:

$$N_{\text{critical}} = \frac{k \cdot \text{avg\_skill}}{\text{architectural\_coupling}}$$

When $N \to N_{\text{critical}}$, the system will collapse unless you partition teams (reducing $N$ locally) and decouple the architecture.

## Framework Fit and Correctness Evaluation

> [!NOTE]
> **Theoretical Convergence:** Conway's Law maps flawlessly into the V2.1 architecture. It is the empirical foundation for the Master Equation's primary structural gate: $E_{\text{eff}} = E \cdot A$.

In the framework, you cannot solve a Block A (Org Alignment) constraint by pulling a Block E (Execution) lever. If Cross-Team Architecture ($XT$) is fractured, local team Coordination ($Co$) will asymptotically approach zero regardless of how many Agile ceremonies are applied. The framework explicitly formalizes Conway's Law as a hard multiplier against the Execution block.

## Related
- [Block E: Coordination ($Co$)](12-block-E.md) — The local condition constrained by global structure.
- [Block A: Cross-Team ($XT$)](13-block-A.md) — The structural macro-variable representing Conway's Law.
- [P5: Scaling](p5-scaling.md) — The state where Conway's Law limits are hit.
