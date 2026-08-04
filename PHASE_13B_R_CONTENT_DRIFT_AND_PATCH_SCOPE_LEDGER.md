# Phase 13B-R Content Drift and Patch Scope Ledger

## 1. Objective

This ledger identifies YouTube/content-creation drift and converts it into precise patch scope for the next implementation phase.

## 2. Drift table

| Drift ID | File/path | Surface family | Drift evidence | Why it conflicts with Cinema Engine | Patch required | Priority |
|---|---|---|---|---|---|---|
| D-001 | `directors/distribution/saraswati.md` | director | content repurposing, audience expansion, channel optimization, platform specs | the surface is about multiplying content, not cinema-native story craft | isolate distribution from cinema-core and add language/music clarity | P0 |
| D-002 | `directors/supreme_vision/krishna.md` | director | YouTube, retention, thumbnail, script_generation, full_video_pipeline | counsel/strategy is buried under content-routing language | move counsel, subtext, and dharma logic into cinema-core framing | P0 |
| D-003 | `skills/publishing/D-501-platform-metadata-generator.py` | skill | platform metadata, hashtags, platform-specific copy, publish optimization | platform packaging is content-engine logic, not screenplay craft | move packaging behind cinema-core boundary | P0 |
| D-004 | `skills/system_intelligence/M-080-shorts-generator.py` | skill | shorts generator, hook/retention gate, script_generation route | shorts are a content route, not a cinema-native screenplay owner | isolate shortform optimization from film brain | P0 |
| D-005 | `skills/script_intelligence_army/M-047-thumbnail-psychology-engine.py` | skill | thumbnail psychology, platform packages, caption/thumbnail gates | thumbnail psychology is distribution conversion, not film storytelling | keep packaging downstream only | P0 |
| D-006 | `skills/script_intelligence_army/M-042-editing-optimization-engine.py` | skill | editing optimization, re-hook sync, platform-safe zone | editing optimization is useful, but the file is still content-retention centric | separate film editing rhythm from YouTube retention loops | P1 |
| D-007 | `skills/sub_skills/SS-108-youtube-publish-oauth-guard.subskill.md` | subskill | YouTube publish guard, OAuth, publish lanes | publishing guard is operational content infrastructure, not cinema brain | keep as downstream guard only | P1 |
| D-008 | `skills/sub_skills/SS-244-retention-loop-engine.py` | subskill | recurring re-hooks, 25-second cadence, retention loop law | retention-loop logic belongs to content-engine packaging, not cinema-native story architecture | isolate as content-route guardrail | P1 |
| D-009 | `skills/media_production/A-405-media-qa-validator.py` | skill | media package validation, thumbnails, timing alignment, platform readiness | validates packaged media, not the screenplay brain | keep as downstream quality validator | P1 |
| D-010 | `skills/media_production/A-402-visual-asset-planner.py` | skill | visual asset planning, platform content package output | asset planning supports production, but still centers content packaging | move behind story/scene authoring | P1 |
| D-011 | `skills/media_video/M-218-video-editing-script.skill.md` | skill | editing packaging, publishing, final MP4 path | editing packager is not cinema-native story design | preserve only as downstream edit lane | P1 |
| D-012 | `directors/strategy/narada.md` | director | operations orchestrator, distribution coordinator, data ingestion master | operations and analytics are not cinema-native department ownership | keep as execution support, not story brain | P1 |
| D-013 | `directors/supreme_vision/shakti.md` | director | audience multiplier, engagement accelerator, viral acceleration | amplification is content growth, not cinematic force/transformation | recast as force/protection, not just engagement | P1 |
| D-014 | `skills/system_intelligence/M-087-lighting-designer.py` | skill | visual context and image generation, but still tied to content-route workflows | lighting is cinema-adjacent, but the file is not yet a cinema-core department surface | keep, but tighten its film-grammar role | P2 |
| D-015 | `subagents/wf_200/wf_200_sub_agent.py` | subagent | script_generation / full_video_pipeline support lane | generic support lane, not a cinema-native department | no direct patch until cinema responsibilities are assigned | P2 |
| D-016 | `subagents/wf_400/wf_400_sub_agent.py` | subagent | voice_context / media_factory_handoff / visual_media_plan | downstream media support, not the cinema brain itself | keep as handoff support | P2 |
| D-017 | `.agents/skills/shadow-content-orchestration/SKILL.md` | skill | explicit YouTube / shorts / social orchestration | strongly content-engine oriented | isolate as content-route skill only | P1 |
| D-018 | `.agents/skills/shadow-context-engineering/SKILL.md` | skill | mandatory cinematic story block for YouTube scripts | still a content-script orchestration law rather than cinema-native ownership | keep as context-engine support, not cinema brain | P2 |
| D-019 | `.agents/skills/shadow-media-factory/SKILL.md` | skill | storyboard, B-roll, handoff, Media Factory output | production handoff support, not story architecture | preserve downstream boundary only | P2 |

## 3. Patch scope list

### P0 immediate blockers

- `directors/distribution/saraswati.md`
- `directors/supreme_vision/krishna.md`
- `skills/publishing/D-501-platform-metadata-generator.py`
- `skills/system_intelligence/M-080-shorts-generator.py`
- `skills/script_intelligence_army/M-047-thumbnail-psychology-engine.py`

### P1 required implementation

- `skills/script_intelligence_army/M-042-editing-optimization-engine.py`
- `skills/sub_skills/SS-108-youtube-publish-oauth-guard.subskill.md`
- `skills/sub_skills/SS-244-retention-loop-engine.py`
- `skills/media_production/A-405-media-qa-validator.py`
- `skills/media_production/A-402-visual-asset-planner.py`
- `skills/media_video/M-218-video-editing-script.skill.md`
- `directors/strategy/narada.md`
- `directors/supreme_vision/shakti.md`

### P2 recommended improvements

- `skills/system_intelligence/M-087-lighting-designer.py`
- `subagents/wf_200/wf_200_sub_agent.py`
- `subagents/wf_400/wf_400_sub_agent.py`
- `.agents/skills/shadow-context-engineering/SKILL.md`
- `.agents/skills/shadow-media-factory/SKILL.md`

### P3 optional refinement

- `directors/cinematic/garuda.md`
- `directors/cinematic/hanuman.md`
- `directors/cinematic/varuna.md`
- `directors/research/vyasa.md`
- `directors/research/valmiki.md`
- `directors/research/parashara.md`
- `agents/hanuman/hanuman_agent.py`
- `agents/vyasa/vyasa_agent.py`
- `agents/valmiki/valmiki_agent.py`
- `agents/varuna/varuna_agent.py`

