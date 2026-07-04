# Script Generation Drift Patch Blueprint

## Authority

- Production authority for repair work: `ShadowCreatorOS_Lightweight`
- Mirror-only evidence store: `Backup/ShadowMediaFactory 1`
- Scope: repair script-generation drift end to end
- Mode: blueprint only, no repo implementation yet

## Repair Strategy

Repair in this order:

1. P0 proof-surface blockers
2. P1 route/validator alignment
3. P2 director/skill consistency
4. P3 cleanup and documentation alignment

Do not start P1 before the P0 proof surface is machine-checkable.

## P0 Blueprint

| priority | file | exact change instructions | why |
| --- | --- | --- | --- |
| P0 | `registries/route_slices/script_generation.registry_slice.yaml` | Expand `output_contracts` so the canonical script route explicitly requires `VALIDATION_SCORECARD` and `LINE_BY_LINE_INFLUENCE_MAP`, not only `SCRIPT_BODY_DEPTH_LOCK`, `FINAL_SCRIPT`, and `DYNAMIC_TIMED_BEAT_MAP`. If the route is kept script-only, keep the downstream media contracts blocked until after `FINAL_SCRIPT`. | The current slice is narrower than the acceptance surface, so integrity proof can be skipped while the route still looks complete. |
| P0 | `registries/route_manifests/script_generation.yaml` | Add `VALIDATION_SCORECARD` to `mandatory_output_blocks` and to the required proof surface. Tighten `pass_rules` so the route cannot pass without a real scorecard, `LINE_BY_LINE_INFLUENCE_MAP`, and weakest-gate proof. If the manifest uses `script_integrity_lock` as the canonical name, require it explicitly. | The manifest must match what the acceptance tests and validator expect. |
| P0 | `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md` | Add an explicit `VALIDATION_SCORECARD` block after `SCRIPT_BODY_DEPTH_LOCK` and before `FINAL_SCRIPT`. Require structured `source_row_json`, `fact_map_row_json`, and `rehook_row_json` rows to be emitted in machine-checkable form. Add a required `SOURCE_LIMITATION_NOTES` or equivalent honesty block if the evidence is partial. | The contract currently allows proof-shaped prose where the audit needs structured proof objects. |
| P0 | `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md` | Add a canonical integrity proof section that requires `TOPIC_QUALITY_GATE`, `HOOK_GENERATION_GATE`, `SCRIPT_QUALITY_GATE`, `VALIDATION_SCORECARD`, `SCRIPT_BODY_DEPTH_LOCK`, `RECURRING_HOOK_DENSITY_LOCK`, and `GOVERNANCE_LOCK` to be explicit before final proof. Require the final proof to match the weakest gate. | The quality layer must stop allowing pass-shaped output without a real scorecard. |
| P0 | `validators/validate_script_generation_output.py` | Harden the validator so the script fails when any of the following are missing: `VALIDATION_SCORECARD`, structured `source_row_json`, structured `fact_map_row_json`, structured `rehook_row_json`, `LINE_BY_LINE_INFLUENCE_MAP`, or canonical route proof blocks in order. Add a fail path for noncanonical route proof labels such as `TASK_INTENT_ROUTING_LEDGER` when they are used as primary proof instead of `TASK_ROUTE_LOCK`. | This is the strongest enforcement point for the drift that produced the shallow artifact. |
| P0 | `validators/validate_mac06_1a_output.py` | Extend the quality checks so `quality_gate_without_threshold` and scoreless hook blocks fail hard when a scorecard is missing. Make `VALIDATION_SCORECARD` a first-class signal instead of a soft presence marker. | The validator must not accept thresholdless quality claims. |
| P0 | `skills/script_intelligence/S-202-first-draft-generation.py` | Remove or gate the placeholder default re-hook fallback. If strict packet mode cannot produce a real re-hook plan, return `failed` or `BLOCKED_BEFORE_OUTPUT` instead of fabricating placeholder hook lines. Ensure the skill emits structured re-hook rows, not pseudo-hook text. | This file can currently drift into generic placeholder output if the upstream packet is incomplete. |
| P0 | `skills/script_intelligence/S-210-final-script-packager.skill.md` | Enforce preservation of `RECURRING_REHOOK_MAP`, `DYNAMIC_TIMED_BEAT_MAP`, `LINE_BY_LINE_INFLUENCE_MAP`, and the new `VALIDATION_SCORECARD` through final packaging. Reject final packaging if any internal re-hook or CTA hook is lost. | Final packaging must not strip the proof surface. |

## P1 Blueprint

