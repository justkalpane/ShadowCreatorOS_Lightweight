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

## Verdict

- `PASS`: complete proof packet, repo-first evidence, no drift.
- `PARTIAL`: useful output but missing required fields or evidence.
- `FAIL`: generic, invented, execution-drifted, or not repo-first.

