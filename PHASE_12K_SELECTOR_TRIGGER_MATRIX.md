# Phase 12K Selector Trigger Matrix

## 1. Objective
Define candidate selector triggers and anti-triggers for the future film route binding.

## 2. Trigger matrix

| Prompt pattern | Future expected route | Current safety concern | Required supporting fixture | Binding priority | Notes |
|---|---|---|---|---|---|
| short film on NEET | `FILM_SCREENPLAY_GENERATION` | Could be flattened into content script by duration wording | `tests/fixtures/film_route_selection/neet_short_film.json` | High | Explicit film intent should win |
| 5-minute short film on NEET | `FILM_SCREENPLAY_GENERATION` | Duration should not force content routing | `tests/fixtures/film_route_selection/five_minute_neet_short_film.json` | High | Short runtime still film-core |
| screenplay about exam leak impact | `FILM_SCREENPLAY_GENERATION` | Could be mistaken for commentary content | `tests/fixtures/film_route_selection/screenplay_exam_leak_student.json` | High | Screenplay keyword is decisive |
| screenplay about a student after exam leak allegations | `FILM_SCREENPLAY_GENERATION` | Real-incident language can be misrouted | `tests/fixtures/film_route_selection/screenplay_exam_leak_student.json` | High | Requires source-ledger support later |
| short film on exam leak allegations | `FILM_SCREENPLAY_GENERATION` | Real-incident short film needs film-core route | `tests/fixtures/film_route_selection/neet_short_film.json` | High | Keep film intent above content style |
| YouTube script about NEET | `SCRIPT_GENERATION` | Content route must remain preserved | `tests/fixtures/film_route_selection/youtube_neet_script.json` | High | Explicit content/script wording |
| Instagram reel script about NEET | `SCRIPT_GENERATION` | Social video wording must not jump to film-core | `tests/fixtures/film_route_selection/instagram_reel_neet_script.json` | High | Preserve content/social route |
| voiceover script about NEET | `SCRIPT_GENERATION` | Voiceover wording is content-route language | `tests/fixtures/film_route_selection/voiceover_neet_script.json` | High | Preserve content route default |
| make a cinematic explainer for YouTube | `SCRIPT_GENERATION` | Cinematic style alone is ambiguous | `tests/fixtures/film_route_selection/cinematic_explainer_youtube.json` | Medium | Ask for clarification if screenplay intent is unclear |
| cinematic explainer for YouTube about NEET | `SCRIPT_GENERATION` by default | Ambiguous because platform and style conflict | `tests/fixtures/film_route_selection/cinematic_explainer_youtube.json` | Medium | Stay content-route unless screenplay terms appear |
| trailer for the NEET short film | downstream distribution | Trailer is not screenplay generation | `tests/fixtures/film_route_selection/trailer_for_neet_short_film.json` | High | Downstream only |
| thumbnail and title for the NEET film | downstream packaging | Packaging should not activate film-core | `tests/fixtures/film_route_selection/thumbnail_title_for_neet_film.json` | High | Downstream only |
| full video pipeline for a film screenplay | downstream pipeline | Pipeline phrasing is not screenplay intent | `tests/fixtures/film_route_selection/full_video_pipeline_for_film_screenplay.json` | High | Keep as downstream family |
| film packet to visual media plan | downstream handoff | Handoff should stay downstream | `tests/fixtures/downstream_handoff/film_packet_to_visual_media_plan.json` | Medium | Not a selector trigger for film-core |
| film packet to voice context | downstream handoff | Handoff should stay downstream | `tests/fixtures/downstream_handoff/film_packet_to_voice_context.json` | Medium | Not a selector trigger for film-core |
| film packet to editing packaging | downstream handoff | Handoff should stay downstream | `tests/fixtures/downstream_handoff/film_packet_to_editing_packaging.json` | Medium | Not a selector trigger for film-core |
| film packet to media factory handoff | downstream handoff | Handoff should stay downstream | `tests/fixtures/downstream_handoff/film_packet_to_media_factory_handoff.json` | Medium | Not a selector trigger for film-core |
| film packet to full video pipeline | downstream handoff | Pipeline remains downstream | `tests/fixtures/downstream_handoff/film_packet_to_full_video_pipeline.json` | Medium | Not a selector trigger for film-core |
| trailer after film packet | downstream distribution | Trailer must remain downstream | `tests/fixtures/downstream_handoff/trailer_after_film_packet.json` | High | Downstream-only behavior |
| social cutdown after film packet | downstream distribution | Social cutdowns must remain downstream | `tests/fixtures/downstream_handoff/social_cutdown_after_film_packet.json` | High | Downstream-only behavior |
| valid minimal film packet | `FILM_SCREENPLAY_GENERATION` | Needs film schema/validator readiness later | `tests/fixtures/film_packet_validation/valid_minimal_film_packet.json` | High | PASS later only after binding |
| missing beat sheet should fail | `FILM_SCREENPLAY_GENERATION` | Missing required filmcraft field | `tests/fixtures/film_packet_validation/missing_beat_sheet_should_fail.json` | High | No fake PASS |
| missing character arc should fail | `FILM_SCREENPLAY_GENERATION` | Missing required character field | `tests/fixtures/film_packet_validation/missing_character_arc_should_fail.json` | High | No fake PASS |
| missing scene turns should fail | `FILM_SCREENPLAY_GENERATION` | Missing dramaturgy support | `tests/fixtures/film_packet_validation/missing_scene_turns_should_fail.json` | High | No fake PASS |
| missing dialogue subtext should fail | `FILM_SCREENPLAY_GENERATION` | Missing dialogue depth | `tests/fixtures/film_packet_validation/missing_dialogue_subtext_should_fail.json` | High | No fake PASS |
| missing visual motif should fail | `FILM_SCREENPLAY_GENERATION` | Missing visual language support | `tests/fixtures/film_packet_validation/missing_visual_motif_should_fail.json` | High | No fake PASS |
| missing camera composition should fail | `FILM_SCREENPLAY_GENERATION` | Missing shot/camera grammar | `tests/fixtures/film_packet_validation/missing_camera_composition_should_fail.json` | High | No fake PASS |
| missing validation scorecard should fail | `FILM_SCREENPLAY_GENERATION` | Missing film validation gate | `tests/fixtures/film_packet_validation/missing_validation_scorecard_should_fail.json` | High | No fake PASS |
| content packet pretending film should fail | `BLOCK_FILM` | Content-mode packets must not masquerade as film-core | `tests/fixtures/film_packet_validation/content_packet_pretending_film_should_fail.json` | High | Collision guard |
| hook retention only packet should fail | `BLOCK_FILM` | Content-only hook logic must not satisfy film-core | `tests/fixtures/film_packet_validation/hook_retention_only_packet_should_fail.json` | High | Collision guard |
| GitHub read not runtime proof | `BLOCK_FILM` | Repo inspection must not become governed proof | `tests/fixtures/no_fake_pass/github_read_not_runtime_proof.json` | High | No fake PASS |
| film output without film schema should fail | `BLOCK_FILM` | Missing schema must fail later | `tests/fixtures/no_fake_pass/film_output_without_film_schema_should_fail.json` | High | No fake PASS |
| film output without lineage ledger should fail | `BLOCK_FILM` | Missing lineage must fail later | `tests/fixtures/no_fake_pass/film_output_without_lineage_ledger_should_fail.json` | High | No fake PASS |
| film output without filmcraft scorecard should fail | `BLOCK_FILM` | Missing scorecard must fail later | `tests/fixtures/no_fake_pass/film_output_without_filmcraft_scorecard_should_fail.json` | High | No fake PASS |
| real world film without source ledger should fail | `BLOCK_FILM` | Real incidents need source discipline | `tests/fixtures/no_fake_pass/real_world_film_without_source_ledger_should_fail.json` | High | No fake PASS |
| runtime artifact names cannot be invented | `BLOCK_FILM` | Invented proof artifacts must fail later | `tests/fixtures/no_fake_pass/runtime_artifact_names_cannot_be_invented.json` | High | No fake PASS |

