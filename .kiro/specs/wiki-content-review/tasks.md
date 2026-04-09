# Implementation Plan: Wiki Content Review

## Overview

This is a structured manual review process executed by the LLM (Kiro) with human oversight. The review assesses 80 wiki pages across four phases: automated checks, page-level quality, cross-page coherence, and V2.1 framework compliance. Each phase produces documented findings that feed into a final remediation plan.

## Tasks

- [x] 1. Initialize review session
  - Create review session with unique identifier and timestamp
  - Enumerate all 80 wiki pages organized by category (sources, entities, concepts, syntheses)
  - Load WIKI_SCHEMA.md to establish V2.1 compliance standards
  - Confirm review scope with user (full vs incremental)
  - Apply any filters for incremental review (type, tag, status, date range)
  - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [x] 2. Phase 1 - Run automated CLI tool checks
  - [x] 2.1 Execute find-orphans.ps1 to identify orphan pages
    - Run `pwsh tools/find-orphans.ps1`
    - Capture list of pages with no inbound backlinks
    - Convert each orphan to a coherence-gap finding (severity: medium)
    - _Requirements: 8.1, 5.2_

  - [x] 2.2 Execute find-stale.ps1 to identify stale pages
    - Run `pwsh tools/find-stale.ps1 -Days 30`
    - Capture list of pages not updated in 30+ days with last-updated dates
    - Convert each stale page to a quality-issue finding (severity: medium)
    - _Requirements: 8.2, 2.5_

  - [x] 2.3 Execute validate-frontmatter.ps1 to check frontmatter compliance
    - Run `pwsh tools/validate-frontmatter.ps1`
    - Capture list of pages with missing/invalid frontmatter fields
    - Convert each issue to a correctness-error finding (severity: high for missing required fields)
    - _Requirements: 8.3, 3.4, 3.5, 3.6_

  - [x] 2.4 Execute stats.ps1 to gather baseline metrics
    - Run `pwsh tools/stats.ps1`
    - Capture page counts by type, tag distribution, link density
    - Record baseline metrics in session state
    - _Requirements: 8.4_

- [x] 3. Checkpoint - Phase 1 complete
  - Ensure all automated tool findings are documented
  - Ask the user if questions arise before proceeding to Phase 2

- [-] 4. Phase 2 - Page-level quality review
  - [ ] 4.1 Review source pages (wiki/sources/)
    - For each source page, apply quality checklist:
      - Accuracy: Verify claims against source documents in raw/
      - Completeness: Check for required sections (Summary, Key Entities, Key Concepts, Ingestion Log)
      - Clarity: Analyze prose structure and readability
    - Score each dimension 1-5, generate findings for scores ≤2
    - _Requirements: 2.1, 2.2, 2.3, 2.6_

  - [ ] 4.2 Review entity pages (wiki/entities/)
    - For each entity page, apply quality checklist:
      - Accuracy: Verify claims against source documents
      - Completeness: Check for required sections (Overview, Components, Usage, References)
      - Clarity: Analyze prose structure and readability
    - Score each dimension 1-5, generate findings for scores ≤2
    - _Requirements: 2.1, 2.2, 2.3, 2.6_

  - [ ] 4.3 Review concept pages (wiki/concepts/)
    - For each concept page, apply quality checklist:
      - Accuracy: Verify claims against source documents, check mathematical notation
      - Completeness: Check for required sections (Definition, Mechanism, Implications, Related Concepts)
      - Clarity: Analyze prose structure, jargon usage, formatting
    - Score each dimension 1-5, generate findings for scores ≤2
    - Identify stub pages (status: stub) requiring expansion
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.6_

  - [ ] 4.4 Review index pages (wiki/_indexes/)
    - Verify each index accurately lists all pages in its category
    - Check for missing entries or outdated information
    - Generate findings for index drift issues
    - _Requirements: 5.6_

- [ ] 5. Checkpoint - Phase 2 complete
  - Ensure all page-level findings are documented
  - Ask the user if questions arise before proceeding to Phase 3

