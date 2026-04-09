# Wiki to Text Export - 5 Book Structure

## Overview
This directory contains all wiki markdown files exported as `.txt` files, organized into 5 book folders representing the logical structure for publishing.

## Export Summary
- **Total files mapped:** 83
- **Successfully exported:** 67
- **Missing files:** 16 (files that were in the original mapping but don't exist in wiki)

## Book Structure

### Book 1: Foundations (19 files)
**Focus:** Theory, mathematics, physics, and foundational concepts

Files include:
- Model identity and master equation
- V2.1 canonical architecture
- Time constants and theorems
- Order parameter, hysteresis, self-organized criticality
- Queuing theory (Little's Law, utilization curve)
- Measurement theory and falsifiability
- Digital twin and discrete-event simulation
- Literature map

### Book 2: Diagnostics (11 files)
**Focus:** Practical diagnosis and intervention

Files include:
- Diagnostic sequence (20-step process)
- Zero-override protocol
- Table 2 diagnostics
- Structure-vs-development rule
- Lever-access rule
- Metrics by block
- Anti-patterns
- Practitioner's checklist
- Ethical measurement

### Book 3: Team States (16 files)
**Focus:** States, dynamics, and loops

Files include:
- P1-P6 team states (Crisis → Thriving → Scaling → Mixed)
- V2 extended states
- Losing loop and winning loop
- Four cross-layer dynamics:
  - Incentive death spiral
  - Fear amplification loop
  - Sustainability drain loop
  - Strategic drift loop
- Hero culture trap and rushing trap
- Cynical equilibrium

### Book 4: Five Blocks (8 files)
**Focus:** Deep dives into V, P, E, A, L blocks

Files include:
- Block V (Value Alignment)
- Block P (People System)
- Block E (Execution System)
- Block A (Org Alignment)
- Block L (Learning & Adaptation)
- Feedback speed
- Conway's Law
- Resource allocation game

**Note:** Many legacy block detail files (clarity, focus, skill, coordination, quality, etc.) were not found in the wiki. The canonical block files (10-14) contain the comprehensive information.

### Book 5: Scaling (13 files)
**Focus:** Scaling, cross-domain applications, and research

Files include:
- Fractal scaling
- Multi-scale dynamics
- Cross-domain extensions
- Open research questions
- Source summaries (diagram sets 1-4, extended framework)
- Operations log
- All index files

## File Naming Convention
Files are named using the pattern: `[directory]__[filename].txt`

Examples:
- `concepts/00-model-identity.md` → `concepts__00-model-identity.txt`
- `_indexes/root.md` → `_indexes__root.txt`
- `sources/6-canonical-v2-1.md` → `sources__6-canonical-v2-1.txt`

## Missing Files (16)
The following files were in the original book mapping but don't exist in the wiki:

**Book 1:**
- concepts/v2-theorems.md
- concepts/nyquist-constraint.md

**Book 2:**
- concepts/fix-order.md
- concepts/zero-override-rule.md
- concepts/metrics-framework.md
- concepts/anti-patterns.md

**Book 4:**
- concepts/value-alignment.md
- concepts/people-system.md
- concepts/execution-system.md
- concepts/clarity.md
- concepts/focus.md
- concepts/skill.md
- concepts/coordination.md
- concepts/quality.md
- concepts/org-alignment.md
- concepts/learning-adaptation.md

**Note:** Most missing files are legacy versions that have been superseded by canonical numbered files (e.g., `10-block-V.md` replaces `value-alignment.md`).

## How to Use

### Re-run Export
To re-export all files:
```bash
cd C:\Users\hi\Desktop\SystemsEM\text_export
python export_wiki_to_books.py
```

### Verify Export
Check the summary output for:
- Number of files exported per book
- Any missing or failed files
- Total export statistics

## Directory Structure
```
text_export/
├── Book1_Foundations/       (19 .txt files)
├── Book2_Diagnostics/       (11 .txt files)
├── Book3_TeamStates/        (16 .txt files)
├── Book4_FiveBlocks/        (8 .txt files)
├── Book5_Scaling/           (13 .txt files)
├── export_wiki_to_books.py  (export script)
└── README.md                (this file)
```

## Next Steps for Publishing

1. **Review Content:** Read through each book folder to ensure logical flow
2. **Add Transitions:** Create chapter introductions and transitions between files
3. **Consolidate:** Merge related files where appropriate
4. **Add Examples:** Supplement with real-world case studies
5. **Create Appendices:** Add glossary, index, and reference materials
6. **Format:** Convert to publishing format (LaTeX, Word, etc.)

## Notes
- All files retain their original markdown formatting
- Cross-references between files are preserved
- Frontmatter metadata is included in each file
- Mermaid diagrams are included as code blocks
