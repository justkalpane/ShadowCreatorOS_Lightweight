# Phase 13E_18 Agent Runtime Selection Index Film Lane Identity Readiness Gate

## 1. Objective

Phase 13E_18 is a readiness gate for a future additive film lane identity overlay in `registries/agent_runtime_selection_index.yaml`.

This phase does not modify the agent runtime selection index, selector, active route manifests, active route slices, agents, subagents, workflow contracts, skills, subskills, schemas, validators, fixtures, or runtime behavior. It verifies whether the repository has enough evidence to safely add film lane identity mirror metadata to the existing WF-200 agent selection entries in a later bounded patch.

## 2. Current Repo State

```text
phase=13E_18
base_head=7e86fa20f0024f522cce37950a7293bf20039863
phase_13e_17_coherence_complete=true
phase_13e_16_subagent_matrix_overlay_complete=true
agent_runtime_selection_index_film_lane_identity_overlay_complete=false
runtime_behavior_changed=false
selector_modified=false
active_route_registry_modified=false
runtime_proof_claimed=false
pass_claimed=false
worktree_dirty=true
implementation_started=false
```

The worktree contains pre-existing unrelated modified files. This readiness gate leaves those files untouched and commits only this documentation report.

## 3. Evidence Reviewed

| Evidence | File/path inspected | Status | Notes |
| --- | --- | --- | --- |
| Phase 13E_17 coherence audit | `PHASE_13E_17_POST_SUBAGENT_MATRIX_FILM_LANE_IDENTITY_COHERENCE_AUDIT.md` | Present | Confirms Phase 13E_16 matrix overlay is coherent and recommends this readiness gate. |
| Agent runtime selection index | `registries/agent_runtime_selection_index.yaml` | Present | Parses with Ruby/Psych; contains 85 agent runtime selection entries. |
| Subagent matrix | `registries/sub_agent_matrix.json` | Present | Contains Phase 13E_16 film lane identity overlays on five approved workflow entries. |
| Workflow binding contracts | `agents/common/workflow_binding_contracts.py` | Present | Contains Phase 13E_13 film lane identity metadata for `wf_200`, `cwf_210`, `cwf_220`, `cwf_230`, and `cwf_240`. |
| Phase 13E_16 test | `tests/test_phase_13e16_subagent_matrix_film_lane_identity.py` | Present | Provides focused matrix overlay invariant coverage. |
| Active selector boundary | `runtime/state/route_chain_mode_selector.yaml` | Not modified | Must remain unchanged in the future index patch. |
| Active film route manifest/slice boundary | `registries/route_manifests/film_screenplay_generation.yaml`, `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | Not modified | Must remain unchanged in the future index patch. |

## 4. Agent Runtime Selection Index Inventory

```text
index_path=registries/agent_runtime_selection_index.yaml
parser_used=Ruby/Psych
top_level_key=agent_runtime_selection_index
entry_count=85
entries_with_cwf_refs=5
entries_with_phase_13e_16_film_lane_identity=0
entries_with_FILM_SCREENPLAY_GENERATION=0
entries_with_SCRIPT_GENERATION=0
```

The index is currently script/content oriented for the WF-200 selection rows. That is not automatically a failure because this readiness gate is only checking whether a later additive film-lane mirror can be added without changing the existing `SCRIPT_GENERATION` behavior.

## 5. Current Target Entry State

| Agent ID | Agent name | Task family | Current subagent binding | Current selection use | Evidence status | Film lane identity in index? |
| --- | --- | --- | --- | --- | --- | --- |
| `vyasa_wf200_script_generation` | `Vyasa Script Generation Agent` | `script_generation` | `registries/sub_agent_matrix.json#CWF-210` | WF-200 script generation owner; cite for script_generation tasks. | `PROVEN_BY_FILE_DISCOVERY` | No |
| `krishna_wf200_script_debate` | `Krishna Script Debate Agent` | `script_debate` | `registries/sub_agent_matrix.json#CWF-220` | WF-200 script debate owner; cite for debate and critique tasks. | `PROVEN_BY_FILE_DISCOVERY` | No |
| `saraswati_wf200_script_refinement` | `Saraswati Script Refinement Agent` | `script_refinement` | `registries/sub_agent_matrix.json#CWF-230` | WF-200 script refinement owner; cite for refinement/final shaping tasks. | `PROVEN_BY_FILE_DISCOVERY` | No |
| `durga_wf200_quality_gate` | `Durga Script Quality Gate Agent` | `quality_gate` | `registries/sub_agent_matrix.json#CWF-240` | WF-200 quality gate support; cite for content quality validation. | `PROVEN_BY_FILE_DISCOVERY` | No |
| `yama_wf200_boundary_gate` | `Yama Boundary Gate Agent` | `provider_handoff_packet` | `registries/sub_agent_matrix.json#CWF-240` | WF-200 provider/media boundary support; cite for no-execution handoff safety. | `PROVEN_BY_FILE_DISCOVERY` | No |

