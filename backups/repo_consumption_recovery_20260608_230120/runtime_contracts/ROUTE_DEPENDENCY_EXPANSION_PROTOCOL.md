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
- starting n8n
- calling providers
- creating media
- importing workflows

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
```
