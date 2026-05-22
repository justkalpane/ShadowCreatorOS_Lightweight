# MAC-06.1A Verification Checklist

Use this checklist after the user pastes the fresh-agent result back into Codex.

## Checks

- Did the new agent detect/read `AGENTS.md`?
- Did a layman task trigger repo-first orchestration without the user saying `use repo`?
- Did the output avoid generic direct answer behavior?
- Did the new agent use GitHub repo `main`?
- Did it read `START_HERE_FOR_AGENTS.md`?
- Did it follow `AGENT_READ_ORDER.md`?
- Did it create a Shadow Mission Packet?
- Did it show repo context loading?
- Did it perform registry-first selection?
- Did it cite real paths for directors/agents/subagents/skills/subskills?
- Did it assess tools/connectors/plugins honestly?
- Did it avoid invented components?
- Did it avoid fake n8n/provider/media claims?
- Did it produce the complete chat packet?
- Did it pass quality gate?
- Did it mark unsupported parts as `NOT_ACTIVE` or `NEEDS_CONFIRMATION`?
- Did it include chat-visible approval gate blocks?
- Did it avoid creating files in chat-only proof mode?
- If files were created, did it have explicit user approval and use consolidated output mode?
- Does final status match the weakest required evidence layer?
- If `agents_selected_with_evidence=false`, is final status `PARTIAL` (unless agent layer is explicitly optional)?
- Are gate statuses limited to `PASS / BLOCKED / NEEDS_USER_APPROVAL / NEEDS_CONFIRMATION`?
- Does Final Approval Gate use `waiting_for_user_approval=true` when awaiting user decision?
- Does research brief disclose `real_time_sources_used=true/false`?
- If internet/web research is used, are sources listed?
- Does lineage include exact paths per selected director/agent/subagent/skill/subskill?
- Does context engineering packet include platform, visual, voice, caption, retention, and provider handoff details?
- Did output disclose `research_mode`?
- Did output disclose `web_access_available` and `web_access_used`?
- If `real_time_sources_used=true`, is a source list present?
- If no sources are listed, does output avoid claiming real-time research?
- If the task needs freshness and web was not used, was repo-only continuation explicitly approved?
- If `agents_selected_with_evidence=false`, is final status `PARTIAL` unless optionality is explicitly cited?
- Is context packet summary treated as valid only for chat-only mode?
- Is final status aligned to the weakest required evidence layer?
- Is `TASK_FRESHNESS_CLASSIFICATION` present and coherent?
- Is `RESEARCH_MODE_DECISION` present and coherent?
- Is `TOOLS_CONNECTORS_PLUGINS_ASSESSMENT` present?
- Is `NATIVE_AGENT_CAPABILITY_ASSESSMENT` present?
- Does output include explicit task-to-capability routing reference?
- Are claimed capabilities aligned with environment evidence?
- If current data is required but web is unavailable/unused, is gate set to `NEEDS_USER_APPROVAL` or `NEEDS_CONFIRMATION`?
- If capability is missing, does output disclose limitation and gate impact?
- Did output cite `registries/native_capability_routing_matrix.yaml`?
- Did output cite `registries/agent_runtime_selection_index.yaml`?
- Did output include `TASK_TO_CAPABILITY_ROUTING`?
- Did output include `NATIVE_AGENT_CAPABILITY_ASSESSMENT`?
- Did output include `AGENT_RUNTIME_SELECTION`?
- Did output avoid file creation and dossier artifacts?
- Did output use chat-only mode?
- Did output avoid old dossier-first behavior?
- Did a content/script/video task include the Content Engineering Output Contract?
- Did output include `TIMED_BEAT_MAP`?
- Did output include `VOICE_GENERATION_CONTEXT`?
- Did output include `IMAGE_GENERATION_CONTEXT`?
- Did output include `VIDEO_GENERATION_CONTEXT`?
- Did output include `MUSIC_AND_SFX_CONTEXT`?
- Did output include `EDITING_CONTEXT`?
- Did output include `PLATFORM_PACKAGING`?
- If output is script-only, did the user explicitly request script-only?
- Are invalid gate statuses absent?
- If capability matrix or agent runtime index is not cited, is final status blocked from PASS?
- If context engineering media handoff is missing, is video/script task status blocked from PASS?

## Verdict

- `PASS`: complete proof packet, repo-first evidence, no drift.
- `PARTIAL`: useful output but missing required fields or evidence.
- `FAIL`: generic, invented, execution-drifted, or not repo-first.
