# Script Failure Tribunal

## Verdict

This audit proves a real production failure in the generated 5-minute script.
The failure is not a single issue. It is a stack of:

- model error
- contract mismatch
- route-scope under-specification
- false-pass reporting

## Proven root causes

1. The beat map violates the hard `3-20` second block law.
2. The script claims source proof without structured `source_row_json` and `fact_map_row_json` rows.
3. The output claims quality/pass status without the required scorecard fields.
4. The canonical route surface does not elevate `VALIDATION_SCORECARD` or `script_integrity_lock`, even though acceptance tests require them.
5. The output omits the required `LINE_BY_LINE_INFLUENCE_MAP` section entirely.

## Evidence anchor set

- `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md:10-14, 32-56`
- `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md:77-89, 155-201, 216-227`
- `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md:40-53, 93-115, 154-204, 218-223`
- `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md:8-19, 30-70, 151-198`
- `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md:19-36, 53-59, 87-108`
- `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md:6-26, 30-44, 53-85, 87-132`
- `registries/route_manifests/script_generation.yaml:119-130, 178-210, 245-279`
- `registries/route_slices/script_generation.registry_slice.yaml:63-66`
- `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:64-85, 146-159`
- `validators/validate_script_generation_output.py:2210-2318, 2320-2552, 2070-2087`
- `validators/validate_mac06_1a_output.py:647-667, 760-823, 923-953`
- `/Users/apple/.codex/attachments/b1a5eaa5-e7a3-44f5-a1a9-9494f8360a6a/pasted-text.txt:48-85, 117-220, 227-254`

## Classification

- `MODEL_ERROR`: yes
- `REPO_GAP`: yes
- `SHARED_FAILURE`: yes

## Proven counts

- P0 blockers proven: 4
- P1 blockers proven: 2
- P2 blockers proven: 0
- P3 blockers proven: 0

## What was not proven

- No separate primary knowledge failure was proven.
- No isolated agent-only or subagent-only root cause was proven.
- No corruption / dead-file / orphan-file proof was established from the inspected evidence set.

