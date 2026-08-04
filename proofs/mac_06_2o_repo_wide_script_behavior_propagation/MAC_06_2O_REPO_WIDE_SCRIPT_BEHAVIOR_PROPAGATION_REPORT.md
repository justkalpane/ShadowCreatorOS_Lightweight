# MAC-06.2O Repo-Wide Script Behavior Propagation Report

## PATCH_SUMMARY

The prior script/media contracts are now propagated into active script-route
actors and executable nodes. The patch adds a recurring hook-density law:

- Three opening hook variants select the opening hook only.
- Every 3-10 minute YouTube script requires dynamic recurring re-hooks.
- The default interval is 70-90 seconds.
- An unexplained gap above 90 seconds is rejected.
- A five-minute script requires at least three internal re-hooks plus a CTA
  hook.
- Media Factory final drafts must map re-hooks into scene synchronization.

## REPO_WIDE_DISCOVERY_SUMMARY

```text
total_text_files_scanned=4207
keyword_candidates_detected=1721
propagated_actor_marker_files=67
propagation_gate_files_checked=63
missing_patch_files=0
```

The 63 gate-checked files are recorded in
`PROPAGATION_AUDIT_TABLE.csv`. Additional marker files are supporting creative
skill specs that consume the law but are not required by the validator gate.

## PROPAGATION_GATE

```text
DIRECTOR checked=10 missing=0
AGENT checked=11 missing=0
SUBAGENT checked=5 missing=0
SCRIPT_SKILL checked=11 missing=0
SUBSKILL checked=6 missing=0
EXECUTABLE_SKILL checked=20 missing=0
```

## HOOK_DENSITY_ENFORCEMENT

```text
opening_hook_variants_required=true
recurring_rehooks_required=true
default_rehook_interval_seconds=70-90
max_gap_without_rehook_seconds=90
five_minute_minimum_internal_rehooks=3
cta_hook_required=true
rehooks_mapped_to_script=true
rehooks_mapped_to_beat_map=true
rehooks_mapped_to_influence_map=true
rehooks_mapped_to_scene_sync_matrix_when_media_factory_final=true
```

Strict packet probes:

```text
3m required=1 points=[90] max_gap=90
5m required=3 points=[75, 150, 225] max_gap=75
6m required=4 points=[72, 144, 216, 288] max_gap=72
10m required=6 points=[86, 171, 257, 343, 429, 514] max_gap=86
```

## VALIDATOR_AND_SCHEMA_UPDATES

- `validators/validate_script_generation_output.py` checks propagation,
  recurring re-hook density, max gap, dynamic timing fields, output mappings,
  Media Factory scene sync, source honesty, language control, and weakest-gate
  status.
- `schemas/media_factory/scene_sync_matrix.schema.json` requires
  `hook_marker`. Re-hook scenes require `rehook_type` and
  `retention_reset_goal`.
- `deployment/proofs/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md` includes
  propagation, hook-density, and Media Factory re-hook synchronization tests.

## VERIFICATION

```text
git_diff_check=PASS
python_compile=PASS
scene_sync_schema_json_parse=PASS
script_generation_validator_self_test=PASS (16/16)
script_generation_route_validation=PASS
script_generation_vein_validation=PASS
script_generation_packet_validation=PASS
script_generation_dry_run=PASS
shadow_runtime_regression=PASS (20/20)
validator_integrity_scanner=PASS
schema_rationalizer=PASS
provider_boundary=PASS
preflight=PASS
```

## REMAINING_LIMITATIONS

- This proves local repo behavior propagation and structural enforcement. It
  does not prove final creative quality for every future script topic.
- No provider, n8n, or media execution was started.
- The working tree intentionally remains uncommitted for user review.
- Lightweight OS onboarding remains false.

## DO_NOT_COMMIT_STATUS

```text
commit_performed=false
push_performed=false
```

## FINAL_CLASSIFICATION

```text
MAC_06_2O_REPO_WIDE_SCRIPT_BEHAVIOR_PROPAGATION_STATUS=PASS
```