No direct `registries/sub_agent_matrix.json#WF-200` index entry was found. The WF-200 parent pack appears through the five agent IDs and `selection_use` text, while concrete subagent bindings point to CWF-210 through CWF-240.

## 6. Readiness Delta

| Target | Current state | Required future state | Safe future edit? | Conditions |
| --- | --- | --- | --- | --- |
| `registries/agent_runtime_selection_index.yaml` | Five WF-200 script-family rows point to CWF-210 through CWF-240 but do not expose film lane identity metadata. | Add additive metadata to those five rows only. | Yes, with conditions | Do not alter existing script/content selection text or bindings. |
| `registries/sub_agent_matrix.json` | Already contains Phase 13E_16 film lane identity metadata for referenced CWF lanes. | No change required. | No | Use as evidence only. |
| `agents/common/workflow_binding_contracts.py` | Already contains Phase 13E_13 film lane identity metadata. | No change required. | No | Use as evidence only. |
| Active selector and route files | Already preserved by previous phases. | No change required. | No | Must remain out of scope. |

## 7. Proposed Metadata Shape for Phase 13E_19

The future additive overlay should be clearly mirror-only and should not change existing index semantics.

Suggested metadata key:

```text
phase_13e_19_film_lane_identity
```

Required future metadata fields:

```text
status=ADDITIVE_AGENT_RUNTIME_SELECTION_FILM_LANE_IDENTITY
source_phase=13E_19
mirrors_subagent_matrix_phase=13E_16
mirrors_workflow_contract_phase=13E_13
runtime_behavior_changed=false
selector_modified=false
active_route_registry_modified=false
selection_rule_modified=false
subagent_binding_modified=false
director_binding_modified=false
skill_binding_modified=false
task_family_modified=false
evidence_status_modified=false
pass_claimed=false
runtime_proof_claimed=false
script_generation_preserved=true
film_screenplay_generation_preserved=true
shared_with_script_generation=true
film_route_id=FILM_SCREENPLAY_GENERATION
script_route_id=SCRIPT_GENERATION
matrix_mirror_only=true
no_fake_pass_boundary=true
```

## 8. Invariants for Phase 13E_19

```text
do_not_change_agent_ids=true
do_not_change_agent_names=true
do_not_change_agent_file_paths=true
do_not_change_task_families=true
do_not_change_director_bindings=true
do_not_change_subagent_bindings=true
do_not_change_skill_bindings=true
do_not_change_selection_use=true
do_not_change_evidence_status=true
do_not_change_disabled_entries=true
do_not_change_source_evidence=true
do_not_modify_subagent_matrix=true
do_not_modify_workflow_contracts=true
do_not_modify_selector=true
do_not_modify_active_route_manifests=true
do_not_modify_active_route_slices=true
do_not_modify_agents=true
do_not_modify_subagents=true
do_not_modify_skills_or_subskills=true
do_not_claim_pass=true
do_not_claim_runtime_proof=true
```

The future patch should preserve existing `script_generation`, `script_debate`, `script_refinement`, `quality_gate`, and `provider_handoff_packet` task families. The film lane identity overlay should explain the cinema-preproduction mirror role without converting these rows into exclusive film selectors.

## 9. Collision Risks

