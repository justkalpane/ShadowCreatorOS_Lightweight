# Validator Content Proof

audit_date=2026-05-22
operator_mode=OLD_LOCAL_MAC_CODEX_CHAT

file=validators/validate_mac06_1a_output.py
file_exists=true
line_count=185
py_compile_pass=true

## Rule Names

- REQUIRED_SECTIONS
- INVALID_GATE_STATUSES
- FALSE_EXECUTION_CLAIMS
- GENERIC_OUTPUT_MARKERS
- CANONICAL_RESEARCH_MODES
- GATE_STATUSES
- PROOF_CLASSIFICATIONS
- collect_invalid_research_modes
- collect_invalid_gate_values
- source_claim_without_source_list
- final_status_matches_weakest_evidence_layer

checks_required_sections=true
checks_invalid_statuses=true
checks_false_execution_claims=true
checks_content_engineering=true
checks_capability_matrix_citation=true
checks_agent_runtime_index_citation=true
checks_weakest_layer_status=true

## Relevant Rule Definitions

```python
REQUIRED_SECTIONS = [
    "AGENTS.md",
    "agents_md_detected",
    "agents_md_read",
    "layman_task_trigger_contract_read",
    "generic_direct_answer_avoided",
    "NATIVE_AGENT_CAPABILITY_ASSESSMENT",
    "TASK_FRESHNESS_CLASSIFICATION",
    "RESEARCH_MODE_DECISION",
    "Research Sufficiency Gate",
    "TASK_TO_CAPABILITY_ROUTING",
    "registries/native_capability_routing_matrix.yaml",
    "Registry-First Route",
    "Director Selection",
    "AGENT_RUNTIME_SELECTION",
    "registries/agent_runtime_selection_index.yaml",
    "Subagent Selection",
    "Skill Selection",
    "Subskill Selection",
    "TOOLS_CONNECTORS_PLUGINS_ASSESSMENT",
    "CONTENT_MISSION_BRIEF",
    "RESEARCH_AND_SOURCE_STATUS",
    "SCRIPT_STRUCTURE",
    "Final script",
    "TIMED_BEAT_MAP",
    "VOICE_GENERATION_CONTEXT",
    "IMAGE_GENERATION_CONTEXT",
    "VIDEO_GENERATION_CONTEXT",
    "MUSIC_AND_SFX_CONTEXT",
    "EDITING_CONTEXT",
    "PLATFORM_PACKAGING",
    "Provider Handoff Boundary",
    "Quality Gate",
    "Lineage Summary",
    "Final Proof Classification",
    "proof_classification",
    "chat_only_mode_used",
    "files_created=false",
    "dossier_artifacts_created=false",
]

INVALID_GATE_STATUSES = [
    "PASS_WITH_NOTICE",
    "PASS_WITH_REFINEMENT",
    "READY_FOR_USER_DECISION",
]

FALSE_EXECUTION_CLAIMS = [
    "n8n_used=true",
    "providers_called=true",
    "media_artifacts_claimed=true",
    "workflow_executed=true",
    "gemini_api_called=true",
]

GENERIC_OUTPUT_MARKERS = [
    "Here is a script",
    "Here's a script",
    "Sure, here",
    "Here is your script",
    "Here's your script",
]
```

```python
matrix_missing = "registries/native_capability_routing_matrix.yaml" not in text
index_missing = "registries/agent_runtime_selection_index.yaml" not in text
files_created = re.search(r"(?im)^\\s*[-*]?\\s*`?files_created`?\\s*=\\s*true\\b", text) is not None
dossier_created = re.search(r"(?im)^\\s*[-*]?\\s*`?dossier_artifacts_created`?\\s*=\\s*true\\b", text) is not None
source_claim_without_list = (
    re.search(r"(?im)^\\s*[-*]?\\s*`?real_time_sources_used`?\\s*=\\s*true\\b", text) is not None
    and not re.search(r"(?im)^\\s*[-*]?\\s*`?source_list(?:_present)?`?\\s*=\\s*(true|\\[|http)", text)
)
final_proof = find_key_value(text, "proof_classification") or find_key_value(text, "final_proof_classification")
final_status_matches_weakest = not (final_proof == "PASS" and status != "PASS")
```

validator_content_proof_created=true
