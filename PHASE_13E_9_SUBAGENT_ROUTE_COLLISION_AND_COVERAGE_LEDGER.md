# Phase 13E_9 Subagent Route Collision and Coverage Ledger

## 1. Objective

Document the current subagent route collisions, cinema-preproduction coverage gaps, and downstream boundaries before any subagent implementation patch.

## 2. Route Collision Table

| Collision ID | Surface | Evidence | Why it matters | Required mitigation | Priority |
| --- | --- | --- | --- | --- | --- |
| E9-COL-001 | Film route vs script route subagents | `FILM_SCREENPLAY_GENERATION` and `SCRIPT_GENERATION` both require `wf_200`, `cwf_210`, `cwf_220`, `cwf_230`, `cwf_240`. | Film can inherit YouTube/content scripting behavior without a route-specific lane boundary. | Add route-aware cinema overlays to the shared five lanes. | P0_BLOCKER |
| E9-COL-002 | `cwf_210` draft lane | Contains YouTube draft and opening-hook behavior. | Film screenplay drafts should be structured around screenplay, scene, sequence, character, and dialogue needs, not YouTube hook mechanics. | Preserve script behavior; add film-only draft lane responsibilities. | P0_BLOCKER |
| E9-COL-003 | `cwf_220` critique lane | References cinematic story but also recurring hook density. | Film critique needs story structure, character motivation, scene dramaturgy, source ethics, and visual grammar critique. | Add film-specific critique criteria while isolating content re-hook scoring. | P0_BLOCKER |
| E9-COL-004 | `cwf_230` revision lane | Repairs re-hooks inside `FINAL_SCRIPT` and related content maps. | Film revision needs act/sequence, scene, conflict, dialogue, motif, and continuity repair. | Add film-specific revision lane responsibilities. | P0_BLOCKER |
| E9-COL-005 | `cwf_240` final shaping lane | Preserves re-hook map and Media Factory scene synchronization. | Film final shaping must distinguish screenplay packet closure from downstream media sync. | Add film output packet/scene continuity boundary. | P0_BLOCKER |
| E9-COL-006 | `wf_200` parent lane | Requires English master script, cinematic story, and recurring re-hook map. | Film parent lane should orchestrate screenplay structure and filmcraft gates without content-route hook criteria as PASS authority. | Add film-screenplay parent lane overlay. | P0_BLOCKER |
| E9-COL-007 | Downstream media lanes | `wf_400`, `cwf_410`, `cwf_420`, `cwf_430`, `cwf_440` are visual, voice, avatar, Media Factory, and context oriented. | Downstream media generation must not become cinema-preproduction authority. | Mark downstream-only boundaries in registry overlay and later lane patches. | P1_REQUIRED |
| E9-COL-008 | Editing/packaging lanes | `wf_500`, `cwf_510`, `cwf_520`, `cwf_530` belong to editing/packaging. | Film trailer, title, thumbnail, social cutdown, and release packaging are downstream. | Keep downstream handoff allowed but not film-core. | P1_REQUIRED |
| E9-COL-009 | Workflow binding contracts | `wf_200` and related contracts still route through `ROUTE_PHASE1_STANDARD` / `ROUTE_PHASE1_FAST`. | Runtime contract identity does not yet distinguish film subagent lanes. | Defer workflow contract edit; document as later patch. | P1_REQUIRED |
| E9-COL-010 | General-support registry profile | `SUB_AGENT_RUNTIME_REGISTRY.yaml` remains general-support. | Registry cannot prove cinema department lane ownership. | Add additive cinema lane overlay to registry. | P1_REQUIRED |

## 3. Current Coverage Table

| Cinema-preproduction lane | Current evidence | Current status | Candidate subagent lane | Patch need |
| --- | --- | --- | --- | --- |
| Story architecture | Film route uses `wf_200`; current `wf_200` is script-generation parent. | PARTIAL | `wf_200` | Add film screenplay parent lane overlay. |
| Screenplay drafting | `cwf_210` exists but carries YouTube draft/hook behavior. | DRIFTED_TO_CONTENT_ENGINE | `cwf_210` | Add film draft lane overlay. |
| Critique and notes | `cwf_220` exists with language/source/cinematic story/re-hook critique. | PARTIAL | `cwf_220` | Add film critique lane overlay. |
| Revision and repair | `cwf_230` exists with re-hook repair focus. | DRIFTED_TO_CONTENT_ENGINE | `cwf_230` | Add film revision lane overlay. |
| Final screenplay packet | `cwf_240` exists with CTA hook and Media Factory sync. | PARTIAL_WITH_DOWNSTREAM_DRIFT | `cwf_240` | Add film final-shaping/output packet overlay. |
| Character arc | No explicit subagent lane marker found. | MISSING | `wf_200` / `cwf_210` / `cwf_220` | Add responsibilities in shared film lanes. |
| Dialogue craft | No explicit subagent lane marker found. | MISSING | `cwf_210` / `cwf_220` / `cwf_230` | Add responsibilities in shared film lanes. |
| Scene dramaturgy | No explicit subagent lane marker found. | MISSING | `cwf_210` / `cwf_230` / `cwf_240` | Add responsibilities in shared film lanes. |
| Visual grammar handoff | Current `wf_400` family is downstream media/context. | DOWNSTREAM_ONLY | `wf_400`, `cwf_410`, `cwf_420` | Keep downstream-only for Phase 13E_10. |
| Source ethics/docudrama | General support and Yama governance exist, but no film subagent lane marker. | PARTIAL | `wf_200`, `cwf_220`, `cwf_240` | Add source-vs-render and no-fake-PASS lane boundaries. |

## 4. Subagent Family Inventory

| Family | Files | Current profile | Film-core use now | Future role |
| --- | ---: | --- | --- | --- |
| Topic discovery | 5 | Topic discovery/general support | Not mandatory for current film route. | Later source/theme discovery support. |
| Script generation | 5 | Script/content generation and refinement | Mandatory for current film route. | Phase 13E_10 primary target. |
| Context engineering | 5 | Context/general support | Not mandatory for current film route. | Later film packet expansion and handoff support. |
| Media/visual/voice | 5 | Visual media, voice, avatar, Media Factory | Downstream only. | Preserve downstream-only boundary. |
| Editing/packaging | 4 | Editing and packaging | Downstream only. | Preserve downstream-only boundary. |
| Governance/support | 12 | Control, kernel, analytics/recovery/governance support | Supporting only. | Later no-fake-PASS/source/rollback support. |

## 5. Readiness Classification

```text
subagent_source_file_count=37
subagent_python_file_count=36
film_route_subagent_count=5
script_route_subagent_count=5
film_script_shared_subagent_count=5
phase_13_cinema_subagent_markers_present=0
content_drift_found_in_film_mandatory_subagents=true
downstream_media_lane_boundary_needed=true
```

## 6. Non-Implementation Boundary

```text
phase_13e_9_created_docs_only=true
subagents_modified=false
subagent_registry_modified=false
selector_modified=false
route_manifests_modified=false
route_slices_modified=false
runtime_behavior_changed=false
pass_claimed=false
runtime_proof_claimed=false
```
