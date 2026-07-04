fixture_id=FX-GOLD-001
fixture_type=gold
stage=script_generation
reconstruction_status=RECONSTRUCTED_GOLD_SPEC
expected_validator=validate_route_claim_evidence_consistency.py
expected_result=PASS

SHADOW_BOOT_CONFIRMATION
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment

TASK_ROUTE_LOCK
route_id=SCRIPT_GENERATION
route_manifest_path=registries/route_manifests/script_generation.yaml
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
file_counts_are_telemetry_only=true

SOURCE_RESEARCH_LOCK
web_used=true
freshness_class=CURRENT
source_ledger_urls_count=2
status=PASS

SOURCE_LEDGER
source_1_url=https://en.wikipedia.org/wiki/Yash_(actor)
source_1_use=biographical cross-check only
source_2_url=https://www.hindustantimes.com/entertainment/others/yash-from-bus-driver-son-to-pan-india-star-kgf-journey-101652435743215.html
source_2_use=career-journey cross-check only

SOURCE_LIMITATION_NOTES
Do not present unsupported claims such as all early income being invested as verified fact.

FACT_VS_ANECDOTE_MAP
fact=Yash is the screen name of Naveen Kumar Gowda.
fact=Yash is associated with Kannada cinema and KGF fame.
anecdote_or_claim_needs_care=Exact details of early cash use require source caution.
mythological_parallel=Ekalavya-style self-training metaphor is a narrative choice.

CINEMATIC_SHORT_STORY_BLOCK
duration_target_seconds=60
character=Young Naveen/Yash as a struggling performer.
setting=Bengaluru theater and early screen-work environment.
conflict=No industry shortcut and pressure to choose stability.
turning_point=Backstage learning becomes self-investment.
lesson_bridge=Attention, money, and time are treated as personal capital.

FINAL_SCRIPT
language=English
runtime_seconds=300
opening_hook_present=true
internal_rehooks_count=4
cta_hook_present=true

DYNAMIC_TIMED_BEAT_MAP
beat_rows_detected=13
timings_dynamic=true
max_gap_without_rehook_seconds=70

CONTENT_CONTEXTS
voice_generation_context_present=true
image_generation_context_present=true
video_generation_context_present=true
music_and_sfx_context_present=true
local_cloud_hybrid_execution_plan_present=true

SEMANTIC_INFLUENCE_MAP
component_or_file=registries/route_manifests/script_generation.yaml
rule_or_contract_used=SCRIPT_GENERATION route requirements
output_section=FINAL_SCRIPT
output_line_or_block=script structure and timed beat map
influence_type=route_scope
validator_check=route_claim_evidence_consistency
status=USED

VALIDATION_SCORECARD
quality_lock=PASS
source_research_lock=PASS
provider_honesty_gate=PASS
final_proof_classification=PASS

CLAIM_EVIDENCE_STATUS
claim=Gold reconstructed script output satisfies route locks and source honesty.
evidence=Fixture includes route lock, exact source URLs, semantic influence, final script markers, and validation scorecard.
evidence_scope=current_cycle
evidence_path=validators/fixtures/gold/gold_script_reconstructed.md
command_output_or_file_reference=fixture reconstruction from audit blueprint
status=PASS
