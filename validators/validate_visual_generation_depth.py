#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from lib.route_slice_truth import resolve_route_slice_claim


BAD_SFX_FIXTURE = Path("validators/fixtures/bad/bad_visual_sfx_generic_prose.md")
BAD_DAVINCI_FIXTURE = Path("validators/fixtures/bad/bad_davinci_generic_prose.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_visual_draft_reconstructed.md")

TIMECODE_RE = re.compile(r"\b\d{1,2}:\d{2}(?:-\d{1,2}:\d{2})?\b")
TRACK_RE = re.compile(r"\b[VA]\d\b")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    timecode_count: int
    track_token_count: int


def parse_kv(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() in {"true", "yes", "1", "pass"}


def is_false(value: str | None) -> bool:
    return (value or "").strip().lower() in {"false", "no", "0", "fail"}


def int_value(value: str | None) -> int:
    if value is None or value == "":
        return 0
    try:
        return int(value)
    except ValueError:
        return 0


def pass_or_ready_claimed(data: dict[str, str]) -> bool:
    return (
        data.get("status", "").upper() == "PASS"
        or data.get("final_status", "").upper() == "PASS"
        or data.get("DaVinci_Resolve", "").upper() == "PACKET_READY"
        or data.get("FFmpeg", "").upper() == "PACKET_READY"
    )


def has_any(text: str, options: list[str]) -> bool:
    lower = text.lower()
    return any(option.lower() in lower for option in options)


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    data = parse_kv(text)
    errors: list[str] = []
    warnings: list[str] = []
    timecodes = TIMECODE_RE.findall(text)
    tracks = TRACK_RE.findall(text)
    claimed_ready = pass_or_ready_claimed(data)
    route_resolution = resolve_route_slice_claim(
        route_id=data.get("route_id") or data.get("canonical_route_id"),
        task_mode=data.get("task_mode") or data.get("route_mode") or data.get("output_classification"),
        route_manifest_path=data.get("route_manifest_path"),
        route_slice_path=data.get("selected_route_slice_path") or data.get("route_slice_path"),
    )

    if not claimed_ready:
        warnings.append("no_PASS_or_PACKET_READY_visual_claim_detected")
        return ValidationResult(path, True, errors, warnings, len(timecodes), len(tracks))

    if (data.get("selected_route_slice_path") or data.get("route_slice_path")) and not route_resolution["slice_exists"]:
        errors.append("visual_ready_claim_route_slice_missing")

    if not route_resolution["source_manifest_matches"]:
        errors.append("visual_ready_claim_route_slice_source_manifest_mismatch")

    if not route_resolution["task_mode_matches"]:
        errors.append("visual_ready_claim_route_slice_task_mode_mismatch")

    has_scene_table = "Scene-by-scene Multi-Arc Table" in text or "| scene_id |" in text
    has_reasoning = "Reasoning" in text or "reasoning" in text
    has_sfx_structure = "SFX timestamp" in text or is_true(data.get("sfx_timestamp_map_present"))
    has_davinci_structure = "DaVinci/FFmpeg Assembly Plan" in text or bool(data.get("track_map"))
    has_marker_structure = bool(data.get("marker_rows")) or int_value(data.get("marker_rows_detected")) > 0
    has_asset_order_or_graph = "Asset Generation Order" in text or is_true(data.get("asset_dependency_graph_present"))
    has_ffmpeg_structure = is_true(data.get("ffmpeg_command_plan_present")) or bool(data.get("ffmpeg_command_script_path"))

    if not has_scene_table:
        errors.append("scene_level_multi_arc_table_missing")

    if not has_reasoning:
        errors.append("scene_level_reasoning_missing")

    if not has_sfx_structure:
        errors.append("sfx_timestamp_map_missing")

    if int_value(data.get("exact_sfx_cues_count")) == 0 and "SFX_PLAN" in text:
        errors.append("exact_sfx_cues_count_zero")

    if data.get("sfx_clip_count", "").lower() == "generic":
        errors.append("sfx_clip_count_generic")

    if has_any(text, ["throughout the video", "edit nicely", "add music, color grade"]) and not has_scene_table:
        errors.append("generic_visual_prose_without_scene_structure")

    if not has_davinci_structure:
        errors.append("davinci_ffmpeg_assembly_plan_missing")

    if is_false(data.get("davinci_track_map_present")):
        errors.append("davinci_track_map_present_false")

    if not has_marker_structure:
        errors.append("davinci_marker_rows_missing")

    if len(tracks) < 3 and not bool(data.get("track_map")):
        errors.append("davinci_track_tokens_insufficient")

    if is_false(data.get("asset_dependency_graph_present")):
        errors.append("asset_dependency_graph_present_false")

    if not has_asset_order_or_graph:
        errors.append("asset_generation_order_or_dependency_graph_missing")

    if data.get("FFmpeg", "").upper() == "PACKET_READY" and not has_ffmpeg_structure:
        errors.append("FFmpeg_PACKET_READY_without_command_plan")

    required_contracts = set(route_resolution.get("output_contracts", []))
    if "MISSION_MEDIA_OUTPUT_BUNDLE" in required_contracts and "MISSION_MEDIA_OUTPUT_BUNDLE" not in text:
        errors.append("route_slice_required_output_contract_missing:MISSION_MEDIA_OUTPUT_BUNDLE")
    if "SCENE_BREAKOUT_BLOCKS" in required_contracts and "SCENE_BREAKOUT_BLOCKS" not in text:
        errors.append("route_slice_required_output_contract_missing:SCENE_BREAKOUT_BLOCKS")
    if "DAVINCI_TIMELINE_PACKET" in required_contracts and not has_davinci_structure:
        errors.append("route_slice_required_output_contract_missing:DAVINCI_TIMELINE_PACKET")

    if is_false(data.get("ffmpeg_command_plan_present")):
        errors.append("ffmpeg_command_plan_present_false")

    if data.get("DaVinci_Resolve", "").upper() == "PACKET_READY" and errors:
        errors.append("DaVinci_PACKET_READY_with_visual_depth_errors")

    if data.get("FFmpeg", "").upper() == "PACKET_READY" and errors:
        errors.append("FFmpeg_PACKET_READY_with_visual_depth_errors")

    return ValidationResult(path, not errors, errors, warnings, len(timecodes), len(tracks))


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"timecode_count={result.timecode_count}")
    print(f"track_token_count={result.track_token_count}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")
    if result.warnings:
        print(f"warnings={len(result.warnings)}")
        for warning in result.warnings:
            print(f"- {warning}")


def run_self_test() -> int:
    bad_sfx = validate(BAD_SFX_FIXTURE)
    bad_davinci = validate(BAD_DAVINCI_FIXTURE)
    gold = validate(GOLD_FIXTURE)
    ok = (not bad_sfx.passed) and (not bad_davinci.passed) and gold.passed

    print("VISUAL_GENERATION_DEPTH_SELF_TEST")
    print(f"bad_sfx_fixture: {'FAIL' if not bad_sfx.passed else 'PASS'}")
    if bad_sfx.passed:
        print_result(bad_sfx)
    print(f"bad_davinci_fixture: {'FAIL' if not bad_davinci.passed else 'PASS'}")
    if bad_davinci.passed:
        print_result(bad_davinci)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    print("VISUAL_GENERATION_DEPTH_SUMMARY")
    print("bad_sfx_expected=FAIL")
    print("bad_davinci_expected=FAIL")
    print("gold_expected=PASS")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return run_self_test()

    ok = True
    for arg in argv:
        result = validate(Path(arg))
        print("VISUAL_GENERATION_DEPTH_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("VISUAL_GENERATION_DEPTH_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