## 3. Negative trigger rules

| Negative trigger | Blocks film-core? | Expected fallback | Fixture support | Notes |
|---|---|---|---|---|
| YouTube | Yes, when it is the only clear cue | `SCRIPT_GENERATION` | `youtube_neet_script.json` | Content route stays default |
| Shorts | Yes, when it is the only clear cue | `SCRIPT_GENERATION` | `shorts_script_preserved.json` | Content route stays default |
| Instagram reel | Yes, when it is the only clear cue | `SCRIPT_GENERATION` | `instagram_reel_neet_script.json` | Social route stays content-side |
| TikTok | Yes, when it is the only clear cue | `SCRIPT_GENERATION` | future fixture needed | Not yet present in Phase 12A |
| voiceover script | Yes, when it is the only clear cue | `SCRIPT_GENERATION` | `voiceover_neet_script.json` | Content route stays default |
| thumbnail/title | Yes | downstream packaging | `thumbnail_title_for_neet_film.json` | Not screenplay intent |
| trailer | Yes | downstream distribution | `trailer_for_neet_short_film.json` | Not screenplay intent |
| SEO | Yes | content route | future fixture needed | Content optimization language |
| content hook | Yes | content route | `hook_retention_only_packet_should_fail.json` | Must not pass film-core |
| retention loop | Yes | content route | `hook_retention_only_packet_should_fail.json` | Must not pass film-core |

## 4. Ambiguity policy
`ASK_FOR_CLARIFICATION`

When a prompt mixes cinematic style with content-platform wording and does not clearly request a screenplay, the selector should ask for clarification rather than silently moving to film-core.

