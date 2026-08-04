# Phase 13E_12 Workflow Binding Contract Film Lane Identity Readiness Gate

## 1. Objective

Verify whether the workflow binding contract layer is ready for a bounded film-lane identity patch after Phase 13E_10 added subagent cinema department lane overlays and Phase 13E_11 confirmed post-overlay coherence.

This is a readiness gate only. It does not modify workflow contracts, subagents, agents, directors, skills, subskills, route selector files, active route manifests, active route slices, schemas, validators, contracts, fixtures, or runtime behavior.

## 2. Baseline

```text
phase=13E_12
base_head=515f80c6050ce79dc3a667db11a39117be79f56a
phase_13e_11_coherence_complete=true
phase_13e_10_subagent_lane_overlay_batch_1_complete=true
workflow_binding_contract_film_lane_identity_complete=false
skill_cinema_craft_overlay_complete=false
subskill_cinema_craft_overlay_complete=false
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
| Phase 13E_11 coherence audit | `PHASE_13E_11_POST_SUBAGENT_LANE_OVERLAY_COHERENCE_AUDIT.md` | VERIFIED | Recommends this readiness gate and confirms Phase 13E_10 did not modify selector, active route manifests, active route slices, skills, or subskills. |
| Workflow binding contracts | `agents/common/workflow_binding_contracts.py` | GAP_FOUND | `wf_200` is still legacy `ROUTE_PHASE1_*`; child lanes `cwf_210`, `cwf_220`, `cwf_230`, and `cwf_240` have empty `route_bindings`. |
| Workflow contract caller | `agents/common/workflow_sub_agent_base.py` | BLAST_RADIUS_IDENTIFIED | `WorkflowSubAgentBase` imports `get_workflow_contract` and includes `workflow_contract` in subagent runtime results. |
| Subagent runtime registry | `subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml` | READY_AS_REFERENCE | Phase 13E_10 overlay lists the five film/script shared lanes and marks runtime/selector/pass/proof as false. |
| Five shared subagent files | `subagents/wf_200`, `cwf_210`, `cwf_220`, `cwf_230`, `cwf_240` | READY_AS_REFERENCE | Each file contains the Phase 13E_10 cinema lane overlay and preserves SCRIPT_GENERATION route behavior. |
| Subagent matrix | `registries/sub_agent_matrix.json` | GAP_MIRRORS_CONTRACT | WF-200 has legacy `ROUTE_PHASE1_*`; CWF-210 through CWF-240 have empty `route_bindings`. |
| Active selector | `runtime/state/route_chain_mode_selector.yaml` | PRESERVED | `default_mode: script_only` remains present and `film_screenplay_generation` mode exists. No selector edit is needed for the next additive workflow identity patch. |
| Film route manifest | `registries/route_manifests/film_screenplay_generation.yaml` | PRESERVED_WITH_BOUNDARY_CAUTION | Active film manifest still declares `runtime_behavior_changed: false`, `pass_claimed: false`, and `bound_to_route_selector: false`. |
| Film route slice | `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | PRESERVED_WITH_BOUNDARY_CAUTION | Active film slice still declares `runtime_behavior_changed: false`, `pass_claimed: false`, `bound_to_route_selector: false`, and `SCRIPT_GENERATION_PRESERVED: true`. |
| Script route manifest/slice | `registries/route_manifests/script_generation.yaml`, `registries/route_slices/script_generation.registry_slice.yaml` | PRESERVED_WITH_DIRTY_WORKTREE_CAUTION | Script route still shares the same five subagents. The manifest has a pre-existing dirty hunk outside this phase. |
| Agent selection registry | `registries/agent_runtime_selection_index.yaml` | CONTENT_ORIENTED | WF-200 agent selection language remains script/content oriented; this should not be patched in the workflow-contract-only batch. |
| Skill registries | `registries/skill_registry_wf200.yaml`, `registries/skill_registry_wf-200.yaml` | CONTENT_ORIENTED | WF-200 skill registries remain content/script oriented and should be handled in later skill/subskill phases. |

