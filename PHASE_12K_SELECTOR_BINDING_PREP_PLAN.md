# Phase 12K Selector Binding Prep Plan

## 1. Objective
Prepare selector binding for `FILM_SCREENPLAY_GENERATION` without modifying the selector.

## 2. Evidence reviewed

| Evidence | File/path inspected | Status | Notes |
|---|---|---|---|
| Phase 12J decision packet | `PHASE_12J_ACTIVE_REGISTRATION_DECISION_PACKET.md` | Reviewed | Confirms owner decision is required before any live activation |
| Phase 12J owner options | `PHASE_12J_OWNER_DECISION_OPTIONS.md` | Reviewed | Recommends selector-binding preparation, not active activation |
| Phase 12J next phase | `PHASE_12J_NEXT_PHASE_RECOMMENDATION.md` | Reviewed | Names `Phase 12K` as the next safe phase |
| Phase 12I lint report | `PHASE_12I_INACTIVE_ROUTE_DRAFT_STATIC_LINT_REPORT.md` | Reviewed | Inactive draft files parsed cleanly and stayed draft-only |
| Phase 12I collision review | `PHASE_12I_ROUTE_COLLISION_REVIEW.md` | Reviewed | Collision review passed for inactive drafts |
| Phase 12I blocker ledger | `PHASE_12I_ACTIVATION_BLOCKER_LEDGER.md` | Reviewed | Shows route selector and activation work are still blocked |
| Phase 12H inactive drafts | `route_drafts/film_screenplay_generation/README.md`, `film_screenplay_generation.manifest.draft.yaml`, `film_screenplay_generation.registry_slice.draft.yaml`, `phase_12h_inactive_route_draft_manifest.json` | Reviewed | Still inactive, unregistered, and unbound |
| Active selector | `runtime/state/route_chain_mode_selector.yaml` | Reviewed | Content-first `script_only` remains the active default |
| Active content route | `registries/route_manifests/script_generation.yaml`, `registries/route_slices/script_generation.registry_slice.yaml` | Reviewed | `SCRIPT_GENERATION` remains active and canonical |
| Downstream active routes | `registries/route_manifests/full_video_pipeline.yaml`, `registries/route_slices/full_video_pipeline.registry_slice.yaml`, `registries/route_manifests/media_factory_handoff.yaml`, `registries/route_slices/media_factory_handoff.registry_slice.yaml` | Reviewed | Downstream production and handoff routes remain separate |
| Phase 12A fixtures | `tests/fixtures/phase_12a_fixture_manifest.json` | Reviewed | Route-selection, content-preservation, downstream-handoff, and no-fake-PASS fixtures already exist |
| Phase 12B schemas | `schemas/film/phase_12b_schema_manifest.json` | Reviewed | Film schema skeletons exist but are not enforced |
| Phase 12C validators | `validators/film/phase_12c_validator_manifest.json` | Reviewed | Film validators exist but are not bound |
| Phase 12D contracts | `runtime_contracts/film/phase_12d_contract_manifest.json` | Reviewed | Film contract prep exists but is not bound |
| Phase 12E route prep | `route_drafts/film_screenplay_generation/phase_12h_inactive_route_draft_manifest.json` | Reviewed | Route draft files are not active registry files |
| Phase 12F selector plan | `PHASE_12F_ROUTE_SELECTOR_INTEGRATION_PLAN.md` | Reviewed | Selector modification was intentionally deferred |
| Phase 12G registration prep | `PHASE_12G_ACTIVE_ROUTE_REGISTRATION_PREP_PLAN.md` | Reviewed | Active registration was still framed as future work |

## 3. Future selector binding model
Future selector behavior should separate four classes of intent:

- Film-core triggers: short film, feature film, screenplay, shooting script, cinematic screenplay, film scene, dialogue scene, character arc film, animated short film, docudrama film, real-incident short film.
- Content-route triggers: YouTube script, Shorts script, Instagram reel script, TikTok script, voiceover script, explainer video script, content script, creator video, hook-focused script, retention-focused script.
- Downstream-only triggers: trailer, teaser, thumbnail, title pack, social cutdown, edit package, visual media plan, voice context, media factory handoff, full video pipeline.
- Ambiguous triggers: cinematic explainer for YouTube, 5-minute cinematic video, documentary-style video, film-like YouTube script, cinematic short for Instagram, voiceover for short film.

Ambiguous prompts should stay on the content route by default unless screenplay terms are explicit enough to justify film-core intent or the owner has asked for clarification.

## 4. Non-goals
- no selector modification
- no active registration
- no route binding
- no runtime behavior change
- no PASS claim
- no governed runtime proof claim

