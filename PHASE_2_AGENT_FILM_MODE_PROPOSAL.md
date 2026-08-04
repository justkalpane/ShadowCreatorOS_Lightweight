# Phase 2 Agent Film Mode Proposal

## Proposed Film-Mode Agent Stack

The cinema-first agent stack should eventually look like this:

- `film_story_architect_agent`
- `screenplay_structure_agent`
- `character_arc_agent`
- `scene_dramaturgy_agent`
- `dialogue_subtext_agent`
- `visual_motif_agent`
- `cinematic_composition_agent`
- `director_style_agent`
- `performance_direction_agent`
- `production_feasibility_agent`
- `film_continuity_agent`
- `film_validation_agent`
- `release_adaptation_agent`

These names are proposals, not implemented components in this phase.

## Reuse Map

| Existing agent | Reuse as-is | Reuse with film mode | Duplicate for film mode | Move downstream | Do not use in film core | Notes |
|---|---|---|---|---|---|---|
| Krishna | No | No | Yes | No | No | Needs a new film-route arbiter sibling or a route-separated role. |
| Narada | No | No | No | Yes | No | Keep as downstream trend/distribution intelligence. |
| Saraswati | Yes | Yes | No | No | No | Good downstream and refinement support; may gain film release-adaptation sibling. |
| Garuda | Yes | Yes | No | No | No | Keep as downstream release dispatcher. |
| Chanakya | No | Yes | No | No | No | Convert to film opportunity fit / story-market fit. |
| Shakti | No | Yes | No | No | No | Convert to emotional-force / dramatic-pressure support. |
| Kama | No | No | No | Yes | No | Keep in attention/retention or trailer/packaging lanes. |
| Durga | Yes | Yes | No | No | No | Governance stays reusable. |
| Ganesha | Maybe | Maybe | Maybe | No | Maybe | Needs a design decision before film-core reuse. |
| Yama | Yes | Yes | No | No | No | Governance and release compliance stay reusable. |
| Arjuna | No | Yes | No | No | No | Convert to production feasibility and scene-readiness support. |
| Maya | Yes | Yes | No | No | No | Strong candidate for visual language support in film mode. |
| Nataraja | No | Yes | No | No | No | Convert to scene/cut rhythm and pacing. |
| Tumburu | Yes | Yes | No | No | No | Sound motif and performance texture support. |
| Vishwakarma | Yes | Yes | No | No | No | Production backbone remains useful. |
| Vishnu | No | Yes | Yes | No | No | Duplicate as film continuity sync and preserve current sync role. |
| Indra | Yes | Yes | No | No | No | Premium finish and release readiness. |
| Hanuman | Yes | Maybe | No | No | No | Keep as fast-track support; not a creative core owner. |
| Agastya | Yes | Yes | No | No | No | Reusable for source-safe research briefs. |
| Chandra | No | Maybe | No | Yes | No | Better as downstream audience intelligence than screenplay authority. |
| Brahma | Yes | Yes | No | No | No | Governance coordinator remains valuable. |
| Kubera | Yes | Yes | No | No | No | Budget gate remains useful. |
| Chitragupta | Yes | Yes | No | No | No | Audit/lineage support is valuable for film development. |
| Parashara | No | Yes | No | No | No | Convert to film pattern/thematic analysis. |

## Old-to-New Responsibility Map

| Existing agent responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| Top-level script arbitration | `SCRIPT_GENERATION` and hook enforcement | Film screenplay route arbitration | Yes, for content routes | Krishna should not remain the only top-level owner for all script work. |
| Trend and distribution analysis | Platform/trend-first | Film research signals and market signals | Yes | Narada should stop steering core screenplay choice. |
| Hook density / retention gating | Content retention | Dramatic tension / scene hook / trailer hook support | Yes | Keep as downstream content support. |
| Creator/platform fit scoring | Creator/content growth logic | Film-market / story-market fit | Yes | Chanakya needs new wording. |
| Amplification / virality logic | Engagement growth | Dramatic force / emotional pressure | Yes | Shakti is useful but mis-scoped for cinema. |
| Production scoring | Hook/retention/platform score fields | Scene readiness / shoot readiness / film feasibility | Yes | Arjuna should be retargeted. |
| Pacing and editing | Creator-style pacing | Scene rhythm / cut rhythm / editorial motion | Yes | Nataraja is a strong film candidate once retargeted. |
| Distribution packaging | Channel-first repurposing | Film release adaptation / trailer packaging | Yes | Saraswati and Garuda stay useful downstream. |
| Governance and policy | Boundary enforcement | Same, but film-policy aware | Yes | Durga and Yama are reusable. |
| Audio and voice direction | Voiceover/content emphasis | Cinematic sound motif and performance texture | Yes | Tumburu is reusable with only language retargeting. |
| Visual production | Storyboard/content support | Film visual language and cinematography support | Yes | Maya is already close. |
| Audit and lineage | Content provenance | Film provenance and screenplay lineage | Yes | Chitragupta is highly reusable. |

## Future Patch Plan

Phase 3 should inspect subagents next, because subagents are where the agent-level route split becomes operational.

Phase 3 should verify:

- which subagents are hard-wired to `script_generation`
- which subagents already support refinement, packaging, or distribution
- which subagents can be reused for film scene packets
- which subagents need a film-mode sibling
- which subagents should remain downstream only

That next pass should also check whether subagents already carry hook, retention, pace, and packaging logic that needs to be kept out of film-core screenplay generation.

## Phase 2 Boundary

This proposal is intentionally not implementation. It defines the target agent architecture so the next patch phase can be clean and reviewable.

## Phase 11U Canon/Style Supplement Linkage Addendum

This is a later linkage update and does not rewrite the original Phase 2 finding.
Future agent film mode must now consult the supplement pack before any implementation:

- `FILMCRAFT_CANON_SOURCE_LEDGER.md`
- `CINEMA_STYLE_BIBLE_REQUIREMENTS.md`
- `ANIMATION_CANON_REQUIREMENTS.md`
- `FILM_ROUTE_PLATFORM_SEPARATION_LAW.md`
- `REAL_INCIDENT_DOCUDRAMA_ETHICS_REQUIREMENTS.md`

Agent film mode must keep `SCRIPT_GENERATION` preserved, add `FILM_SCREENPLAY_GENERATION` in parallel later, and keep platform/content logic downstream or content-only.
Agent decisions must not treat hook, retention, or creator-fit logic as film-core PASS law.
Phase 12 remains blocked until the supplement layer is reviewed.