## 4. Current Workflow Contract State

| Workflow | File source | Current route binding state | Film lane identity evidence | Required later delta |
| --- | --- | --- | --- | --- |
| `wf_200` | `agents/common/workflow_binding_contracts.py` | `['ROUTE_PHASE1_STANDARD', 'ROUTE_PHASE1_FAST']` | No explicit `FILM_SCREENPLAY_GENERATION` lane identity in workflow contract. | Add an additive film lane identity overlay without removing legacy route bindings. |
| `cwf_210` | `agents/common/workflow_binding_contracts.py` | `[]` | Subagent file has `film_screenplay_draft_lane`, but workflow contract does not. | Add additive film screenplay draft lane metadata. |
| `cwf_220` | `agents/common/workflow_binding_contracts.py` | `[]` | Subagent file has `film_screenplay_critique_lane`, but workflow contract does not. | Add additive film screenplay critique lane metadata. |
| `cwf_230` | `agents/common/workflow_binding_contracts.py` | `[]` | Subagent file has `film_screenplay_revision_lane`, but workflow contract does not. | Add additive film screenplay revision lane metadata. |
| `cwf_240` | `agents/common/workflow_binding_contracts.py` | `[]` | Subagent file has `film_screenplay_output_packet_lane`, but workflow contract does not. | Add additive film screenplay output packet lane metadata. |

The same current route binding state appears in `registries/sub_agent_matrix.json`:

```text
wf_200 WF-200 parent_pack ['ROUTE_PHASE1_STANDARD', 'ROUTE_PHASE1_FAST'] subagents/wf_200/wf_200_sub_agent.py
cwf_210 CWF-210 script [] subagents/cwf_210/cwf_210_sub_agent.py
cwf_220 CWF-220 script [] subagents/cwf_220/cwf_220_sub_agent.py
cwf_230 CWF-230 script [] subagents/cwf_230/cwf_230_sub_agent.py
cwf_240 CWF-240 script [] subagents/cwf_240/cwf_240_sub_agent.py
```

## 5. Caller and Blast-Radius Map

| Surface | Uses workflow binding data? | Blast radius | Patch implication |
| --- | --- | --- | --- |
| `agents/common/workflow_sub_agent_base.py` | Yes | Runtime result packets include `workflow_contract`; required input validation uses `required_inputs`, `allowed_directors`, and `gate_rules`. | Do not change required inputs, allowed directors, gate rules, or fallback behavior in the next patch. |
| `subagents/wf_200/wf_200_sub_agent.py` | Indirectly | Constructor passes `workflow_slug="wf_200"` to `WorkflowSubAgentBase`. | Future patch may add metadata read through the base contract but should not alter subagent source. |
| `subagents/cwf_210/cwf_210_sub_agent.py` | Indirectly | Constructor passes `workflow_slug="cwf_210"`. | Future patch may add metadata read through the base contract but should not alter subagent source. |
| `subagents/cwf_220/cwf_220_sub_agent.py` | Indirectly | Constructor passes `workflow_slug="cwf_220"`. | Same. |
| `subagents/cwf_230/cwf_230_sub_agent.py` | Indirectly | Constructor passes `workflow_slug="cwf_230"`. | Same. |
| `subagents/cwf_240/cwf_240_sub_agent.py` | Indirectly | Constructor passes `workflow_slug="cwf_240"`. | Same. |
| `registries/sub_agent_matrix.json` | Registry mirror | Static matrix mirrors route binding and workflow metadata. | If a later patch changes workflow metadata, add a focused coherence test proving matrix/contract expectations or explicitly defer matrix regeneration. |
| `registries/workflow_bindings.yaml` | Workflow routing registry | YAML parse succeeds; contains WF/CWF routing references. | Do not patch in the next workflow-contract-only batch unless a targeted evidence gate proves it is required. |

