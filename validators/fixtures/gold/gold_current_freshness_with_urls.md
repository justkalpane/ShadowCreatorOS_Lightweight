fixture_id=FX-GOLD-005
fixture_type=gold
stage=script_source_research
expected_validator=validate_source_freshness_url_ledger.py
expected_result=PASS

SOURCE_RESEARCH_LOCK
web_used=true
freshness_class=CURRENT
real_time_sources_used=true
source_ledger_present=true
source_ledger_urls_count=3
exact_url_ledger_present=true
status=PASS

SOURCE_LEDGER
source_1_url=https://en.wikipedia.org/wiki/Yash_(actor)
source_1_title=Yash actor profile
source_1_freshness_scope=biographical_reference
source_2_url=https://www.hindustantimes.com/entertainment/others/yash-from-bus-driver-son-to-pan-india-star-kgf-journey-101652435743215.html
source_2_title=Yash career journey reference
source_2_freshness_scope=biographical_reference
source_3_url=https://www.imdb.com/name/nm5232139/
source_3_title=Yash filmography reference
source_3_freshness_scope=profile_reference

CLAIM_EVIDENCE_STATUS
claim=CURRENT/web-assisted source use is supported by exact URLs.
evidence=The fixture contains exact URLs and source purposes.
evidence_scope=current_cycle
evidence_path=validators/fixtures/gold/gold_current_freshness_with_urls.md
command_output_or_file_reference=fixture
status=PASS
