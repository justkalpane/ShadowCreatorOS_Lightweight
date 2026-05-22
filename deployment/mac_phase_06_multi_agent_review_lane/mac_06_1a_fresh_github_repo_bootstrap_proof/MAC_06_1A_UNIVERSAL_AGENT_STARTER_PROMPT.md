# MAC-06.1A Universal Agent Starter Prompt

```text
Repo:
https://github.com/justkalpane/ShadowCreatorOS_Lightweight

Branch:
main

Instruction:
Detect/read `AGENTS.md` first if available. Then read `START_HERE_FOR_AGENTS.md`.

Canonical boot order:
1. `AGENTS.md`
2. `START_HERE_FOR_AGENTS.md`
3. `AGENT_READ_ORDER.md`
4. `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
5. `AGENT_ANTI_DRIFT_RULES.md`
6. `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`
7. `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`
8. `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`
9. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`
10. `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
11. `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`
12. `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`
13. `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
14. `registries/native_capability_routing_matrix.yaml`
15. `registries/agent_runtime_selection_index.yaml`

Mission:
Operate Shadow Creator OS repo-first for this task:

"Create a YouTube Shorts script on: Why AI tools fail when creators do not build systems first."

Output mode:
- MAC-06.1A ACTIVE OUTPUT MODE = CHAT_ONLY_MODE.
- Do not create files.
- Do not create dossier artifacts.
- Do not create consolidated files.
- Return output in chat only.
- If future repo-write is explicitly approved, default to one consolidated output file.
- Create full dossier only if user explicitly requests `FULL_DOSSIER_ARCHIVE_MODE`.

Required output:
- SHADOW_BOOT_CONFIRMATION
- shadow_boot_confirmation_present=true/false
- first_visible_output_is_boot_confirmation=true/false
- agents_md_detected=true/false
- agents_md_read=true/false
- repo_first_orchestration_started=true/false
- layman_task_trigger_contract_read=true/false
- generic_direct_answer_avoided=true/false
- shadow_mode=CHAT_ONLY_MODE
- AGENTS.md detection/read confirmation
- Layman task trigger confirmation
- Shadow Mission Packet
- Repo Context Loader summary
- Registry-first route summary
- Director selection with evidence paths
- Agent selection with evidence paths
- Subagent selection with evidence paths
- Skill selection with evidence paths
- Subskill selection with evidence paths
- Tools/connectors/plugins availability assessment
- Research brief
- Script V1
- Debate
- Critique
- Final script
- Full Content Engineering Output Contract sections:
  - CONTENT_MISSION_BRIEF
  - RESEARCH_AND_SOURCE_STATUS
  - SCRIPT_STRUCTURE
  - FINAL_SCRIPT
  - TIMED_BEAT_MAP
  - VOICE_GENERATION_CONTEXT
  - IMAGE_GENERATION_CONTEXT
  - VIDEO_GENERATION_CONTEXT
  - MUSIC_AND_SFX_CONTEXT
  - EDITING_CONTEXT
  - PLATFORM_PACKAGING
  - PROVIDER_HANDOFF_BOUNDARY
  - QUALITY_GATE
- Provider handoff boundary
- Quality gate report
- Lineage summary
- Research mode disclosure:
  - research_mode
  - web_access_available
  - web_access_used
  - real_time_sources_used
  - source_list
  - current_fact_confidence
- Research Sufficiency Gate block
- Task freshness classification block:
  - freshness_class
  - current_data_required
  - reason
- Research mode decision block:
  - research_mode
  - web_access_available
  - web_access_used
  - real_time_sources_used
  - source_list
  - current_fact_confidence
  - unsupported_claims
- NATIVE_AGENT_CAPABILITY_ASSESSMENT block:
  - repo_read
  - repo_write
  - shell_available
  - git_available
  - github_remote_available
  - web_access_available
  - web_fetch_available
  - file_search_available
  - code_execution_available
  - package_install_available
  - browser_available
  - provider_credentials_available
  - n8n_runtime_available
  - capabilities_used
  - capabilities_not_used
  - capabilities_requiring_approval
  - limitations_disclosed
- TASK_TO_CAPABILITY_ROUTING block:
  - task_family
  - capability_matrix_path=registries/native_capability_routing_matrix.yaml
  - required_capabilities
  - optional_capabilities
  - forbidden_by_default
  - approval_required_for
  - missing_required_capabilities
  - gate_result
- AGENT_RUNTIME_SELECTION block:
  - agent_runtime_index_path=registries/agent_runtime_selection_index.yaml
  - selected_agents
  - agent_evidence_paths
  - agent_layer_status
- Final proof classification
- proof_classification=PASS/PARTIAL/FAIL
- chat_only_mode_used=true
- files_created=false
- dossier_artifacts_created=false

Hard rules:
- no n8n execution
- no provider execution
- no Gemini API call
- no OpenWebUI
- no media artifact claims
- no invented directors/skills/subskills/tools/connectors/plugins
- if tools/connectors/plugins are not present or not runtime-active, mark NEEDS_CONFIRMATION or NOT_ACTIVE
- output to chat if no filesystem write access
- no commit/push unless explicitly approved
- if claiming real-time sources, include source list
- if no source list, set real_time_sources_used=false
- include TOOLS_CONNECTORS_PLUGINS_ASSESSMENT with runtime statuses
- if any final answer/script/summary/outline/advice appears before `SHADOW_BOOT_CONFIRMATION`, classify `FAIL`
- generic direct answer is forbidden
- content/script/video tasks must include the Content Engineering Output Contract
- script-only output is PARTIAL unless user explicitly requested script-only
- invalid gate statuses cause PARTIAL or FAIL
- if capability matrix or agent runtime index is not cited, status cannot be PASS
- if media/context engineering handoff is missing, status cannot be PASS for video/script tasks
- PASS is impossible if `AGENTS.md` is not detected/read
- PASS is impossible if `registries/native_capability_routing_matrix.yaml` is not cited
- PASS is impossible if `registries/agent_runtime_selection_index.yaml` is not cited
- PASS is impossible if generic direct answer occurs before repo routing
```

## MAC-06.1B Governance Addendum

- For MAC-06.1A chat proof, do not create files.
- If a future repo-write proof is requested, default to one consolidated output file.
- Full dossier mode requires explicit user approval.
- Chat output must include approval gate blocks and blocker visibility.
- User approval is required before file creation, full dossier creation, commit, push, or provider handoff.

## Always-On Trigger Addendum

MAC-06.1A must prove that normal layman task language triggers Shadow OS orchestration. If the output answers directly before repo routing, classify as `FAIL`.
