# Gold Fixture: Alias Claims With Complete Evidence

route_id=SCRIPT_GENERATION
task_mode=script_only
route_manifest_path=registries/route_manifests/script_generation.yaml
selected_route_slice_path=registries/route_slices/script_generation.registry_slice.yaml
route_manifest_read=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
semantic_influence_map_present=true
output_phase_started=true
final_script_generated=true
validators_run=true
source_research_lock_status=PASS
web_access_used=true
freshness_class=CURRENT
source_ledger_urls_count=2
exact_url_ledger_present=true
consumption_lock_status=PASS
duration_fit_status=PASS
production_pass_allowed=true
artifacts_present=true
proof_json_present=true
artifact_path=/tmp/shadow_media_factory/example/master.mp4
proof_json_path=/tmp/shadow_media_factory/example/proof.json
evidence_scope=persisted_route_state_with_hash
evidence_path=runtime/state/route_state_example.json
command_output_or_file_reference=sha256 route state and source ledger verified
route_id=SCRIPT_GENERATION
route_manifest_hash=sha256:0123456789abcdef
route_state_hash=sha256:abcdef0123456789
route_state_path=runtime/state/route_state_example.json
task_intent=script_generation
output_mode=CHAT_ONLY_MODE
phase=output
last_completed_lock=OUTPUT_PHASE_STARTED
next_required_lock=FINAL_VALIDATION
files_read=AGENTS.md,registries/route_manifests/script_generation.yaml
file_hashes={"AGENTS.md":"sha256:a","registries/route_manifests/script_generation.yaml":"sha256:b"}
selected_directors=Krishna
selected_agents=krishna_agent
selected_subagents=wf_200
selected_skills=S-201
selected_subskills=SS-240
dependencies_complete=true
final_output_allowed=true
compaction_detected=true
compaction_recovery_allowed=true
FINAL_PROOF_STATUS=PASS

Sources:
- https://example.com/source-one
- https://example.com/source-two

CLAIM_EVIDENCE_STATUS
claim=alias pass fields are backed by concrete evidence
evidence=URLs, route state hash, route manifest, route slice, artifact path, proof path
status=PASS
