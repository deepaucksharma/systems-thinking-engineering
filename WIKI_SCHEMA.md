# Wiki Schema — Engineering Management Systems

This file governs how the LLM maintains, expands, and queries this wiki. All operations (Ingest, Query, Lint) must follow these conventions.

## Domain

**Canonical V2.1 Engineering Management Control Theory** — a sociotechnical systems-thinking framework for managing software engineering teams. Built on:
- A Multiplicative 5-Block Master Equation ($V \cdot P \cdot E \cdot A \cdot L$)
- Causal loop dynamics (e.g., Fear Amplification, Sustainability Drain)
- Diagnostic decision trees resolving Macro-Gates ($V, P, A$) before Micro-Execution ($E$)
- Queuing physics constraints (Batch Size, Tail Risk / Obesity Index)
- Cognitive Load decomposition and Cynefin framework domain awareness

---

## Directory Structure

```
SystemsEM/
├── raw/                    # Immutable source documents (the LLM never modifies these)
├── wiki/
│   ├── _indexes/           # Hierarchical index files (LLM-maintained)
│   │   ├── root.md         # Master index — links to category indexes
│   │   ├── entities.md     # Index of all entity pages
│   │   ├── concepts.md     # Index of all concept pages
│   │   ├── sources.md      # Index of all source summaries
│   │   └── syntheses.md    # Index of all synthesis/analysis pages
│   ├── entities/           # Pages for specific named things (people, teams, tools, models)
│   ├── concepts/           # Pages for abstract ideas, principles, patterns
│   ├── sources/            # One summary page per ingested source document
│   ├── syntheses/          # Cross-cutting analyses, comparisons, query results filed back
│   └── log/                # Partitioned operation logs
│       └── YYYY-MM.md      # One log file per month
├── tools/                  # CLI helper scripts for search, lint, metadata queries
├── WIKI_SCHEMA.md          # This file
└── .kiro/                  # IDE configuration (do not modify)

---

## The Definitive Editorial Architecture

When drafting new pages in `wiki/concepts/` or `wiki/entities/`, map them conceptually into the following 6-part Canonical taxonomy (ensuring progressive disclosure through tags and links):
1. **Theory**: Fundamental rules, master equations, causal dynamics (Losing/Winning loops), state machines, time constants.
2. **Blocks**: Deep-dives into the $V$, $P$, $E$, $A$, and $L$ blocks and their sub-variables.
3. **Diagnosis**: Symptom maps, zero-override protocols, domain calibration (Cynefin), and cognitive load decomposition.
4. **Playbook**: Intervention rules, Lever-Access constraints, J-curve anticipation, and mixed-state handling.
5. **Measurement**: Telemetry design, leading vs lagging indicators, SPACE frameworks, and managing distorted data.
6. **Reference**: Formal theorems, executive anti-patterns, glossary, and open falsifiability conditions.
```

---

## Page Conventions

### YAML Frontmatter (required on every wiki page)

Every `.md` file in `wiki/` **must** have YAML frontmatter with the following fields:

```yaml
---
title: "Page Title"
type: entity | concept | source | synthesis
tags: [tag1, tag2, tag3]
sources: [raw/filename.md]          # Which raw sources contributed to this page
backlinks: [wiki/concepts/foo.md]   # Pages that link TO this page (maintained by LLM)
created: 2026-04-08
updated: 2026-04-08
status: active | stub | stale       # active = maintained, stub = needs expansion, stale = may be outdated
---
```

### Wikilinks

Use standard markdown relative links for cross-references:
- `[Clarity](../concepts/clarity.md)` — link to a concept page
- `[Master Equation](../entities/master-equation.md)` — link to an entity page

### Page Naming

- All lowercase, hyphens for spaces: `feedback-speed.md`, `causal-loop-diagram.md`
- No special characters except hyphens
- Filenames should be descriptive enough to identify content without opening the file

---

## Hierarchical Index System

The index system is designed to scale to 100K+ pages. Instead of one monolithic index, we use a tree:

### `_indexes/root.md`
The master index. Contains:
- Counts per category
- Links to each category index
- Quick-reference: recently updated pages, recently ingested sources

### `_indexes/{category}.md`
One index per page type (entities, concepts, sources, syntheses). Each entry:
```markdown
- [Page Title](../category/page-name.md) — one-line summary | tags: `tag1`, `tag2` | updated: YYYY-MM-DD
```

Sorted alphabetically within each index. When a category index exceeds ~500 entries, split into sub-indexes by first letter or by tag group.

---

## Operations

