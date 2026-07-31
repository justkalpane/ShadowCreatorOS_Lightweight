# Phase 13E_5 Agent and Skill Surface Inventory and Gap Ledger

## 1. Objective

Record the current agent, subagent, skill, and subskill state before any Phase 13E implementation proceeds beyond directors.

## 2. Inventory Summary

| Surface | Count basis | Count | Current organization | Cinema Engine status |
| --- | --- | ---: | --- | --- |
| Agent files | Clean text files under `agents/` | 122 | Named mythology agents plus numbered control, evolution, governance, kernel, media, plugin, recovery, and research agents. | Partial, not 24-craft aligned. |
| Agent matrix entries | `registries/agent_class_matrix.json` | 114 | `named_director`, `control_plane`, `evolution`, `governance`, `kernel`, `media`, `plugin_runtime`, `recovery`, `research`. | Partial, legacy registry shape. |
| Subagent files | Clean text files under `subagents/` | 37 | Workflow lanes and registry. | Partial, workflow-family oriented. |
| Subagent matrix entries | `registries/sub_agent_matrix.json` | 36 | topic, script, context, media, publishing, analytics, system, governance. | Partial, no cinema department lane map. |
| Skill files | Clean text files under `skills/` | 565 | Script, topic, media, operations, swarm, analytics, autonomous loop, governance, subskills. | Not safe for broad rewrite. |
| Skill registry entries | `registries/skill_registry.yaml` | 218 | Canonical skill IDs M/A/S/E/P with content-production route families. | Requires phased migration. |
| Runtime subskills | `registries/subskill_runtime_registry.yaml` | Registry references `skills/sub_skills/` | Provider, media, research, and script micro-tools. | Requires separate gate. |
| Top-level subskills | Clean text files under `subskills/` | 1 | README only. | Not runtime authoritative. |
| Codex skills | Clean text files under `.agents/skills/` | 42 | Codex helper skills, including Shadow content/media/research orchestration. | Out of first implementation batch. |

## 3. 24-Craft Named Agent Parity Matrix

| Director/craft archetype | Agent surface | Registry entries | Cinema signal found? | Content drift found? | Phase 13 marker found? | Gap classification | Priority |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| Agni | `agents/agni/agni_agent.py` | 1 | yes | yes | no | PARTIAL_CINEMA_WITH_CONTENT_DRIFT | P1_REQUIRED |
| Arjuna | `agents/arjuna/arjuna_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Aruna | `agents/aruna/aruna_agent.py` | 5 | no | yes | no | CONTENT_ENGINE_DRIFT | P1_REQUIRED |
| Brahma | `agents/brahma/brahma_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Durga | `agents/durga/durga_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Ganesha | `agents/ganesha/ganesha_agent.py` | 6 | no | yes | no | CONTENT_ENGINE_DRIFT | P1_REQUIRED |
| Garuda | `agents/garuda/garuda_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Hanuman | `agents/hanuman/hanuman_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Indra | `agents/indra/indra_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Kali | `agents/kali/kali_agent.py` | 0 | no | no | no | MISSING_AGENT_SURFACE | P0_BLOCKER |
| Kama | `agents/kama/kama_agent.py` | 1 | no | yes | no | CONTENT_ENGINE_DRIFT | P1_REQUIRED |
| Krishna | `agents/krishna/krishna_agent.py` | 13 | yes | yes | no | PARTIAL_CINEMA_WITH_CONTENT_DRIFT | P1_REQUIRED |
| Maya | `agents/maya/maya_agent.py` | 21 | yes | no | no | PARTIAL_CINEMA_NATIVE | P1_REQUIRED |
| Narada | `agents/narada/narada_agent.py` | 7 | no | yes | no | CONTENT_ENGINE_DRIFT | P1_REQUIRED |
| Nataraja | `agents/nataraja/nataraja_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Parashara | `agents/parashara/parashara_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Saraswati | `agents/saraswati/saraswati_agent.py` | 1 | no | yes | no | CONTENT_ENGINE_DRIFT | P1_REQUIRED |
| Shakti | `agents/shakti/shakti_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Shiva | `agents/shiva/shiva_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Valmiki | `agents/valmiki/valmiki_agent.py` | 19 | yes | yes | no | PARTIAL_CINEMA_WITH_CONTENT_DRIFT | P1_REQUIRED |
| Varuna | `agents/varuna/varuna_agent.py` | 1 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Vishnu | `agents/vishnu/vishnu_agent.py` | 9 | no | no | no | MISSING_CINEMA_AGENT_OWNERSHIP | P1_REQUIRED |
| Vyasa | `agents/vyasa/vyasa_agent.py` | 1 | yes | yes | no | PARTIAL_CINEMA_WITH_CONTENT_DRIFT | P1_REQUIRED |
| Yama | `agents/yama/yama_agent.py` | 11 | no | yes | no | CONTENT_ENGINE_DRIFT | P1_REQUIRED |

