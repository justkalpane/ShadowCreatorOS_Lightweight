# MAC-06.1J/K Remote File Presence Audit

MAC_06_1J_K_REMOTE_FILE_PRESENCE_AUDIT_STATUS=PASS

local_head=c9d73a28da8d551639f95edd73bd18729f43b2d3
remote_origin_main=c9d73a28da8d551639f95edd73bd18729f43b2d3
local_matches_remote=true

bootstrap_prompt_local_present=true
bootstrap_prompt_tracked=true
bootstrap_prompt_in_head=true
bootstrap_prompt_in_origin_main=true

route_manifests_local_present=true
route_manifests_tracked=true
route_manifests_in_head=true
route_manifests_in_origin_main=true

script_generation_manifest_local_present=true
script_generation_manifest_tracked=true
script_generation_manifest_in_head=true
script_generation_manifest_in_origin_main=true

ignored_by_gitignore=false
ignore_rule=

repair_needed=false
repair_performed=false
repair_commit_hash=
push_success=false

n8n_started=false
providers_called=false
media_artifacts_created=false
dossier_4_started=false

safe_to_rerun_test_b_bootstrap_required=true
safe_to_declare_lightweight_os_onboarded=false
safe_to_start_n8n_execution_bus=false

NEXT_ACTION=Rerun Codex Cloud preflight with explicit path checks against origin/main because the required files are present in the remote commit.

## Evidence Summary

Required files verified in local filesystem, Git tracking, committed `HEAD`, and fetched `origin/main`:

- `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md`
- `registries/route_manifests/`
- `registries/route_manifests/script_generation.yaml`

`git check-ignore` returned no ignore rule for the bootstrap prompt or script generation route manifest.

The Codex Cloud preflight result:

```text
bootstrap_operating_mode_prompt_present=false
route_manifests_folder_present=false
script_generation_route_manifest_present=false
```

is contradicted by the remote Git tree at commit `c9d73a28da8d551639f95edd73bd18729f43b2d3`.
