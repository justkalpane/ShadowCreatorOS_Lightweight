#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
import re

REQUIRED = [
    "Route Verification & System Locks",
    "Assumption Verification Table",
    "Asset Generation Order",
    "Scene-by-scene Transposed Scene Blocks",
    "Reasoning",
    "Media Method Distribution",
    "B-roll Ratio Breakdown",
    "Provider Honesty Gate",
    "Local/Cloud/Hybrid Boundary",
    "DaVinci/FFmpeg Assembly Plan",
    "QC/Proof Registry",
    "Final Classification",
]

REQUIRED_LAYER_PATTERNS = [
    r"\|\s*Visual\s*\|",
    r"\|\s*Motion\s*\|",
    r"\|\s*Audio/SFX\s*\|",
    r"\|\s*Editing\s*\|",
    r"\|\s*Provider/Local Boundary\s*\|",
    r"\|\s*Proof/QC\s*\|",
    r"\|\s*Reasoning\s*\|",
]

SCENE_HEADING_RE = re.compile(r"^###\s+SC-\d{2}\b", re.MULTILINE)


def scene_blocks(text: str) -> list[str]:
    matches = list(SCENE_HEADING_RE.finditer(text))
    blocks: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append(text[start:end])
    return blocks


def validate_scene_block(block: str) -> list[str]:
    errors: list[str] = []
    required_literals = [
        "scene_id=",
        "timecode=",
        "duration_seconds=",
        "method=",
        "> Script:",
        "| Layer | Detail |",
    ]
    for literal in required_literals:
        if literal not in block:
            errors.append(f"scene_block_missing:{literal}")
    for pattern in REQUIRED_LAYER_PATTERNS:
        if not re.search(pattern, block, flags=re.IGNORECASE):
            errors.append(f"scene_block_missing_layer:{pattern}")
    return errors


def validation_errors(text: str) -> list[str]:
    errors: list[str] = []
    for section in REQUIRED:
        if section not in text:
            errors.append(f"missing_section:{section}")

    blocks = scene_blocks(text)
    if not blocks:
        errors.append("transposed_scene_blocks_missing")
    for index, block in enumerate(blocks, start=1):
        for error in validate_scene_block(block):
            errors.append(f"SCENE_{index}:{error}")

    if "status=PACKET_READY" not in text:
        errors.append("status_PACKET_READY_missing")

    if "B-roll Ratio Breakdown" in text and "cinematic_broll_seconds" not in text:
        errors.append("broll_ratio_math_missing")

    return errors


def validate(text: str) -> bool:
    return not validation_errors(text)


def validate_paths(paths: list[Path]) -> int:
    ok = True
    for path in paths:
        text = path.read_text()
        errors = validation_errors(text)
        missing = [error.removeprefix("missing_section:") for error in errors if error.startswith("missing_section:")]
        blocks = scene_blocks(text)
        passed = not errors
        print("VISUAL_TEMPLATE_LOCK_RESULT")
        print(f"fixture={path}")
        print(f"result={'PASS' if passed else 'FAIL'}")
        print(f"missing_sections={','.join(missing) if missing else 'none'}")
        print(f"transposed_scene_blocks={len(blocks)}")
        print(f"layer_detail_table_present={'| Layer | Detail |' in text}")
        print(f"reasoning_layer_present={bool(re.search(r'\\|\\s*Reasoning\\s*\\|', text, flags=re.IGNORECASE))}")
        print(f"packet_ready_status_present={'status=PACKET_READY' in text}")
        print(f"errors={len(errors)}")
        for error in errors:
            print(f"- {error}")
        ok = ok and passed
    print("VISUAL_TEMPLATE_LOCK_SUMMARY")
    print(f"files_checked={len(paths)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def self_test() -> int:
    good = Path("validators/fixtures/gold/gold_visual_transposed_scene_blocks.md").read_text()
    bad_flat = Path("validators/fixtures/bad/visual_media_generation_draft_bad_flat_template.md").read_text()
    bad_reasoning = Path("validators/fixtures/bad/visual_media_generation_draft_bad_missing_reasoning.md").read_text()
    bad_horizontal = Path("validators/fixtures/bad/bad_visual_horizontal_table_only.md").read_text()
    bad_layers = Path("validators/fixtures/bad/bad_visual_missing_transposed_layers.md").read_text()
    print(f"good_fixture: {'PASS' if validate(good) else 'FAIL'}")
    print(f"bad_flat_fixture: {'FAIL' if not validate(bad_flat) else 'PASS'}")
    print(f"bad_reasoning_fixture: {'FAIL' if not validate(bad_reasoning) else 'PASS'}")
    print(f"bad_horizontal_fixture: {'FAIL' if not validate(bad_horizontal) else 'PASS'}")
    print(f"bad_missing_layers_fixture: {'FAIL' if not validate(bad_layers) else 'PASS'}")
    return 0 if (
        validate(good)
        and not validate(bad_flat)
        and not validate(bad_reasoning)
        and not validate(bad_horizontal)
        and not validate(bad_layers)
    ) else 1


def main(argv: list[str]) -> int:
    if argv:
        return validate_paths([Path(arg) for arg in argv])
    return self_test()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
