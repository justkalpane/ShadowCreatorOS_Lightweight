fixture_id=FX-BAD-005
fixture_type=bad
stage=visual_media_generation_draft
expected_validator=validate_broll_ratio.py
expected_result=FAIL

BROLL_RATIO_BREAKDOWN
total_runtime_seconds=305
cinematic_broll_seconds=16
required_cinematic_broll_seconds=37
broll_ratio_percent=5.2
minimum_required_percent=12.0
status=PASS

failure_reason=Cinematic B-roll is below ceil(total_runtime_seconds * 0.12).
