# Executive Summary

## What failed

The reference script failed as a production-grade, repo-driven script because it
looked complete while missing the required proof surfaces. The failure is a mix
of model error, proof-shape drift, and one real repo-gap.

## Proven flaws

1. Route proof was not canonical.
   - The transcript used `TASK_INTENT_ROUTING_LEDGER`-style proof instead of the
     required lock order and route-state proof.
   - Required order and route-state fields are defined in
     `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md:8-19, 30-70`.

2. Beat timing violated the contract.
   - The repo allows dynamic blocks only in the `3-20` second range.
   - The transcript contains `50`, `60`, `65`, `50`, and `30` second blocks.
   - Evidence:
     `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md:10-14, 54-56`
     and `/Users/apple/.codex/attachments/b1a5eaa5-e7a3-44f5-a1a9-9494f8360a6a/pasted-text.txt:129-220`.

3. Source proof was too shallow for a real-person script.
   - The repo requires at least 3 sources, 2 non-encyclopedia sources, and 3
     source categories when suitable sources exist.
   - The transcript shows only 2 source rows.
   - Evidence:
     `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md:77-89`
     and `runtime_contracts/SOURCE_QUALITY_CLASSIFICATION_CONTRACT.md:22-39`.

4. Unsupported absolutes were spoken as fact.
   - The contracts forbid unsupported absolutes like `every`, `always`,
     `never`, `only`, `all`, and `entirely` unless source-backed.
   - The transcript uses exactly that style of language.
   - Evidence:
     `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md:218-223`
     and `/Users/apple/.codex/attachments/6fa3b68e-40a2-4839-97a8-9f1fb9a11644/pasted-text.txt:233-251`.

5. Integrity and quality proof were not fully emitted.
   - The repo expects `TOPIC_QUALITY_GATE`, `HOOK_GENERATION_GATE`,
     `SCRIPT_QUALITY_GATE`, `SCRIPT_BODY_DEPTH_LOCK`,
     `RECURRING_HOOK_DENSITY_LOCK`, and `GOVERNANCE_LOCK`.
   - The transcript prints pass-like booleans, but not the full scorecard and
     lock proof surface.
   - Evidence:
     `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md:17-53, 154-204`
     and `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md:171-198`.

6. Lineage and influence mapping is incomplete.
   - The repo requires `LINE_BY_LINE_INFLUENCE_MAP` and exact rule lineage for
     critical lines.
   - The transcript only shows partial lineage proof.
   - Evidence:
     `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md:16-26, 87-132`
     and `/Users/apple/.codex/attachments/b1a5eaa5-e7a3-44f5-a1a9-9494f8360a6a/pasted-text.txt:117-124`.

## Real repo-gap

The canonical `SCRIPT_GENERATION` route slice is narrower than the acceptance
surface.

- `registries/route_slices/script_generation.registry_slice.yaml:63-66` only
  requires `SCRIPT_BODY_DEPTH_LOCK`, `FINAL_SCRIPT`, and
  `DYNAMIC_TIMED_BEAT_MAP`.
- `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:64-85,
  146-159` also expects `VALIDATION_SCORECARD` and
  `script_integrity_lock=PASS`.

That mismatch is a real repo-gap, not just a model mistake.

## Failure classification

- `MODEL_ERROR`: yes
- `REPO_GAP`: yes
- `SHARED_FAILURE`: yes

## P0 blockers to carry forward

1. Beat-map overflow.
2. Missing structured source rows.
3. False quality/pass claims without a real scorecard.
4. Missing line-by-line influence map.

## What to trust for the next P0 pass

- The current lightweight repo is the production authority for this audit.
- The backup mirror was mirror-only evidence storage.
- The prior tribunal findings remain applicable to the current repo.

## Next safe step

Start the P0 repair cycle against the current repo only:

1. Rebuild the beat map.
2. Emit structured source and fact rows.
3. Emit a real quality scorecard.
4. Emit a full line-by-line influence map.
5. Align the canonical route slice with acceptance-test integrity proof.
