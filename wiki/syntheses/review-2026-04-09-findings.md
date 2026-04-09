# Wiki Content Review — Findings Report

**Session**: review-2026-04-09-001
**Scope**: Full (75 content pages)
**Started**: 2026-04-09
**Status**: In Progress

---

## Executive Summary

The wiki has undergone a major V2.1 restructuring on 2026-04-09. The canonical V2.1 pages (00-, 02-, 06-, 10-14-, 20-, 21-, 41-, 51-, 53-prefixed) are high quality and internally consistent. However, a significant portion of legacy V1/V2 pages remain marked as "stale" but have not been fully updated or archived, creating potential confusion for readers.

**Key Finding**: The wiki has a two-tier quality structure:
1. **Canonical V2.1 pages** (13 pages): Excellent quality, complete, clear
2. **Legacy V1/V2 pages** (62 pages): Variable quality, many marked stale, inconsistent cross-references

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total content pages | 75 |
| Canonical V2.1 pages | 13 |
| Legacy V2 pages | 62 |
| Pages marked "stale" | ~20 |
| Pages marked "stub" | 0 |
| Orphan pages | 1 |

---

## Findings by Severity

### CRITICAL (0)

No critical findings identified.

---

### HIGH (6)

#### Finding H1: Orphan Page — sources/diagram-set-2.md

- **Page**: wiki/sources/diagram-set-2.md
- **Type**: coherence-gap
- **Source**: automated (find-orphans.ps1)
- **Description**: Page has no inbound backlinks from other wiki pages
- **Evidence**: Tool output shows this as the only orphan
- **Recommendation**: Add cross-references from related pages (diagram-set-1.md, metrics-framework.md, fix-order.md) or confirm if this is intentional

---

#### Finding H2: Inconsistent Status Marking — Legacy Pages Marked "Stale" Without Clear Migration Path

- **Pages**: clarity.md, focus.md, skill.md, coordination.md, quality.md, fix-order.md, zero-override-rule.md, nyquist-constraint.md, master-equation.md (entity)
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: Multiple core concept pages are marked "stale" with warnings pointing to V2.1 canonical pages, but the relationship between legacy and canonical pages is inconsistent
- **Evidence**: 
  - clarity.md, focus.md, skill.md, coordination.md, quality.md all have status: stale and point to 12-block-E.md
  - fix-order.md points to 20-diagnostic-sequence.md
  - zero-override-rule.md points to 21-zero-override.md
  - nyquist-constraint.md points to 06-time-constants.md
  - master-equation.md (entity) points to 02-master-equation.md
- **Recommendation**: 
  1. Create a consistent "Legacy Page" template that clearly indicates: "This page is retained for historical reference. For current guidance, see [canonical page]."
  2. Consider whether stale pages should be moved to a wiki/legacy/ directory
  3. Update all stale pages to have consistent warning formatting

---

#### Finding H3: Missing Backlinks in Source Pages

- **Pages**: wiki/sources/3-extended-framework.md, wiki/sources/4-visual-architecture.md, wiki/sources/diagram-set-1.md, wiki/sources/diagram-set-2.md, wiki/sources/canonical-v2-consolidated-model.md
- **Type**: coherence-gap
- **Source**: human-judgment
- **Description**: Source pages have empty backlinks arrays but are referenced from concept pages
- **Evidence**: All source pages show `backlinks: []` in frontmatter, but concept pages link to them
- **Recommendation**: Run backlink maintenance to populate these fields

---

#### Finding H4: Inconsistent Tag Usage — v2-framework vs v2.1-canonical

- **Pages**: Multiple
- **Type**: taxonomy-misalignment
- **Source**: human-judgment
- **Description**: Two different tag schemes exist for V2 content: `v2-framework` (legacy) and `v2.1-canonical` (current). This creates confusion about which pages are current.
- **Evidence**:
  - Canonical V2.1 pages use `v2.1-canonical`
  - Legacy V2 pages use `v2-framework`
  - Some pages have both tags
- **Recommendation**: Establish clear tag semantics:
  - `v2.1-canonical` = current, maintained, authoritative
  - `v2-framework` = legacy, retained for reference only
  - Pages should not have both tags

---

#### Finding H5: Missing Canonical Block Pages — 13-block-A.md and 14-block-L.md Not Reviewed

