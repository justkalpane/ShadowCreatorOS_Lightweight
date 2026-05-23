# MAC-06.1J/K Route Scope and Manifest Proof

ROUTE_SCOPE_AND_MANIFEST_PROOF_STATUS=PASS

## Manifest Inventory

| route_id | manifest_path | line_count | directors | agents | subagents | skills | subskills | status |
|---|---|---:|---:|---:|---:|---:|---:|---|
| TOPIC_DISCOVERY | `registries/route_manifests/topic_discovery.yaml` | 64 | 5 | 5 | 5 | 6 | 5 | PASS |
| SCRIPT_GENERATION | `registries/route_manifests/script_generation.yaml` | 74 | 6 | 6 | 5 | 9 | 8 | PASS |
| SCRIPT_REFINEMENT | `registries/route_manifests/script_refinement.yaml` | 25 | 4 | 4 | 3 | 6 | 4 | PASS |
| CONTEXT_ENGINEERING | `registries/route_manifests/context_engineering.yaml` | 25 | 5 | 5 | 4 | 5 | 5 | PASS |
| VOICE_CONTEXT | `registries/route_manifests/voice_context.yaml` | 25 | 3 | 3 | 2 | 5 | 1 | PASS |
| AVATAR_VIDEO_CONTEXT | `registries/route_manifests/avatar_video_context.yaml` | 25 | 5 | 4 | 4 | 5 | 5 | PASS |
| EDITING_PACKAGING | `registries/route_manifests/editing_packaging.yaml` | 25 | 4 | 3 | 4 | 8 | 3 | PASS |
| FULL_VIDEO_PIPELINE | `registries/route_manifests/full_video_pipeline.yaml` | 27 | 11 | 11 | 6 | 8 | 7 | PARTIAL |

## Route IDs

- `TOPIC_DISCOVERY`
- `SCRIPT_GENERATION`
- `SCRIPT_REFINEMENT`
- `CONTEXT_ENGINEERING`
- `VOICE_CONTEXT`
- `AVATAR_VIDEO_CONTEXT`
- `EDITING_PACKAGING`
- `FULL_VIDEO_PIPELINE`

## Binding Proof

missing_bindings=none_detected_by_path_existence_scan
NEEDS_CONFIRMATION_items=none_detected_in_route_manifests
create_missing_registry_binding=false

Every manifest includes:

- `mandatory_startup_docs`
- `mandatory_runtime_contracts`
- `mandatory_registries`
- `mandatory_directors`
- `mandatory_agents`
- `mandatory_subagents`
- `mandatory_skills`
- `mandatory_subskills`
- `mandatory_governance`
- `mandatory_output_blocks`
- `required_locks`
- `fail_rules`
- `partial_rules`
- `pass_rules`

## FULL_VIDEO_PIPELINE Partial Reason

FULL_VIDEO_PIPELINE=PARTIAL
full_video_pipeline_partial_reason=provider/media/n8n activation remains disabled until separately proven and approved.

## Gumloop Boundary

gumloop_is_benchmark_only=true
gumloop_not_source_registry_truth=true

The active route source of truth is the local repo:

- `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
- `registries/task_intent_routing_matrix.yaml`
- `registries/route_manifests/*.yaml`
- local directors, agents, subagents, skills, subskills, registries, and runtime contracts.
