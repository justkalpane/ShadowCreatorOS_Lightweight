# Antigravity HyperFrames Audit Prompt Pack

Use these prompt blocks in the same Antigravity chat, one stage at a time.

---

## Prompt 1 — HyperFrames Method Test Suite

```text
Antigravity, run a deep HyperFrames method-validation suite for `yash_self_investment`.

This is not a production render. This is a method-by-method capability test and drift audit.

Read these exact files first:
1. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/hyperframes_method_validation_packet.json
2. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/hyperframes_30s_proof_packet.json
3. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/media_factory_packet.json
4. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/support/antigravity_hyperframes_method_test_checklist.md
5. /Users/apple/ShadowMediaFactory/control_panel/templates/hyperframes_template_registry.json
6. /Users/apple/ShadowMediaFactory/control_panel/templates/hyperframes_effect_pack_registry.json

Hard rules:
- No repo changes inside /Users/apple/Documents/ShadowCreatorOS_Lightweight
- No provider calls
- No n8n
- No new image generation
- No Depth Anything V2
- No DaVinci
- No silent fallback
- For alpha overlay tests, `.mov` is the only production-safe output container on this machine

Your job:
- Test every active HyperFrames family one by one
- Test payload injection
- Test source-background integration
- Test V3 effect composition using proved assets
- Test HUD/border treatment
- Test alpha overlay compositing
- Test duration truth and proof truth

For every test return:
- test_id
- template_family
- expected_capabilities
- actual_capabilities
- output_path
- proof_json_path
- registry_evidence_path
- ffprobe_summary
- verification_frame_path
- drift_found=true/false
- drift_reason=
- status=PASS/PARTIAL/BLOCKED

Do not summarize early. Finish the full method suite first.
```

---

## Prompt 2 — Deep Result Analysis

```text
Antigravity, now perform a deep analysis of the HyperFrames method-test outputs you just produced.

Read these exact files first:
1. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/support/antigravity_result_deep_analysis_checklist.md
2. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/hyperframes_method_validation_packet.json
3. all proof JSON files and output artifacts produced in the previous test suite

Hard rules:
- No repo changes
- No provider calls
- No n8n
- Do not convert missing evidence into PASS
- Do not say visible without frame evidence
- Do not say payload honored without text evidence
- Do not say 30 seconds without ffprobe

Your job:
- Compare expected vs actual for every method test
- Identify every drift
- Classify each failure with root-cause categories
- Separate PROVEN_NOW from PRESENT_BUT_NOT_PROVEN
- Separate REQUESTED_BUT_MISSED from OVERCLAIMED
- End with ROOT_CAUSE_PRIORITY_ORDER and SAFE_NEXT_ACTIONS

Use exact claim/evidence/status formatting.
```

---

## Prompt 3 — Repo and Runtime Deep Audit

```text
Antigravity, now run a repo-and-runtime deep audit for the HyperFrames non-cinematic B-roll lane.

Read these exact files first:
1. /Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/support/antigravity_repo_deep_audit_checklist.md
2. /Users/apple/ShadowMediaFactory/07_PROJECTS/hyperframes/package.json
3. /Users/apple/ShadowMediaFactory/control_panel/config/capability_map.json
4. /Users/apple/ShadowMediaFactory/control_panel/templates/hyperframes_template_registry.json
5. /Users/apple/ShadowMediaFactory/control_panel/templates/hyperframes_effect_pack_registry.json
6. /Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/local_media_factory_bridge.yaml
7. /Users/apple/Documents/ShadowCreatorOS_Lightweight/runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md
8. /Users/apple/Documents/ShadowCreatorOS_Lightweight/skills/sub_skills/SS-116-notebooklm-visual-style-orchestrator.subskill.md
9. /Users/apple/Documents/ShadowCreatorOS_Lightweight/skills/sub_skills/SS-117-depth-anything-v2-depth-map-generator.subskill.md
10. /Users/apple/Documents/ShadowCreatorOS_Lightweight/skills/sub_skills/SS-118-hyperframes-html-renderer.subskill.md

Hard rules:
- No repo changes
- No provider calls
- No n8n
- No speculative promotion

Your job:
- classify each capability as PROVEN / FEASIBLE_WITH_TEMPLATE_ENGINEERING / NOT_PRESENT / NEEDS_HARDENING
- correct all overclaims
- list safe-to-promote modules
- list do-not-claim-yet modules
- identify repo truth gaps and runtime truth gaps

Use exact claim/evidence/status formatting.
```

---

## Prompt 4 — Codex Return Handoff

```text
Antigravity, prepare a Codex return handoff based only on the evidence you just gathered.

The handoff must include:
- method tests run
- artifacts created
- proven capabilities
- missed capabilities
- drift causes
- repo/runtime truth gaps
- exact next safe actions

Do not recommend repo changes unless the evidence clearly supports them.
Do not collapse missing evidence into PASS.
```
