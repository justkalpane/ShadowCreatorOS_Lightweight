# Local Repo Trigger Simulation (What Should Have Happened)

prompt="Create a YouTube Shorts script on Is AI is replacing the Human or humans are replacing the humans?"
expected_output_mode=CHAT_ONLY_MODE
files_created=false

## Expected Boot Sequence (First Visible Output)

The first visible output should be a boot confirmation (not a script), proving the repo was actually used:

- agents_md_detected=true
- agents_md_read=true
- layman_task_trigger_contract_read=true
- generic_direct_answer_avoided=true
- shadow_mode=CHAT_ONLY_MODE
- next_stage=Native Capability Assessment

## Required Repo Reads (Evidence Paths)

The agent should cite these exact paths before generating any script:

1. `AGENTS.md`
2. `START_HERE_FOR_AGENTS.md`
3. `AGENT_READ_ORDER.md`
4. `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
5. `AGENT_ANTI_DRIFT_RULES.md`
6. `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`
7. `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
8. `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
9. `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`
10. `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`
11. `registries/native_capability_routing_matrix.yaml`
12. `registries/agent_runtime_selection_index.yaml`

## Required Routing Proof (Minimal)

The agent should include:

- `NATIVE_AGENT_CAPABILITY_ASSESSMENT` (declares what the environment can actually do)
- `TASK_FRESHNESS_CLASSIFICATION` (EVERGREEN vs CURRENT_SENSITIVE etc.)
- `RESEARCH_MODE_DECISION` (repo_only/web_assisted/real_time_web + web availability/usage disclosure)
- `TASK_TO_CAPABILITY_ROUTING` citing `registries/native_capability_routing_matrix.yaml`
- `AGENT_RUNTIME_SELECTION` citing `registries/agent_runtime_selection_index.yaml`

## Content Engineering Requirement

Because the user asked for a "YouTube Shorts script", the output must include the full content engineering sections from:

`runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`

At minimum:

- CONTENT_MISSION_BRIEF
- RESEARCH_AND_SOURCE_STATUS
- SCRIPT_STRUCTURE
- FINAL_SCRIPT
- TIMED_BEAT_MAP
- VOICE_GENERATION_CONTEXT
- IMAGE_GENERATION_CONTEXT
- VIDEO_GENERATION_CONTEXT
- MUSIC_AND_SFX_CONTEXT
- EDITING_CONTEXT
- PLATFORM_PACKAGING
- PROVIDER_HANDOFF_BOUNDARY (no execution)
- QUALITY_GATE

## Why The Cloud Result Was A Fail

The cloud output jumped straight to a script and omitted the boot proof blocks and routing evidence. Under current contracts, that should be classified FAIL for MAC-06.1A plain layman trigger testing.

