# Design Document — Wiki Content Review

## Overview

This document defines the technical approach for executing a systematic content review of the Engineering Management Control Theory wiki. The review process is designed as a human-in-the-loop workflow where the LLM (Kiro) acts as the review agent, guided by structured checklists and producing documented findings.

## Review Architecture

### Execution Model

The review is **not a software system** — it is a **structured process** executed by the LLM with human oversight. The architecture consists of:

```
┌─────────────────────────────────────────────────────────────┐
│                    REVIEW SESSION                            │
├─────────────────────────────────────────────────────────────┤
│  Phase 1: Automated Checks (CLI Tools)                       │
│  ├── find-orphans.ps1 → orphan pages                         │
│  ├── find-stale.ps1 → stale pages                            │
│  ├── validate-frontmatter.ps1 → frontmatter issues           │
│  └── stats.ps1 → baseline metrics                            │
├─────────────────────────────────────────────────────────────┤
│  Phase 2: Page-Level Quality Review                          │
│  ├── Sample pages by category                                │
│  ├── Apply quality checklist per page                        │
│  └── Document findings                                       │
├─────────────────────────────────────────────────────────────┤
│  Phase 3: Cross-Page Coherence Analysis                      │
│  ├── Link graph validation                                   │
│  ├── Contradiction detection                                 │
│  └── Taxonomy alignment check                                │
├─────────────────────────────────────────────────────────────┤
│  Phase 4: V2.1 Framework Compliance                          │
│  ├── Legacy terminology scan                                 │
│  ├── Macro-Gate disambiguation check                         │
│  └── Canonical reference validation                          │
├─────────────────────────────────────────────────────────────┤
│  Output: Findings Report + Remediation Plan                  │
└─────────────────────────────────────────────────────────────┘
```

### Review Session State

Each review session maintains state in a findings document:

```yaml
session:
  id: "review-2026-04-09-001"
  started: "2026-04-09T10:00:00Z"
  scope: "full" | "incremental"
  filters: {}  # if incremental
  
pages_reviewed: []
findings: []
metrics:
  total_pages: 80
  pages_reviewed: 0
  findings_by_severity: { critical: 0, high: 0, medium: 0, low: 0 }
  findings_by_type: {}
```

---

## Phase 1: Automated Checks

### Tool Execution Sequence

Run existing CLI tools in sequence, capturing output:

| Tool | Purpose | Output Captured |
|------|---------|-----------------|
| `find-orphans.ps1` | Pages with no inbound backlinks | List of orphan page paths |
| `find-stale.ps1 -Days 30` | Pages not updated in 30+ days | List of stale page paths with last-updated dates |
| `validate-frontmatter.ps1` | Missing/invalid frontmatter fields | List of pages with specific field issues |
| `stats.ps1` | Wiki statistics | Page counts, tag distribution, link density |

### Automated Finding Generation

Each tool output is converted to structured findings:

```markdown
- page: wiki/concepts/example.md
  type: coherence-gap
  severity: medium
  source: automated (find-orphans.ps1)
  description: Page has no inbound backlinks
  recommendation: Add links from related pages or identify if page should be archived
```

---

## Phase 2: Page-Level Quality Review

### Page Selection Strategy

For a full review, all 80 pages are reviewed. For incremental reviews, pages are selected by:
- Category filter (entity, concept, source, synthesis)
- Tag filter
- Status filter (stub, stale, active)
- Date range filter

### Quality Checklist

Each page is evaluated against this checklist:

#### Accuracy
- [ ] Factual claims traceable to source documents
- [ ] Mathematical notation correct and consistent
- [ ] Definitions match canonical V2.1 definitions
- [ ] No outdated information contradicted by newer sources

#### Completeness
- [ ] Required frontmatter fields present (title, type, tags, sources, created, updated, status)
- [ ] Appropriate sections for page type:
  - **Concept pages**: Definition, Mechanism, Implications, Related Concepts
  - **Entity pages**: Overview, Components, Usage, References
  - **Source pages**: Summary, Key Entities, Key Concepts, Ingestion Log
