# Bad Fixture: Dominant Failure Must Escalate Route Slice Registry Failure

route_id=SCRIPT_GENERATION
task_mode=script_only
route_manifest_path=registries/route_manifests/script_generation.yaml
selected_route_slice_path=registries/route_slices/not_real.registry_slice.yaml
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
semantic_influence_map_present=true
output_phase_started=true
final_script_generated=true
validators_run=true
production_pass_allowed=true
artifacts_present=true
proof_json_present=true
artifact_path=/tmp/fake/master.mp4
proof_json_path=/tmp/fake/proof.json
FINAL_PROOF_STATUS=PASS

This fixture looks healthy on the self-reported surface, but the route slice does not exist in the registry.