## 6. Invariants for Future Patch

```text
default_mode_preserved=script_only
SCRIPT_GENERATION_preserved=true
FILM_SCREENPLAY_GENERATION_preserved=true
selector_must_not_be_modified=true
active_route_manifest_must_not_be_modified=true
active_route_slice_must_not_be_modified=true
runtime_behavior_changed=false
required_inputs_must_not_change=true
allowed_directors_must_not_change=true
gate_rules_must_not_change=true
legacy_ROUTE_PHASE1_bindings_preserved=true
child_empty_route_bindings_not_reinterpreted_as_runtime_activation=true
film_lane_identity_metadata_additive_only=true
youtube_hook_retention_logic_remains_SCRIPT_GENERATION_only=true
media_generation_downstream_only=true
pass_claimed=false
runtime_proof_claimed=false
```

## 7. Proposed Phase 13E_13 File Scope

If this gate is accepted, the next implementation phase should be:

```text
Phase 13E_13: additive workflow binding contract film lane identity patch
```

Allowed file scope for Phase 13E_13 should be limited to:

```text
agents/common/workflow_binding_contracts.py
tests/test_phase_13e13_workflow_binding_film_lane_identity.py
PHASE_13E_13_WORKFLOW_BINDING_FILM_LANE_IDENTITY_PATCH_REPORT.md
```

Optional file only if explicitly approved after implementation evidence:

```text
registries/sub_agent_matrix.json
```

Do not include by default:

```text
agents/common/workflow_sub_agent_base.py
subagents/
agents/
directors/
skills/
subskills/
.agents/skills/
runtime/state/route_chain_mode_selector.yaml
registries/route_manifests/
registries/route_slices/
schemas/
validators/
runtime_contracts/
tests/fixtures/
```

## 8. Acceptance Test Matrix for Future Patch

| Test | Required evidence | Expected result |
| --- | --- | --- |
| Import workflow contracts | `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ... get_workflow_contract(...)` | All five target workflow contracts import and expose existing workflow IDs. |
| Film lane identity metadata | Focused Phase 13E_13 test | `wf_200`, `cwf_210`, `cwf_220`, `cwf_230`, and `cwf_240` expose additive `film_screenplay_*` lane metadata. |
| Existing script route preservation | Focused Phase 13E_13 test | Existing workflow names, required inputs, allowed directors, gate rules, and legacy route bindings are unchanged. |
| Phase 13E_10 overlay compatibility | `python3 tests/test_phase_13e10_subagent_cinema_lane_overlay.py` | Still passes. |
| Named-agent coherence preservation | `python3 tests/test_phase_13e8_named_agent_registry_profile_coherence.py` | Still passes. |
| Named-agent cinema alignment preservation | `python3 tests/test_phase_13e6_named_agent_cinema_alignment.py` | Still passes. |
| Python syntax | `python3 -m py_compile agents/common/workflow_binding_contracts.py tests/test_phase_13e13_workflow_binding_film_lane_identity.py` | No syntax errors. |
| Route boundary parse | Ruby/Psych parse of selector and active route YAML files | Selector and route YAML still parse. |

## 9. Readiness Findings

