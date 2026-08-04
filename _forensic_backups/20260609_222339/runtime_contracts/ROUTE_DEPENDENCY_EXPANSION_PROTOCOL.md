# Route Dependency Expansion Protocol

`ROUTE_DEPENDENCY_EXPANSION` means taking the selected `route_id` and expanding it into the complete required repo scope before output.

## Hard Rules

- No output before route dependency expansion.
- No script before route manifest is read.
- No script before all mandatory files for the route are read.
- No script before transitive dependencies are checked.
- No script before governance files are included.
- Gumloop benchmark is reference only, never source registry truth.
- If a route mandatory file is missing, mark `NEEDS_CONFIRMATION` or `BLOCKED`.
- If a file is listed but not read, route lock fails.
- If a component is selected but not consumed, consumption lock fails.

## COMPLETE_REQUIRED_REPO_SCOPE

For a task, complete required repo scope means:

1. startup law files
2. task intent contract
3. task routing matrix
4. selected route manifest
5. route-specific directors
6. route-specific agents
7. route-specific subagents
8. route-specific skills
9. route-specific subskills
10. route-specific runtime contracts
11. route-specific registries
12. governance / quality / risk directors
13. source/research contracts when freshness is required
14. content engineering contract when content/video/script is involved
15. provider boundary contracts if downstream execution is referenced
16. validator/proof expectations for the current mode

It does not mean:

- blindly reading archive/quarantine docs
- blindly reading unrelated routes
- blindly reading historical `outputs/missions` or `downloads/chat_transcript.txt`
- reading Media Factory contracts during `script_only` before `FINAL_SCRIPT`
- rereading unchanged boot files after `ROUTE_LOCKED` without a declared
  reread reason
- starting n8n
- calling providers
- creating media
- importing workflows

## Route-Scoped Registry Slice Law

Normal route execution consumes the selected route manifest and then the
matching route slice in `registries/route_slices/`. Full registries remain
source of truth, but unrelated repo areas are dormant by default.

For supported production routes, the route slice is mandatory. If no matching
route slice exists, block before output. Full registry scans are allowed only in
`audit_mode=true` or `rebuild_mode=true`.

```text
FULL_REPO_IS_AUTHORITY=true
SELECTED_ROUTE_MANIFEST_DEFINES_ACTIVE_SCOPE=true
UNRELATED_REPO_AREAS_DORMANT_BY_DEFAULT=true
FULL_REGISTRY_SCAN_ALLOWED_ONLY_IN_AUDIT_OR_REBUILD_MODE=true
```

## Read Ledger Law

Every consumed file must be recorded in a read ledger with file hash, phase,
read count, reread reason, and semantic-use status. Unchanged file + already
consumed + no allowed reread reason blocks reread.

Allowed reread reasons:

```text
file_hash_changed
audit_mode
validator_mode
explicit_user_requested_compare
route_manifest_changed
krishna_directive_dependency_trace
semantic_influence_verification
compaction_recovery_validation
```

## Required Output Block

```text
ROUTE_DEPENDENCY_EXPANSION_LEDGER
route_id=
route_name=
route_manifest_path=
mandatory_files_expected=
mandatory_files_read=
missing_mandatory_files=
transitive_dependencies_checked=true/false
governance_files_included=true/false
route_scope_complete=true/false
route_scope_status=PASS/FAIL/NEEDS_CONFIRMATION
route_slice_path=
selected_route_slice_read=true/false
mandatory_route_slice_paths_consumed=true/false
read_ledger_present=true/false
repeat_read_blocker_present=true/false
output_phase_gate_present=true/false
semantic_influence_map_present=true/false
final_deliverable_generated=true/false
```
