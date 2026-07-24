# Phase 8 Film Validator Canon Proposal

## 1. Proposed film validator families

The cinema route needs its own validator family, separate from the content/script validator family:

* `validators/film/`
* `validators/film/route/`
* `validators/film/screenplay_structure/`
* `validators/film/character/`
* `validators/film/scene_dramaturgy/`
* `validators/film/dialogue/`
* `validators/film/visual_language/`
* `validators/film/directorial_style/`
* `validators/film/performance/`
* `validators/film/output_packet/`

## 2. Proposed film validators

Recommended future validators:

* `validate_film_route_selection.py`
* `validate_film_content_route_collision.py`
* `validate_film_screenplay_packet.py`
* `validate_save_the_cat_beat_sheet.py`
* `validate_three_act_structure.py`
* `validate_eight_sequence_structure.py`
* `validate_hero_journey_map.py`
* `validate_dan_harmon_story_circle.py`
* `validate_mckee_scene_value_turns.py`
* `validate_syd_field_plot_points.py`
* `validate_truby_22_step_story_map.py`
* `validate_character_want_need_flaw_arc.py`
* `validate_character_web_opposing_force.py`
* `validate_scene_objective_obstacle_tactic.py`
* `validate_scene_conflict_and_turns.py`
* `validate_dialogue_subtext.py`
* `validate_dialogue_voice_distinctness.py`
* `validate_visual_motif_image_system.py`
* `validate_mise_en_scene.py`
* `validate_blocking_composition.py`
* `validate_camera_lens_framing.py`
* `validate_sound_motif_silence.py`
* `validate_performance_beats.py`
* `validate_screenplay_format.py`
* `validate_film_scorecard_no_fake_pass.py`

## 3. Top 20 filmcraft validation matrix

| # | Filmcraft technique/system | Repo support status | Existing evidence | Missing validator? | Proposed validator | Notes |
|---|---|---|---|---|---|---|
| 1 | Save the Cat 15-beat sheet | MISSING | No dedicated filmcraft validator found | Yes | `validate_save_the_cat_beat_sheet.py` | Content system does not validate beat-sheet canon |
| 2 | Syd Field three-act paradigm and Plot Points I/II | MISSING | No dedicated filmcraft validator found | Yes | `validate_syd_field_plot_points.py` | Needs screenplay-specific structure gate |
| 3 | Robert McKee scene value turns | MISSING | No dedicated filmcraft validator found | Yes | `validate_mckee_scene_value_turns.py` | Scene-level dramatic turn is absent |
| 4 | Joseph Campbell Hero’s Journey / monomyth | MISSING | No dedicated filmcraft validator found | Yes | `validate_hero_journey_map.py` | Absent from current validator stack |
| 5 | Dan Harmon Story Circle | MISSING | No dedicated filmcraft validator found | Yes | `validate_dan_harmon_story_circle.py` | No validation support found |
| 6 | John Truby 22-step / moral argument / symbol web | MISSING | No dedicated filmcraft validator found | Yes | `validate_truby_22_step_story_map.py` | Entire canon missing |
| 7 | three-act structure | MISSING | No dedicated filmcraft validator found | Yes | `validate_three_act_structure.py` | Should not be inferred from content beat maps |
| 8 | eight-sequence structure | MISSING | No dedicated filmcraft validator found | Yes | `validate_eight_sequence_structure.py` | No current support found |
| 9 | character want vs need | MISSING | No dedicated filmcraft validator found | Yes | `validate_character_want_need_flaw_arc.py` | Character transformation gate absent |
| 10 | character flaw and transformation | MISSING | No dedicated filmcraft validator found | Yes | `validate_character_want_need_flaw_arc.py` | Needs explicit filmcraft validation |
| 11 | character web and opposing force | MISSING | No dedicated filmcraft validator found | Yes | `validate_character_web_opposing_force.py` | Absent |
| 12 | scene objective / obstacle / tactic | MISSING | No dedicated filmcraft validator found | Yes | `validate_scene_objective_obstacle_tactic.py` | Absent |
| 13 | scene conflict and scene turn | MISSING | No dedicated filmcraft validator found | Yes | `validate_scene_conflict_and_turns.py` | Absent |
| 14 | dialogue subtext | MISSING | No dedicated filmcraft validator found | Yes | `validate_dialogue_subtext.py` | Absent |
| 15 | dialogue voice distinctness | MISSING | No dedicated filmcraft validator found | Yes | `validate_dialogue_voice_distinctness.py` | Absent |
| 16 | visual motif / image system | MISSING_VALIDATOR_ONLY | Downstream visual media supports imagery, but not screenplay canon | Yes | `validate_visual_motif_image_system.py` | Downstream media only today |
| 17 | mise-en-scène | MISSING_VALIDATOR_ONLY | Downstream media and storyboard support, but no film validator | Yes | `validate_mise_en_scene.py` | Downstream-only support at best |
| 18 | blocking and composition | MISSING_VALIDATOR_ONLY | Visual planning tools exist, not film validation | Yes | `validate_blocking_composition.py` | Downstream-only support at best |
| 19 | camera language, lens grammar, and framing | MISSING_VALIDATOR_ONLY | Visual media/tooling can express this downstream | Yes | `validate_camera_lens_framing.py` | Not film-core validated |
| 20 | sound motif, silence design, and performance beat | MISSING_VALIDATOR_ONLY | Voice/audio routes exist downstream, not film canon validation | Yes | `validate_sound_motif_silence.py` and `validate_performance_beats.py` | Needs dedicated film gate |

## 4. Reuse map

| Existing validator/family | Current bias | Film-mode use | Downstream retained? | Recommendation |
|---|---|---|---|---|
| Script generation validators | Content/hooks/retention | Not film-core | Yes | Keep for content mode only |
| Route-state validators | Governance | Reuse as-is | Yes | KEEP |
| Route-scope telemetry validators | Governance | Reuse as-is | Yes | KEEP |
| Evidence bundle validators | Governance | Reuse as-is | Yes | KEEP |
| Patch provenance validators | Governance | Reuse as-is | Yes | KEEP |
| Visual media validators | Downstream media | Downstream only | Yes | MOVE |
| Phase0 proof-plane validators | Governance/proof | Reuse as-is | Yes | KEEP |

## 5. Old-to-new responsibility map

| Existing validator responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| Hook density / recurring rehook validation | Content retention | Film screenplay structure validation | Yes | Must not govern cinema-core |
| Short-story block before teaching content | Content teaching | Film opening sequence / inciting incident checks | No | Wrong default for film core |
| Dynamic timed beat map | Content pacing | Scene dramaturgy / act structure validation | Yes | Useful only if reinterpreted for film |
| Source integrity and evidence | Generic governance | Reuse unchanged | Yes | Strong reusable gate |
| Route-state / no-fake-pass | Generic governance | Reuse unchanged | Yes | Essential spine |
| Visual media plan checks | Downstream media | Keep downstream | Yes | Not screenplay validation |

## 6. Interface to Phase 9 Schemas

Phase 9 should inspect and propose schemas for:

* film route state capsule
* film screenplay output packet
* film beat sheet
* film character arc map
* film scene dramaturgy map
* film dialogue subtext pass
* film visual motif system
* film composition/camera/sound packet
* film validation scorecard
* no fake film PASS schema
* film downstream handoff packet

## 7. Non-goals

This phase does not patch validators yet. It only identifies the current content-mode validation bias, the reusable governance spine, and the missing filmcraft validator canon.
