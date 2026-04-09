---
title: "Concepts Index"
type: synthesis
tags: [index, concepts]
sources: []
backlinks: [wiki/_indexes/root.md]
created: 2026-04-08
updated: 2026-04-09
status: active
---

# Concepts Index

Principles, conditions, rules, dynamics, team states, and failure modes.

## Canonical reading order (V2.1 hierarchy)

Use this spine when navigating end-to-end; branch into blocks and tools only after the spine makes sense.

1. [00 — Model Identity](../concepts/00-model-identity.md) — five blocks in one screen.
2. [02 — Master Equation](../concepts/02-master-equation.md) — definitions, debt/variability, **gates** (what constrains what).
3. Block pages [V](../concepts/10-block-V.md) · [P](../concepts/11-block-P.md) · [E](../concepts/12-block-E.md) · [A](../concepts/13-block-A.md) · [L](../concepts/14-block-L.md).
4. Operator sequence: [20 — Diagnostic Sequence](../concepts/20-diagnostic-sequence.md), [21 — Zero-Override](../concepts/21-zero-override.md), [41 — Metrics by Block](../concepts/41-metrics-by-block.md).
5. **[Legacy](../legacy/) pages** — comparison and OM1–OM6 vocabulary only; they do not override `00`, `02`, or the numbered block pages.

Entity index entry for the equation: [Master Equation (entity)](../entities/master-equation.md).

## Core Framework

- [00 - Model Identity](../concepts/00-model-identity.md) - entry point and high-level block overview | tags: `summary`, `framework`
- [02 - Master Equation](../concepts/02-master-equation.md) - expanded model of interacting constraints | tags: `theory`, `framework`
- [06 - Time Constants](../concepts/06-time-constants.md) - intervention and observation windows | tags: `timing`, `framework`
- [20 - Diagnostic Sequence](../concepts/20-diagnostic-sequence.md) - operational flow for diagnosis and intervention | tags: `diagnostics`, `framework`
- [21 - Zero-Override](../concepts/21-zero-override.md) - what to do when a condition is near-collapse | tags: `diagnostics`, `framework`
- [41 - Metrics by Block](../concepts/41-metrics-by-block.md) - telemetry reference by block and variable | tags: `measurement`, `framework`
- [51 - Anti-Patterns](../concepts/51-anti-patterns.md) - recurring management and system failure modes | tags: `reference`, `framework`
- [53 - Literature Map](../concepts/53-literature-map.md) - supporting theory and citation map | tags: `reference`, `framework`

## Major Blocks

- [10 - Block V (Value Alignment)](../concepts/10-block-V.md) - strategic and value-side constraints | tags: `block-v`
- [11 - Block P (People System)](../concepts/11-block-P.md) - human-system constraints | tags: `block-p`
- [12 - Block E (Execution System)](../concepts/12-block-E.md) - delivery mechanics and reliability | tags: `block-e`
- [13 - Block A (Org Alignment)](../concepts/13-block-A.md) - structural and incentive constraints | tags: `block-a`
- [14 - Block L (Learning & Adaptation)](../concepts/14-block-L.md) - feedback, adaptation, and organizational learning | tags: `block-l`

## Legacy V2 block summaries (reference only)

- [Value Alignment](../legacy/value-alignment.md) - earlier V2 summary retained for comparison | tags: `v2-framework`, `block-v`, `stale`
- [People System](../legacy/people-system.md) - earlier V2 summary retained for comparison | tags: `v2-framework`, `block-p`, `stale`
- [Execution System](../legacy/execution-system.md) - earlier V2 summary retained for comparison | tags: `v2-framework`, `block-e`, `stale`
- [Org Alignment](../legacy/org-alignment.md) - earlier V2 summary retained for comparison | tags: `v2-framework`, `block-a`, `stale`
- [Learning and Adaptation](../legacy/learning-adaptation.md) - earlier V2 summary retained for comparison | tags: `v2-framework`, `block-l`, `stale`

