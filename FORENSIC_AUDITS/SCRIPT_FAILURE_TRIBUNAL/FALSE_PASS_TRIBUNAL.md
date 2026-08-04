# False Pass Tribunal

| claim | reality | verdict | evidence | severity |
| --- | --- | --- | --- | --- |
| `topic_quality_gate_present=true` | No `TOPIC_QUALITY_GATE` section appears in the inspected transcript | FALSE_PASS | `/Users/apple/.codex/attachments/b1a5eaa5-e7a3-44f5-a1a9-9494f8360a6a/pasted-text.txt:35-38` and `validators/validate_mac06_1a_output.py:659-662, 949-952` | P0 |
| `hook_generation_gate_present=true` | No scored `HOOK_GENERATION_GATE` block appears in the inspected transcript | FALSE_PASS | same transcript plus `validators/validate_mac06_1a_output.py:423-426, 949-952` | P0 |
| `script_quality_gate_present=true` | No `script_overall_score` or `script_pass_threshold` appears | FALSE_PASS | `validators/validate_mac06_1a_output.py:647-667, 953` | P0 |
| `route_scope_file_audit_present` with `missing_required_repo_scope=None` | Required structured proof blocks are still missing | FALSE_PASS | transcript `:15-24` versus acceptance tests `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:64-85` | P1 |