- **Pages**: wiki/concepts/13-block-A.md, wiki/concepts/14-block-L.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: Block A and Block L canonical pages were not included in the sample review
- **Evidence**: Only reviewed 10-block-V.md, 11-block-P.md, 12-block-E.md
- **Recommendation**: Complete review of all 5 canonical block pages

---

#### Finding H6: Index Page Counts Inconsistent with Actual

- **Page**: wiki/_indexes/root.md
- **Type**: correctness-error
- **Source**: human-judgment
- **Description**: Root index states "Concepts: 67" but actual count is 67 files. Need to verify all counts are accurate.
- **Evidence**: Directory listing shows 67 concept files, index says 67 — appears correct but should verify other counts
- **Recommendation**: Verify all statistics in root.md match actual counts

---

### MEDIUM (8)

#### Finding M1: Legacy Condition Pages Have Incomplete V2 Context

- **Pages**: clarity.md, focus.md, skill.md, coordination.md, quality.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: Legacy OM1-OM5 condition pages have V2 context sections but they are brief and could be expanded
- **Evidence**: Each page has a "V2 Context" section but it's minimal compared to the canonical Block E page
- **Recommendation**: Either expand V2 context or clearly mark as "retained for V1 reference only"

---

#### Finding M2: Feedback Speed Page Status Inconsistency

- **Page**: wiki/concepts/feedback-speed.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: Feedback Speed is listed as OM6 in the conditions section of the concepts index, but it belongs to Block L in V2.1
- **Evidence**: Concepts index shows "Feedback Speed — OM6, Multiplier relocated to Concept L"
- **Recommendation**: Update index entry to clarify V2.1 placement

---

#### Finding M3: Team State Pages Have Inconsistent Update Dates

- **Pages**: p1-crisis.md through p5-scaling.md (updated 2026-04-09), p6-mixed-state.md (updated 2026-04-08)
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: P1-P5 team state pages were updated on 2026-04-09 but P6 was updated on 2026-04-08
- **Evidence**: Frontmatter dates show inconsistency
- **Recommendation**: Review P6-mixed-state.md for V2.1 consistency with other team state pages

---

#### Finding M4: Causal Loop Pages Not Marked Stale

- **Pages**: losing-loop.md, winning-loop.md, fear-amplification-loop.md, sustainability-drain-loop.md, incentive-death-spiral.md, strategic-drift-loop.md
- **Type**: taxonomy-misalignment
- **Source**: human-judgment
- **Description**: Causal loop pages are marked "active" but reference legacy V2 framework. Unclear if they need V2.1 updates.
- **Evidence**: All have `status: active` and `v2-framework` tag
- **Recommendation**: Review for V2.1 consistency or mark as legacy reference

---

#### Finding M5: Missing Cross-References Between Canonical and Legacy Pages

- **Pages**: Multiple
- **Type**: coherence-gap
- **Source**: human-judgment
- **Description**: Some canonical pages don't reference their legacy counterparts, making it hard to find historical context
- **Evidence**: 12-block-E.md references legacy condition pages, but 20-diagnostic-sequence.md doesn't reference fix-order.md
- **Recommendation**: Add "Historical Reference" sections to canonical pages linking to legacy equivalents

---

#### Finding M6: Concepts Index Organization Could Be Improved

- **Page**: wiki/_indexes/concepts.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: The concepts index is well-organized but the "System Blocks (Legacy V2 Comparison)" section could be clearer about the relationship to canonical pages
- **Evidence**: Section title says "Legacy V2 Comparison" but pages are marked stale
- **Recommendation**: Rename section to "Legacy V2 Block Summaries (Retained for Reference)"

---

#### Finding M7: Entity Page master-equation.md Has Confusing Status

- **Page**: wiki/legacy/master-equation.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: The entity page is marked "stale" but serves as a useful historical bridge between V1 and V2.1
- **Evidence**: Page has clear warning and redirect, but "stale" status implies it should be updated
- **Recommendation**: Consider changing status to "active" with a "legacy-reference" tag, since it serves a valid purpose

---

#### Finding M8: Missing Syntheses

- **Directory**: wiki/syntheses/
- **Type**: coherence-gap
- **Source**: human-judgment
- **Description**: The syntheses directory is empty despite the wiki having been queried and analyzed
- **Evidence**: Directory listing shows no files
- **Recommendation**: File this findings report as the first synthesis page