## Legacy Conditions

- [Clarity](../legacy/clarity.md) - legacy OM1 page retained for comparison | tags: `condition`, `om1`, `stale`
- [Focus](../legacy/focus.md) - legacy OM2 page retained for comparison | tags: `condition`, `om2`, `stale`
- [Skill](../legacy/skill.md) - legacy OM3 page retained for comparison | tags: `condition`, `om3`, `stale`
- [Coordination](../legacy/coordination.md) - legacy OM4 page retained for comparison | tags: `condition`, `om4`, `stale`
- [Quality](../legacy/quality.md) - legacy OM5 page retained for comparison | tags: `condition`, `om5`, `stale`
- [Feedback Speed](../concepts/feedback-speed.md) - OM6 vocabulary; in V2.1 the same signal is `$FS$` inside Block L (see [14 - Block L](../concepts/14-block-L.md)) | tags: `condition`, `om6`, `v2-framework`

## Theory and Computation

- [Order Parameter ($\Phi$)](../concepts/order-parameter.md) - threshold-style model of state change | tags: `thermodynamics`, `state-machine`
- [V2 Theorems](../concepts/v2-theorems.md) - stronger claims and constraints from the older framing | tags: `theorems`, `v2-framework`
- [Hysteresis](../concepts/hysteresis.md) - asymmetric state transition gaps | tags: `thermodynamics`, `memory`
- [Self-Organized Criticality](../concepts/self-organized-criticality.md) - avalanche-style failure behavior | tags: `failure-mode`, `collapse`
- [Digital Twin](../concepts/digital-twin.md) - simulation and instrumentation framing | tags: `simulation`, `modeling`
- [Discrete-Event Simulation (DES)](../concepts/discrete-event-simulation.md) - computational stochastic model | tags: `simulation`, `algorithms`
- [Transfer Functions](../concepts/transfer-functions.md) - formal continuous differential mapping between major constraints | tags: `theory`, `control-theory`
- [Mechanism Design & Game Theory](../concepts/incentive-mechanism-design.md) - solving the principal-agent paradox through incentive compatibility | tags: `economics`, `game-theory`
- [Open Research Questions](../concepts/open-research-questions.md) - unproven or weakly supported hypotheses | tags: `research`, `future`

## Dynamics

