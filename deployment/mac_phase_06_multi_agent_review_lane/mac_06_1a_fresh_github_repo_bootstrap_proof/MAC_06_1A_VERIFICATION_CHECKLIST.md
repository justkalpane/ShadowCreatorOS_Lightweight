# MAC-06.1A Verification Checklist

Use this checklist after the user pastes the fresh-agent result back into Codex.

## Checks

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

## Verdict

- `PASS`: complete proof packet, repo-first evidence, no drift.
- `PARTIAL`: useful output but missing required fields or evidence.
- `FAIL`: generic, invented, execution-drifted, or not repo-first.
