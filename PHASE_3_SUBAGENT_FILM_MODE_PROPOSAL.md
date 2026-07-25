# Phase 3 Subagent Film Mode Proposal

## 1. Proposed film-mode subagent stack
The future cinema stack should be additive, not destructive. We should keep the current content subagents and create a film-first mirror set.

Proposed film-mode subagents:

- `film_research_brief_subagent`
- `story_premise_development_subagent`
- `screenplay_beat_sheet_subagent`
- `character_web_subagent`
- `scene_dramaturgy_subagent`
- `dialogue_subtext_subagent`
- `visual_motif_subagent`
- `cinematic_composition_subagent`
- `shot_design_subagent`
- `sound_motif_subagent`
- `performance_direction_subagent`
- `continuity_guard_subagent`
- `film_validation_subagent`
- `release_adaptation_subagent`

## 2. Reuse map

| Existing subagent family | Reuse as-is | Reuse with film mode | Duplicate for film mode | Move downstream | Do not use in film core | Notes |
|---|---|---|---|---|---|---|
| `cwf_110`-`cwf_140` topic/research family | No | Yes | Maybe | No | No | best upstream research support for film premise work |
| `cwf_210`-`cwf_240` script family | No | Yes | Yes | No | No | strongest need for film mirror stack |
| `cwf_310` context engineering | No | Yes | Yes | No | No | should become route-neutral film context support |
| `wf_320` / `cwf_420` / `cwf_440` packaging and media handoff | No | No | No | Yes | Yes | keep as downstream production/release support |
| `cwf_430` voice context | No | Yes | Maybe | No | No | can become performance/voice-direction support |
| `wf_340` lineage validator | Yes | Yes | No | No | No | reusable governance lane |
| `wf_500` / `cwf_510`-`cwf_530` publishing | Yes | No | No | Yes | Yes | downstream release and metadata only |
| `wf_600` / `cwf_610`-`cwf_630` analytics | Yes | No | No | Yes | Yes | downstream audience and trend signal only |
| `wf_000` / `wf_001` / `wf_010` / `wf_020` / `wf_021` / `wf_022` / `wf_023` / `wf_900` | Yes | Yes | No | No | No | infrastructure/governance lanes are reusable |

## 3. Old-to-new responsibility map

| Existing subagent responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| topic discovery / qualification / scoring / synthesis | broad content discovery | film research brief + story premise research | Yes | can help choose a film premise before story drafting |
| script generation with hooks | YouTube/content cadence | screenplay beat sheet + scene sequence planning | Yes, for content mode | film mode should not require hook cadence as a primary law |
| script critique / refinement | retention and re-hook density | cinematic story criticism, scene turns, subtext, pacing | Yes, for content mode | keep content critique separate from film critique |
| packaging and media handoff | media factory / avatar video | production packet handoff + release adaptation | Yes | keep downstream execution lanes intact |
| voice context | creator delivery / voiceover | performance direction + dialogue rhythm + voice texture | Yes | should become film-performance aware |
| platform packager / publish readiness | platform-first release | film release adaptation and distribution metadata | Yes | distribution stays downstream |
| analytics / audience feedback / trends | platform optimization | film-market signal and audience insight adapter | Yes | trend data must not control screenplay craft |
| lineage / governance / error handling | control-plane safety | continuity guard + validation + error recovery | Yes | these are reusable and should be preserved |

## 4. Interface to Phase 4 Skills
Phase 4 should turn the film-mode subagent proposals into skills and subskills that match craft responsibilities:

- structure skills
- character arc skills
- scene dramaturgy skills
- dialogue and subtext skills
- visual composition skills
- performance direction skills
- continuity validation skills
- release adaptation skills

## 5. Future patch plan
Phase 4 should inspect the skill layer in this order:

1. existing content/script skills
2. hook and retention skills
3. context and media skills
4. governance and validation skills
5. any missing film-craft skills

That phase should then decide which skills are:

- reusable as-is
- reusable with film mode
- duplicated for film mode
- moved downstream
- unsafe in film core

## Phase 11U Canon/Style Supplement Linkage Addendum

This is a later linkage update and does not rewrite the original Phase 3 finding.
Future subagent film mode must now inherit the supplement pack:

- `FILMCRAFT_CANON_SOURCE_LEDGER.md`
- `CINEMA_STYLE_BIBLE_REQUIREMENTS.md`
- `ANIMATION_CANON_REQUIREMENTS.md`
- `FILM_ROUTE_PLATFORM_SEPARATION_LAW.md`
- `REAL_INCIDENT_DOCUDRAMA_ETHICS_REQUIREMENTS.md`

Subagents must keep `SCRIPT_GENERATION` preserved, add `FILM_SCREENPLAY_GENERATION` in parallel later, and keep platform/content logic downstream or content-only.
Hook, pacing, retention, and creator-fit logic may remain in content subagents, but they must not become film-core PASS criteria.
Phase 12 remains blocked until the supplement layer is reviewed and linked.
