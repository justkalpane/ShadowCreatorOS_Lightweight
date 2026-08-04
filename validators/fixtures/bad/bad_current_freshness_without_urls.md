fixture_id=FX-BAD-002
fixture_type=bad
stage=script_source_research
expected_validator=validate_source_freshness_url_ledger.py
expected_result=FAIL

SOURCE_RESEARCH_LOCK
web_used=true
freshness_class=CURRENT
real_time_sources_used=true
source_ledger_present=true
source_ledger_urls_count=0
exact_url_ledger_present=false
status=PASS

CLAIM_EVIDENCE_STATUS
claim=The source research is current.
evidence=Search was mentioned, but no URL, timestamp, source title, or tool output was recorded.
evidence_scope=current_cycle
evidence_path=
command_output_or_file_reference=
status=PASS

failure_reason=CURRENT freshness cannot PASS without exact source URLs or equivalent tool evidence.