- [Losing Loop](../concepts/losing-loop.md) - self-reinforcing overload cycle | tags: `dynamics`, `reinforcing-loop`
- [Winning Loop](../concepts/winning-loop.md) - self-reinforcing improvement cycle | tags: `dynamics`, `reinforcing-loop`
- [Incentive Death Spiral](../concepts/incentive-death-spiral.md) - incentive damage propagating into people and execution | tags: `v2-framework`, `loop`
- [Fear Amplification Loop](../concepts/fear-amplification-loop.md) - low safety degrading learning and value | tags: `v2-framework`, `loop`
- [Sustainability Drain Loop](../concepts/sustainability-drain-loop.md) - overload degrading execution and structure | tags: `v2-framework`, `loop`
- [Strategic Drift Loop](../concepts/strategic-drift-loop.md) - weak learning distorting value over time | tags: `v2-framework`, `loop`
- [Condition Decay](../concepts/condition-decay.md) - conditions drift downward without maintenance | tags: `dynamics`, `principle`
- [Multi-Scale Dynamics](../concepts/multi-scale-dynamics.md) - micro, meso, and macro coupling | tags: `scale`, `coupling`
- [Fractal Scaling](../concepts/fractal-scaling.md) - recursive ecosystem behavior | tags: `scale`, `ecosystem`
- [Cross-Domain Extensions](../concepts/cross-domain-extensions.md) - extensions beyond software organizations | tags: `cross-domain`
- [Conway's Law](../concepts/conways-law.md) - structure and architecture co-shaping each other | tags: `structure`, `scaling`

## Rules and Diagnostic Aids

- [Structure-vs-Development Rule](../concepts/structure-vs-development-rule.md) - when ambiguous, fix coordination and structure before blaming skill | tags: `rule`, `diagnostics`
- [Lever-Access Rule](../concepts/lever-access-rule.md) - verify you can actually pull the lever you are recommending | tags: `rule`, `escalation`
- [Fix-Order](../legacy/fix-order.md) - older diagnostic shorthand retained for comparison | tags: `diagnostics`, `hierarchy`, `stale`
- [Zero-Override Rule](../legacy/zero-override-rule.md) - older zero-state page retained for comparison | tags: `rule`, `foundation`, `stale`
- [Nyquist Constraint](../legacy/nyquist-constraint.md) - older timing page retained for comparison | tags: `control-theory`, `timing`, `stale`

## Team States

- [P1 - Crisis](../concepts/p1-crisis.md) - deep losing loop, confusion, panic | tags: `team-state`, `crisis`
- [P2 - Stabilizing](../concepts/p2-stabilizing.md) - exiting the losing loop, still fragile | tags: `team-state`, `stabilizing`
- [P3 - Functional](../concepts/p3-functional.md) - neutral state where delivery mostly works | tags: `team-state`, `functional`
- [P4 - Thriving](../concepts/p4-thriving.md) - stable improvement and strong learning | tags: `team-state`, `thriving`
- [P5 - Scaling](../concepts/p5-scaling.md) - growth pressure threatens a previously healthy state | tags: `team-state`, `scaling`
- [P6 - Mixed State](../concepts/p6-mixed-state.md) - different subsystems occupy different states | tags: `team-state`, `mixed-state`
- [V2 Extended States](../concepts/v2-extended-states.md) - older V2 state taxonomy | tags: `team-state`, `v2-framework`

## Measurement and Validation

- [Measurement Theory](../concepts/measurement-theory.md) - methodological foundation for latent-variable construction and validation | tags: `measurement-theory`, `pca`
- [Ethical Measurement](../concepts/ethical-measurement.md) - surveillance, gaming, and governance risks in telemetry | tags: `ethics`, `psychology`
- [Metrics Framework](../legacy/metrics-framework.md) - older V2 measurement summary retained for comparison | tags: `metrics`, `measurement`, `stale`
- [Little's Law](../concepts/littles-law.md) - stock, flow, and cycle-time intuition | tags: `queuing-theory`, `flow`
- [Utilization Curve](../concepts/utilization-curve.md) - why high utilization can collapse flow | tags: `physics`, `utilization`
- [Goodhart's Law](../concepts/goodharts-law.md) - target distortion and metric gaming | tags: `ethics`, `measurement`
- [Falsifiability Criteria](../concepts/falsifiability-criteria.md) - empirical checks for the model's claims | tags: `science`, `validation`
- [Boundary Conditions](../concepts/boundary-conditions.md) - where the model stops being trustworthy | tags: `limitations`, `edge-cases`

## Failure Modes, Traps, and Execution

- [Hero Culture Trap](../concepts/hero-culture-trap.md) - high effort masking fragility | tags: `trap`, `failure-mode`
- [Rushing Trap](../concepts/rushing-trap.md) - apparent speed purchased with hidden debt | tags: `trap`, `failure-mode`
- [Anti-Patterns](../legacy/anti-patterns.md) - older anti-pattern map retained for comparison | tags: `anti-pattern`, `executive`, `stale`
- [Resource Allocation Game](../concepts/resource-allocation-game.md) - slack versus utilization as a political conflict | tags: `game-theory`, `slack`
- [The Cynical Equilibrium](../concepts/cynical-equilibrium.md) - rational local behavior producing destructive global outcomes | tags: `failure-mode`, `equilibrium`
- [Temporal Integration Loop](../concepts/temporal-integration-loop.md) - observe, diagnose, act, measure, scale | tags: `control-loop`, `process`
- [Practitioner's Checklist](../concepts/practitioners-checklist.md) - staged integration path for operators | tags: `implementation`, `execution`
