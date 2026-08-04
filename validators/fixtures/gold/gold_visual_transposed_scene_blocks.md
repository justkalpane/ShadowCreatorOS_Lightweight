# Gold Fixture: Visual Transposed Scene Blocks

## Route Verification & System Locks

route_id=MEDIA_FACTORY_HANDOFF
task_mode=script_plus_visual_generation_draft
script_integrity_lock=PASS
visual_plan_integrity_lock=PASS

## Assumption Verification Table

| assumption | status | evidence |
| --- | --- | --- |
| locked script present | PASS | final script reference |
| planning only | PASS | provider execution disabled |

## Asset Generation Order

1. Master voice reference
2. Scene prompt packets
3. Storyboard stills
4. Cinematic B-roll
5. Motion graphics overlays
6. DaVinci/FFmpeg assembly packet
7. QC/proof registry

## Scene-by-scene Transposed Scene Blocks

### SC-01 — Stop Scrolling Hook
scene_id=SC-01
timecode=0:00-0:15
duration_seconds=15
method=A-roll + motion graphics

> Script: Stop scrolling. Stop hallucinating. Your future is not loading by itself.

| Layer | Detail |
| --- | --- |
| Visual | Presenter close-up, phone reflection in eyes, dark room with controlled warm rim light. |
| Motion | Slow push-in for 6 seconds, then punch-in cut on "future". |
| Audio/SFX | Low phone-scroll ticks, sub hit at 0:07, short riser into scene cut. |
| Editing | V1 A-roll, V3 kinetic text overlay, A2 SFX ticks, captions safe-zone centered. |
| Provider/Local Boundary | Planning-only; no HeyGen, Runway, FFmpeg, or DaVinci execution claimed. |
| Proof/QC | Requires generated asset path and proof JSON before execution status can become PASS. |
| Reasoning | Directly attacks passive scrolling and opens the self-investment loop. |

### SC-02 — Yash Self-Investment Story
scene_id=SC-02
timecode=0:15-1:15
duration_seconds=60
method=cinematic B-roll

> Script: A young dreamer steps into Bengaluru with almost nothing except discipline.

| Layer | Detail |
| --- | --- |
| Visual | Young Indian actor silhouette at bus stand, theater backstage, warm dust beams, grounded realism. |
| Motion | Slow handheld walk-in, dissolve to sweeping stage floor, final dolly toward rehearsal mirror. |
| Audio/SFX | Bus brake hiss, theater room tone, wood floor sweep, restrained orchestral swell. |
| Editing | V2 cinematic B-roll, A3 environmental SFX, A1 voiceover lead, color grade teal shadows/gold highlights. |
| Provider/Local Boundary | Planning-only B-roll prompt; provider call requires explicit approval. |
| Proof/QC | Needs source ledger for biographical claims and generated clip registry before production PASS. |
| Reasoning | Converts the motivational claim into a visual proof arc without pretending assets exist. |

## Media Method Distribution

| Method | Seconds | Share |
| --- | ---: | ---: |
| A-roll | 90 | 29.5% |
| cinematic B-roll | 40 | 13.1% |
| motion graphics | 175 | 57.4% |

## B-roll Ratio Breakdown

total_runtime_seconds=305
cinematic_broll_seconds=40
required_cinematic_broll_seconds=37

## Provider Honesty Gate

provider_execution_allowed=false
media_artifacts_claimed=false
no_asset_creation_claim=true

## Local/Cloud/Hybrid Boundary

planning_only=true
local_engine_handoff=not yet executed

## DaVinci/FFmpeg Assembly Plan

V1=A-roll
V2=cinematic B-roll
V3=motion graphics
A1=voice
A2=music
A3=SFX

## QC/Proof Registry

proof_status=pending
proof_json_required=true

## Final Classification

status=PACKET_READY

