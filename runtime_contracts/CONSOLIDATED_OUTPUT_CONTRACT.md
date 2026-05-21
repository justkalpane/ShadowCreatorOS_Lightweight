# Consolidated Output Contract

This contract prevents default file-sprawl behavior and keeps lightweight operation product-clean.

## Output Modes

### A. CHAT_ONLY_MODE

- Default for web/chat LLMs.
- No repo files created.
- Agent outputs complete Shadow Mission Packet and final output bundle in chat.
- Chat output must include gate status, blocker status, quality gate, lineage summary, and next action.

### B. CONSOLIDATED_REPO_WRITE_MODE

- Default for coding agents with filesystem access only after user approves repo-write.
- Create exactly one consolidated output file:
  - `outputs/missions/<mission_id>/MISSION_OUTPUT.md`
- Optional metadata JSON only when needed:
  - `outputs/missions/<mission_id>/MISSION_METADATA.json`
- Do not create separate files for each director/agent/subagent/skill/subskill by default.
- Subtask outputs must be sections inside `MISSION_OUTPUT.md`.

### C. FULL_DOSSIER_ARCHIVE_MODE

- Multi-file dossier mode only when user explicitly requests:
  - `create full dossier`
  - `archive this`
  - `production dossier mode`
  - `commit-ready dossier`
- Existing MAC-05 dossier contract remains valid here.
- This is not the default mode for normal chat tasks.

## Required Consolidated Sections

- Shadow Mission Packet
- Repo Context Loader Summary
- Registry-First Route
- Director Selection
- Agent Selection
- Subagent Selection
- Skill Selection
- Subskill Selection
- Tools/Connectors/Plugins Assessment
- Research Brief
- Script V1 / Draft Output
- Debate
- Critique
- Final Output
- Context Engineering Packet
- Provider Handoff Boundary
- Quality Gate
- Lineage Summary
- User Approval Log
- Next Action

