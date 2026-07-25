# Phase 11R Phase Doc Update Plan

This plan describes how to repair the Phase 1 through Phase 11 documentation chain before Phase 12.

## Update strategy

`HYBRID_APPEND_PLUS_SUPPLEMENT`

This is the safest option because:

- the existing phase docs are already coherent
- the missing pieces are mostly canon depth, style depth, animation depth, and anti-collision clarity
- append-only repairs preserve the audit lineage
- supplement docs let us add depth without rewriting the full chain

## Required update packages

| Package | Purpose | Docs affected | New docs needed? | Risk | Acceptance gate | Commit strategy |
|---|---|---|---|---|---|---|
| Package A — Platform/Cinema Separation Cleanup | Clarify what remains downstream and prevent content laws from leaking into film-core | Phase 1, 2, 5, 6, 8, 9, 11 docs | Maybe | Medium | No content hook law should be treated as film canon | Append-only clarification notes |
| Package B — Filmcraft Canon Injection | Add screenwriting, directing, cinematography, editing, sound, and production canon depth | Phase 1, 6, 8, 9, 11 docs | Yes | High | Canon areas are expressed with enough depth to support implementation | Supplement docs first, then appendix references |
| Package C — Animation Canon Injection | Add Disney principles, animation styles, motion language, and animation continuity law | Phase 4, 5, 9, 11 docs | Yes | High | Animation-specific law exists, not just generic visual language | New supplement docs |
| Package D — Style / Palette / Template System | Add visual style bible, palette law, genre templates, and anti-drift rules | Phase 1, 4, 6, 9, 11 docs | Yes | High | Style templates are explicit and reusable | New supplement docs |
| Package E — Real Incident / Docudrama Ethics | Add source ledger, fact-vs-anecdote law, and source-vs-render separation | Phase 6, 8, 9, 11 docs | Yes | High | Real incident handling is explicit and non-hallucinated | New supplement docs |
| Package F — Phase 12 Readiness Gate | Define the final doc gate before implementation patches begin | Phase 11 docs | Yes | High | Readiness gate is explicit and evidence-backed | New gate doc + checklist |

## Proposed new supplement docs

These are the highest-value follow-up docs to create before implementation begins:

- `FILMCRAFT_CANON_SOURCE_LEDGER.md`
- `CINEMA_STYLE_BIBLE_REQUIREMENTS.md`
- `ANIMATION_CANON_REQUIREMENTS.md`
- `FILM_ROUTE_PLATFORM_SEPARATION_LAW.md`
- `FILM_OUTPUT_STYLE_PALETTE_SCHEMA_REQUIREMENTS.md`
- `REAL_INCIDENT_DOCUDRAMA_ETHICS_REQUIREMENTS.md`
- `PHASE_12_READINESS_GATE.md`

## What each supplement should add

### FILMCRAFT_CANON_SOURCE_LEDGER.md

- list of canon families
- source references or owner-supplied canon references
- which canon areas are required versus optional
- which canon areas need external validation

### CINEMA_STYLE_BIBLE_REQUIREMENTS.md

- genre templates
- visual DNA
- camera grammar
- lens grammar
- palette law
- lighting law
- aspect-ratio / framing rules
- continuity rules

### ANIMATION_CANON_REQUIREMENTS.md

- Disney 12 principles
- 2D / 3D / anime / stop-motion / motion graphics / hybrid families
- motion continuity
- frame economy
- animation timing charts
- style bible for animated output

### FILM_ROUTE_PLATFORM_SEPARATION_LAW.md

- explicit downstream-only law for YouTube / Shorts / TikTok / Instagram / creator metrics
- anti-collision rules so content laws do not become cinema law
- route split enforcement language

### FILM_OUTPUT_STYLE_PALETTE_SCHEMA_REQUIREMENTS.md

- style fields
- palette fields
- lighting fields
- camera and lens fields
- template fields
- continuity fields

### REAL_INCIDENT_DOCUDRAMA_ETHICS_REQUIREMENTS.md

- source-vs-render separation
- real-person / real-incident handling
- composite-character rules
- fact vs dramatization law

### PHASE_12_READINESS_GATE.md

- what must be repaired first
- what must be present before implementation starts
- what conditions block Phase 12

## Phase 12 go / no-go

`PHASE_12_BLOCKED_PENDING_DOC_REPAIR`

Phase 12 should not begin yet.
The current phase docs are structurally coherent, but they still need canon injection, style depth, and explicit anti-collision supplements before implementation can safely start.

