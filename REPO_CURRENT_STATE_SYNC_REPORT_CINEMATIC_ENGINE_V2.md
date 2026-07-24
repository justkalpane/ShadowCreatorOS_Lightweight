# Repo Current State Sync Report - Cinematic Engine V2

## Bottom Line

The repo still has a strong content-engineering and media-production stack, but the core screenplay route is `SCRIPT_GENERATION`, which remains explicitly YouTube/content-first. A true cinema-first screenplay route family is still missing.

## Synchronization Table

| Handoff finding | Repo path checked | Evidence found | Current repo status | Classification | Risk if ignored | Recommended action | Patch priority |
|---|---|---|---|---|---|---|---|
| `SCRIPT_GENERATION` is still content-first and YouTube-biased | `registries/route_manifests/script_generation.yaml`, `registries/route_slices/script_generation.registry_slice.yaml`, `registries/task_intent_routing_matrix.yaml` | Trigger terms include `YouTube script`, `Shorts script`, `reel script`, `voiceover script`; recurring re-hooks are defined for `3-10 minute YouTube scripts`; `CINEMATIC_SHORT_STORY_BLOCK` is present but inside a YouTube/content route | Core route remains content-first with cinematic overlays | CONFIRMED | Short-film / screenplay requests keep landing in the wrong lane | Split the route family into film-core and social/content downstream lanes | P0 |
| Dedicated film screenplay route is missing | `rg --files | rg 'FILM_SCREENPLAY_GENERATION|SHORT_FILM|FEATURE_FILM|CINEMATIC_SCREENPLAY|FILM_STORY_DEVELOPMENT|CINEMATIC_DIRECTOR_PLAN|FEATURE_FILM_PRODUCTION_PIPELINE'` | No matches returned | No film route family exists in the live repo | MISSING | Add `FILM_SCREENPLAY_GENERATION` and related route manifests/slices | P0 |
| Platform/content cadence laws still dominate the script contract stack | `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`, `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`, `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md`, `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md` | YouTube defaults, opening hooks, recurring re-hooks, CTA hook, 25-second cadence, and `CINEMATIC_SHORT_STORY_BLOCK` rules are all defined around 3-10 minute YouTube scripts | Strong content engineering, but still platform-led | CONFIRMED | Film requests will inherit retention-first behavior instead of screenplay-first behavior | Refactor core film routes and keep platform cadence in downstream distribution only | P0 |
| Cinema/production layers already exist and should be preserved | `registries/route_manifests/media_factory_handoff.yaml`, `registries/route_manifests/full_video_pipeline.yaml`, `registries/route_manifests/voice_context.yaml`, `registries/route_manifests/editing_packaging.yaml` | Media factory, full video pipeline, voice context, and editing packaging are already modeled as downstream/production lanes | Reusable downstream stack is present | CONFIRMED | Overwriting these layers would destroy useful production capability | Preserve these layers as downstream distribution and production adapters | P1 |
| Director layer has cinematic foundations but also platform drift | `directors/DIRECTOR_REGISTRY_MANIFEST.yaml`, `directors/supreme_vision/krishna.md`, `directors/strategy/chanakya.md`, `directors/strategy/narada.md`, `directors/distribution/saraswati.md`, `directors/strategy/durga.md`, `directors/production/maya.md`, `directors/cinematic/nataraja.md` | Registry contains cinematic council and production council; search hits show `script_generation`, `platform`, `creator`, `viral`, `engagement`, `YouTube`, `Instagram`, `TikTok`, and platform-fit language in several high-authority directors | Mixed state: cinema-capable, but not film-mode separated | PARTIAL | Platform-first reasoning will keep leaking into core story generation | Add film_mode / distribution_mode separation and refactor high-authority wording | P1 |
| Reusable repo-law contracts are strong | `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`, `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md`, `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`, `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`, `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`, `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md` | Route classification, route expansion, consumption ledgers, active precedence, output mode, and wrapper-required command expansion are all already defined | Governance and routing backbone is reusable | CONFIRMED | Rebuilding this from scratch would be wasteful | Reuse these laws as the spine of the film conversion | P1 |
| Film-specific contracts are missing | `rg --files | rg 'FILM_SCREENPLAY_STRUCTURE|SAVE_THE_CAT|CHARACTER_ARC|SCENE_DRAMATURGY|DIALOGUE_SUBTEXT|CINEMATIC_COMPOSITION|DIRECTORIAL_STYLE|VISUAL_MOTIF|PERFORMANCE_DIRECTION|SHORT_FILM_VALIDATION'` | No matches returned | No filmcraft contract set exists yet | MISSING | The repo cannot validate screenplay craft at a film level | Add the film contract family | P0 |
| Film-specific validators are missing | `validators/`, `rg --files | rg 'validate_film|validate_save_the_cat|validate_character_arc|validate_scene_turns|validate_dialogue_subtext|validate_visual_motif|validate_directorial_composition|validate_short_film'` | No film-specific validators were found | Validation exists for content/media routes, not for screenplay craft | MISSING | Film outputs will not be mechanically checked | Add screenplay validators and film-contamination checks | P1 |
| Governed Shadow action surface still points to a placeholder host | `openapi/custom_gpt_shadow_orchestrator_actions.openapi.yaml` | `servers` points at `https://shadow-gateway.example.com`; GitHub read surface points at `https://api.github.com` | Read-only GitHub surface is real; governed Shadow surface is still placeholder-based | CONFIRMED | Live governed runtime calls will continue to fail until a real host exists | Replace placeholder Shadow host with a durable HTTPS bridge | P0 |

