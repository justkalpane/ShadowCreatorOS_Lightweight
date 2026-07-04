fixture_id=FX-BAD-007
fixture_type=bad
stage=visual_media_generation_draft
expected_validator=validate_visual_generation_depth.py
expected_result=FAIL

DAVINCI_FFMPEG_ASSEMBLY_PLAN
DaVinci_Resolve=PACKET_READY
FFmpeg=PACKET_READY
status=PASS

ASSEMBLY_NOTES
Import everything into DaVinci, edit nicely, add music, color grade, and export the final video.

TRACK_STRUCTURE
davinci_track_map_present=false
video_tracks=
audio_tracks=
marker_rows_detected=0
asset_dependency_graph_present=false
ffmpeg_command_plan_present=false

failure_reason=DaVinci/FFmpeg readiness is claimed without track map, markers, dependency graph, or command structure.
