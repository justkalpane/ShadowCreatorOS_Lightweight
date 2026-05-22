# MAC-06.1E EVIDENCE MANIFEST

audit_date=2026-05-22
operator_mode=OLD_LOCAL_MAC_CODEX_CHAT
working_directory=/Users/apple/Documents/ShadowCreatorOS_Lightweight

## Git Truth

```text
command=git rev-parse HEAD; git ls-remote origin main
local_head=0a63918fc6d72c90c40f89539e0388d883afb961
remote_origin_main=0a63918fc6d72c90c40f89539e0388d883afb961
local_matches_remote=true
commit_18064_exists_local=false
commit_18064_exists_remote=false
git_truth_status=PARTIAL
proof_classification=PARTIAL
reason=Requested historical commit not found, but latest local HEAD matched remote before current uncommitted patch.
```

## Master Plan

```text
command=wc -l handoff/production_remediation/SHADOW_CREATOR_OS_LIGHTWEIGHT_PRODUCTION_REMEDIATION_MASTER_PLAN_SINGLE_ZERO_LOSS_CONSOLIDATED.txt
master_plan_line_count=2445
master_plan_read=true
status=PASS
```

## BT Runbook Evidence

```text
command=rg -n "BT-001|BT-060|BUILD TASK QUEUE|SHADOW_CREATOR_OS_LIGHTWEIGHT_CODEX_EXECUTABLE_REMEDIATION_RUNBOOK_V3" handoff/production_remediation/SHADOW_CREATOR_OS_LIGHTWEIGHT_PRODUCTION_REMEDIATION_MASTER_PLAN_SINGLE_ZERO_LOSS_CONSOLIDATED.txt
v3_runbook_present=true
bt_001_present=true
bt_060_present=true
build_task_queue_present=true
status=PASS
```

## Critical File Evidence

```text
AGENTS.md=97
START_HERE_FOR_AGENTS.md=195
AGENT_STARTUP_PROMPT.md=162
AGENT_REPO_FIRST_OPERATING_DOCTRINE.md=209
AGENT_READ_ORDER.md=216
AGENT_ANTI_DRIFT_RULES.md=115
runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md=134
registries/native_capability_routing_matrix.yaml=190
registries/agent_runtime_selection_index.yaml=773
validators/validate_mac06_1a_output.py=185
status=PASS
```

## Validator Fixture Evidence

```text
fixtures_created=true
fixture_tests_run=true
fixture_tests_passed=true
fail_generic_output=FAIL
partial_missing_content_engineering=PARTIAL
partial_missing_agent_index=PARTIAL
pass_minimal_complete=PASS
status=PASS
```

## Skill Metadata Evidence

```text
.agents/skills/shadow-content-orchestration/SKILL.md frontmatter_possible=true has_name=true has_description=true
.agents/skills/shadow-research-gate/SKILL.md frontmatter_possible=true has_name=true has_description=true
.agents/skills/shadow-context-engineering/SKILL.md frontmatter_possible=true has_name=true has_description=true
status=PASS
```

## Registry Evidence

```text
registries/native_capability_routing_matrix.yaml line_count=190
registries/agent_runtime_selection_index.yaml line_count=773
native task families verified: trend_research, script_generation, context_engineering_packet, n8n_execution_bus, voice_generation, image_generation, video_generation, publishing, analytics_pull
WF-200 agent entries verified: vyasa_wf200_script_generation, krishna_wf200_script_debate, saraswati_wf200_script_refinement, durga_wf200_quality_gate, yama_wf200_boundary_gate
status=PASS
```

## Validator Evidence

```text
command=python3 -m py_compile validators/validate_mac06_1a_output.py
validator_compile=PASS
checks: AGENTS detection/read, generic output, native capability assessment, freshness classification, research mode decision, research sufficiency gate, task-to-capability routing, capability matrix citation, agent runtime index citation, content engineering sections, invalid gate statuses, false execution claims, source-list honesty, files/dossiers in chat-only mode, weakest-layer mismatch.
status=PASS
```
