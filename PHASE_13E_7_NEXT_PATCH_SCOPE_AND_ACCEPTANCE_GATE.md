# Phase 13E_7 Next Patch Scope and Acceptance Gate

## 1. Objective

Define the exact next implementation boundary for closing the named mythology agent registry/profile coherence gap discovered after Phase 13E_6.

## 2. Recommended Next Phase

```text
Phase 13E_8: additive named agent registry/profile coherence patch
```

Phase 13E_8 should be narrow. It should align the registry/profile truth surfaces with the already-created Phase 13E_6 named mythology agent file surfaces.

## 3. Allowed File Scope For Phase 13E_8

```text
agents/AGENT_RUNTIME_REGISTRY.yaml
agents/common/director_authority_profiles.py
registries/agent_class_matrix.json
tests/test_phase_13e8_named_agent_registry_profile_coherence.py
PHASE_13E_8_NAMED_AGENT_REGISTRY_PROFILE_COHERENCE_PATCH_REPORT.md
```

No other files should be edited unless an execution-time test proves a direct registry/profile coherence dependency inside this exact scope.

## 4. Required Patch Intent

| Target | Required change | Required boundary |
| --- | --- | --- |
| `agents/AGENT_RUNTIME_REGISTRY.yaml` | Add Kali and/or a bounded 24-craft named-agent cinema overlay. | Additive only; preserve legacy registry entries and non-film routes. |
| `agents/common/director_authority_profiles.py` | Add Kali profile and cinema-specific profile overlay fields for named mythology agents. | Preserve existing fallback behavior and avoid deleting legacy role strings unless explicitly approved later. |
| `registries/agent_class_matrix.json` | Add Kali exact agent entry and/or additive cinema metadata. | Preserve existing 114 entries unless deliberately incrementing metadata for a new Kali entry. |
| `tests/test_phase_13e8_named_agent_registry_profile_coherence.py` | Assert 24/24 named agents are coherent across file, runtime registry, class matrix, and authority profiles. | Must not require selector, route, schema, validator, contract, fixture, subagent, skill, or subskill edits. |
| `PHASE_13E_8_NAMED_AGENT_REGISTRY_PROFILE_COHERENCE_PATCH_REPORT.md` | Record exact changes and preserved boundaries. | Must not claim full Cinema Engine completion, PASS, or governed runtime proof. |

## 5. Invariants

```text
patch_mode=additive_only
do_not_rewrite_agent_runtime_registry=true
do_not_delete_existing_agent_class_matrix_entries=true
do_not_remove_existing_profile_role_strings=true
do_not_change_get_director_profile_fallback=true
do_not_bind_kali_to_selector_or_route_runtime=true
SCRIPT_GENERATION_preserved=true
FILM_SCREENPLAY_GENERATION_preserved=true
runtime_behavior_changed=false
pass_claimed=false
runtime_proof_claimed=false
```

If `registries/agent_class_matrix.json` adds Kali as a new exact entry, metadata must be updated coherently:

```text
agent_class_matrix_total_agents_expected=115
agent_class_matrix_family_totals.named_director_expected=33
```

If Phase 13E_8 instead uses an additive cinema overlay without adding a top-level class-matrix entry, it must document why the matrix total remains 114 and still prove Kali coherence through the overlay.

## 6. Prohibited File Scope

```text
runtime/state/route_chain_mode_selector.yaml
registries/route_manifests/
registries/route_slices/
schemas/
validators/
runtime_contracts/
tests/fixtures/
directors/
agents/*/*_agent.py
subagents/
skills/
subskills/
.agents/skills/
```

The next patch must not modify the 24 named agent implementation files that Phase 13E_6 already patched.

## 7. Acceptance Gate For Phase 13E_8

| Gate | Required evidence | Required status |
| --- | --- | --- |
| 24 named mythology agent files exist | File scan under `agents/<name>/<name>_agent.py` | PASS |
| 24 named mythology agents carry Phase 13E_6 markers | Marker scan | PASS |
| Runtime registry includes or overlays all 24 named agents | Registry parse/text scan | PASS |
| Agent class matrix includes or overlays all 24 named agents | JSON parse and exact/overlay scan | PASS |
| Authority profiles include all 24 named agents | Python AST or import-safe parse | PASS |
| Kali coherence closed | Kali present in all required registry/profile surfaces | PASS |
| Legacy entries preserved | Diff and count checks | PASS |
| Selector untouched | Diff check | PASS |
| Active route manifests/slices untouched | Diff check | PASS |
| Schemas/validators/contracts/fixtures untouched | Diff check | PASS |
| Dirty unrelated files unstaged | `git diff --cached --name-only` scope check | PASS |
| Runtime proof not claimed | Report grep and diff review | PASS |
| PASS not claimed | Report grep and diff review | PASS |

## 8. Suggested Test Assertions

```text
all_24_named_agent_files_exist=true
all_24_named_agent_files_have_phase_13e6_marker=true
runtime_registry_has_24_named_agent_surfaces=true
agent_class_matrix_has_24_named_agent_surfaces_or_overlay=true
director_authority_profiles_have_24_named_agent_profiles=true
kali_runtime_registry_present=true
kali_agent_class_matrix_present_or_overlay_present=true
kali_authority_profile_present=true
legacy_agent_registry_entries_preserved=true
legacy_agent_class_matrix_entries_preserved=true
get_director_profile_unknown_fallback_preserved=true
selector_file_untouched=true
active_route_registry_files_untouched=true
dirty_unrelated_files_unstaged=true
```

## 9. Future Approval Phrase

```text
Approved: proceed with Phase 13E_8 additive named agent registry/profile coherence patch.
```

Do not infer this approval from this document.

## 10. Verdict

```text
PHASE_13E_7_FINAL_VERDICT=READY_WITH_CONDITIONS
SAFE_TO_START_PHASE_13E_8_AFTER_OWNER_APPROVAL=true
SAFE_TO_REWRITE_AGENT_REGISTRY=false
SAFE_TO_REWRITE_AGENT_CLASS_MATRIX=false
SAFE_TO_MODIFY_SELECTOR=false
SAFE_TO_MODIFY_ROUTE_REGISTRY=false
FULL_CINEMA_ENGINE_IMPLEMENTED=false
RUNTIME_PROOF_CLAIMED=false
PASS_CLAIMED=false
```