## 4. Subagent Gap Ledger

| Gap ID | Evidence | Impact | Required future action | Priority |
| --- | --- | --- | --- | --- |
| SG-001 | `subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml` lists workflow files, not 24-craft cinema departments. | Film route cannot prove department crew coverage. | Add or overlay cinema department subagent mapping after agent layer is aligned. | P1_REQUIRED |
| SG-002 | `registries/sub_agent_matrix.json` families are topic/script/context/media/publishing/analytics/system. | Current lanes preserve content workflow bias. | Create a cinema route-lane mapping before patching subagents. | P1_REQUIRED |
| SG-003 | Script subagents CWF-210 through CWF-240 have route profile comments for `SCRIPT_GENERATION`, not `FILM_SCREENPLAY_GENERATION`. | Film screenplay may inherit YouTube script gates. | Add explicit film-core boundaries or separate film subagent lanes in later phase. | P1_REQUIRED |
| SG-004 | Media and publishing subagents include thumbnail, metadata, distribution, and publish readiness. | Downstream modules can leak into cinema core if not isolated. | Keep downstream-only, never film-core authority. | P0_BLOCKER |

## 5. Skill Gap Ledger

| Gap ID | Evidence | Impact | Required future action | Priority |
| --- | --- | --- | --- | --- |
| SK-001 | `registries/skill_registry.yaml` canonical closure is 218 skills, mostly legacy content-production scope. | Skill layer cannot be broadly declared cinema-native. | Build craft-specific skill overlay in bounded batches. | P1_REQUIRED |
| SK-002 | Signal scan found large content drift: YouTube, hook, retention, thumbnail, viral, SEO, platform, and publishing terms across skills. | Film-core could accidentally become content optimization. | Add route-boundary guards before enabling any skill for film core. | P0_BLOCKER |
| SK-003 | Film manifest currently mandates `S-201`, `S-202`, `S-203`, `M-039`, and Shadow content/context/research Codex skills. | Mandatory film route skill set is still script/content-first. | Replace or isolate with cinema-preproduction skill authority later. | P1_REQUIRED |
| SK-004 | Several script/retention skill and subskill files are dirty before this phase. | Index-safe patching is required. | Defer dirty skill patching to its own phase. | P1_REQUIRED |
| SK-005 | `skills/media_video/M-216-shot-list-generator.skill.md` is useful but tied to media/visual route families and platform constraints. | Useful downstream capability is not yet cinema-core shot grammar authority. | Rebind as downstream handoff or craft-specific skill after route boundary audit. | P2_RECOMMENDED |
| SK-006 | `skills/media_production/A-401-thumbnail-concept-designer.skill.md` is active downstream media skill. | Thumbnail surface must not own film screenplay creation. | Keep downstream-only. | P0_BLOCKER |

## 6. Immediate Patch Candidates

The next implementation should start with clean named-agent files. It should not patch dirty skill files yet.

```text
recommended_next_phase=Phase 13E_6: named mythology agent 24-craft cinema alignment patch batch 1
candidate_create=agents/kali/kali_agent.py
candidate_patch_clean_named_agents=true
candidate_patch_dirty_skills=false
candidate_modify_selector=false
candidate_modify_active_route_registry=false
```

## 7. Current Blockers To Full Worker Alignment

```text
missing_kali_agent=true
agent_phase_13_alignment_markers_absent=true
subagent_cinema_department_lanes_absent=true
skill_layer_content_drift_high=true
dirty_skill_surfaces_present=true
subskill_runtime_truth_is_under_skills_sub_skills=true
full_worker_alignment_proven=false
```