| Finding ID | Finding | Risk | Required next action |
| --- | --- | --- | --- |
| E12-F01 | Workflow contracts do not yet expose `FILM_SCREENPLAY_GENERATION` lane identity for the five Phase 13E_10 subagent lanes. | P1, contract/subagent semantic mismatch. | Add additive metadata in `agents/common/workflow_binding_contracts.py`. |
| E12-F02 | `wf_200` still uses legacy `ROUTE_PHASE1_STANDARD` and `ROUTE_PHASE1_FAST`. | P1, legacy route naming can obscure film/script boundary. | Preserve legacy bindings but add explicit film lane identity overlay. |
| E12-F03 | CWF-210 through CWF-240 have empty `route_bindings` in workflow contracts and subagent matrix. | P1, no workflow-level route identity evidence. | Add metadata without treating empty child bindings as runtime activation. |
| E12-F04 | `WorkflowSubAgentBase` includes workflow contracts in runtime results. | P0, metadata changes are observable. | Do not change validation gates or required inputs. Test exact preserved fields. |
| E12-F05 | Skill and subskill registries remain script/content oriented and dirty files exist under skill surfaces. | P1, later drift risk. | Defer skills/subskills to their own readiness gate after workflow contract identity closes. |
| E12-F06 | Active film manifest and slice still declare `bound_to_route_selector: false` while selector mode exists. | P1, pre-existing marker coherence caution. | Do not repair in Phase 13E_13; track separately for a later bounded registry/selector marker reconciliation. |

## 10. Validation Commands Run in This Gate

```text
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from agents.common.workflow_binding_contracts import get_workflow_contract
for slug in ["wf_200", "cwf_210", "cwf_220", "cwf_230", "cwf_240"]:
    c = get_workflow_contract(slug)
    print(slug, c.get("workflow_id"), c.get("workflow_name"), c.get("route_bindings"), c.get("required_inputs"))
PY
```

Result:

```text
wf_200 WF-200 wf200_script_intelligence_pack ['ROUTE_PHASE1_STANDARD', 'ROUTE_PHASE1_FAST'] ['topic_finalization_packet', 'research_synthesis_packet', 'orchestration_decision']
cwf_210 CWF-210 cwf210_script_generation [] ['topic_finalization_packet', 'research_synthesis_packet']
cwf_220 CWF-220 cwf220_script_debate [] ['script_draft_packet']
cwf_230 CWF-230 cwf230_script_refinement [] ['script_debate_packet']
cwf_240 CWF-240 cwf240_final_script_shaping [] ['script_refinement_packet']
```

```text
ruby -rpsych -e 'ARGV.each { |p| Psych.load_file(p); puts "parsed #{p}" }' registries/workflow_bindings.yaml registries/director_binding_wf200.yaml registries/skill_registry_wf200.yaml registries/skill_registry_wf-200.yaml registries/agent_runtime_selection_index.yaml
```

Result:

```text
parsed registries/workflow_bindings.yaml
parsed registries/director_binding_wf200.yaml
parsed registries/skill_registry_wf200.yaml
parsed registries/skill_registry_wf-200.yaml
parsed registries/agent_runtime_selection_index.yaml
```

## 11. Gate Verdict

```text
PHASE_13E_12_STATUS=READY_WITH_CONDITIONS
SAFE_TO_PATCH_WORKFLOW_BINDING_FILM_LANE_IDENTITY_ADDITIVE_ONLY=true
SAFE_TO_REWRITE_WORKFLOW_ARCHITECTURE=false
SAFE_TO_MODIFY_WORKFLOW_SUB_AGENT_BASE=false
SAFE_TO_MODIFY_SUBAGENTS=false
SAFE_TO_MODIFY_SELECTOR=false
SAFE_TO_MODIFY_ACTIVE_ROUTE_MANIFESTS=false
SAFE_TO_MODIFY_ACTIVE_ROUTE_SLICES=false
SAFE_TO_MODIFY_SKILLS=false
SAFE_TO_MODIFY_SUBSKILLS=false
SAFE_TO_CLAIM_FULL_CINEMA_ENGINE_COMPLETE=false
RUNTIME_BEHAVIOR_CHANGED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
```

## 12. Recommended Next Phase

```text
Phase 13E_13: additive workflow binding contract film lane identity patch
```

Phase 13E_13 should add film-lane identity metadata to `agents/common/workflow_binding_contracts.py` only, with one focused regression test and one patch report. It must preserve the script route, default selector mode, active route manifests, active route slices, subagent source files, skills, subskills, and all unrelated dirty files.
