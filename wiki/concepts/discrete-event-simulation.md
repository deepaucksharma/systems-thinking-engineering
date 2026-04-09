---
title: "Discrete-Event Simulation (DES)"
type: concept
tags: [simulation, algorithms, operations-research, digital-twin, queuing-theory]
sources: [raw/3.md]
backlinks: [wiki/concepts/digital-twin.md, wiki/legacy/master-equation.md]
created: 2026-04-08
updated: 2026-04-09
status: active
---

# Discrete-Event Simulation (DES)

## Definition

Discrete-event simulation is one plausible computational backbone for the framework's digital-twin idea. In a DES, the system evolves through state-changing events such as work arrival, task start, review delay, defect escape, rework, staffing changes, or intervention events.

DES is useful here because engineering work is not smooth and continuous. It is lumpy, interrupted, queued, and dependent on coordination events.

## What a Simulation Should Represent

A useful simulation does not need to model every human detail. It needs to represent the main mechanisms that plausibly drive the outcomes the framework cares about.

Typical ingredients:
- work arrival and prioritization;
- service capacity and work-in-progress constraints;
- interrupts, handoffs, and queueing delays;
- defect escape and rework loops;
- burnout, recovery, or other capacity-degradation mechanisms;
- management interventions and their lagged effects.

## Typical Model Components

### Agents

- engineers or engineering teams as service units with finite capacity;
- managers as intervention sources;
- intake sources such as product, incidents, or external requests.

### Events

- task arrival;
- task start;
- task completion;
- review delay;
- defect discovery;
- rework insertion;
- intervention or policy change.

### State Variables

- queue length and WIP;
- cycle time and waiting time;
- batch size distribution;
- defect and rework load;
- block-level condition estimates where the model supports them.

## What "Validation" Really Means

A simulation is not validated because it looks sophisticated. It is validated when it reproduces patterns that matter:
- rising WIP should usually increase waiting and cycle time;
- larger batches should usually worsen feedback speed and increase risk;
- structural coordination burdens should produce more delay variability;
- sustained overload should reduce future effective capacity.

The bar is behavioral realism, not perfect prediction.

## Example Use Cases

- compare the likely effect of lowering WIP versus lowering batch size;
- estimate how much coordination drag a dependency-heavy topology introduces;
- test whether a quality investment reduces long-run rework enough to offset short-run throughput loss;
- explore how quickly overload debt accumulates under different intake regimes.

## Practical Warnings

- Avoid pretending every social variable can be simulated with high fidelity.
- Avoid hard-coding the framework's conclusions into the simulation and then calling the result validation.
- Prefer simple models that illuminate mechanisms over complicated models with fake precision.

## Related

- [Digital Twin](digital-twin.md) - broader operational use of a continuously updated model
- [Little's Law](littles-law.md) - queueing intuition that often belongs inside the simulation
- [Transfer Functions](transfer-functions.md) - alternative way to think about coupling and lag
