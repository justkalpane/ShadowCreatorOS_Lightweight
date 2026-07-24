# Phase 8: Validator Route Split Plan

## 1. Objective

Phase 8 audits the validator layer so we can prepare the hard gates for a cinema-first route split. The goal is to keep the current content/script validators where they belong, preserve the generic governance validators, and identify the missing film-specific validator family that will eventually prevent fake PASS states on a cinema route.

## 2. Relationship to Phases 1-7

Phase 1 found director-level platform drift.
Phase 2 found agent-level drift.
Phase 3 found subagent-level drift.
Phase 4 found skill-layer content-hook and retention drift plus missing filmcraft skills.
Phase 5 found subskill-layer micro-behavior drift plus missing filmcraft subskills.
Phase 6 found the contract layer still missing a film contract family.
Phase 7 found the route manifest and route slice layer still missing a film route family.
Phase 8 now checks whether validators can prevent a future film route from being falsely validated by content-mode criteria.

## 3. Validator inventory

The validator layer is large. For this phase I directly inspected 11 validator sources that carry the highest signal for route and film-risk analysis:

| Validator | File path | Current role | Cinema-core ready? | Platform/content drift? | Film-validator gap? | Patch priority | Notes |
|---|---|---:|---:|---:|---:|---:|---|
| validate_script_generation_output | `validators/validate_script_generation_output.py` | SCRIPT_GENERATION output gate with hook, rehook, story, beat-map, and media-factory checks | No | High | Yes | P0 | Hard-wired to content script structure |
| validate_route_scope_telemetry_law | `validators/validate_route_scope_telemetry_law.py` | Route-scope telemetry law and 68-file proof expectation | Yes, generically | Low | No | P1 | Good governance gate |
| validate_route_consumption_order | `validators/validate_route_consumption_order.py` | Boot / dependency read order validator | Yes, generically | Low | No | P1 | Good no-shortcut gate |
| validate_route_mode_contract | `validators/validate_route_mode_contract.py` | Route-mode normalization and script-only enforcement | Partial | Medium | Yes | P1 | Useful, but content-mode biased |
| validate_mac06_1a_output | `validators/validate_mac06_1a_output.py` | Mac-06 content-engineering output standard | No | High | Yes | P0 | Strongly content-first |
| validate_visual_media_plan_row | `validators/validate_visual_media_plan_row.py` | Visual media plan row validator | Partial | Medium | No | P2 | Downstream media support |
| validate_final_visual_media_generation_draft | `validators/validate_final_visual_media_generation_draft.py` | Final visual media draft validator | Partial | Medium | No | P2 | Downstream media support |
| validate_evidence_bundle | `validators/validate_evidence_bundle.py` | Evidence bundle integrity gate | Yes, generically | Low | No | P1 | Governance/reproducibility |
| validate_route_state_capsule | `validators/validate_route_state_capsule.py` | Route-state capsule validator | Yes, generically | Low | No | P1 | Strong route-state boundary |
| validate_patch_transaction | `validators/validate_patch_transaction.py` | Patch transaction provenance gate | Yes, generically | Low | No | P1 | Good change-control gate |
| validate_phase0_control_plane | `validators/validate_phase0_control_plane.py` | Phase 0 proof-plane / no-fake-pass control-plane validator | Yes, generically | Low | No | P1 | Useful proof spine, not filmcraft |

### 4. Validator family classification

The current validator families group into a few clear buckets:

* Script generation validators: content-route only
* Script quality validators: content-route only
* Route/state validators: core governance and reusable
* Source / evidence validators: reusable governance
* Visual/media validators: downstream distribution only
* Phase0 proof validators: reusable governance spine

The repo does not currently show a dedicated film validator family.

## 5. Film-core validator requirements

A cinema-first validator layer will need:

* film route selection validator
* film-vs-content collision validator
* film screenplay packet validator
* Save the Cat beat sheet validator
* three-act validator
* eight-sequence validator
* Hero’s Journey validator
* Dan Harmon Story Circle validator
* McKee scene value turn validator
* Syd Field plot point validator
* Truby 22-step / moral argument / symbol web validator
* character want/need/flaw/arc validator
* character web / opposing force validator
* scene objective / obstacle / tactic validator
* scene turn validator
* dialogue subtext validator
* dialogue voice distinctness validator
* visual motif / image system validator
* mise-en-scène validator
* blocking / composition validator
* camera / lens / framing validator
* sound motif / silence validator
* performance beat validator
* screenplay format validator
* film validation scorecard validator
* no fake film PASS validator

## 6. Non-goals

This phase does not patch validators yet. It only identifies the current content bias, the reusable governance gates, and the missing filmcraft validation family.
