# Bad Fixture: PASS Claim With Fake Route Slice Path

route_id=SCRIPT_GENERATION
task_mode=script_only
route_manifest_path=registries/route_manifests/script_generation.yaml
selected_route_slice_path=registries/route_slices/not_real.registry_slice.yaml
route_manifest_read=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
semantic_influence_map_present=true
output_phase_started=true
final_script_generated=true
validators_run=true
FINAL_PROOF_STATUS=PASS

CLAIM_EVIDENCE_STATUS
claim=PASS is claimed with a fake but plausible route slice path.
evidence=The path string exists only in the claim surface, not in the registry.
status=PASS
