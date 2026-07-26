# Phase 13A Cinema Brain Surface Alignment Audit

## Scope
This audit reviews the repo's cinema-facing brain surfaces across directors, agents, subagents, skills, subskills, and `.agents/skills`.

The goal is to answer a narrow question:

`film_route_registry_pair_exists=true`
`film_selector_mode_exists=true`
`FILM_SCREENPLAY_GENERATION_selector_bound=true`
`runtime_proof_claimed=false`
`cinema_brain_alignment_proven=false`

This is a repo-surface audit only. Selector binding exists, but selector binding alone is not cinema engine completion.

## Surface Family Summary

| Surface family | Matched files | Dominant evidence | Classification |
|---|---:|---|---|
| directors | 28 | Cinematic directors exist, but many director files still resolve to distribution, production, research, approval, or pipeline governance | `MIXED_PARTIAL_WITH_CONTENT_DRIFT` |
| agents | 32 | Most agents route through script_generation, full_video_pipeline, media_factory_handoff, or context_engineering rather than a cinema-native screenplay core | `CONTENT_ENGINE_DRIFT` |
| subagents | 11 | Subagents are support lanes and route support, not cinema-native core brain surfaces | `CONTENT_ENGINE_DRIFT` |
| skills | 241 | A small cluster is cinema-adjacent, but the bulk still optimizes content packaging, editing, publishing, SEO, or media factory support | `PARTIAL_WITH_STRONG_CONTENT_DRIFT` |
| subskills | 55 | Subskills are mostly support mechanics for content/video pipelines | `CONTENT_ENGINE_DRIFT` |
| `.agents/skills` | 3 | Shadow content, context, and media factory skills are powerful, but they are still pipeline planning surfaces rather than cinema-native screenplay architecture | `CONTENT_ENGINE_DRIFT` |

## What the evidence says

Strong cinema-adjacent signals exist in the repo, especially in:

- `skills/system_intelligence/M-086-cinematic-shot-planner.py`
- `skills/system_intelligence/M-088-scene-composition-engine.py`
- `skills/system_intelligence/M-089-motion-director.py`
- `directors/cinematic/*.md`

But the broader surface still leans toward content-engine behavior:

- `agents/krishna/krishna_agent.py` still carries `script_generation` and `full_video_pipeline`.
- `skills/media_video/M-218-video-editing-script.skill.md` is editing and packaging oriented.
- `skills/media_audio/M-231-voiceover-direction-script.skill.md` is voice-context support, not screenplay-core ownership.
- `.agents/skills/shadow-content-orchestration/SKILL.md` and `.agents/skills/shadow-context-engineering/SKILL.md` are explicitly content/script/media orchestration surfaces.
- `subagents/wf_*` and `subagents/cwf_*` are support lanes, not a cinema-native core brain.

## Verdict

`overall_verdict=CINEMA_BRAIN_ALIGNMENT_PARTIAL_REQUIRES_PATCHING`

Reason:

1. The film route registry pair exists.
2. The selector mode exists and the film route is selector-bound.
3. The current surfaces prove pipeline capability, but not a fully cinema-native brain surface.
4. Runtime proof is still blocked until cinema brain alignment is actually implemented and verified.

## Hard boundary

`repo_selector_binding_alone_is_not_cinema_engine_completion=true`

`runtime_proof_blocked_until_cinema_brain_alignment=true`