- [ ] Backlinks field populated (if other pages link here)
- [ ] Tags include relevant taxonomy classification

#### Clarity
- [ ] Opening paragraph provides clear summary
- [ ] Technical terms defined or linked
- [ ] Prose structure follows logical flow
- [ ] Appropriate use of formatting (headers, lists, tables)

### Quality Scoring

Each dimension scored 1-5:

| Score | Meaning |
|-------|---------|
| 5 | Excellent — no issues |
| 4 | Good — minor improvements possible |
| 3 | Adequate — some issues to address |
| 2 | Needs Work — significant issues |
| 1 | Poor — requires major revision |

**Overall Quality Score** = min(accuracy, completeness, clarity)

Pages scoring ≤2 on any dimension generate a finding.

---

## Phase 3: Cross-Page Coherence Analysis

### Link Graph Validation

Build and validate the wikilink graph:

1. **Extract all wikilinks** from each page using pattern: `\[([^\]]+)\]\(([^)]+\.md)\)`
2. **Verify link targets exist** — flag broken links
3. **Verify backlinks accuracy** — frontmatter `backlinks` should match actual inbound links
4. **Identify orphan pages** — pages with no inbound links (already captured by CLI tool)

### Contradiction Detection

Scan for potential contradictions between related pages:

1. **Identify page pairs** that share tags or cross-reference each other
2. **Extract key claims** from each page (definitions, rules, theorems)
3. **Compare claims** for logical consistency
4. **Flag contradictions** for human review

Note: Contradiction detection is heuristic and requires human judgment to confirm.

### Taxonomy Alignment

Map each concept page to the 6-part Canonical taxonomy:

| Category | Expected Content | Example Pages |
|----------|------------------|---------------|
| Theory | Master equation, causal dynamics, state machines, time constants | 00-model-identity, 02-master-equation |
| Blocks | V, P, E, A, L block deep-dives | 10-block-V through 14-block-L |
| Diagnosis | Symptom maps, zero-override, domain calibration | 20-diagnostic-sequence, 21-zero-override |
| Playbook | Intervention rules, lever-access, J-curve | fix-order, lever-access-rule |
| Measurement | Telemetry, indicators, SPACE frameworks | 41-metrics-by-block |
| Reference | Theorems, anti-patterns, glossary | 51-anti-patterns, 53-literature-map |

Check:
- Pages are tagged with appropriate taxonomy tag
- Block pages (10-14) are properly numbered and cross-referenced
- Diagnostic content follows fix-order sequence

---

## Phase 4: V2.1 Framework Compliance

### Legacy Terminology Scan

Search for V1 terminology that should be updated to V2.1:

| V1 Term (Legacy) | V2.1 Equivalent |
|------------------|-----------------|
| "linear boundary" | Use "Macro-Gate" or specific block reference |
| "execution metrics" | Disambiguate: E-block metrics vs system-wide |
| "team health" | Use specific P-block vectors where applicable |
| Generic "alignment" | Specify: V-block (value) or A-block (org) |

### Macro-Gate Disambiguation Check

Verify that execution-related content properly distinguishes:

- **Macro-Gates** (V, P, A): Strategic/structural conditions that must be resolved first
- **Micro-Execution** (E): Operational delivery metrics

Pages discussing "execution problems" should reference the diagnostic sequence to determine if the root cause is a Macro-Gate issue or an E-block issue.

### Canonical Reference Validation

Verify that:
- Core concepts reference the canonical V2.1 source (6-canonical-v2-1.md)
- Block pages reference the Master Equation (02-master-equation.md)
- Diagnostic content references the Diagnostic Sequence (20-diagnostic-sequence.md)

---

## Finding Documentation Format

### Finding Structure

```markdown
### Finding: [Short Title]

- **Page**: wiki/concepts/example.md
- **Type**: quality-issue | correctness-error | framework-violation | coherence-gap | taxonomy-misalignment
- **Severity**: critical | high | medium | low
- **Source**: automated | human-judgment
- **Description**: [What was found]
- **Evidence**: [Specific quote or location]
- **Recommendation**: [Actionable fix]
```

