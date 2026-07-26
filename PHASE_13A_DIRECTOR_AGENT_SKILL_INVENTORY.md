# Phase 13A Director / Agent / Skill Inventory

## Legend

- `CINEMA_NATIVE_READY`: explicitly cinema-native surface, or close enough to justify cinema-core ownership
- `PARTIAL_CINEMA_NATIVE`: cinema-adjacent, but still mixed with broader pipeline or content behavior
- `CONTENT_ENGINE_DRIFT`: supports content, media, publishing, or pipeline mechanics rather than cinema-core ownership
- `MISSING_CINEMA_SURFACE`: no direct cinema-native evidence in the inspected surface

## Inventory

| Surface ID | Family | File / path | Exists? | Cinema relevance evidence | Classification | Patch priority | Notes |
|---|---|---|---|---|---|---|---|
| D-CIN-01 | director | `directors/cinematic/garuda.md` | yes | Cinematic director, but route families still include `full_video_pipeline`, `editing_packaging`, and approval/repo-write behavior | `PARTIAL_CINEMA_NATIVE` | high | Strong visual/media production support, not a complete cinema brain |
| D-CIN-02 | director | `directors/cinematic/nataraja.md` | yes | Explicit cinematic + media factory handoff and visual media plan support | `PARTIAL_CINEMA_NATIVE` | high | Useful for downstream cinematic orchestration |
| D-CIN-03 | director | `directors/cinematic/varuna.md` | yes | Visual media plan and media factory handoff surfaces are present | `PARTIAL_CINEMA_NATIVE` | high | Pipeline support, not screenplay core |
| D-CIN-04 | director | `directors/cinematic/hanuman.md` | yes | Cinematic acceleration namespace exists, but route families remain quality gate / full video pipeline | `PARTIAL_CINEMA_NATIVE` | medium | Speed layer, not story architecture |
| D-DIST-01 | director | `directors/distribution/kama.md` | yes | Distribution / conversion / growth language dominates | `CONTENT_ENGINE_DRIFT` | low | Good for publishing, not cinema-core |
| D-PROD-01 | director | `directors/production/agni.md` | yes | Production acceleration and timeline compression | `CONTENT_ENGINE_DRIFT` | low | Useful execution layer, not cinema-native |
| D-RESEARCH-01 | director | `directors/research/valmiki.md` | yes | Research and cinematic reconstruction support | `PARTIAL_CINEMA_NATIVE` | medium | Strong research support, still not the cinema brain itself |
| D-SUP-01 | director | `directors/supreme_vision/krishna.md` | yes | Supreme orchestration and arbitration, with script_generation/full_video_pipeline routing | `CONTENT_ENGINE_DRIFT` | low | Governance layer, not cinema-native craft |
| A-KRI-01 | agent | `agents/krishna/krishna_agent.py` | yes | Route families include `script_generation` and `full_video_pipeline` | `CONTENT_ENGINE_DRIFT` | medium | Strong orchestration support, but content-engine lineage remains |
| A-MAYA-01 | agent | `agents/maya/maya_agent.py` | yes | Palette presets and media factory style support | `PARTIAL_CINEMA_NATIVE` | medium | Visually helpful, but still a media pipeline surface |
| A-NAT-01 | agent | `agents/nataraja/nataraja_agent.py` | yes | Route families include `media_factory_handoff`, `visual_media_plan`, and `full_video_pipeline` | `CONTENT_ENGINE_DRIFT` | medium | Production support, not cinema-core |
| A-VC-01 | agent | `agents/varuna/varuna_agent.py` | yes | Context engineering and handoff routing | `CONTENT_ENGINE_DRIFT` | medium | Good glue, not film-story ownership |
| SA-WF-200 | subagent | `subagents/wf_200/wf_200_sub_agent.py` | yes | Generic support with `script_generation` / `full_video_pipeline` in route families | `CONTENT_ENGINE_DRIFT` | low | Support lane only |
| SA-WF-400 | subagent | `subagents/wf_400/wf_400_sub_agent.py` | yes | Voice/context/media-factory support | `CONTENT_ENGINE_DRIFT` | low | Support lane only |
| SA-WF-500 | subagent | `subagents/wf_500/wf_500_sub_agent.py` | yes | Editing packaging and general support | `CONTENT_ENGINE_DRIFT` | low | Support lane only |
| SA-CWF-410 | subagent | `subagents/cwf_410/cwf_410_sub_agent.py` | yes | Visual media plan / media factory handoff support | `CONTENT_ENGINE_DRIFT` | low | Support lane only |
| SA-CWF-420 | subagent | `subagents/cwf_420/cwf_420_sub_agent.py` | yes | Avatar video / media factory handoff support | `CONTENT_ENGINE_DRIFT` | low | Support lane only |
| SA-CWF-430 | subagent | `subagents/cwf_430/cwf_430_sub_agent.py` | yes | Voice-context support | `CONTENT_ENGINE_DRIFT` | low | Support lane only |
| S-M086 | skill | `skills/system_intelligence/M-086-cinematic-shot-planner.py` | yes | Directly cinematic shot planning; route families include `video_context`, `avatar_video_context`, `full_video_pipeline` | `PARTIAL_CINEMA_NATIVE` | very high | One of the strongest cinema-adjacent skills |
| S-M087 | skill | `skills/system_intelligence/M-087-lighting-designer.py` | yes | Lighting designer for visual context | `PARTIAL_CINEMA_NATIVE` | high | Important visual grammar support |
| S-M088 | skill | `skills/system_intelligence/M-088-scene-composition-engine.py` | yes | Scene composition and validator bindings for video context | `PARTIAL_CINEMA_NATIVE` | very high | Strong scene-level support |
| S-M089 | skill | `skills/system_intelligence/M-089-motion-director.py` | yes | Motion direction for video/avatar/full pipeline | `PARTIAL_CINEMA_NATIVE` | very high | Strong movement grammar support |
| S-M218 | skill | `skills/media_video/M-218-video-editing-script.skill.md` | yes | Editing and packaging for script_generation / full_video_pipeline | `CONTENT_ENGINE_DRIFT` | medium | Good production support, not cinema-native craft |
| S-M231 | skill | `skills/media_audio/M-231-voiceover-direction-script.skill.md` | yes | Voice context and lineage summary support | `PARTIAL_CINEMA_NATIVE` | medium | Useful for cinematic voice, but still pipeline-led |
| S-A404 | skill | `skills/media_production/A-404-media-package-assembler.skill.md` | yes | Media packaging and lineage support | `CONTENT_ENGINE_DRIFT` | low | Assembly tool, not cinema core |
| S-SHADOW-CC | `.agents/skill` | `.agents/skills/shadow-content-orchestration/SKILL.md` | yes | Explicit content/script/YouTube/shorts/social orchestration | `CONTENT_ENGINE_DRIFT` | low | Powerful, but content-engine framed |
| S-SHADOW-CE | `.agents/skill` | `.agents/skills/shadow-context-engineering/SKILL.md` | yes | Mandatory cinematic story block and scene sync matrix for content routes | `CONTENT_ENGINE_DRIFT` | low | Strong planning support, not cinema-core |
| S-SHADOW-MF | `.agents/skill` | `.agents/skills/shadow-media-factory/SKILL.md` | yes | Storyboard, B-roll, local handoff, and media factory output | `CONTENT_ENGINE_DRIFT` | low | Production handoff surface, not cinema-native ownership |

## Inventory conclusion

The repo has meaningful cinematic support, but it is still split across content-engine, media-factory, and production governance surfaces.

The cinema-native pieces are present, yet they are not enough on their own to claim full alignment of the brain surface.

The patch priority should be to lift the partial cinema-native clusters into a clearer cinema-core model and separate them cleanly from content-engine drift.

