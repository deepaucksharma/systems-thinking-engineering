---
title: "Wiki Content Review — Findings Register"
type: synthesis
tags: [review, maintenance, quality]
sources: []
backlinks: [wiki/_indexes/syntheses.md]
created: 2026-04-09
updated: 2026-04-09
status: active
---

# Wiki Content Review — Findings Register

**Scope:** Full wiki under `wiki/` (content pages excluding `wiki/log/` unless noted).  
**Automation:** Run [`tools/check-wiki-links.ps1`](../../tools/check-wiki-links.ps1) from the repo root for empty links, broken relative `.md` targets, frontmatter `wiki/*.md` list paths, and conflicting tag hints.

## Executive summary

The wiki uses a deliberate **two-tier** structure: V2.1 **canonical** concept pages versus **legacy** comparison material. Prior drift (missing files, empty legacy links, stale index counts) broke navigation; this register records what was fixed and what ongoing hygiene looks like.

## Inventory (post-remediation)

| Area | Count |
|------|------:|
 Sources | 6 |
 Entities | 2 |
 Concepts | 57 |
 Legacy | 16 |
 Syntheses | 2 |
 Indexes | 5 |
 **Content pages (excl. log)** | **88** |

## Resolved issues (2026-04-09 remediation)

1. **Missing high-traffic concept files** — Restored from git: `wiki/concepts/02-master-equation.md`, `wiki/concepts/incentive-mechanism-design.md`, `wiki/concepts/littles-law.md` (working tree had deleted them while indexes and inbound links still referenced them).

2. **Legacy empty links** — Replaced all empty-URL markdown anchors under `wiki/legacy/` with correct `../concepts/...` targets.

3. **Master Equation duplication** — Clarified roles:
   - [`wiki/concepts/02-master-equation.md`](../concepts/02-master-equation.md): canonical math and gates.
   - [`wiki/concepts/00-model-identity.md`](../concepts/00-model-identity.md): overview + same equation in context.
   - [`wiki/legacy/master-equation.md`](../legacy/master-equation.md): historical V1/V2 narrative (`type: concept`, legacy tags).
   - [`wiki/entities/master-equation.md`](../entities/master-equation.md): short **entity index** stub; [`wiki/_indexes/entities.md`](../_indexes/entities.md) lists it.

4. **Index drift** — Updated [`wiki/_indexes/root.md`](../_indexes/root.md) statistics and entities index; renamed the concepts index legacy section per readability review.

5. **Frontmatter backlink path** — [`wiki/concepts/conways-law.md`](../concepts/conways-law.md): `coordination` backlink pointed at a non-existent `concepts/` path; corrected to `wiki/legacy/coordination.md`.

6. **Epistemic wording (canonical set)** — Softened over-strong “theorem / mathematically proven / guarantees” language where it conflicted with the model’s own disclaimers (e.g. [`51-anti-patterns.md`](../concepts/51-anti-patterns.md), [`41-metrics-by-block.md`](../concepts/41-metrics-by-block.md), [`winning-loop.md`](../concepts/winning-loop.md), [`p4-thriving.md`](../concepts/p4-thriving.md)).

## Ongoing tooling

| Script | Purpose |
|--------|---------|
| [`tools/check-wiki-links.ps1`](../../tools/check-wiki-links.ps1) | Links with empty destinations, broken `.md` links, YAML list paths under `backlinks` / `superseded_by` / `historical_lineage` |
| [`tools/find-orphans.ps1`](../../tools/find-orphans.ps1) | Inbound link count (excludes `_indexes` and `log`; triage only) |
| [`tools/fix-legacy-links.ps1`](../../tools/fix-legacy-links.ps1) | Legacy path rewrites **inside** `wiki/concepts` only |

**Convention:** After bulk moves or renames, run `check-wiki-links.ps1` and fix reports before updating index statistics.

## Backlog (non-blocking)

- **Source page `backlinks:`** — Often empty while concepts cite sources; either populate from automation or drop the field for sources-only.
- **Causal loop pages** — Mix `v2-framework` and `active` status; periodic review for V2.1 alignment or explicit `legacy-reference` tagging.
- **CI** — Optional: run `check-wiki-links.ps1` in pipeline; exit code 1 on any reported issue.

## Prior review artifact note

Earlier sections of this file claimed an empty `syntheses/` directory and other state that no longer matched the tree. This version **replaces** that narrative with the remediation above and with automation as the source of truth for link integrity.

