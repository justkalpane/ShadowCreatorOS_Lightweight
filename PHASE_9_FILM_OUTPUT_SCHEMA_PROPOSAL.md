# Phase 9 Film Output Schema Proposal

## 1. Proposed film schema families

The cinema route should eventually live under a dedicated schema family:

* `schemas/film/`
* `schemas/film/route/`
* `schemas/film/output_packet/`
* `schemas/film/source/`
* `schemas/film/story_structure/`
* `schemas/film/character/`
* `schemas/film/scene_dramaturgy/`
* `schemas/film/dialogue/`
* `schemas/film/visual_language/`
* `schemas/film/directorial_style/`
* `schemas/film/downstream_handoff/`
* `schemas/film/validation/`

## 2. Proposed film schemas

Recommended future schema files:

* `film_route_state_capsule.schema.json`
* `film_screenplay_output_packet.schema.json`
* `film_source_ledger.schema.json`
* `film_fact_vs_anecdote_map.schema.json`
* `film_beat_sheet.schema.json`
* `film_three_act_map.schema.json`
* `film_eight_sequence_map.schema.json`
* `film_hero_journey_map.schema.json`
* `film_story_circle_map.schema.json`
* `film_mckee_scene_value_turn_map.schema.json`
* `film_syd_field_plot_point_map.schema.json`
* `film_truby_story_map.schema.json`
* `film_character_arc.schema.json`
* `film_character_web.schema.json`
* `film_scene_dramaturgy_map.schema.json`
* `film_dialogue_subtext_pass.schema.json`
* `film_visual_motif_system.schema.json`
* `film_mise_en_scene_blocking_composition.schema.json`
* `film_camera_language.schema.json`
* `film_sound_motif_performance.schema.json`
* `film_screenplay_format_status.schema.json`
* `film_downstream_handoff_packet.schema.json`
* `film_validation_scorecard.schema.json`
* `no_fake_film_pass.schema.json`
* `film_content_packet_separation.schema.json`

## 3. Top film output packet field matrix

| # | Target field | Current schema support | Existing evidence | Missing schema? | Proposed schema location | Notes |
|---|---|---|---|---|---|---|
| 1 | Route state capsule | SUPPORTED | `schemas/runtime_state/route_state_capsule.schema.json` | No | existing + film variant | Needs film route-id variant |
| 2 | Route ID and route mode | PARTIAL | `runtime/state/route_state.schema.json` | No | route state schema | Present, but content modes dominate |
| 3 | Film intent lock | MISSING | No film packet found | Yes | `film_route_state_capsule.schema.json` | Required for cinema routing |
| 4 | Source research status | PARTIAL | `context_packet`, `source_evidence_packet`, `research_brief_packet` | No | film source schema | Needs film-specific status semantics |
| 5 | Source ledger | PARTIAL | `source_evidence_packet`, `lineage_packet` | No | `film_source_ledger.schema.json` | Good groundwork, missing film framing |
| 6 | Fact vs anecdote map | MISSING | No dedicated schema found | Yes | `film_fact_vs_anecdote_map.schema.json` | Required for real-world film proofs |
| 7 | Logline | MISSING | No dedicated schema found | Yes | `film_screenplay_output_packet.schema.json` | Core screenplay field |
| 8 | Theme | MISSING | No dedicated schema found | Yes | `film_screenplay_output_packet.schema.json` | Core screenplay field |
| 9 | Premise | MISSING | No dedicated schema found | Yes | `film_screenplay_output_packet.schema.json` | Core screenplay field |
| 10 | Genre | PARTIAL | `script_strategy_packet` / `context_packet` | No | film screenplay packet | Needs stronger schema support |
| 11 | Tone | PARTIAL | `voice_context_packet`, `context_packet` | No | film screenplay packet | Present in fragments only |
| 12 | Cinematic world | MISSING | No dedicated schema found | Yes | film screenplay packet | Required |
| 13 | Protagonist want | MISSING | No dedicated schema found | Yes | film character schema | Required |
| 14 | Protagonist need | MISSING | No dedicated schema found | Yes | film character schema | Required |
| 15 | Protagonist flaw | MISSING | No dedicated schema found | Yes | film character schema | Required |
| 16 | Protagonist arc | MISSING | No dedicated schema found | Yes | film character arc schema | Required |
| 17 | Antagonist / opposing force | MISSING | No dedicated schema found | Yes | film character web schema | Required |
| 18 | Character web | MISSING | No dedicated schema found | Yes | film character web schema | Required |
| 19 | Save the Cat beat sheet | MISSING | No dedicated schema found | Yes | film beat sheet schema | Required |
| 20 | Three-act map | MISSING | No dedicated schema found | Yes | film three-act map schema | Required |
| 21 | Eight-sequence map | MISSING | No dedicated schema found | Yes | film eight-sequence map schema | Required |
| 22 | Hero’s Journey map | MISSING | No dedicated schema found | Yes | film hero journey schema | Optional canon support |
| 23 | Dan Harmon Story Circle map | MISSING | No dedicated schema found | Yes | film story circle schema | Optional canon support |
| 24 | McKee scene value-turn map | MISSING | No dedicated schema found | Yes | film scene dramaturgy schema | Required |
| 25 | Syd Field plot point map | MISSING | No dedicated schema found | Yes | film story structure schema | Required |
| 26 | Truby moral argument / symbol web map | MISSING | No dedicated schema found | Yes | film story structure schema | Required |
| 27 | Scene list | PARTIAL | `scene_prompt_packet`, `storyboard_export_packet` | No | film screenplay packet | Needs screenplay semantics |
| 28 | Scene objective / obstacle / tactic | MISSING | No dedicated schema found | Yes | film scene dramaturgy schema | Required |
| 29 | Scene conflict and turn | MISSING | No dedicated schema found | Yes | film scene dramaturgy schema | Required |
| 30 | Dialogue subtext pass | MISSING | No dedicated schema found | Yes | film dialogue schema | Required |
| 31 | Dialogue voice distinctness pass | MISSING | No dedicated schema found | Yes | film dialogue schema | Required |
| 32 | Visual motif / image system | SUPPORTED_DOWNSTREAM_ONLY | `visual_media_plan_row`, `scene_prompt_packet`, `storyboard_export_packet` | Yes | film visual language schema | Strong downstream support only |
| 33 | Mise-en-scène notes | SUPPORTED_DOWNSTREAM_ONLY | `visual_media_plan_row` and media factory packets | Yes | film visual language schema | Downstream-only support |
| 34 | Blocking and composition notes | SUPPORTED_DOWNSTREAM_ONLY | `visual_media_plan_row` | Yes | film visual language schema | Downstream-only support |
| 35 | Camera language / lens / framing notes | SUPPORTED_DOWNSTREAM_ONLY | `visual_media_plan_row`, `scene_prompt_packet` | Yes | film visual language schema | Downstream-only support |
| 36 | Sound motif / silence design | SUPPORTED_DOWNSTREAM_ONLY | `voice_context_packet`, `video_context_packet`, music/sfx packets | Yes | film sound schema | Downstream-only support |
| 37 | Performance direction | SUPPORTED_DOWNSTREAM_ONLY | `voice_context_packet`, `audio_performance_packet` | Yes | film performance schema | Downstream-only support |
| 38 | Screenplay body | SUPPORTED | `final_script_packet`, `script_draft_packet` | No | existing + film variant | Strong content support already |
| 39 | Screenplay formatting status | MISSING | No dedicated schema found | Yes | film screenplay format schema | Required |
| 40 | Director’s notes | MISSING | No dedicated schema found | Yes | film output packet | Required |
| 41 | Production notes | PARTIAL | `context_engineering_packet`, media factory packets | No | film output packet | Needs film-specific semantics |
| 42 | Downstream visual handoff recommendations | SUPPORTED_DOWNSTREAM_ONLY | visual/media factory packets | No | film downstream handoff | Keep downstream |
| 43 | Downstream voice handoff recommendations | SUPPORTED_DOWNSTREAM_ONLY | `voice_context_packet` | No | film downstream handoff | Keep downstream |
| 44 | Downstream editing handoff recommendations | SUPPORTED_DOWNSTREAM_ONLY | `editing_timeline_packet`, editing-related packets | No | film downstream handoff | Keep downstream |
| 45 | Downstream media factory handoff recommendations | SUPPORTED_DOWNSTREAM_ONLY | media factory packet family | No | film downstream handoff | Keep downstream |
| 46 | Film validation scorecard | MISSING | `quality_scorecard` is content-mode only | Yes | film validation scorecard schema | Required |
| 47 | No-fake-PASS gate result | PARTIAL | generic route-state / no-fake-pass guards exist | No | film validation scorecard | Needs film-specific gating |
| 48 | Unsupported claims ledger | PARTIAL | `source_evidence_packet`, `lineage_packet`, source contracts | No | film source ledger | Needs explicit film output row |
| 49 | Route lineage / consumption ledger | SUPPORTED | `lineage_packet`, `route_state` read ledger | No | existing + film variant | Reusable governance support |
| 50 | Final status | SUPPORTED | many packet `status` fields | No | film output packet | Generic status support already exists |

