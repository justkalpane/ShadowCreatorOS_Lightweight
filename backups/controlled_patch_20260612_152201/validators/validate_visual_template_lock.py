#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = [
    "Route Verification & System Locks",
    "Assumption Verification Table",
    "Asset Generation Order",
    "Scene-by-scene Multi-Arc Table",
    "Reasoning",
    "Media Method Distribution",
    "B-roll Ratio Breakdown",
    "Provider Honesty Gate",
    "Local/Cloud/Hybrid Boundary",
    "DaVinci/FFmpeg Assembly Plan",
    "QC/Proof Registry",
    "Final Classification",
]


def validate(text: str) -> bool:
    return all(section in text for section in REQUIRED) and "Reasoning |" in text and "status=PACKET_READY" in text


def validate_paths(paths: list[Path]) -> int:
    ok = True
    for path in paths:
        text = path.read_text()
        missing = [section for section in REQUIRED if section not in text]
        passed = validate(text)
        print("VISUAL_TEMPLATE_LOCK_RESULT")
        print(f"fixture={path}")
        print(f"result={'PASS' if passed else 'FAIL'}")
        print(f"missing_sections={','.join(missing) if missing else 'none'}")
        print(f"reasoning_column_present={'Reasoning |' in text}")
        print(f"packet_ready_status_present={'status=PACKET_READY' in text}")
        ok = ok and passed
    print("VISUAL_TEMPLATE_LOCK_SUMMARY")
    print(f"files_checked={len(paths)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def self_test() -> int:
    good = Path("validators/fixtures/gold/visual_media_generation_draft_good_13_1_percent.md").read_text()
    bad_flat = Path("validators/fixtures/bad/visual_media_generation_draft_bad_flat_template.md").read_text()
    bad_reasoning = Path("validators/fixtures/bad/visual_media_generation_draft_bad_missing_reasoning.md").read_text()
    print(f"good_fixture: {'PASS' if validate(good) else 'FAIL'}")
    print(f"bad_flat_fixture: {'FAIL' if not validate(bad_flat) else 'PASS'}")
    print(f"bad_reasoning_fixture: {'FAIL' if not validate(bad_reasoning) else 'PASS'}")
    return 0 if validate(good) and not validate(bad_flat) and not validate(bad_reasoning) else 1


def main(argv: list[str]) -> int:
    if argv:
        return validate_paths([Path(arg) for arg in argv])
    return self_test()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