### Severity Guidelines

| Severity | Criteria | Response Time |
|----------|----------|---------------|
| Critical | Factual error, broken core concept, V2.1 violation in canonical page | Immediate |
| High | Missing required content, significant clarity issue, broken link to core page | This session |
| Medium | Incomplete content, minor clarity issue, orphan page | Next session |
| Low | Style inconsistency, minor tag issue, enhancement opportunity | Backlog |

---

## Output Artifacts

### 1. Findings Report

Generated at end of review session:

```markdown
# Wiki Content Review — Findings Report

**Session**: review-2026-04-09-001
**Scope**: Full (80 pages)
**Duration**: [start] to [end]

## Summary

- Total pages reviewed: 80
- Total findings: N
- By severity: critical: X, high: Y, medium: Z, low: W
- By type: [breakdown]

## Critical Findings
[List]

## High Priority Findings
[List]

## Medium Priority Findings
[List]

## Low Priority Findings
[List]

## Quick Wins
[Low-effort, high-impact fixes]
```

### 2. Remediation Plan

Prioritized action list:

```markdown
# Remediation Plan

## Immediate (Critical)
1. [ ] Fix [specific issue] in [page]
2. [ ] Correct [factual error] in [page]

## This Session (High)
1. [ ] Expand stub: [page]
2. [ ] Add missing section to [page]

## Next Session (Medium)
1. [ ] Add backlinks to orphan page [page]
2. [ ] Update stale page [page]

## Backlog (Low)
1. [ ] Style improvements in [page]
```

### 3. Review Log Entry

Appended to `wiki/log/2026-04.md`:

```markdown
## [2026-04-09 HH:MM] review | Full Content Review
- Session ID: review-2026-04-09-001
- Scope: Full wiki (80 pages)
- Findings: N total (critical: X, high: Y, medium: Z, low: W)
- Automated tools: find-orphans.ps1, find-stale.ps1, validate-frontmatter.ps1, stats.ps1
- Key issues: [summary of top 3-5 issues]
- Remediation plan: [link to plan]
```

---

## Incremental Review Mode

When scope is limited, the same process applies but with filtered page set:

### Filter Options

| Filter | Implementation |
|--------|----------------|
| Page type | Filter by frontmatter `type` field |
| Tag | Filter by presence of tag in `tags` array |
| Status | Filter by `status` field |
| Date range | Filter by `updated` field |

### Scope Indication

All outputs clearly indicate the review scope:

```markdown
**Scope**: Incremental
**Filters**: type=concept, status=stub
**Pages in scope**: 12 of 80
```

---

## Review Execution Checklist

For the LLM executing the review:

### Pre-Review
- [ ] Confirm review scope with user (full vs incremental)
- [ ] Apply any filters for incremental review
- [ ] Load WIKI_SCHEMA.md for reference

### Phase 1: Automated
- [ ] Run find-orphans.ps1
- [ ] Run find-stale.ps1 -Days 30
- [ ] Run validate-frontmatter.ps1
- [ ] Run stats.ps1
- [ ] Convert tool outputs to findings

### Phase 2: Page Quality
- [ ] For each page in scope:
  - [ ] Read page content
  - [ ] Apply quality checklist
  - [ ] Score accuracy, completeness, clarity
  - [ ] Generate findings for scores ≤2

### Phase 3: Coherence
- [ ] Build link graph
- [ ] Validate link targets
- [ ] Verify backlinks accuracy
- [ ] Scan for contradictions (heuristic)
- [ ] Check taxonomy alignment

### Phase 4: V2.1 Compliance
- [ ] Scan for legacy terminology
- [ ] Check Macro-Gate disambiguation
- [ ] Validate canonical references

### Post-Review
- [ ] Generate findings report
- [ ] Create remediation plan
- [ ] Append log entry to wiki/log/2026-04.md
- [ ] Present summary to user