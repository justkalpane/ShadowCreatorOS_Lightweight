# Script Generation Deep RCA

## Scope

This document records the failure analysis for the earlier 5-minute YouTube script generation attempt around the Yash topic.

It is based on:

- the attached conversation transcript
- the current repo contracts and route manifests
- the earlier generated script and its audit discussion

This is a forensic audit document, not the blueprint or patch plan.

## Core Conclusion

The main failure was **module/model execution drift**, not a missing repo governance model.

The repo does contain quality gates, debate/critique/refinement controls, governance checks, approval gates, route-state evidence, and recurring re-hook requirements. The earlier script output failed because those controls were not translated into a visible, auditable production artifact with enough cadence, proof, and retention pressure.

## Audit Question

The user asked whether the repo was missing the audit/debate/approval system or whether the model failed to follow it.

### Answer

- The repo does contain the control layer.
- The earlier response did not prove that the control layer was executed end to end.
- The script therefore behaved like a partially governed output, not a fully audited production script.

## What Was Actually Present in the Repo

- `Topic Intake Gate`
- `Topic Quality Gate`
- `Director / Skill Selection Gate`
- `Research Sufficiency Gate`
- `Script Quality Gate`
- `Critique / Refinement Gate`
- `Governance Lock`
- `Final Approval Gate`
- route state and audit-event evidence surfaces
- recurring re-hook density requirements
- dynamic beat map requirements
- source ledger and fact-vs-anecdote mapping for real-person proof

Relevant contract evidence:

- [TASK_INTENT_ROUTING_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md)
- [CHAT_APPROVAL_GATE_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md)
- [CONTENT_ENGINEERING_OUTPUT_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md)
- [SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md)
- [TASK_EXECUTION_STATE_MACHINE_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md)
- [DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md)
- [QUALITY_GATE_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/QUALITY_GATE_CONTRACT.md)

## Failure Pattern Summary

The earlier script failed in four layers:

1. **Structural failure**  
   The beat map was summary-like instead of production-timed.

2. **Retention failure**  
   The re-hook rhythm was too soft for a 5-minute YouTube script.

3. **Performance failure**  
   The script read like an article instead of spoken, camera-facing content.

4. **Evidence failure**  
   The output did not visibly surface the audit trail, scorecard, source mapping, or route-state evidence the repo expects.

## Repo vs Module Drift

### Repo drift

Low to moderate.

The repo already encodes the required control layers. The later audit work confirmed the repo is not merely “missing approval logic.” It already has the necessary language and route expectations.

### Module/model drift

High.

The model did not consistently translate the repo’s control laws into the script output. The result was output that was valid enough to read, but not valid enough to behave like a production script under the repo’s own gates.

## Gate-by-Gate Failure Summary

### 1. Topic Quality Gate

- **repo expectation:** sharp topic framing, audience promise, transformation target
- **observed output:** topic was on-theme, but not fully engineered around one sharp audience outcome
- **root cause:** the topic was treated as a theme, not a conversion target
- **hardening action:** define a one-line topic contract before drafting

### 2. Hook Generation Gate

- **repo expectation:** at least three scored opening hook variants
- **observed output:** hooks existed, but lacked enough contrast and tension
- **root cause:** hook generation was under-diversified
- **hardening action:** force contrarian, emotional, and story-based variants and score them

### 3. Cinematic Short Story Block

- **repo expectation:** 45-75 second cinematic short story for 3-10 minute scripts
- **observed output:** Yash story was present, but compressed and explanatory
- **root cause:** story was used as proof text instead of momentum engine
- **hardening action:** expand into setup, conflict, turning point, emotional peak, bridge

### 4. Source / Fact Mapping

- **repo expectation:** real-person proof requires source ledger and fact-vs-anecdote map
- **observed output:** facts were used, but the proof layer was not surfaced cleanly
- **root cause:** source evidence was implicit instead of ledgered
- **hardening action:** expose structured source rows and downgrade unsupported absolutes

### 5. Source Limitation Disclosure

- **repo expectation:** disclose what is verified, what is not, and why it matters
- **observed output:** the draft did not clearly separate verified claim vs motivational inference
- **root cause:** fact and persuasion were blurred
- **hardening action:** add a concise limitation block before the final script

### 6. Claim Evidence Status

