# Requirements Document

## Introduction

The LLM Wiki System is a pattern for building personal knowledge bases where an LLM incrementally builds and maintains a persistent wiki of structured, interlinked markdown files. Unlike RAG-style retrieval systems that query raw documents at runtime, this system creates a compounding knowledge artifact that becomes richer with every source added. The LLM acts as a knowledge curator, reading sources, extracting information, and integrating it into an evolving wiki structure that can be viewed in tools like Obsidian.

## Glossary

- **Wiki**: The collection of LLM-generated markdown files representing structured knowledge
- **Source**: An immutable input document (article, paper, image, data file) to be processed
- **Entity_Page**: A wiki page describing a specific person, place, organization, or thing
- **Concept_Page**: A wiki page explaining an idea, theory, or abstract concept
- **Index**: A content-oriented catalog file (index.md) listing all wiki pages with links and summaries
- **Log**: A chronological append-only record file (log.md) of all operations performed on the wiki
- **Schema**: A configuration document (CLAUDE.md or AGENTS.md) defining wiki structure and workflows
- **Ingest_Operation**: The process of adding a new source to the wiki
- **Query_Operation**: The process of answering questions using the wiki
- **Lint_Operation**: The process of checking wiki health for issues
- **Wiki_System**: The complete system managing the three-layer architecture

## Requirements

### Requirement 1: Three-Layer Architecture

**User Story:** As a knowledge worker, I want a clear separation between raw sources, curated knowledge, and system configuration, so that I can maintain a clean and organized knowledge base.

#### Acceptance Criteria

1. THE Wiki_System SHALL maintain three distinct layers: raw sources, wiki pages, and schema configuration
2. THE Wiki_System SHALL treat all sources as immutable after ingestion
3. THE Wiki_System SHALL store wiki pages as markdown files with wikilink-style cross-references
4. THE Wiki_System SHALL store the schema as a configuration document readable by the LLM

### Requirement 2: Ingest Sources

**User Story:** As a user, I want to add new sources to my wiki, so that the LLM can extract and integrate knowledge into my existing knowledge base.

#### Acceptance Criteria

1. WHEN a user provides a new source, THE Wiki_System SHALL read and analyze the source content
2. WHEN processing a source, THE Wiki_System SHALL identify entities, concepts, and key information to extract
3. WHEN relevant wiki pages exist, THE Wiki_System SHALL update them with new information from the source
4. WHEN no relevant wiki page exists, THE Wiki_System SHALL create new pages as needed
5. WHEN information conflicts with existing wiki content, THE Wiki_System SHALL note the contradiction on the relevant page
6. WHEN completing an ingest operation, THE Wiki_System SHALL update the Index with any new or modified pages
7. WHEN completing an ingest operation, THE Wiki_System SHALL append an entry to the Log documenting the operation

### Requirement 3: Maintain Index

**User Story:** As a user, I want a comprehensive catalog of all wiki pages, so that I can discover and navigate my knowledge base.

#### Acceptance Criteria

1. THE Wiki_System SHALL maintain an index.md file listing all wiki pages
2. FOR EACH wiki page, THE Index SHALL include a wikilink and a brief summary
3. WHEN a new page is created, THE Wiki_System SHALL add it to the Index
4. WHEN a page is modified, THE Wiki_System SHALL update its summary in the Index
5. THE Wiki_System SHALL organize the Index in a content-oriented manner for easy browsing

### Requirement 4: Maintain Operation Log

**User Story:** As a user, I want a chronological record of all operations, so that I can track how my wiki evolved over time.

#### Acceptance Criteria

1. THE Wiki_System SHALL maintain a log.md file as an append-only record
2. WHEN any operation completes, THE Wiki_System SHALL append an entry to the Log
3. FOR EACH log entry, THE Wiki_System SHALL include a timestamp, operation type, and summary of changes
4. THE Wiki_System SHALL preserve all log entries without modification or deletion

### Requirement 5: Query Wiki

**User Story:** As a user, I want to ask questions about my knowledge base, so that I can retrieve synthesized information without reading raw sources.

#### Acceptance Criteria

1. WHEN a user asks a question, THE Wiki_System SHALL search relevant wiki pages to formulate an answer
2. WHEN answering a question, THE Wiki_System SHALL cite specific wiki pages as sources
3. WHEN a query produces a high-quality answer, THE Wiki_System SHALL offer to save it as a new wiki page
4. WHEN the user accepts, THE Wiki_System SHALL create the new page and update the Index and Log

