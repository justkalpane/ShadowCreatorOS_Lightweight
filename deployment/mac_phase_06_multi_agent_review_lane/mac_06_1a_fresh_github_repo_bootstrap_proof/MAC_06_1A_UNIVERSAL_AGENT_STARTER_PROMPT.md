# MAC-06.1A Universal Agent Starter Prompt

```text
Repo:
https://github.com/justkalpane/ShadowCreatorOS_Lightweight

Branch:
main

Instruction:
Read `START_HERE_FOR_AGENTS.md` first.

Mission:
Operate Shadow Creator OS repo-first for this task:

"Create a YouTube Shorts script on: Why AI tools fail when creators do not build systems first."

Output mode:
- If you have repo write access, default to one consolidated output file only after explicit user approval.
- If you only have chat access, return a complete chat-only Shadow output packet.

Required output:
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
- Context engineering packet summary
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
  - file_search_available
  - code_execution_available
  - package_install_available
  - provider_credentials_available
  - n8n_runtime_available
  - capabilities_used
  - capabilities_not_used
  - capabilities_requiring_approval
  - limitations_disclosed
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
```

## MAC-06.1B Governance Addendum

- For MAC-06.1A chat proof, do not create files.
- If a future repo-write proof is requested, default to one consolidated output file.
- Full dossier mode requires explicit user approval.
- Chat output must include approval gate blocks and blocker visibility.
- User approval is required before file creation, full dossier creation, commit, push, or provider handoff.
