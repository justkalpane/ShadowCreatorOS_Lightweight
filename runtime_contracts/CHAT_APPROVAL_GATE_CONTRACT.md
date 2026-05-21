# Chat Approval Gate Contract

The chat is the user-facing control UI. Gate decisions must be visible in chat, not hidden in backend files.

## Gate Block Format

Use this block at each major stage:

```text
SHADOW_GATE_STATUS
- stage_name
- current_status = PASS / BLOCKED / NEEDS_USER_APPROVAL / NEEDS_CONFIRMATION
- director_or_gate_owner
- evidence_used
- issue_detected
- recommendation
- user_options
- waiting_for_user_approval=true/false
```

## Required Gates

- Topic Intake Gate
- Topic Qualification Gate
- Director/Skill Selection Gate
- Research Sufficiency Gate
- Script Quality Gate
- Critique/Refinement Gate
- Context Packet Gate
- Provider Handoff Gate
- Final Approval Gate

## Required User Options

- `APPROVE_CONTINUE`
- `REVISE_TOPIC`
- `REVISE_SCRIPT`
- `CHANGE_TONE`
- `CHANGE_PLATFORM`
- `STOP`
- `CREATE_CONSOLIDATED_FILE`
- `CREATE_FULL_DOSSIER`
- `HANDOFF_TO_N8N_LATER`