| priority | file | exact change instructions | why |
| --- | --- | --- | --- |
| P1 | `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md` | If the repo wants strict canonical ordering, include `VALIDATION_SCORECARD` in the final lock sequence or explicitly bind it to `QUALITY_LOCK` so it cannot be bypassed. Ensure the route-state capsule includes the fields needed to prove route authority and output phase start. | The route state machine should expose the integrity proof, not merely the narrative proof. |
| P1 | `registries/task_intent_routing_matrix.yaml` | Align the `SCRIPT_GENERATION` route entry with the integrity proof surface. If the route currently resolves to `SCRIPT_BODY_DEPTH_LOCK`, `FINAL_SCRIPT`, and `DYNAMIC_TIMED_BEAT_MAP` only, add the missing integrity and influence blocks. | The route router must not advertise a narrower proof surface than the validator expects. |
| P1 | `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md` | No product logic change is required, but keep this file as the acceptance baseline. Only update if the acceptance surface itself changes intentionally. | This is the authoritative acceptance reference, not the implementation target. |
| P1 | `directors/research/vyasa.md` | Add an explicit rejection rule for scoreless 3-10 minute script outputs and require the final script to be accompanied by a full quality/integrity block. | The narrative director should not approve a script without proving retention and structure. |
| P1 | `directors/research/valmiki.md` | Add an explicit requirement that source sufficiency, source categories, and structured fact mapping must be proven before any real-person script is approved. | Research grounding must be strict enough to prevent shallow proof. |

## P2 Blueprint

| priority | file | exact change instructions | why |
| --- | --- | --- | --- |
| P2 | `agents/krishna/krishna_agent.py` | If needed, add a clearer reject condition for missing canonical route-proof blocks and missing weakest-gate honesty. | The governance agent already looks strong, but it can be made more explicit. |
| P2 | `agents/vyasa/vyasa_agent.py` | If needed, add explicit handling for scorecard-complete, re-hook-complete, and line-influence-complete script packets. | This reduces drift toward generic narrative output. |
| P2 | `agents/valmiki/valmiki_agent.py` | If needed, add stronger rejection language for inadequate source breadth or weak evidence serialization. | This reduces the chance of weak source proof reaching the final pack. |
| P2 | `skills/script_intelligence_army/M-039-re-hook-system.skill.md` | If implementation work is needed, force the re-hook system to emit machine-checkable re-hook rows and never generic filler. | The re-hook layer is part of the production proof chain. |
| P2 | `skills/script_intelligence/S-203-retention-engineer.skill.md` | If implementation work is needed, ensure the retention engineer writes its output in a validator-friendly form and not just as descriptive prose. | Retention logic must be inspectable, not only rhetorically strong. |

## P3 Blueprint

| priority | file | exact change instructions | why |
| --- | --- | --- | --- |
| P3 | `FORENSIC_AUDITS/SCRIPT_FAILURE_TRIBUNAL/EXECUTIVE_SUMMARY.md` | Keep as the one-page handoff summary, but if you want it even cleaner, trim it to the four P0 blockers and the one repo-gap. | This is a handoff artifact, not a production file. |
| P3 | `FORENSIC_AUDITS/SCRIPT_FAILURE_TRIBUNAL/ROOT_CAUSE_TREE.md` | Keep as an audit record; no product change needed. | Useful for history, not for runtime repair. |
| P3 | `FORENSIC_AUDITS/SCRIPT_FAILURE_TRIBUNAL/P0_BLOCKER_LEDGER.md` and siblings | Keep as frozen audit history unless you want to add post-fix verification rows later. | These are evidence artifacts, not runtime code. |

## Cross-Cutting Repair Rules

1. Do not let prose substitute for structured proof rows.
2. Do not let `PASS` appear without a scorecard and threshold.
3. Do not let route routing claim completeness unless the route-state capsule is complete.
4. Do not let the final script keep unsupported absolutes.
5. Do not let `LINE_BY_LINE_INFLUENCE_MAP` degrade into route-level summary only.
6. Do not let placeholder hook text leak into final output.

## Recommended Implementation Order

1. Patch validator enforcement first.
2. Patch route manifest and route slice second.
3. Patch content/quality contracts third.
4. Patch script packager and first-draft generator fourth.
5. Patch directors and agents only if the validator still shows drift after the proof surface is fixed.

## End State

The repair is complete only when all of these are true:

- canonical route proof order is explicit
- beat map stays within `3-20` second blocks
- source proof is structured and sufficient
- quality proof includes a real scorecard
- line-by-line influence mapping is present
- unsupported absolutes are downgraded or removed
- the route slice and acceptance surface agree

