# Route State Persistence Contract

## Purpose

This contract defines the persisted state needed to recover from compaction or
continuation without restarting the boot loop.

## Required Fields

```text
route_id
route_manifest_path
route_manifest_hash
task_intent
output_mode
phase
last_completed_lock
next_required_lock
files_read
file_hashes
selected_directors
selected_agents
selected_subagents
selected_skills
selected_subskills
evidence_scope
evidence_bundle_id
evidence_bundle_schema_path
validator_ledger
validator_results
bridge_job_packet_path
bridge_job_packet_hash
patch_transaction_id
compaction_recovery_allowed
final_output_allowed
```

## Rule

If `post_bootstrap_task_persistence_status=FAILED`, final onboarding cannot be
declared `PASS` without an explicit recovery proof.