- [ ] 6. Phase 3 - Cross-page coherence analysis
  - [ ] 6.1 Build and validate link graph
    - Extract all wikilinks from each page using pattern: `\[[^\]]+\]\([^)]+\.md\)`
    - Verify each link target exists - flag broken links as correctness-error (severity: high)
    - _Requirements: 5.1_

  - [ ] 6.2 Verify backlinks accuracy
    - For each page, compare frontmatter `backlinks` field against actual inbound links found
    - Flag discrepancies as coherence-gap findings (severity: medium)
    - _Requirements: 5.4_

  - [ ] 6.3 Scan for contradictions between related pages
    - Identify page pairs that share tags or cross-reference each other
    - Extract key claims (definitions, rules, theorems) from each page
    - Compare claims for logical consistency
    - Flag potential contradictions for human review as correctness-error (severity: high)
    - Note: Contradiction detection is heuristic and requires human judgment
    - _Requirements: 5.3_

  - [ ] 6.4 Identify concept clusters with weak interconnection
    - Analyze tag-based clusters for link density
    - Flag clusters with low internal linkage as coherence-gap (severity: low)
    - _Requirements: 5.5_

  - [ ] 6.5 Map pages to Canonical taxonomy
    - Map each concept page to one of 6 Canonical categories (Theory, Blocks, Diagnosis, Playbook, Measurement, Reference)
    - Identify pages spanning multiple categories without clear primary classification
    - Verify Block pages (10-block-V through 14-block-L) are properly tagged and cross-referenced
    - Verify diagnostic content follows fix-order sequence
    - Identify gaps in taxonomy coverage
    - Generate taxonomy-misalignment findings as needed
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [ ] 7. Checkpoint - Phase 3 complete
  - Ensure all coherence findings are documented
  - Ask the user if questions arise before proceeding to Phase 4

- [ ] 8. Phase 4 - V2.1 framework compliance check
  - [ ] 8.1 Scan for legacy V1 terminology
    - Search for legacy terms: "linear boundary", generic "execution metrics", "team health", generic "alignment"
    - Identify V2.1 equivalents: "Macro-Gate" or specific block reference, disambiguated E-block metrics, P-block vectors, V-block/A-block specificity
    - Generate framework-violation findings for legacy terminology (severity: high for canonical pages, medium otherwise)
    - _Requirements: 4.1, 4.6_

  - [ ] 8.2 Check Macro-Gate disambiguation
    - Verify execution-related content properly distinguishes Macro-Gates (V, P, A) from Micro-Execution (E)
    - Check that pages discussing "execution problems" reference the diagnostic sequence
    - Generate framework-violation findings for improper disambiguation (severity: medium)
    - _Requirements: 4.2_

  - [ ] 8.3 Validate multi-dimensional vector usage
    - Check that multi-dimensional vectors are used where applicable
    - Generate framework-violation findings for missing vector decomposition (severity: medium)
    - _Requirements: 4.3_

  - [ ] 8.4 Check Nyquist time constraint references
    - Verify intervention guidance includes Nyquist time constraint references where applicable
    - Generate framework-violation findings for missing time constraints (severity: medium)
    - _Requirements: 4.4_

  - [ ] 8.5 Validate canonical references
    - Verify core concepts reference canonical V2.1 source (6-canonical-v2-1.md)
    - Verify Block pages reference Master Equation (02-master-equation.md)
    - Verify diagnostic content references Diagnostic Sequence (20-diagnostic-sequence.md)
    - Check for missing v2.1-canonical or v2-framework tags where appropriate
    - Generate framework-violation findings for missing canonical references (severity: medium)
    - _Requirements: 4.5_

- [ ] 9. Checkpoint - Phase 4 complete
  - Ensure all V2.1 compliance findings are documented
  - Ask the user if questions arise before generating output

- [ ] 10. Generate output artifacts
  - [ ] 10.1 Generate findings report
    - Create report organized by severity (critical, high, medium, low)
    - Include aggregate statistics: total pages reviewed, findings by category, findings by severity
    - Identify pages requiring immediate attention due to critical findings
    - _Requirements: 9.1, 9.5, 9.6, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_

  - [ ] 10.2 Create remediation plan
    - Produce prioritized action list sorted by severity and impact
    - Identify quick wins (low-effort, high-impact fixes)
    - Organize by timeframe: Immediate (Critical), This Session (High), Next Session (Medium), Backlog (Low)
    - _Requirements: 9.2, 9.3_

  - [ ] 10.3 Log review session
    - Append entry to wiki/log/YYYY-MM.md following schema format
    - Include session ID, scope, finding counts, tools used, key issues summary
    - _Requirements: 9.4_

- [ ] 11. Final checkpoint - Review complete
  - Present summary to user
  - Ensure all findings are documented with actionable recommendations
  - Ask the user if questions arise

## Notes

- This is a manual review process executed by the LLM, not a software implementation
- Each finding includes: page path, finding type, severity, description, evidence, and recommendation
- Finding types: quality-issue, correctness-error, framework-violation, coherence-gap, taxonomy-misalignment
- Severity levels: critical (immediate), high (this session), medium (next session), low (backlog)
- Checkpoints allow for human review and questions between phases
- All findings reference specific requirements for traceability