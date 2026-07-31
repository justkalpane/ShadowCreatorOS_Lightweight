# Phase 13E_5 Next Patch Scope and Acceptance Gate

## 1. Objective

Lock the next safe implementation boundary after the agent and skill readiness review.

## 2. Recommended Next Phase

```text
Phase 13E_6: named mythology agent 24-craft cinema alignment patch batch 1
```

Phase 13E_6 should align the named mythology agent layer with the already-patched 24-craft director layer. It must not attempt the full skill/subskill rewrite yet.

## 3. Proposed Phase 13E_6 File Scope

Primary allowed files:

```text
agents/agni/agni_agent.py
agents/arjuna/arjuna_agent.py
agents/aruna/aruna_agent.py
agents/brahma/brahma_agent.py
agents/durga/durga_agent.py
agents/ganesha/ganesha_agent.py
agents/garuda/garuda_agent.py
agents/hanuman/hanuman_agent.py
agents/indra/indra_agent.py
agents/kali/kali_agent.py
agents/kama/kama_agent.py
agents/krishna/krishna_agent.py
agents/maya/maya_agent.py
agents/narada/narada_agent.py
agents/nataraja/nataraja_agent.py
agents/parashara/parashara_agent.py
agents/saraswati/saraswati_agent.py
agents/shakti/shakti_agent.py
agents/shiva/shiva_agent.py
agents/valmiki/valmiki_agent.py
agents/varuna/varuna_agent.py
agents/vishnu/vishnu_agent.py
agents/vyasa/vyasa_agent.py
agents/yama/yama_agent.py
tests/test_phase_13e6_named_agent_cinema_alignment.py
PHASE_13E_6_NAMED_AGENT_CINEMA_ALIGNMENT_PATCH_REPORT.md
```

Optional registry overlay files only if the implementation can prove they are additive and non-breaking:

```text
agents/AGENT_RUNTIME_REGISTRY.yaml
registries/agent_class_matrix.json
```

If registry overlays are touched, they must preserve legacy registry entries and add only cinema-specific overlay or marker data. They must not delete or rewrite existing non-film route behavior.

## 4. Files Explicitly Out Of Scope For Phase 13E_6

```text
runtime/state/route_chain_mode_selector.yaml
registries/route_manifests/
registries/route_slices/
schemas/
validators/
runtime_contracts/
tests/fixtures/
subagents/
skills/
subskills/
.agents/skills/
directors/
```

`skills/` contains pre-existing dirty files, so skill implementation must wait for a separate index-aware patch phase.

## 5. Required Agent Ownership Block Shape

Each patched named agent should include an explicit Phase 13E_6 block or equivalent metadata with:

```text
phase_13e_6_status: NAMED_AGENT_24_CRAFT_CINEMA_ALIGNMENT
runtime_behavior_changed: false
selector_modified: false
active_route_registry_modified: false
runtime_proof_claimed: false
pass_claimed: false
script_generation_preserved: true
film_screenplay_generation_preserved: true
cinema_craft_authority=<one or more 24-craft IDs>
mythology_fidelity_lock=<character symbolism and work style>
cinema_department_execution_role=<agent-level responsibility>
downstream_boundary=<content/media/platform limits>
```

## 6. Acceptance Gate

| Gate | Required evidence | Current status | Required before Phase 13E_6 completion |
| --- | --- | --- | --- |
| 24 named mythology agent surfaces exist | File inspection under `agents/` | PARTIAL, Kali missing | Create `agents/kali/kali_agent.py` or explicitly block. |
| All 24 named agents have cinema ownership markers | Marker scan | FAIL, zero Phase 13 markers found in named agents | Add bounded marker blocks to all 24 named agents. |
| Agent mythology fidelity preserved | Text evidence in each agent file | PARTIAL | Add character-faithful execution role per agent. |
| Content drift isolated | Drift scan | PARTIAL | Keep YouTube, hook, retention, thumbnail, viral, platform, SEO out of film-core authority. |
| SCRIPT_GENERATION preserved | Boundary text and tests | NEEDS_TEST | Add test ensuring agent patch does not alter script route files. |
| FILM_SCREENPLAY_GENERATION preserved | Boundary text and tests | NEEDS_TEST | Add test ensuring film route boundary remains repo-level only. |
| Runtime behavior unchanged | Diff inspection | REQUIRED | No runtime implementation or selector edit. |
| Dirty skill files untouched | Git staged-scope check | REQUIRED | Stage no dirty skill/subskill files. |

## 7. Suggested Phase 13E_6 Test Assertions

```text
all_24_named_agent_surfaces_exist=true
all_24_named_agent_surfaces_have_phase_13e6_marker=true
all_24_named_agent_surfaces_preserve_runtime_boundaries=true
kali_agent_surface_created=true
script_generation_boundary_text_present=true
film_screenplay_generation_boundary_text_present=true
content_platform_drift_not_marked_as_film_core_authority=true
selector_file_untouched=true
active_route_registry_files_untouched=true
dirty_skill_files_unstaged=true
```

## 8. Prohibited Changes Unless Separately Approved

```text
do_not_modify_route_selector=true
do_not_modify_active_route_manifests=true
do_not_modify_active_route_slices=true
do_not_modify_schemas=true
do_not_modify_validators=true
do_not_modify_runtime_contracts=true
do_not_modify_fixtures=true
do_not_modify_subagents=true
do_not_modify_skills=true
do_not_modify_subskills=true
do_not_modify_dot_agents_skills=true
do_not_claim_runtime_proof=true
do_not_claim_pass=true
do_not_push=true
```

## 9. Future Skill/Subskill Plan

After Phase 13E_6, later phases should proceed in this order:

1. Subagent cinema department lane readiness gate.
2. Subagent cinema department lane patch batch.
3. Clean skill cinema-craft overlay readiness gate.
4. Dirty skill/subskill index-aware patch batches.
5. Skill registry overlay and route consumption coherence audit.

## 10. Future Approval Phrase

```text
Approved: proceed with Phase 13E_6 named mythology agent 24-craft cinema alignment patch batch 1.
```

Do not infer this approval from this document.

## 11. Verdict

```text
PHASE_13E_5_FINAL_VERDICT=READY_WITH_CONDITIONS
SAFE_TO_START_PHASE_13E_6_AFTER_OWNER_APPROVAL=true
SAFE_TO_REWRITE_ALL_SKILLS_NOW=false
FULL_CINEMA_ENGINE_IMPLEMENTED=false
RUNTIME_PROOF_CLAIMED=false
PASS_CLAIMED=false
```
