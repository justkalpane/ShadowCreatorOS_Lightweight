# Output To Chat Contract

Chat-mode agents that cannot write files must return a complete structured output packet.

## Required Sections

1. `mission_packet`
2. `selected_directors_agents_skills_summary`
3. `research_brief`
4. `script_v1`
5. `debate`
6. `critique`
7. `final_script`
8. `context_engineering_packet`
9. `provider_handoff_packet`
10. `quality_gate_report`
11. `lineage_summary`
12. `next_action`

## Quality Rules

- Must be specific to the topic.
- Must not be generic chatbot advice.
- Must include grounding references to repo doctrine/contracts where possible.
- Must clearly say whether output is chat-only or repo-file-backed.

## Execution Boundary

Provider handoff remains reference-only unless external execution is separately approved.

