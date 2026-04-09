---
title: "00 - Model Identity"
type: concept
tags: [v2.1-canonical, summary, master-equation, hierarchy]
sources: [raw/6.md]
backlinks: [wiki/_indexes/root.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Engineering Organization Control Theory: Model Identity

## What This Is

A diagnostic and intervention framework for engineering organizations, built on the claim that **output is constrained multiplicatively across five major conditions**. In practice, severe weakness in one condition can dominate the whole system even when the others look healthy.

## The Master Equation

```text
Output(t) = theta * V(t) * P(t) * E(t) * A(t) * L(t) * exp(-lambda * Debt) * g(Var)
```

| Block | Question | Failure Pattern |
|-------|----------|-----------------|
| **V** Value Alignment | Are we building the right thing? | Fast execution of the wrong goal |
| **P** People System | Can humans tell truth and sustain? | Fear, burnout, and distortion |
| **E** Execution System | Can work actually flow? | Work stalls despite good intent |
| **A** Org Alignment | Does the org permit this to work? | Local fixes fail structurally |
| **L** Learning | Do we improve over time? | Repeated mistakes and shallow adaptation |

## The Diagnostic Sequence

```text
Step 0: Check for no-win conditions (V, PS, Su, IA, XT near zero)
Step 1: Verify People System integrity (Safety first; then Sustainability)
Step 2: Diagnose Execution (OM1 -> OM5) with structural awareness
Step 3: If E problems persist, inspect Org Alignment (A)
Step 4: Improve Learning only after V/P/E/A are minimally stable
```

## The Three Rules That Matter Most

1. **Zero-Override:** A near-zero anywhere is treated as urgent because it can dominate every downstream diagnosis.
2. **Gating:** Some capabilities depend on others. Learning depends on safety; local execution depends on structure.
3. **Nyquist:** Every block has a minimum observation window. Re-intervening too early can make the manager the instability source.

## The Most Important Insight

**The measurement system is itself a variable.** When Psychological Safety (`PS`) is low, many metrics become less trustworthy because people mask, comply, or selectively report. Fix the measurement environment before over-trusting the dashboard.

## Related Core Concepts

- [02 - Master Equation](02-master-equation.md) - the expanded formulation of the model.
- [20 - Diagnostic Sequence](20-diagnostic-sequence.md) - the operational decision tree.
- [06 - Time Constants](06-time-constants.md) - the systemic feedback window.