### Requirement 6: Lint Wiki Health

**User Story:** As a user, I want to check my wiki for quality issues, so that I can maintain a coherent and reliable knowledge base.

#### Acceptance Criteria

1. WHEN a user requests a lint operation, THE Wiki_System SHALL scan all wiki pages for issues
2. THE Wiki_System SHALL identify contradictions between different pages
3. THE Wiki_System SHALL identify stale claims that may need updating
4. THE Wiki_System SHALL identify orphan pages with no incoming links
5. THE Wiki_System SHALL identify missing cross-references between related pages
6. WHEN lint issues are found, THE Wiki_System SHALL report them to the user with specific page references

### Requirement 7: Cross-Reference Pages

**User Story:** As a user, I want wiki pages to link to related pages, so that I can navigate between connected concepts and entities.

#### Acceptance Criteria

1. WHEN creating or updating a page, THE Wiki_System SHALL identify related pages in the wiki
2. WHEN related pages exist, THE Wiki_System SHALL add wikilink-style cross-references
3. THE Wiki_System SHALL use the format [[Page Name]] for cross-references
4. THE Wiki_System SHALL ensure cross-references are bidirectional where semantically appropriate

### Requirement 8: Handle Contradictions

**User Story:** As a user, I want to see when sources disagree, so that I can evaluate conflicting information and make informed judgments.

#### Acceptance Criteria

1. WHEN a new source contradicts existing wiki content, THE Wiki_System SHALL preserve both perspectives
2. WHEN noting a contradiction, THE Wiki_System SHALL document which sources support each perspective
3. THE Wiki_System SHALL mark contradictions clearly on the relevant wiki page
4. THE Wiki_System SHALL avoid silently overwriting existing information with contradictory claims

### Requirement 9: Support Multiple Page Types

**User Story:** As a user, I want different types of wiki pages for different kinds of knowledge, so that information is organized appropriately.

#### Acceptance Criteria

1. THE Wiki_System SHALL support Entity_Page creation for people, places, organizations, and things
2. THE Wiki_System SHALL support Concept_Page creation for ideas, theories, and abstract concepts
3. THE Wiki_System SHALL support summary pages for individual sources
4. THE Wiki_System SHALL support comparison pages analyzing multiple related entities or concepts
5. THE Wiki_System SHALL support overview pages synthesizing information across multiple pages

### Requirement 10: Obsidian Compatibility

**User Story:** As a user, I want to view my wiki in Obsidian, so that I can leverage its graph view, search, and navigation features.

#### Acceptance Criteria

1. THE Wiki_System SHALL generate markdown files compatible with Obsidian syntax
2. THE Wiki_System SHALL use wikilink format [[Page Name]] for all internal links
3. THE Wiki_System SHALL organize files in a directory structure navigable by Obsidian
4. WHEN the user edits files in Obsidian, THE Wiki_System SHALL respect the existing structure and content

### Requirement 11: Schema Configuration

**User Story:** As a user, I want to configure how the wiki is structured, so that I can customize it for different use cases like research, book notes, or competitive analysis.

#### Acceptance Criteria

1. THE Wiki_System SHALL read a schema configuration file (CLAUDE.md or AGENTS.md)
2. THE Schema SHALL define the wiki structure including page types and organization
3. THE Schema SHALL define workflows for ingest, query, and lint operations
4. WHEN processing operations, THE Wiki_System SHALL follow the workflows defined in the Schema
5. THE Wiki_System SHALL allow users to modify the Schema to customize behavior

### Requirement 12: Incremental Knowledge Building

**User Story:** As a user, I want my wiki to become richer with each source I add, so that I build a compounding knowledge asset over time.

#### Acceptance Criteria

1. WHEN ingesting a source, THE Wiki_System SHALL integrate new information with existing pages rather than creating duplicates
2. WHEN a concept appears in multiple sources, THE Wiki_System SHALL strengthen the synthesis on the relevant page
3. WHEN new details emerge about an entity, THE Wiki_System SHALL enrich the Entity_Page with additional information
4. THE Wiki_System SHALL preserve the history of how pages evolved through the Log