### 1. Ingest

Triggered when the user adds a new source to `raw/` and asks the LLM to process it.

**Steps:**
1. Read the source document completely.
2. Discuss key takeaways with the user (unless batch mode).
3. Create a **source summary page** in `wiki/sources/`.
4. For each entity mentioned: create or update its page in `wiki/entities/`.
5. For each concept discussed: create or update its page in `wiki/concepts/`.
6. Update all relevant **backlinks** in frontmatter of touched pages.
7. Update the relevant **category indexes** in `wiki/_indexes/`.
8. Append an entry to the current month's **log file** in `wiki/log/`.

**Log entry format:**
```markdown
## [YYYY-MM-DD HH:MM] ingest | Source Title
- Source: `raw/filename.md`
- Pages created: [list]
- Pages updated: [list]
- Key entities: [list]
- Key concepts: [list]
```

### 2. Query

Triggered when the user asks a question about the wiki contents.

**Steps:**
1. Read `wiki/_indexes/root.md` to orient.
2. Identify relevant category indexes and read them.
3. Read the most relevant wiki pages.
4. Synthesize an answer with citations `[Page Title](link)`.
5. If the answer is substantial and reusable, offer to file it as a new **synthesis page** in `wiki/syntheses/`.
6. Log the query in the current month's log.

**Log entry format:**
```markdown
## [YYYY-MM-DD HH:MM] query | Short Question Summary
- Question: "full question text"
- Pages consulted: [list]
- Filed as: wiki/syntheses/page-name.md (if applicable)
```

### 3. Lint

Triggered when the user asks for a health check, or periodically by the LLM.

**Checks:**
- **Orphan pages**: Pages with no inbound backlinks.
- **Stale pages**: Pages not updated in >30 days with newer sources available.
- **Missing pages**: Concepts or entities mentioned in links but with no corresponding page (broken links / red links).
- **Contradictions**: Claims on one page that conflict with claims on another.
- **V2.1 Compliance Drift**: Identify logic falling back to legacy V1 linear boundaries. (e.g., Execution analysis that fails to disambiguate Macro-Gates ($V, P, A$), ignores multi-dimensional Vectors, or violates Nyquist time constraints).
- **Frontmatter compliance**: Pages missing required frontmatter fields, or lacking context labels like `v2-framework`.
- **Index drift**: Pages that exist but are not listed in their category index.
- **Tag inconsistency**: Same concept tagged differently across pages.
- **Suggested expansions**: Stubs that could be expanded with available source material.

**Log entry format:**
```markdown
## [YYYY-MM-DD HH:MM] lint | Health Check
- Orphan pages: [count] — [list]
- Stale pages: [count] — [list]
- Missing pages: [count] — [list]
- Contradictions found: [count] — [details]
- Frontmatter issues: [count]
- Actions taken: [list of fixes applied]
- Recommendations: [list of suggested improvements]
```

---

## CLI Tools

Located in `tools/`. These are PowerShell scripts the LLM can invoke for efficient operations at scale.

### `tools/search.ps1`
Full-text search across all wiki pages. Usage:
```powershell
pwsh tools/search.ps1 -Query "feedback speed" [-Tags "concept"] [-Type "entity"]
```

### `tools/find-orphans.ps1`
Find pages with no inbound backlinks. Usage:
```powershell
pwsh tools/find-orphans.ps1
```

### `tools/find-stale.ps1`
Find pages not updated within N days. Usage:
```powershell
pwsh tools/find-stale.ps1 -Days 30
```

### `tools/validate-frontmatter.ps1`
Check all pages for frontmatter compliance. Usage:
```powershell
pwsh tools/validate-frontmatter.ps1
```

### `tools/stats.ps1`
Wiki statistics: page counts, tag distribution, link density. Usage:
```powershell
pwsh tools/stats.ps1
```

---

## Scaling Notes

- **Index sharding**: When any category index exceeds ~500 entries, split by first letter (`_indexes/concepts-a.md`, `_indexes/concepts-b.md`, etc.) or by tag group.
- **Log partitioning**: Logs are already partitioned by month. At very high volume, partition by week.
- **Search**: At small scale (<200 pages), `tools/search.ps1` with grep is sufficient. At larger scale, integrate `qmd` or a similar local search engine.
- **Batch ingest**: For bulk source ingestion, process sources sequentially but skip the interactive discussion step. Still create all pages and update all indexes.
- **Backlink maintenance**: When updating a page, always scan for new outbound links and update the target pages' `backlinks` frontmatter. The CLI tools can verify backlink consistency.
