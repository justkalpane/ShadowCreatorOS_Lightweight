# Gold Fixture: Concrete Tool Ledger With Route Evidence

FINAL_PROOF_STATUS=PASS
route_manifest_read=true
selected_route_slice_read=true
tool_ledger_present=true
total_route_scope_files_read=4

Repo Consumption & Tool Execution Ledger:

1. action=view_file
   path=AGENTS.md
2. action=view_file
   path=registries/task_intent_routing_matrix.yaml
3. action=view_file
   path=registries/route_manifests/script_generation.yaml
4. action=view_file
   path=registries/route_slices/script_generation.registry_slice.yaml
5. action=run_command
   command=rg -n "route_id" registries/route_manifests/script_generation.yaml

claim=route manifest and selected route slice consumed
evidence=concrete file paths and action markers are present
evidence_path=registries/route_manifests/script_generation.yaml
command_output_or_file_reference=run_command rg route_id
status=PASS

