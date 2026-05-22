# MAC-06.1A Universal Agent Starter Prompt

```text
Repo:
https://github.com/justkalpane/ShadowCreatorOS_Lightweight

Branch:
main

Instruction:
Detect/read `AGENTS.md` first if available. Then read `START_HERE_FOR_AGENTS.md`.

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
- generic direct answer is forbidden
- content/script/video tasks must include the Content Engineering Output Contract
- script-only output is PARTIAL unless user explicitly requested script-only
- invalid gate statuses cause PARTIAL or FAIL
- if capability matrix or agent runtime index is not cited, status cannot be PASS
- if media/context engineering handoff is missing, status cannot be PASS for video/script tasks
```

## MAC-06.1B Governance Addendum

- For MAC-06.1A chat proof, do not create files.
- If a future repo-write proof is requested, default to one consolidated output file.
- Full dossier mode requires explicit user approval.
- Chat output must include approval gate blocks and blocker visibility.
- User approval is required before file creation, full dossier creation, commit, push, or provider handoff.

## Always-On Trigger Addendum

MAC-06.1A must prove that normal layman task language triggers Shadow OS orchestration. If the output answers directly before repo routing, classify as `FAIL`.
