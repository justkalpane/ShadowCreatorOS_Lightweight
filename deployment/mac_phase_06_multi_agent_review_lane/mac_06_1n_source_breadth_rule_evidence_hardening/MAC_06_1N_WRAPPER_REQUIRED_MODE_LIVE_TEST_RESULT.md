# MAC-06.1N Wrapper Required Mode Live Test Result

```text
MAC_06_1N_WRAPPER_REQUIRED_MODE_LIVE_TEST_STATUS=PASS_WITH_NOTICE
structure_status=PASS
source_breadth_lock_status=PASS
rule_consumption_evidence_lock_status=PASS_WITH_NOTICE
per_tool_source_map_present=true
exact_rule_evidence_present=true
role_summary_only_detected=false
all_required_locks_passed=true
```

## Important Limitation

The result was produced with a long explicit wrapper-style prompt.

Therefore, it proves:

```text
wrapper_required_mode_proven=true
raw_layman_default_mode_proven=false
```

It does not prove that a normal raw layman task automatically triggers the full lock sequence in Codex Cloud.

## Safe Status

```text
safe_to_use_wrapper_required_mode=true
safe_to_declare_default_bootstrap_mode_onboarded=false
safe_to_declare_lightweight_os_onboarded=false
safe_to_start_n8n_execution_bus=false
```

## Next UX Fix

MAC-06.1O must provide a layman command gateway so users can type:

```text
Shadow script: <normal task>
```

while Shadow OS internally applies the full task execution wrapper.