| Risk ID | Risk | Evidence | Required control |
| --- | --- | --- | --- |
| `13E18-R1` | Adding film metadata could be mistaken for selector binding or runtime proof. | The index is used for agent selection evidence and currently has no route IDs. | Future overlay must be mirror-only and keep runtime/proof flags false. |
| `13E18-R2` | Existing `SCRIPT_GENERATION` behavior could drift if `selection_use` text is rewritten. | Five target rows explicitly say script generation/debate/refinement/quality/boundary support. | Do not change `selection_use` in the future patch. |
| `13E18-R3` | CWF-240 is referenced by two agent rows with different responsibilities. | Durga and Yama both point to `registries/sub_agent_matrix.json#CWF-240`. | Add role-specific metadata without merging or retiring either row. |
| `13E18-R4` | Parent WF-200 identity could be overclaimed as a direct index binding. | No direct `#WF-200` index binding was found. | Describe WF-200 as implied by agent IDs/selection text, not as a direct subagent binding. |
| `13E18-R5` | Downstream provider/media boundary could become film-core authority. | Yama row is `provider_handoff_packet`. | Future metadata must keep provider/media handoff downstream and no-execution. |

## 10. Proposed Phase 13E_19 File Scope

| Path | Proposed action | Scope status |
| --- | --- | --- |
| `registries/agent_runtime_selection_index.yaml` | Add mirror-only film lane identity metadata to the five target rows. | Allowed for Phase 13E_19 if approved. |
| `tests/test_phase_13e19_agent_runtime_selection_index_film_lane_identity.py` | Add focused static test for index metadata, invariants, and boundary preservation. | Allowed for Phase 13E_19 if approved. |
| `PHASE_13E_19_AGENT_RUNTIME_SELECTION_INDEX_FILM_LANE_IDENTITY_PATCH_REPORT.md` | Document the additive patch and no-runtime-change boundary. | Allowed for Phase 13E_19 if approved. |

No other files should be modified in Phase 13E_19 without a new readiness finding and explicit approval.

## 11. Acceptance Gate for Phase 13E_19

| Gate | Required evidence | Expected result |
| --- | --- | --- |
| YAML parse gate | `ruby -rpsych -e 'Psych.load_file("registries/agent_runtime_selection_index.yaml"); puts "agent_runtime_selection_index_yaml_ok"'` | YAML parses successfully. |
| Target count gate | Five target WF-200 agent IDs are found. | All five approved rows present. |
| Metadata gate | Five target rows expose `phase_13e_19_film_lane_identity`. | Metadata present only on approved rows. |
| Invariant gate | Agent IDs, file paths, bindings, task families, selection use, and evidence status unchanged. | No selection drift. |
| Cross-index gate | Referenced CWF entries still expose Phase 13E_16 matrix metadata. | Matrix/index coherence preserved. |
| Boundary gate | Selector, active route manifests/slices, agents, subagents, workflow contracts, skills, and subskills unchanged. | Scope preserved. |
| No-PASS gate | Patch report and metadata do not claim PASS or governed runtime proof. | Runtime proof remains unclaimed. |

## 12. Verdict

```text
PHASE_13E_18_STATUS=READY_WITH_CONDITIONS
SAFE_TO_PATCH_AGENT_RUNTIME_SELECTION_INDEX_FILM_LANE_IDENTITY_ADDITIVE_ONLY=true
SAFE_TO_MODIFY_AGENT_RUNTIME_SELECTION_INDEX_SELECTION_RULES=false
SAFE_TO_MODIFY_SUBAGENT_MATRIX=false
SAFE_TO_MODIFY_WORKFLOW_CONTRACTS=false
SAFE_TO_MODIFY_SELECTOR=false
SAFE_TO_MODIFY_ACTIVE_ROUTE_MANIFESTS=false
SAFE_TO_MODIFY_ACTIVE_ROUTE_SLICES=false
SAFE_TO_MODIFY_AGENTS=false
SAFE_TO_MODIFY_SUBAGENTS=false
SAFE_TO_MODIFY_SKILLS=false
SAFE_TO_MODIFY_SUBSKILLS=false
SAFE_TO_CLAIM_FULL_CINEMA_ENGINE_COMPLETE=false
RUNTIME_BEHAVIOR_CHANGED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
```

## 13. Recommended Next Phase

```text
Phase 13E_19: additive agent runtime selection index film lane identity patch
```

Phase 13E_19 should be a narrow additive metadata mirror patch on the agent runtime selection index. It should preserve existing script/content selection semantics and must not modify selector behavior, active route registry files, agent source files, subagent source files, workflow binding contracts, skills, subskills, schemas, validators, fixtures, or runtime behavior.
