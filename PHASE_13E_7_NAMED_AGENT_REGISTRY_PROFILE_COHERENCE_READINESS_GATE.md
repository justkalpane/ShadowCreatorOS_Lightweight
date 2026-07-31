# Phase 13E_7 Named Agent Registry/Profile Coherence Readiness Gate

## 1. Objective

Phase 13E_7 verifies whether the Phase 13E_6 named mythology agent file alignment is ready for a bounded registry/profile coherence patch.

This is a readiness gate only. It does not modify agent files, runtime registries, route selectors, active route manifests, active route slices, schemas, validators, contracts, fixtures, directors, subagents, skills, subskills, or `.agents/skills`.

## 2. Baseline

```text
phase=13E_7
base_head=4c490bb3550e1f26fff1db2b301a0a0e9b0217eb
phase_13e_6_named_agent_surface_alignment_complete=true
kali_agent_file_surface_created=true
kali_registered_in_runtime=false
runtime_behavior_changed=false
selector_modified=false
active_route_registry_modified=false
runtime_proof_claimed=false
pass_claimed=false
worktree_dirty=true
implementation_started=false
```

## 3. Evidence Reviewed

| Evidence | File/path inspected | Status | Notes |
| --- | --- | --- | --- |
| Phase 13E_6 patch report | `PHASE_13E_6_NAMED_AGENT_CINEMA_ALIGNMENT_PATCH_REPORT.md` | VERIFIED | Confirms all 24 named mythology agent file surfaces were aligned and Kali file surface was created. |
| Phase 13E_6 boundaries | `PHASE_13E_6_NAMED_AGENT_CINEMA_ALIGNMENT_PATCH_REPORT.md` | VERIFIED | Report explicitly says runtime registry, class matrix, selector, film manifest, film slice, PASS, and runtime proof were not changed or claimed. |
| Phase 13E_5 next scope | `PHASE_13E_5_NEXT_PATCH_SCOPE_AND_ACCEPTANCE_GATE.md` | VERIFIED | Optional registry overlay was deferred unless additive and non-breaking. |
| Runtime registry | `agents/AGENT_RUNTIME_REGISTRY.yaml` | PARTIAL | Lists 23 of the 24 Phase 13E_6 named mythology agents; `agents/kali/kali_agent.py` is absent. |
| Agent class matrix | `registries/agent_class_matrix.json` | PARTIAL | Contains `total_agents=114` and `family_totals.named_director=32`; contains exact entries for 23 of 24 Phase 13E_6 named agents; Kali is absent. |
| Authority profiles | `agents/common/director_authority_profiles.py` | PARTIAL | Contains 23 of 24 Phase 13E_6 named agent profiles; Kali falls through to the generic unknown profile. |
| Named agent files | `agents/<name>/<name>_agent.py` | VERIFIED | All 24 named mythology agent file surfaces exist and carry Phase 13E_6 cinema alignment markers. |
| Dirty worktree scope | `git status --short` | CAUTION | Broad pre-existing dirty worktree exists; Phase 13E_7 must use scoped documentation-only staging. |

## 4. Registry/Profile Current State

```text
named_agent_files_present=24/24
phase_13e_6_markers_present=24/24
runtime_registry_listed=23/24
agent_class_matrix_exact_entries=23/24
authority_profiles_present=23/24
kali_file_exists=true
kali_phase_13e_6_marker_present=true
kali_runtime_registry_listed=false
kali_agent_class_matrix_exact_entries=0
kali_authority_profile_present=false
agent_matrix_total_agents=114
agent_matrix_family_totals.named_director=32
```

## 5. Readiness Findings

| Finding ID | Finding | Evidence | Risk | Required next action |
| --- | --- | --- | --- | --- |
| E7-F01 | Kali has a file surface but no registry/profile coherence. | `agents/kali/kali_agent.py` exists; `agents/AGENT_RUNTIME_REGISTRY.yaml`, `registries/agent_class_matrix.json`, and `agents/common/director_authority_profiles.py` do not include Kali. | P0, incomplete named mythology layer coherence. | Add Kali through an additive registry/profile patch. |
| E7-F02 | Existing 23 named profiles remain legacy/content-coded in several roles. | Roles include rapid publishing, engagement/conversion, content creation, HA coordinator, and routing intelligence. | P1, cinema-craft authority is not fully reflected in profile truth. | Add cinema-specific profile overlay fields without deleting legacy runtime semantics. |
| E7-F03 | The runtime registry is flat and legacy-oriented. | `model: flat_narada_pattern`; no 24-craft cinema ownership overlay. | P1, future execution may not consume the Phase 13E_6 cinema ownership blocks. | Add a bounded cinema overlay or explicit named-agent cinema profile section. |
| E7-F04 | The class matrix has duplicate director-bound worker responsibilities. | Krishna has 13 director-bound entries, Maya 21, Valmiki 19, Yama 11, and several others have more than one. | P1, a broad rewrite could collide with non-film workers. | Use additive exact-agent entries/overlay only and preserve existing worker entries. |
| E7-F05 | Full Cinema Engine is still not implemented. | Phase 13E_6 report says subagent, skill, dirty skill index, and full engine alignment remain incomplete. | P1, registry/profile coherence cannot be claimed as whole-engine completion. | Keep Phase 13E_8 narrow and defer subagent/skill alignment. |

## 6. Prohibited Changes During This Gate

```text
do_not_modify_agents=true
do_not_modify_agent_runtime_registry=true
do_not_modify_agent_class_matrix=true
do_not_modify_director_authority_profiles=true
do_not_modify_route_selector=true
do_not_modify_active_route_manifests=true
do_not_modify_active_route_slices=true
do_not_modify_schemas=true
do_not_modify_validators=true
do_not_modify_runtime_contracts=true
do_not_modify_fixtures=true
do_not_modify_directors=true
do_not_modify_subagents=true
do_not_modify_skills=true
do_not_modify_subskills=true
do_not_modify_dot_agents_skills=true
do_not_claim_runtime_proof=true
do_not_claim_pass=true
do_not_push=true
```

## 7. Gate Verdict

```text
PHASE_13E_7_STATUS=READY_WITH_CONDITIONS
SAFE_TO_PATCH_REGISTRY_PROFILE_ADDITIVE_ONLY=true
SAFE_TO_REWRITE_REGISTRY=false
SAFE_TO_BIND_KALI_TO_RUNTIME=false
SAFE_TO_CLAIM_AGENT_RUNTIME_REGISTRY_24_CRAFT_COMPLETE=false
SAFE_TO_CLAIM_FULL_CINEMA_ENGINE_COMPLETE=false
RUNTIME_BEHAVIOR_CHANGED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
```

## 8. Recommended Next Phase

```text
Phase 13E_8: additive named agent registry/profile coherence patch
```

Phase 13E_8 should patch only the named agent registry/profile coherence gap. It must remain additive, preserve legacy entries, preserve `SCRIPT_GENERATION`, preserve `FILM_SCREENPLAY_GENERATION`, and avoid selector or route-registry edits.
