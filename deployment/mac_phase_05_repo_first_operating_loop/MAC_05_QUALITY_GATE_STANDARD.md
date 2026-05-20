# MAC-05 Quality Gate Standard

## Required Gates

1. Topic adherence gate
2. Generic output detector
3. Script specificity gate
4. Director grounding gate
5. Skill grounding gate
6. JSON validation gate
7. Lineage gate
8. Provider handoff gate
9. False media claim gate
10. Commit readiness gate

## Gate Criteria

- Topic adherence:
  - Script repeatedly and explicitly addresses the requested topic.
- Generic output detector:
  - Fail if script could fit any unrelated generic topic.
- Script specificity:
  - Must include concrete argument structure and audience-facing stakes.
- Director/skill grounding:
  - Each selected item must map to registry + path evidence.
- JSON validation:
  - All required JSON files must parse with `jq`.
- Lineage:
  - Required lineage fields present and truthful runtime flags.
- Provider handoff:
  - Packet complete; execution mode remains reference-only unless approved.
- False media claim:
  - Hard fail if media generation is claimed without artifacts and approved execution.
- Commit readiness:
  - Safety scan clear; user review complete.

## Fail Actions

- If any hard gate fails:
  - set overall gate to fail
  - stop commit
  - produce remediation notes

