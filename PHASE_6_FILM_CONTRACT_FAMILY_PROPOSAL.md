# Phase 6 Film Contract Family Proposal

## 1. Proposed film contract families
```text
runtime_contracts/film/
runtime_contracts/film/route/
runtime_contracts/film/story_structure/
runtime_contracts/film/character/
runtime_contracts/film/scene_dramaturgy/
runtime_contracts/film/dialogue/
runtime_contracts/film/visual_language/
runtime_contracts/film/directorial_style/
runtime_contracts/film/production/
runtime_contracts/film/validation/
```

## 2. Proposed film contracts
```text
FILM_ROUTE_INTENT_CONTRACT.md
FILM_SCREENPLAY_STRUCTURE_CONTRACT.md
SAVE_THE_CAT_BEAT_SHEET_CONTRACT.md
THREE_ACT_EIGHT_SEQUENCE_CONTRACT.md
CHARACTER_ARC_AND_DESIRE_CONTRACT.md
CHARACTER_WEB_AND_OPPOSING_FORCE_CONTRACT.md
SCENE_DRAMATURGY_CONTRACT.md
DIALOGUE_SUBTEXT_CONTRACT.md
VISUAL_MOTIF_AND_IMAGE_SYSTEM_CONTRACT.md
MISE_EN_SCENE_BLOCKING_COMPOSITION_CONTRACT.md
CAMERA_LANGUAGE_CONTRACT.md
SOUND_MOTIF_CONTRACT.md
PERFORMANCE_DIRECTION_CONTRACT.md
SCREENPLAY_FORMAT_CONTRACT.md
FILM_CONTINUITY_CONTRACT.md
FILM_OUTPUT_PACKET_CONTRACT.md
SHORT_FILM_VALIDATION_CONTRACT.md
FEATURE_FILM_VALIDATION_CONTRACT.md
FILM_CONTENT_ROUTE_SEPARATION_CONTRACT.md
```

## 3. Reuse map

| Existing contract/family | Current bias | Film-mode use | Downstream retained? | Recommendation |
|---|---|---|---|---|
| Task routing / dependency / state / proof governance | Generic | Reuse as the legal spine for film routes | Yes | Reuse as-is |
| Script quality / content engineering / beat map / story engine | Content-first | Reuse concepts, but duplicate into film-mode contracts | Some content behavior should remain downstream | Duplicate for film mode |
| Layman command gateway | Content-route default | Add a cinema-aware trigger path | Yes | Reuse with film mode |
| Source-aware decision / source quality | Generic | Reuse for film research and factual claims | Yes | Reuse as-is |
| Media factory / visual draft / voice / editing packets | Downstream production | Reuse only after screenplay approval | Yes | Move downstream |
| No fake pass / output mode / consolidated output | Generic governance | Reuse unchanged | Yes | Reuse as-is |

## 4. Old-to-new responsibility map

| Existing contract responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| Route classification for `SCRIPT_GENERATION` | YouTube/content-first | `FILM_ROUTE_INTENT_CONTRACT` | Yes, content route remains | Film prompts need a dedicated route |
| Hook density, recurring re-hooks, CTA cadence | Creator retention | Scene escalation, act-turn pacing | Yes | Keep in content mode only |
| Dynamic timed beat map | Content timing | Scene / sequence beat map | Yes | Film timing should be scene-based, not retention-based |
| Cinematic short story block inside YouTube scripts | Content bridge | Film opening movement / dramatic launch | No | The film route should not depend on YouTube framing |
| Visual/voice/editing packaging | Downstream media | Film adaptation handoff | Yes | Useful only after screenplay is locked |
| Source honesty and claim mapping | Generic | Film research truth layer | Yes | Reuse unchanged |

## 5. Missing film contract capability check
The audited contract layer does not yet contain dedicated contracts for:
- film route intent
- film screenplay structure
- Save the Cat beat sheet
- three-act / eight-sequence
- Hero’s Journey
- Dan Harmon Story Circle
- McKee scene value turns
- Syd Field plot points
- character want vs need
- character flaw and transformation
- character web
- antagonistic force
- scene objective / obstacle / tactic
- scene value turn
- dialogue subtext
- dialogue voice distinctness
- mise-en-scène
- blocking
- composition
- lens grammar
- camera movement
- visual motif
- sound motif
- performance direction
- screenplay format
- film continuity
- short film validation
- feature film validation
- film output packet
- film-vs-content route separation

## 6. Interface to Phase 7 route manifests and route slices
Phase 7 should inspect and propose:
- `registries/route_manifests/film_screenplay_generation.yaml`
- `registries/route_slices/film_screenplay_generation.registry_slice.yaml`
- `registries/route_manifests/film_story_development.yaml`
- `registries/route_slices/film_story_development.registry_slice.yaml`
- `registries/route_manifests/cinematic_director_plan.yaml`
- `registries/route_slices/cinematic_director_plan.registry_slice.yaml`
- `registries/route_manifests/feature_film_production_pipeline.yaml`
- `registries/route_slices/feature_film_production_pipeline.registry_slice.yaml`
- `registries/route_manifests/film_release_distribution.yaml`
- `registries/route_slices/film_release_distribution.registry_slice.yaml`

It should also verify how the new film routes stay separate from:
- `SCRIPT_GENERATION`
- `VISUAL_MEDIA_PLAN`
- `VOICE_CONTEXT`
- `EDITING_PACKAGING`
- `MEDIA_FACTORY_HANDOFF`
- `FULL_VIDEO_PIPELINE`

## 7. Future patch plan
Phase 7 should inspect route manifests and route slices only after the film contracts are defined. The purpose is to bind the future film route to the reusable governance spine while keeping content, visual, and distribution flows separated by design.

