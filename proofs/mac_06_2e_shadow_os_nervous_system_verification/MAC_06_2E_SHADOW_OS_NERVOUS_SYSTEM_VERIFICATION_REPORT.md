# MAC-06.2E Shadow OS Nervous System Verification Report

generated_at=2026-05-25T16:02:17
repo_root=/Users/apple/Documents/ShadowCreatorOS_Lightweight
branch=main
head=9f64ae34be6d7b5dfd6df13b1ebdaec81cc5ef24

MAC_06_2E_SHADOW_OS_NERVOUS_SYSTEM_VERIFICATION_STATUS=FAIL

## Direct Answers

1. Is MAC-06.2D trustworthy? PARTIAL. It repaired contract metadata and removed active UNKNOWN/template-only markers, but it does not by itself prove executable runtime behavior.
2. Are 740 components truly production-depth? No. They are route-profile enriched. Native executable depth remains uneven; many are FAKE_DEPTH if treated as callable production capability.
3. Are all veins/bindings real? No. Communication veins are mostly CONTRACT_ONLY because no local graph runner executes packet handoffs.
4. Are script quality capabilities deep enough? PARTIAL. Packets/validators exist, but no executable script-quality runner enforces them.
5. Are media context capabilities deep enough? PARTIAL. Planning contracts exist; execution remains disabled and no packet instance generator exists.
6. Are route manifests executable enough? No. They are YAML contract maps, not an enforced DAG/runtime.
7. Are validators strong enough? No. They are useful transcript gates but mostly text-label checks, not JSON/schema/graph validators.
8. Are support files missing? Yes: schemas, CLI wrapper, graph runner, packet validator, non-Codex harness.
9. Should MAC-06.2D be committed? Only as contract/profile remediation, not as proof of production runtime.
10. Should non-Codex operator proof run next? Only after or alongside local validator/wrapper enforcement.
11. Should a local CLI/wrapper/validator be built first? Yes. This is the main blocker.
12. Exact next remediation phases: MAC-06.2F JSON Schema + Route DAG, MAC-06.2G Local CLI Wrapper, MAC-06.2H Non-Codex Operator Harness, MAC-06.2I Active Component Certification.

## Counts

directors_checked=34
production_directors=0
partial_directors=0
fake_depth_directors=34

agents_checked=121
production_agents=0
partial_agents=0
fake_depth_agents=121

subagents_checked=37
production_subagents=0
partial_subagents=0
fake_depth_subagents=37

skills_checked=547
production_skills=0
partial_skills=0
fake_depth_skills=547

subskills_checked=1
production_subskills=0
partial_subskills=0
fake_depth_subskills=1

veins_checked=20
veins_connected=0
veins_partial=1
veins_contract_only=19
veins_broken=0
veins_missing=0

support_files_checked=24
support_files_present=0
support_files_missing=24
blocker_support_files_missing=16
high_risk_support_files_missing=8

validator_rules_checked=24
validator_text_only_rules=24
real_structure_rules=0

## Decision

safe_to_commit_mac06_2d=false
safe_to_run_non_codex_operator_proof_after_commit=false
safe_to_build_local_cli_wrapper=true
safe_to_start_n8n=false
safe_to_declare_lightweight_os_onboarded=false


## Media Context Correction

media_capabilities_checked=24
media_capabilities_connected=24
media_capabilities_partial=0
media_capabilities_missing=0
media_context_status=PARTIAL because contracts/routes/validator labels exist but no executable media planner or packet instance generator exists.