---

### LOW (4)

#### Finding L1: Minor Tag Inconsistency — block-e vs block-e

- **Pages**: Multiple
- **Type**: taxonomy-misalignment
- **Source**: human-judgment
- **Description**: Some pages use `block-e` tag while canonical page uses `block-e` — verify consistency
- **Evidence**: 12-block-E.md has tag `block-e`, execution-system.md has `block-e`
- **Recommendation**: Standardize tag format (lowercase with hyphens)

---

#### Finding L2: Update Date Consistency in Index

- **Page**: wiki/_indexes/concepts.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: Some index entries show update dates while others don't
- **Evidence**: Canonical section entries don't show dates, conditions section entries do
- **Recommendation**: Make date display consistent across all sections

---

#### Finding L3: Mermaid Diagram in losing-loop.md May Need V2.1 Update

- **Page**: wiki/concepts/losing-loop.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: The mermaid diagram is comprehensive but may not reflect V2.1 block structure
- **Evidence**: Diagram shows "R1 — Deep Losing Loop" but doesn't show block boundaries
- **Recommendation**: Consider adding block boundary annotations to the diagram

---

#### Finding L4: P6-Mixed-State Page Shorter Than Other Team State Pages

- **Page**: wiki/concepts/p6-mixed-state.md
- **Type**: quality-issue
- **Source**: human-judgment
- **Description**: P6 page is notably shorter than P1-P5 pages, missing some standard sections
- **Evidence**: P6 has ~50 lines vs ~80 lines for other team state pages
- **Recommendation**: Expand P6 to include same sections as other team state pages (Mathematical Threshold, Phase Space Trajectory if applicable)

---

## Quick Wins

1. **Populate backlinks in source pages** — Run automated backlink maintenance
2. **Update P6-mixed-state.md** — Add missing sections to match other team state pages
3. **Rename legacy section in concepts index** — Clarify "Legacy V2 Block Summaries (Retained for Reference)"
4. **Add cross-reference from 20-diagnostic-sequence.md to fix-order.md** — Help readers find historical context

---

## Remediation Plan

### Immediate (Critical)
None identified.

### This Session (High)
1. [ ] Review and update orphan page diagram-set-2.md with proper cross-references
2. [ ] Create consistent legacy page template/warning format
3. [ ] Run backlink maintenance on source pages
4. [ ] Clarify tag semantics (v2-framework vs v2.1-canonical)
5. [ ] Complete review of 13-block-A.md and 14-block-L.md
6. [ ] Verify index statistics

### Next Session (Medium)
1. [ ] Expand V2 context in legacy condition pages or mark as reference-only
2. [ ] Update feedback-speed.md index entry
3. [ ] Review P6-mixed-state.md for V2.1 consistency
4. [ ] Review causal loop pages for V2.1 consistency
5. [ ] Add historical reference sections to canonical pages
6. [ ] Reorganize concepts index legacy section
7. [ ] Resolve master-equation.md entity page status
8. [ ] File this synthesis in wiki/syntheses/

### Backlog (Low)
1. [ ] Standardize tag format across all pages
2. [ ] Make index date display consistent
3. [ ] Update losing-loop.md mermaid diagram with block boundaries
4. [ ] Expand P6-mixed-state.md to match other team state pages

---

## Phase 2 Status

**Completed Reviews:**
- [x] Source pages (6/6)
- [x] Entity pages (2/2)
- [x] Canonical V2.1 concept pages (sample: 6/13)
- [x] Legacy condition pages (6/6)
- [x] Team state pages (6/6)
- [x] Causal loop pages (6/6)
- [x] Index pages (3/3)

**Remaining:**
- [ ] Complete canonical block pages (13-block-A.md, 14-block-L.md)
- [ ] Review remaining concept pages (~45 pages)
- [ ] Phase 3: Cross-page coherence analysis
- [ ] Phase 4: V2.1 framework compliance check

---

## Next Steps

1. Complete Phase 2 page-level quality review for remaining concept pages
2. Proceed to Phase 3: Cross-page coherence analysis
3. Proceed to Phase 4: V2.1 framework compliance check
4. Generate final remediation plan
5. Log review session in wiki/log/2026-04.md