## Direct Answers

### Does the repo currently have a true cinema-first screenplay generation route?

No. `FILM_SCREENPLAY_GENERATION` and the other film route names do not exist in the current repo.

### Does the repo currently route short film / screenplay prompts into YouTube/content script generation?

Yes. `SCRIPT_GENERATION` is still triggered by `write script`, `YouTube script`, `Shorts script`, `reel script`, and `voiceover script`.

### Which director files contain YouTube/social/platform drift?

Most clearly:

- `directors/supreme_vision/krishna.md`
- `directors/strategy/chanakya.md`
- `directors/strategy/narada.md`
- `directors/strategy/durga.md`
- `directors/distribution/saraswati.md`
- `directors/production/maya.md`

The drift shows up as creator-fit, platform-fit, viral, engagement, platform optimization, YouTube/Instagram/TikTok, and multi-platform distribution language.

### Which directors already support cinematic or production-grade behavior?

Strongly supported:

- `directors/cinematic/nataraja.md`
- `directors/production/maya.md`
- `directors/production/tumburu.md`
- `directors/production/arjuna.md`
- `directors/production/vishwakarma.md`
- `directors/cinematic/garuda.md`
- `directors/cinematic/varuna.md`
- `directors/cinematic/indra.md`
- `directors/supreme_vision/brahma.md`

These are the best reuse candidates for a film-mode stack.

### Which agents, subagents, and skills likely need film-mode separation?

The current `SCRIPT_GENERATION` slice binds agents and skills around content retention and platform scripting, so the following are the most likely split candidates:

- route-bound agents: `krishna`, `aruna`, `vyasa`, `valmiki`, `saraswati`, `yama`
- route-bound skills: hook optimization, retention engineering, emotional spike, story momentum, final script packaging
- route-bound subskills: hook variation, open loop generation, pacing controller, retention loop engine, cliffhanger design

The media-production skills under `media_factory_handoff`, `visual_media_plan`, `visual_media_generation_draft`, `voice_context`, and `editing_packaging` should stay downstream rather than be turned into screenplay-core law.

### Which contracts are reusable?

Reusable as-is or with light adaptation:

- `TASK_INTENT_ROUTING_CONTRACT.md`
- `ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md`
- `DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`
- `ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`
- `SHADOW_OUTPUT_MODE_CONTRACT.md`
- `LAYMAN_COMMAND_GATEWAY_CONTRACT.md`
- `PROVIDER_HANDOFF_CONTRACT.md`
- `LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md`
- `MEDIA_FACTORY_HANDOFF` / `FULL_VIDEO_PIPELINE` route structure

### Which contracts are platform-biased?

Most platform-biased:

- `CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
- `SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`
- `TASK_EXECUTION_STATE_MACHINE_CONTRACT.md`
- `DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md`
- `MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md`
- `registries/route_manifests/script_generation.yaml`
- `registries/route_manifests/editing_packaging.yaml`

## Evidence Summary By Topic

- **Governance/runtime boundary:** repo law is strong; runtime proof is separate and not inventable.
- **Current bias:** the route core is still content-engineering-first.
- **Film gap:** film route family, contracts, validators, and schemas are missing.
- **Preservation target:** media factory and distribution logic should remain downstream.
- **Refactor target:** route identity and director-language contamination in the script core.

## Recommended Action

Add a dedicated film route family, separate film-mode from distribution-mode, and keep the current content/media stack intact as downstream support.

