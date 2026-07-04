# Bad Fixture: PASS Claim With Manifest Slice Mismatch

route_id=SCRIPT_GENERATION
task_mode=script_only
route_manifest_path=registries/route_manifests/script_generation.yaml
selected_route_slice_path=registries/route_slices/visual_media_plan.registry_slice.yaml
route_manifest_read=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
semantic_influence_map_present=true
output_phase_started=true
final_script_generated=true
validators_run=true
FINAL_PROOF_STATUS=PASS

CLAIM_EVIDENCE_STATUS
claim=PASS is claimed while the selected route slice belongs to the media factory manifest family.
evidence=Surface booleans are true, but registry lineage conflicts with the declared route.
status=PASS
