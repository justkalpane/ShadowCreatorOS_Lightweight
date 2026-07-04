fixture_id=FX-GOLD-003
fixture_type=gold
stage=visual_media_generation_draft
reconstruction_status=RECONSTRUCTED_GOLD_SPEC
expected_validator=validate_visual_generation_depth.py
expected_result=PASS
route_id=MEDIA_FACTORY_HANDOFF
canonical_route_id=MEDIA_FACTORY_HANDOFF
task_mode=script_plus_visual_generation_draft
route_manifest_path=registries/route_manifests/media_factory_handoff.yaml
selected_route_slice_path=registries/route_slices/visual_media_generation_draft.registry_slice.yaml
route_manifest_read=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true

Route Verification & System Locks
visual_generation_stage=VISUAL_MEDIA_GENERATION_DRAFT
script_integrity_lock=PASS
visual_plan_integrity_lock=PASS
planning_only_unless_execution_approved=true

Assumption Verification Table
| assumption | evidence | status |
|---|---|---|
| locked final script exists | gold_script_reconstructed.md | PASS |
| locked visual plan exists | gold_visual_plan_reconstructed.md | PASS |
| providers not called | provider honesty gate | PASS |

Asset Generation Order
1. freeze_approved_script_and_scene_ids
2. generate_or_confirm_scene_sync_matrix
3. generate_master_voice_track
4. align_voice_timestamps_to_scene_rows
5. generate_music_segments
6. generate_individual_sfx_clips
7. generate_character_consistency_reference_assets
8. generate_storyboard_and_still_image_assets
9. render_hyperframes_slides_cards_and_alpha_overlays
10. generate_depth_maps_for_still_parallax_assets
11. generate_heygen_a_roll_batches
12. generate_premium_cinematic_b_roll_clips
13. build_davinci_timeline_from_packet
14. qc_sync_captions_safe_zones_color_and_audio
15. export_youtube_master

Scene-by-scene Multi-Arc Table
| scene_id | timecode | visual_method | SFX timestamp | DaVinci track | Reasoning |
|---|---|---|---|---|---|
| 01 | 0:00-0:15 | cinematic B-roll plus kinetic text | 0:02 phone swipe, 0:10 bass hit | V2, V3, A3 | Pattern interrupt and story bridge. |
| 02 | 0:15-0:35 | cinematic B-roll | 0:18 bus brake, 0:31 city bed | V2, A3 | Grounds the Yash journey without claiming exact reenactment. |
| 03 | 0:35-0:55 | storyboard still with parallax | 0:37 stage room tone, 0:50 tea cup | V2, A4 | Makes backstage self-investment visible. |

Media Method Distribution
total_runtime_seconds=305
A_roll_seconds=90
cinematic_broll_seconds=40
motion_graphics_seconds=85
storyboard_stills_seconds=90

B-roll Ratio Breakdown
total_runtime_seconds=305
cinematic_broll_seconds=40
required_cinematic_broll_seconds=37
broll_ratio_percent=13.1
status=PASS

Provider Honesty Gate
providers_called=false
n8n_used=false
local_media_generation_engine_used=false
media_artifacts_claimed=false
status=TEXT_PLAN_ONLY

Local/Cloud/Hybrid Boundary
execution_requires_user_approval=true
provider_payloads_are_plans_not_artifacts=true
local_bridge_status=not_executed

DaVinci/FFmpeg Assembly Plan
track_map=V1 presenter, V2 cinematic broll, V3 text overlays, A1 voice, A2 music, A3 sfx, A4 ambience, A5 room tone
marker_rows=scene_id,timecode,asset_ref,track,reasoning
ffmpeg_command_plan_present=true
artifact_path_required_before_PACKET_READY=true

QC/Proof Registry
proof_json_required=true
registry_update_required=true
human_review_status=required

Final Classification
final_status=PASS
classification_basis=deep visual draft structure present, execution not claimed
