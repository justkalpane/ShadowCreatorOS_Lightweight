fixture_id=FX-BAD-003
fixture_type=bad
stage=script_source_research
expected_validator=validate_source_freshness_url_ledger.py
expected_result=FAIL

SOURCE_RESEARCH_LOCK
web_used=true
freshness_class=CURRENT
source_list_present=true
source_list_format=labels_only
source_ledger_urls_count=0
command_output_or_file_reference=
status=PASS

SOURCE_LIST
- Wikipedia - Yash
- Hindustan Times - Yash Interview

failure_reason=web_used=true is asserted, but the fixture provides source labels only and no exact URL or command output proof.
