# Phase 8 Validator Platform Drift Ledger

| Validator/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| `validators/validate_script_generation_output.py` | `29-38`, `59-67`, `3027-3080`, `3246-3382`, `4531-4630`, `4964-4980` | `HOOK_VARIANTS`, `RECURRING_REHOOK_MAP`, `CINEMATIC_SHORT_STORY_BLOCK`, `SCRIPT_BODY_DEPTH_LOCK`, `VALIDATION_SCORECARD`, `FINAL_SCRIPT`, `DYNAMIC_TIMED_BEAT_MAP`, recurring rehook rules | Content-script output gate with retention, hook density, story block, and media-factory checks | REPLACE | It is tuned for YouTube/content scripting, not cinema-first screenplay validation | `validate_film_screenplay_packet.py` plus filmcraft validators | No | A film route could be falsely PASSed by content-mode checks |
| `validators/validate_mac06_1a_output.py` | `20-25`, `51-82`, `170-231`, `1905-2085`, `4531-4630` | Hook generation gate, recurring rehook map, 5-minute/3-10 minute rules, script body depth lock | Heavy content-engineering standard with fixed hook cadence and spoken runtime expectations | REPLACE | The gate defines content retention behavior, not filmcraft story structure | `validate_film_scorecard_no_fake_pass.py` | No | Makes film output look valid when it only satisfies content rules |
| `validators/validate_route_mode_contract.py` | `19-24`, `35`, `68-85` | `SCRIPT_GENERATION`, `script_only`, `script_plus_visual_plan`, `script_plus_media_factory_handoff`, `standard_script` rejection | Route-mode guard for content script vs downstream media branches | REFACTOR | Useful route normalization, but still content-bound | `validate_film_route_selection.py` | Yes, downstream routing | Could block a future film route unless a separate film mode exists |
| `validators/validate_route_scope_telemetry_law.py` | `23-35`, `85-123` | 68-file route scope, selected route manifest/slice, dependency completion, output phase | Generic route-scope telemetry and proof-law gate | KEEP | Strong reusable governance | `validate_film_route_scope_telemetry.py` if needed | Yes | Safe to reuse; low drift risk |
| `validators/validate_route_consumption_order.py` | `7-25`, `27-57` | Mandatory read order, `script_generation.yaml`, `CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`, `SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`, `SCRIPT_STORY_ENGINE_CONTRACT.md` | Boot/dependency consumption order gate with content-script ordering | REFACTOR | Good boot discipline, but it encodes content-route ordering | `validate_film_boot_consumption_order.py` | Yes | Could be reused with a film route order |
| `validators/validate_evidence_bundle.py` | governance wrapper | Evidence bundle integrity | Generic evidence / provenance gate | KEEP | Reusable governance | `validate_film_evidence_bundle.py` if needed | Yes | Low risk |
| `validators/validate_route_state_capsule.py` | route-state capsule checks | Route state, output phase, ledger, no fake pass | Generic route-state boundary | KEEP | Reusable state governance | `validate_film_route_state_capsule.py` if needed | Yes | Low risk |
| `validators/validate_patch_transaction.py` | patch provenance rules | Patch transaction provenance | Generic change-control gate | KEEP | Reusable provenance law | none required immediately | Yes | Low risk |
| `validators/validate_phase0_control_plane.py` | proof-plane and no-fake-pass clauses | Proof plane, repository lock, completion certificate, evaluator separation | Generic control-plane validator | KEEP | Reusable proof/governance spine | `validate_film_proof_plane.py` only if film route needs separate proof | Yes | Low risk |
| `validators/validate_visual_media_plan_row.py` | visual media row validation | Visual media plan row | Downstream visual production support | MOVE | Useful for downstream distribution only | `validate_film_visual_plan_row.py` only if reused later | Yes | Safe downstream, not film-core |
| `validators/validate_final_visual_media_generation_draft.py` | final visual draft checks | Final visual media generation draft | Downstream media production support | MOVE | Keeps visual handoff healthy, but not film screenplay validation | `validate_film_visual_generation_draft.py` only if needed later | Yes | Safe downstream, not film-core |

### Content-mode drift patterns

The strongest drift is concentrated in the script validators:

* recurring hooks every 25 seconds
* hook variants as mandatory proof
* retention and cadence locks
* short-story block before the teaching section
* spoken runtime and media-factory handoff expectations
* dynamic beat-map checks optimized for content retention

That is useful for content routes, but it is not a film screenplay canon.

### Governance patterns worth keeping

The reusable and safe validator spine is:

* route state
* route-scope telemetry
* dependency order
* evidence bundles
* patch provenance
* no fake pass / no self-certification
* proof-plane separation

### Biggest collision risk

Without a film-specific validator family, a future cinema route could be validated by content-mode hook and retention rules and accidentally receive a false PASS.
