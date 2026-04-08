---
title: "Conway's Law"
type: concept
tags: [architecture, structure, coordination, scaling]
sources: [raw/3.md]
backlinks: [wiki/concepts/coordination.md, wiki/concepts/p5-scaling.md]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Conway's Law

## Definition

> "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." — Melvin Conway, 1967

## The Inviolable Constraint

You cannot fix [Coordination (OM4)](coordination.md) through management directive alone. The org chart *is* the architecture. Attempts to impose a technical architecture that contradicts the organizational structure will fail.

## The Inverse Conway Maneuver

If you wish to change the architecture, you must reorganize the teams to match the desired architecture first. 

*Example:* To build microservices, you must structure small, autonomous teams with end-to-end ownership. You cannot build microservices with monolithic frontend and backend departments.

## Scaling Triggers

Communication overhead scales as a quadratic progression:
$$C_{\text{overhead}} \sim \frac{N(N-1)}{2} = O(N^2)$$

[P5 (Scaling)](p5-scaling.md) is triggered precisely when group size $N$ crosses the critical threshold where architectural coupling forces unmanageable overhead. The predictive formula for hitting that wall is:

$$N_{\text{critical}} = \frac{k \cdot \text{avg\_skill}}{\text{architectural\_coupling}}$$

When $N \to N_{\text{critical}}$, the system will collapse unless you partition teams (reducing $N$ locally) and decouple the architecture.

## Related
- [Coordination](coordination.md) — The condition most directly constrained by Conway's Law.
- [P5: Scaling](p5-scaling.md) — The state where Conway's Law limits are hit.
