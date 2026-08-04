# Phase 13E_5 Agent and Skill 24-Craft Cinema Alignment Readiness Gate

## 1. Objective

Verify whether the repo is ready to move beyond the completed 24-craft director ownership layer into bounded agent, subagent, skill, and subskill Cinema Engine alignment.

This is a readiness gate only. It does not modify agents, subagents, skills, subskills, selectors, registries, schemas, validators, contracts, fixtures, or runtime behavior.

## 2. Baseline

```text
phase=13E_5
base_head=6dd8d12069be667a01f99aa0bb544e7e2f1c6580
branch=codex/shadow-prod-recovery
phase_13e_4_director_registry_coherence_complete=true
director_24_craft_overlay_count=24
legacy_30_director_registry_preserved=true
film_route_selector_bound=true
runtime_behavior_changed=false
runtime_proof_claimed=false
pass_claimed=false
worktree_dirty=true
unrelated_dirty_files_present=true
implementation_started=false
```

## 3. Evidence Inspected

| Evidence | Path | Status | Notes |
| --- | --- | --- | --- |
| Startup law | `AGENTS.md` | INSPECTED | Repo-first boot law is active. |
| 24-craft canon | `PHASE_13C_24_CRAFT_CANON.md` | INSPECTED | Defines the target 24 cinema crafts. |
| Mythology role map | `PHASE_13C_MYTHOLOGY_TO_CINEMA_ROLE_MAP.md` | INSPECTED | Defines mythology-to-cinema mappings for the target workers. |
| Production house architecture | `PHASE_13C_CINEMA_PRODUCTION_HOUSE_ARCHITECTURE.md` | INSPECTED | Confirms worker layers: director, agent, subagent, skill, subskill. |
| Director readiness | `PHASE_13E_0_24_CRAFT_DIRECTOR_OWNERSHIP_READINESS_GATE.md` | INSPECTED | Earlier gate explicitly deferred agents/subagents/skills/subskills. |
| Director patch report | `PHASE_13E_4_REMAINING_DIRECTOR_OWNERSHIP_AND_REGISTRY_PATCH_REPORT.md` | INSPECTED | Confirms director registry coherence and recommends this phase. |
| Active selector | `runtime/state/route_chain_mode_selector.yaml` | INSPECTED | `film_screenplay_generation` mode exists and preserves `script_only` default. |
| Active film manifest | `registries/route_manifests/film_screenplay_generation.yaml` | INSPECTED | Manifest currently references only six mandatory agents and content-script skills. |
| Active film slice | `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | INSPECTED | Slice remains registry-bound but proof/PASS not claimed. |
| Agent registry | `agents/AGENT_RUNTIME_REGISTRY.yaml` | INSPECTED | Flat Narada-pattern registry with 114 runtime agents in matrix truth. |
| Agent matrix | `registries/agent_class_matrix.json` | INSPECTED | 114 agents, including 32 named-director class entries. |
| Subagent registry | `subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml` | INSPECTED | Workflow lanes remain topic/script/context/media/publishing oriented. |
| Subagent matrix | `registries/sub_agent_matrix.json` | INSPECTED | 36 subagents, no film-route-specific route bindings in inspected script/context/media lanes. |
| Skill registry | `registries/skill_registry.yaml` | INSPECTED | 218 canonical skills in registry truth; many remain content/platform biased. |
| Subskill registry | `registries/subskill_runtime_registry.yaml` | INSPECTED | Subskills are registered under `skills/sub_skills/`, not top-level `subskills/`. |

## 4. Surface Count Reconciliation

```text
agents_clean_text_surface_count=122
subagents_clean_text_surface_count=37
skills_clean_text_surface_count=565
top_level_subskills_clean_text_surface_count=1
dot_agents_skills_clean_text_surface_count=42
total_clean_text_surfaces_scanned=767
agent_matrix_total_agents=114
subagent_matrix_total_subagents=36
skill_registry_canonical_skill_count=218
owner_expected_director_craft_count=24
director_layer_24_craft_count=24
agent_layer_24_craft_count=23
missing_24_craft_agent_surface=agents/kali/kali_agent.py
count_reconciliation_status=DOES_NOT_MATCH_DIRECTOR_LAYER_YET
```

The previous Phase 13C broad inventory counted 1,037 relevant brain surfaces. This gate uses a narrower clean text-surface count for the agent/skill readiness boundary and separates registry truth from filesystem noise such as `.DS_Store`, `__pycache__`, and bytecode.

## 5. Worker Family Readiness

| Worker family | Registry truth | Files inspected | Cinema signal | Content drift signal | Phase 13 alignment markers | Readiness verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Agents | 114 matrix entries | 122 clean text surfaces | 13 raw matches | 30 raw matches | 0 raw matches | PARTIAL, requires bounded agent patch |
| Subagents | 36 matrix entries | 37 clean text surfaces | 3 raw matches | 5 raw matches | 0 raw matches | PARTIAL, requires route-lane design before patch |
| Skills | 218 canonical registry entries | 565 clean text surfaces | 92 raw matches | 612 raw matches | 4 raw matches | BLOCKED for broad rewrite, requires phased skill batches |
| Top-level subskills | Registry lives elsewhere | 1 clean text surface | 0 raw matches | 0 raw matches | 0 raw matches | NOT authoritative for runtime subskills |
| `skills/sub_skills` | Subskill registry references these | 128 files within skills count | Mixed | Mixed | Mixed | Requires dedicated subskill patch gate |
| `.agents/skills` | Codex skill surface | 42 clean text surfaces | 20 raw matches | 7 raw matches | 0 raw matches | Out of scope for first implementation batch |

## 6. Key Findings

| Finding ID | Finding | Evidence | Readiness impact |
| --- | --- | --- | --- |
| E5-F01 | Director layer is coherent, but worker layer is not yet aligned to the 24-craft overlay. | Phase 13E_4 report and agent/skill scans. | Blocks full Cinema Engine completion claim. |
| E5-F02 | Kali exists as a director surface but has no matching runtime agent surface. | `agents/kali/kali_agent.py` is missing; agent matrix has zero Kali entries. | P0 blocker for 24-craft agent parity. |
| E5-F03 | Existing film manifest still names only six mandatory agents: Krishna, Aruna, Vyasa, Valmiki, Saraswati, Yama. | `registries/route_manifests/film_screenplay_generation.yaml`. | Full 24-craft agent consumption is not established. |
| E5-F04 | Subagent lanes remain workflow-family oriented: topic, script, context, media, publishing, analytics, governance, and support. | `registries/sub_agent_matrix.json`. | Needs design before cinema department subagent patching. |
| E5-F05 | Skill registry is still a content/media production registry with many YouTube, hook, retention, thumbnail, viral, platform, SEO, and publishing surfaces. | `registries/skill_registry.yaml` and skill signal scan. | Broad skill rewrite is unsafe. |
| E5-F06 | Several script/retention skill and subskill files are already dirty. | `git status --short -- skills subskills .agents/skills`. | Dirty skill surfaces need a separate index-aware patch phase. |
| E5-F07 | The named mythology agent files are not dirty in current status. | `git status --short -- agents`. | Cleanest next patch target is named agent layer. |

## 7. Readiness Decision

```text
PHASE_13E_5_STATUS=READY_WITH_CONDITIONS
SAFE_TO_IMPLEMENT_ALL_AGENT_SKILL_SURFACES_AT_ONCE=false
SAFE_TO_IMPLEMENT_NAMED_AGENT_ALIGNMENT_BATCH=true
SAFE_TO_PATCH_DIRTY_SKILLS_NOW=false
SAFE_TO_CLAIM_FULL_CINEMA_ENGINE_COMPLETE=false
RUNTIME_BEHAVIOR_CHANGED=false
SELECTOR_MODIFIED=false
ROUTE_REGISTRY_MODIFIED=false
RUNTIME_PROOF_CLAIMED=false
PASS_CLAIMED=false
```

## 8. Required Conditions Before Implementation

| Condition | Required before next implementation | Status now |
| --- | --- | --- |
| Exact file scope locked | Yes | Ready for clean named-agent batch. |
| Kali agent placement decided | Yes | Recommended: `agents/kali/kali_agent.py`. |
| Agent registry overlay strategy defined | Yes | Additive overlay only; preserve legacy matrix. |
| Dirty skill files protected | Yes | Must avoid dirty skill/subskill files in next batch. |
| Selector preservation | Yes | Selector must not be modified in next batch. |
| Active registry preservation | Yes | Film manifest/slice should not be modified in first agent patch unless separately approved. |
| Runtime proof boundary | Yes | No PASS or governed proof claims. |

## 9. Verdict

```text
FINAL_VERDICT=READY_WITH_CONDITIONS
NEXT_SAFE_PHASE=Phase 13E_6: named mythology agent 24-craft cinema alignment patch batch 1
```