## 4. Reuse map

| Existing schema/family | Current bias | Film-mode use | Downstream retained? | Recommendation |
|---|---|---|---|---|
| Route-state schemas | Governance | Reuse as-is, add film variant | Yes | KEEP |
| Source/evidence/lineage schemas | Governance | Reuse as-is | Yes | KEEP |
| Registry schema | Identity/governance | Reuse as-is | Yes | KEEP |
| Script/content packets | Content/hook/retention | Do not use as film core | Yes | REPLACE for film core |
| Script refinement packets | Content improvement | Duplicate for film mode later | Yes | DUPLICATE |
| Visual media schemas | Downstream production | Keep downstream | Yes | MOVE |
| Voice/audio schemas | Downstream production | Keep downstream | Yes | MOVE |
| Platform packaging schemas | Release/distribution | Keep downstream | Yes | MOVE |
| Quality scorecard schemas | Content scoring | Reuse only as generic metrics | Yes | REFACTOR |

## 5. Old-to-new responsibility map

| Existing schema responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| `youtube_script_packet` / `tiktok_script_packet` output shapes | Platform script | `film_screenplay_output_packet` | Yes | Keep old packets for content mode |
| `script_draft_packet` hook/section plan | Content drafting | film screenplay packet | Yes | Needs rewrite for film semantics |
| `final_script_packet` + CTA | Content CTA | film screenplay body + director notes | No | CTA is not a film-core default |
| `context_packet` generic topic/script/runtime routing | Generic content | film route-state / film context packet | Yes | Reusable with stronger schema |
| `visual_media_plan_row` / storyboard export | Downstream visual planning | film visual handoff packet | Yes | Valuable downstream |
| `quality_scorecard` | Content scoring | film validation scorecard | Yes | Do not reuse raw for film PASS |

## 6. Interface to Phase 10 Test Fixtures

Phase 10 should build fixtures for:

* NEET short-film screenplay packet
* film route selection
* film-vs-content collision
* content-mode YouTube script preserved
* film screenplay output packet validation
* missing required film field failure
* fake film PASS prevention
* downstream media handoff from film packet

## 7. Non-goals

This phase does not patch schemas yet. It only identifies the current content-mode schema spine, the reusable governance and media scaffolding, and the missing film-first packet family.