- **repo expectation:** line-level evidence rows for production-sensitive claims
- **observed output:** no explicit claim ledger
- **root cause:** prose output replaced evidence traceability
- **hardening action:** map each fact-like line to a source or mark as anecdotal

### 7. Recurring Re-hook Density Gate

- **repo expectation:** recurring re-hooks are mandatory and distinct from opening hook
- **observed output:** re-hooks existed conceptually, but lacked pressure
- **root cause:** attention resets were too soft
- **hardening action:** prebuild the re-hook map and make each reset force a new motion

### 8. Script Body Depth Lock

- **repo expectation:** 5-minute script should normally land around 675-950 spoken words
- **observed output:** script felt like a compact explanation
- **root cause:** optimization for readability instead of runtime coverage
- **hardening action:** estimate runtime first and draft to spoken word target

### 9. Dynamic Timed Beat Map

- **repo expectation:** 3-20 second blocks with duration reason and retention reset goal
- **observed output:** beat map looked like an outline, not a timeline
- **root cause:** structure was described, not operationalized
- **hardening action:** build scene-level timing blocks with cue stack and retention goal

### 10. Validation Scorecard

- **repo expectation:** visible weakest-gate scorecard before final proof
- **observed output:** no auditable gate-by-gate scorecard was surfaced
- **root cause:** quality was asserted, not demonstrated
- **hardening action:** add pass/fail per gate and let the weakest gate control final status

### 11. Governance Lock

- **repo expectation:** directors selected, governance applied, approval or rejection recorded
- **observed output:** no convincing visible governance trail
- **root cause:** governance existed in repo but not in the surfaced answer shape
- **hardening action:** emit the governance block explicitly with approval or repair route

### 12. Line-by-Line Influence Map

- **repo expectation:** each major line should trace back to hook, story, source, or retention logic
- **observed output:** no explicit line influence map
- **root cause:** the script was delivered as a finished artifact, not as a traceable build
- **hardening action:** attach a line influence map to the draft

### 13. Script Quality Gate

- **repo expectation:** critique/refinement delta, not just polished prose
- **observed output:** language was clear, but not sufficiently critique-hardened
- **root cause:** model optimized for surface quality over performance quality
- **hardening action:** run a critique pass against smoothness, then rewrite for spoken punch

### 14. Route-State and Audit Event Evidence

- **repo expectation:** route-state capsule and audit-event surfaces for execution evidence
- **observed output:** route-state / audit-event proof was not shown
- **root cause:** the route was treated as output-only instead of stateful execution
- **hardening action:** add route-state checks before final proof

## RCA by Failure Type

### A. Cadence Failure

The script did not reset attention often enough. The output was coherent, but too smooth.

### B. Density Failure

There were not enough forceful transitions, contrast pivots, or “stop and pay attention” beats.

### C. Proof Failure

The output did not visibly demonstrate source lineage, scorecard lineage, or approval lineage.

### D. Runtime Failure

The script was not calibrated like a 5-minute spoken performance.

### E. Governance Display Failure

The repo’s critique / governance / approval logic was not surfaced as visible state.

## Was the Audit / Debate / Approval Process Followed?

Strict answer: **not convincingly**.

The repo has those controls, but the earlier output did not show enough proof that they were executed and passed in the way the repo expects.

So the correct diagnosis is:

- not “repo lacks governance”
- not “blind approval is intended”
- but “the model failed to surface and honor governance at production depth”

## The Most Important Missing Gaps Noted Later

Additional gaps identified after the first pass:

- source limitation disclosure
- claim evidence rows
- line-by-line influence map
- route-state capsule evidence
- audit-event evidence
- explicit governance visibility
- story thickness
- runtime calibration
- re-hook traceability

## Future Hardening Note

The user requested that later patching should move the default re-hook gap from **90 seconds to 25 seconds**.

That change should not be applied as a single number edit.

It will require a repo-wide consistency pass because the same timing logic appears in multiple places, including:

- [DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md)
- [CONTENT_ENGINEERING_OUTPUT_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md)
- [TASK_EXECUTION_STATE_MACHINE_CONTRACT.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md)
- [registries/route_manifests/script_generation.yaml](/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/route_manifests/script_generation.yaml)
- [MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md](/Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md)

This audit records the change request only. No patch is applied here.

## Next Step

Use this RCA as the source for a stricter severity/evidence/fix-owner table, then convert that table into the blueprint for batch-by-batch repair.
