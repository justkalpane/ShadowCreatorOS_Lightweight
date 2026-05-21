# Universal Agent Bootstrap Prompt Template

Use this with any capable repo-aware chat or coding agent.

```text
Repo:
https://github.com/justkalpane/ShadowCreatorOS_Lightweight

Branch:
main

Instruction:
Read START_HERE_FOR_AGENTS.md first.

Mission:
Operate Shadow Creator OS repo-first for this user task: <TASK>

Output mode:
- If you have repo write access, create dossier artifacts.
- If you only have chat access, return a complete chat-only Shadow Mission Packet and output bundle.

Required output:
- Shadow Mission Packet
- Repo Context Loader summary
- registry-first selection evidence
- directors/agents/subagents/skills/subskills selected
- tools/connectors/plugins availability assessment
- research brief
- script_v1
- debate
- critique
- final_script
- context_engineering_packet
- provider_handoff_boundary
- quality_gate_report
- lineage_summary
- final classification

Hard rules:
- no n8n unless explicitly approved
- no provider execution unless explicitly approved
- no false media claims
- no invented components
- mark missing items NEEDS_CONFIRMATION
```

## Fresh Web/Coding-Agent Bootstrap Addendum

Before answering the user task, load repo context first:

- Read `START_HERE_FOR_AGENTS.md`.
- Follow `AGENT_READ_ORDER.md`.
- Use registry-first selection with evidence paths.
- Assess tools/connectors/plugins as `ACTIVE`, `PLANNED`, `NOT_ACTIVE`, or `NEEDS_CONFIRMATION`.
- Split output mode:
  - chat-only agents return a complete Shadow output packet
  - repo-write agents create dossier artifacts only after confirming contract and access

