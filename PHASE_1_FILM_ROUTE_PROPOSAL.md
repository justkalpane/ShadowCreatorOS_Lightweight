# Phase 1 Film Route Proposal

## Proposed Route ID

```text
FILM_SCREENPLAY_GENERATION
```

## Trigger Terms

This route should be selected for:

```text
short film
screenplay
film script
cinematic script
feature film
shooting script
scene script
director's script
narrative film
cinematic screenplay
dramatic short
character-driven film
```

## Route Purpose

`FILM_SCREENPLAY_GENERATION` should generate cinema-first screenplay outputs, not YouTube/content scripts.

It should treat the screenplay as the core artifact and should optimize for:

- dramatic structure
- character transformation
- scene turns
- cinematic image logic
- sound and performance intent
- production-readiness

The route should **not** inherit creator-platform defaults as its top-level framing.

## Required Output Packet

The film route should eventually produce a packet containing:

- logline
- theme
- premise
- genre
- tone
- cinematic world
- protagonist want
- protagonist need
- flaw
- arc
- antagonist or opposing force
- character web
- Save the Cat beat sheet
- three-act map
- eight-sequence map
- scene list
- scene objective
- scene conflict
- scene turn
- subtext layer
- dialogue pass
- visual motif system
- sound motif system
- mise-en-scène notes
- blocking
- camera language
- editing rhythm
- performance direction
- final screenplay
- director’s notes
- production notes
- validation scorecard

## Relationship to Existing Routes

### `SCRIPT_GENERATION`

`SCRIPT_GENERATION` should remain the route for:

- YouTube scripts
- Shorts scripts
- reels scripts
- voiceover scripts
- creator videos
- explainer videos
- social video scripts
- retention-optimized platform content

### `FILM_SCREENPLAY_GENERATION`

`FILM_SCREENPLAY_GENERATION` should become the default route for:

- cinematic prompts
- short films
- screenplay requests
- feature-film development
- dramatic film writing
- scene-driven film output

### Downstream routes

These should remain downstream adaptation / finishing / release layers:

- `VISUAL_MEDIA_PLAN`
- `VOICE_CONTEXT`
- `EDITING_PACKAGING`
- `MEDIA_FACTORY_HANDOFF`
- `FULL_VIDEO_PIPELINE`

The current downstream stack is useful and should be preserved. The key change is that it must stop acting as the authority over screenplay generation itself.

## Future Contracts

These contracts are proposed for later phases, but should not be created in Phase 1 unless explicitly approved:

- `FILM_SCREENPLAY_STRUCTURE_CONTRACT.md`
- `SAVE_THE_CAT_BEAT_SHEET_CONTRACT.md`
- `CHARACTER_ARC_AND_DESIRE_CONTRACT.md`
- `SCENE_DRAMATURGY_CONTRACT.md`
- `DIALOGUE_SUBTEXT_CONTRACT.md`
- `CINEMATIC_COMPOSITION_CONTRACT.md`
- `DIRECTORIAL_STYLE_CONTRACT.md`
- `VISUAL_MOTIF_AND_IMAGE_SYSTEM_CONTRACT.md`
- `PERFORMANCE_DIRECTION_CONTRACT.md`
- `SHORT_FILM_VALIDATION_CONTRACT.md`

## Future Validators

These validators are proposed for later phases:

- `validate_film_screenplay_output.py`
- `validate_save_the_cat_beat_sheet.py`
- `validate_character_arc_map.py`
- `validate_scene_turns.py`
- `validate_dialogue_subtext.py`
- `validate_visual_motif_system.py`
- `validate_directorial_composition_packet.py`
- `validate_short_film_packet.py`

## Phase 1 Implementation Boundary

This proposal is intentionally narrow.

Phase 1 should only:

- declare the new route family
- define the trigger vocabulary
- define the film packet shape
- preserve current YouTube/content behavior
- preserve downstream distribution behavior

Phase 1 should **not**:

- rewrite `SCRIPT_GENERATION`
- delete platform routing
- patch all directors
- patch all agents
- patch all skills
- patch all validators
- patch all schemas
- claim runtime proof
- claim completion

## Design Principle

The correct architecture is:

**Core Film Engine**

- story development
- character design
- screenplay structure
- scene dramaturgy
- cinematic composition
- directorial style
- production packet

then:

**Downstream Distribution Engine**

- trailers
- teasers
- YouTube cutdowns
- Instagram reels
- TikTok clips
- platform packaging
- metadata
- analytics

This keeps the film brain clean while still preserving the creator/content stack as a valid downstream layer.

## Phase 11U Canon/Style Supplement Linkage Addendum

This is a later linkage update and does not rewrite the original Phase 1 finding.
The future film route must now explicitly obey:

- `FILMCRAFT_CANON_SOURCE_LEDGER.md`
- `CINEMA_STYLE_BIBLE_REQUIREMENTS.md`
- `ANIMATION_CANON_REQUIREMENTS.md`
- `FILM_ROUTE_PLATFORM_SEPARATION_LAW.md`
- `FILM_OUTPUT_STYLE_PALETTE_SCHEMA_REQUIREMENTS.md`
- `REAL_INCIDENT_DOCUDRAMA_ETHICS_REQUIREMENTS.md`
- `PHASE_12_READINESS_GATE.md`

`SCRIPT_GENERATION` remains preserved for content/platform scripts.
`FILM_SCREENPLAY_GENERATION` must still be added in parallel later.
Platform/content logic remains downstream or content-only, not film-core law.
Hook, retention, and recurring-rehook rules remain content-route requirements and must not become film-core PASS criteria.
Phase 12 remains blocked until the supplement layer is reviewed and the smallest safe patch slice is approved.
