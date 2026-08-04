#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

GOOD_SCRIPT = [
    "AGENTS.md",
    "START_HERE_FOR_AGENTS.md",
    "SHADOW_BOOT_CONFIRMATION",
    "AGENT_READ_ORDER.md",
    "AGENT_REPO_FIRST_OPERATING_DOCTRINE.md",
    "AGENT_ANTI_DRIFT_RULES.md",
    "ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md",
    "task_intent_routing_matrix.yaml",
    "SHADOW_TASK_EXECUTION_WRAPPER.md",
    "script_generation.yaml",
    "TASK_INTENT_ROUTING_CONTRACT.md",
    "ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md",
    "TASK_EXECUTION_STATE_MACHINE_CONTRACT.md",
    "DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md",
    "CONTENT_ENGINEERING_OUTPUT_CONTRACT.md",
    "SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md",
    "SCRIPT_STORY_ENGINE_CONTRACT.md",
]

GOOD_VISUAL = [
    "locked_final_script",
    "visual_media_plan_route_or_mode",
    "planning_only_depth",
    "Media Factory final draft contract",
    "scene_sync_matrix",
    "visual_method_taxonomy",
    "A-roll/B-roll/motion_graphic_summary",
    "cost_distribution",
    "provider_honesty_gate",
    "no_asset_execution_claim",
]

GOOD_DRAFT = [
    "locked_final_script",
    "locked_visual_media_plan",
    "MEDIA_FACTORY_HANDOFF",
    "media_factory_handoff_route_manifest",
    "script_integrity_lock",
    "visual_plan_integrity_lock",
    "DEEP_REQUIRED_depth",
    "scene_prompt_packets",
    "storyboard_export_plan",
    "local_media_bridge_status",
    "provider_honesty_gate",
    "asset_generation_order",
    "reasoning_column",
    "B-roll_ratio",
    "DaVinci/FFmpeg_assembly_plan",
    "QC/proof_registry",
]


def load_steps(path: Path) -> list[str]:
    steps: list[str] = []
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if line.startswith("- "):
            steps.append(line[2:].strip())
    return steps


def check_order(steps: list[str], required: list[str]) -> bool:
    pos = -1
    for item in required:
        try:
            next_pos = steps.index(item, pos + 1)
        except ValueError:
            return False
        if next_pos < pos:
            return False
        pos = next_pos
    return True


def expected_order_for(path: Path, steps: list[str]) -> tuple[str, list[str]]:
    name = path.name.lower()
    joined = "\n".join(steps)
    if "visual_media_generation_draft" in name or "MEDIA_FACTORY_HANDOFF" in joined:
        return "visual_media_generation_draft", GOOD_DRAFT
    if "visual_media_plan" in name or "visual_media_plan_route_or_mode" in joined:
        return "visual_media_plan", GOOD_VISUAL
    return "script_generation", GOOD_SCRIPT


def validate_paths(paths: list[Path]) -> int:
    ok = True
    for path in paths:
        steps = load_steps(path)
        route_name, expected_order = expected_order_for(path, steps)
        passed = check_order(steps, expected_order)
        missing = [item for item in expected_order if item not in steps]
        print("ROUTE_CONSUMPTION_ORDER_RESULT")
        print(f"fixture={path}")
        print(f"route_family={route_name}")
        print(f"result={'PASS' if passed else 'FAIL'}")
        print(f"steps_detected={len(steps)}")
        print(f"missing_required_steps={','.join(missing) if missing else 'none'}")
        ok = ok and passed
    print("ROUTE_CONSUMPTION_ORDER_SUMMARY")
    print(f"files_checked={len(paths)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def self_test() -> int:
    base = Path("validators/fixtures")
    cases = [
        ("good_script", base / "gold/script_generation_consumption_order.yaml", GOOD_SCRIPT, True),
        ("good_visual", base / "gold/visual_media_plan_consumption_order.yaml", GOOD_VISUAL, True),
        ("good_draft", base / "gold/visual_media_generation_draft_consumption_order.yaml", GOOD_DRAFT, True),
        ("bad_script", base / "bad/bad_consumption_order.yaml", GOOD_SCRIPT, False),
    ]
    ok = True
    for name, path, expected_order, should_pass in cases:
        steps = load_steps(path)
        passed = check_order(steps, expected_order)
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
        if passed != should_pass:
            ok = False
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if argv:
        return validate_paths([Path(arg) for arg in argv])
    return self_test()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
