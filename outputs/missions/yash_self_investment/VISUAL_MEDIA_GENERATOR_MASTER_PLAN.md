# Yash Self Investment Visual Media Generator Master Plan

mission_id=yash_self_investment
route_id=MEDIA_FACTORY_HANDOFF
runtime_state=production_support_started
source_script_ref=outputs/missions/yash_self_investment/MISSION_OUTPUT.md
source_packet_ref=outputs/missions/yash_self_investment/packets/media_factory_packet.json
control_panel_job_root=/Users/apple/ShadowMediaFactory/control_panel/jobs/yash_self_investment
cleanup_policy=keep_required_delete_temporary

## Purpose

This master plan is the operator-facing execution summary for the approved Yash
mission. It sits above the packet JSON files and support TXT files so that the
generation, save, and assembly order stays readable.

## Canonical Execution Order

1. Freeze approved script and scene IDs.
2. Confirm scene sync matrix.
3. Generate master voice track.
4. Align voice timestamps to scene rows.
5. Generate music segments.
6. Generate SFX clips.
7. Generate character consistency reference assets.
8. Generate storyboard and still image assets.
9. Render HyperFrames slides, cards, and alpha overlays.
10. Generate depth maps for still parallax assets.
11. Generate HeyGen A-roll batches.
12. Generate premium cinematic B-roll clips.
13. Build DaVinci timeline from packet.
14. Assemble V1/V2/V3 and A1-A5 tracks.
15. QC sync, captions, safe zones, color, and audio.
16. Export YouTube master.
17. Collect proofs and update registry.

## Actual Production Start State

- Preflight completed successfully through the local control panel.
- The local stack is ready for FFmpeg, Whisper, HyperFrames, Resolve, and
  Depth Anything V2.
- ComfyUI remains offline and is not part of the primary approved lane.
- External paid provider execution is approved by the user, but not directly
  callable from the current Codex tool surface.
- Local fallback narration and caption generation may be used for timing preview
  only and must not be mislabeled as ElevenLabs output.

## Mission Bundle

- Bundle declaration: `outputs/missions/yash_self_investment/MISSION_MEDIA_OUTPUT_BUNDLE.txt`
- Packet directory: `outputs/missions/yash_self_investment/packets/`
- Support directory: `outputs/missions/yash_self_investment/support/`
- Lane directories:
  - `voice/`
  - `music/`
  - `sfx/`
  - `images/`
  - `broll/`
  - `aroll/`
  - `hyperframes/`
  - `davinci/`
  - `proofs/`

## Honest Status Boundary

Starting production support does not mean provider renders are complete.
Only generated artifacts that exist on disk may be called complete.
