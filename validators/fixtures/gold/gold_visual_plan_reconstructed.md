fixture_id=FX-GOLD-002
fixture_type=gold
stage=visual_media_plan
reconstruction_status=RECONSTRUCTED_GOLD_SPEC
expected_validator=validate_visual_generation_depth.py
expected_result=PASS

VISUAL_MEDIA_PLAN_LOCK
mode=VISUAL_MEDIA_PLAN
planning_only=true
asset_execution_claim=false
locked_script_reference=gold_script_reconstructed.md
provider_honesty_gate=PASS

SCENE_BY_SCENE_TABLE_17_FIELD_SCHEMA
columns=scene_id,timecode,duration,narration_summary,visual_subject,environment,camera_framing,lens_logic,lighting,color_palette,motion_intent,media_method,provider_or_local_lane,cost_level,evidence_or_contract,reasoning,continuity_notes

SCENE_ROW
scene_id=01
timecode=0:00-0:15
duration=15
narration_summary=Stop scrolling hook and Yash story bridge.
visual_subject=Phone reflection to performer silhouette.
environment=Dark room then warm stage.
camera_framing=Close-up to medium wide.
lens_logic=35mm phone close-up, 50mm stage silhouette.
lighting=Blue phone glow, warm gold rim.
color_palette=blue shadows, warm gold highlights.
motion_intent=Fast scroll cut to slow push-in.
media_method=B-roll plus kinetic text.
provider_or_local_lane=planning_only_provider_select_later
cost_level=medium
evidence_or_contract=VISUAL_MEDIA_PLAN planning boundary
reasoning=Contrasts passive attention with earned self-investment.
continuity_notes=No exact celebrity face reproduction.

MEDIA_METHOD_DISTRIBUTION
A_roll_seconds=90
B_roll_seconds=125
motion_graphics_seconds=90
cinematic_broll_seconds=40
total_runtime_seconds=305
broll_ratio_percent=13.1

COST_DISTRIBUTION
low_cost_scenes=4
medium_cost_scenes=7
premium_cost_scenes=2

LOCAL_CLOUD_HYBRID_BOUNDARY
providers_called=false
local_engines_called=false
human_approval_required_before_execution=true
no_asset_execution_claim=true
