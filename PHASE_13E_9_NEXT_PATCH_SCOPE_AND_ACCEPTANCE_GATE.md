# Phase 13E_9 Next Patch Scope and Acceptance Gate

## 1. Objective

Lock the next safe implementation boundary for subagent cinema department lane alignment.

## 2. Recommended Next Phase

```text
Phase 13E_10: additive subagent cinema department lane overlay patch batch 1
```

Phase 13E_10 should align the five shared film/script subagent lanes with explicit route-specific boundaries. It must preserve `SCRIPT_GENERATION` and avoid selector or route registry edits.

## 3. Proposed Phase 13E_10 File Scope

Primary allowed files:

```text
subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml
subagents/wf_200/wf_200_sub_agent.py
subagents/cwf_210/cwf_210_sub_agent.py
subagents/cwf_220/cwf_220_sub_agent.py
subagents/cwf_230/cwf_230_sub_agent.py
subagents/cwf_240/cwf_240_sub_agent.py
tests/test_phase_13e10_subagent_cinema_lane_overlay.py
PHASE_13E_10_SUBAGENT_CINEMA_LANE_OVERLAY_PATCH_REPORT.md
```

## 4. Explicitly Out Of Scope For Phase 13E_10

```text
runtime/state/route_chain_mode_selector.yaml
registries/route_manifests/
registries/route_slices/
agents/
directors/
schemas/
validators/
runtime_contracts/
tests/fixtures/
skills/
subskills/
.agents/skills/
```

Phase 13E_10 must not create new subagent files, rename existing lanes, remove script-generation responsibilities, or change the film route manifest/slice.

## 5. Required Overlay Shape

Each patched subagent should receive an additive Phase 13E_10 block or equivalent metadata with:

```text
phase_13e_10_status: SUBAGENT_CINEMA_DEPARTMENT_LANE_OVERLAY
runtime_behavior_changed: false
selector_modified: false
active_route_registry_modified: false
runtime_proof_claimed: false
pass_claimed: false
script_generation_preserved: true
film_screenplay_generation_preserved: true
shared_with_script_generation: true
film_route_id: FILM_SCREENPLAY_GENERATION
script_route_id: SCRIPT_GENERATION
cinema_department_lane=<specific film preproduction lane>
cinema_craft_responsibility=<one or more screenplay/preproduction responsibilities>
content_route_boundary=<what remains SCRIPT_GENERATION only>
downstream_boundary=<what remains visual/media/packaging only>
no_fake_pass_boundary=true
```

## 6. Target Lane Assignments

| File | Current role | Required cinema overlay |
| --- | --- | --- |
| `subagents/wf_200/wf_200_sub_agent.py` | Script-generation parent lane. | Film screenplay parent lane: story architecture, act/sequence orchestration, source/ethics handoff, and no-fake-PASS coordination. |
| `subagents/cwf_210/cwf_210_sub_agent.py` | Script drafting with YouTube hook references. | Film screenplay draft lane: screenplay structure, scene drafting, character motivation, dialogue/subtext, and content-hook isolation. |
| `subagents/cwf_220/cwf_220_sub_agent.py` | Critique lane with source/cinematic story/re-hook references. | Film critique lane: scene dramaturgy, character arc, dialogue, source-vs-render, docudrama, and style/canon critique. |
| `subagents/cwf_230/cwf_230_sub_agent.py` | Revision lane with re-hook repair focus. | Film revision lane: act/sequence repair, scene conflict, dialogue polish, motif continuity, and false-material removal. |
| `subagents/cwf_240/cwf_240_sub_agent.py` | Final shaping with CTA hook and Media Factory sync. | Film output packet lane: screenplay packet closure, continuity, downstream handoff boundary, and no-fake-PASS packaging. |
| `subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml` | General support registry. | Additive cinema lane overlay listing the five shared lanes and explicitly preserving script route behavior. |

## 7. Acceptance Gate For Phase 13E_10

| Gate | Required evidence | Required status |
| --- | --- | --- |
| Five target subagents exist | File scan | PASS |
| Subagent runtime registry exists | File scan | PASS |
| Five target subagents carry Phase 13E_10 marker | Marker scan | PASS |
| Registry contains Phase 13E_10 cinema lane overlay | YAML/text scan | PASS |
| `SCRIPT_GENERATION` responsibilities preserved | Existing hook/re-hook/content text remains with explicit content-only boundary | PASS |
| `FILM_SCREENPLAY_GENERATION` responsibilities added | Film route ID and cinema lane responsibilities present | PASS |
| Downstream media generation remains downstream | Explicit downstream boundary present | PASS |
| No selector edit | Diff check | PASS |
| No active route manifest/slice edit | Diff check | PASS |
| No schemas/validators/contracts/fixtures edit | Diff check | PASS |
| No skill/subskill edit | Diff check | PASS |
| Dirty unrelated files unstaged | `git diff --cached --name-only` scope check | PASS |
| Runtime proof not claimed | Report grep and diff review | PASS |
| PASS not claimed | Report grep and diff review | PASS |

## 8. Suggested Test Assertions

```text
target_subagent_count=5
target_subagents_have_phase_13e10_marker=true
subagent_runtime_registry_has_phase_13e10_overlay=true
film_route_id_FILM_SCREENPLAY_GENERATION_present=true
script_route_id_SCRIPT_GENERATION_present=true
script_generation_preserved_true_present=true
content_route_boundary_present=true
downstream_boundary_present=true
no_fake_pass_boundary_present=true
selector_file_untouched=true
active_route_manifest_files_untouched=true
active_route_slice_files_untouched=true
dirty_unrelated_files_unstaged=true
```

## 9. Future Approval Phrase

```text
Approved: proceed with Phase 13E_10 additive subagent cinema department lane overlay patch batch 1.
```

Do not infer this approval from this document.

## 10. Verdict

```text
PHASE_13E_9_FINAL_VERDICT=READY_WITH_CONDITIONS
SAFE_TO_START_PHASE_13E_10_AFTER_OWNER_APPROVAL=true
SAFE_TO_REWRITE_SUBAGENT_ARCHITECTURE=false
SAFE_TO_MODIFY_SELECTOR=false
SAFE_TO_MODIFY_ROUTE_REGISTRY=false
SAFE_TO_MODIFY_SKILLS=false
FULL_CINEMA_ENGINE_IMPLEMENTED=false
RUNTIME_PROOF_CLAIMED=false
PASS_CLAIMED=false
```
