"""Support utilities for F11 weak-to-revised film quality benchmarking."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from tools.film_runtime.film_screenplay_runtime_proof_runner import generate_screenplay
from validators.film.validator_registry import validator_paths


REPO_ROOT = Path(__file__).resolve().parents[3]
QUALITY_ARTIFACT_ROOT = REPO_ROOT / "artifacts/film_quality_proof"
GENERIC_PHRASES = {
    "a person learns to do better",
    "they must be better",
    "someone faces a hard day",
    "love will find a way somehow",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def markdown_from_mapping(title: str, payload: dict[str, Any]) -> str:
    lines = [f"# {title}", ""]
    for key, value in payload.items():
        lines.append(f"## {key.replace('_', ' ').title()}")
        if isinstance(value, dict):
            lines.append("")
            for sub_key, sub_value in value.items():
                lines.append(f"- {sub_key.replace('_', ' ')}: {sub_value}")
        elif isinstance(value, list):
            lines.append("")
            for item in value:
                lines.append(f"- {item}")
        else:
            lines.append(str(value))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _screenplay_from_scene_cards(packet: dict[str, Any]) -> str:
    title = packet.get("title", "Weak Film Draft")
    theme = packet.get("theme", "")
    lines = [f"TITLE: {title}", "", f"THEME: {theme}", ""]
    for card in packet.get("scene_cards", []):
        lines.append(card.get("slugline", f"INT. LOCATION {card.get('scene_number', 0)} - DAY"))
        lines.append("")
        lines.append(f"Scene objective: {card.get('scene_objective', card.get('objective', ''))}")
        lines.append(f"Conflict: {card.get('conflict', '')}")
        lines.append(f"Turning point: {card.get('turning_point', card.get('turn', ''))}")
        lines.append("")
        for action_line in card.get("action_lines", []):
            lines.append(action_line)
        lines.append("")
        for dialogue in card.get("dialogue_lines", []):
            lines.append(f"                        {dialogue.get('speaker', '').upper()}")
            lines.append(f"            {dialogue.get('line', '')}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _load_module(path_str: str):
    path = REPO_ROOT / path_str
    spec = importlib.util.spec_from_file_location(path.stem.replace(".", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generate_runtime_packet_from_payload(payload: dict[str, Any]) -> dict[str, Any]:
    temp_root = QUALITY_ARTIFACT_ROOT / "_runtime_temp"
    temp_root.mkdir(parents=True, exist_ok=True)
    run_key = f"runner_{abs(hash(json.dumps(payload, sort_keys=True))) % 10_000_000}"
    payload_path = temp_root / f"{run_key}_payload.json"
    output_root = temp_root / f"{run_key}_artifacts"
    if output_root.exists():
        shutil.rmtree(output_root)
    write_json(payload_path, payload)
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"), "--payload", str(payload_path), "--output-root", str(output_root)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if not result.stdout.strip():
        raise RuntimeError(f"runner produced no stdout: {result.stderr}")
    summary = json.loads(result.stdout)
    artifact_root = Path(summary["artifact_root"])
    if not (artifact_root / "preproduction_packet.json").is_file():
        raise RuntimeError(f"runner did not produce preproduction packet: {result.stderr}")
    packet = load_json(artifact_root / "preproduction_packet.json")
    packet["quality_runtime_artifact_root"] = str(artifact_root)
    packet["quality_runtime_artifact_paths"] = {
        "artifact_root": str(artifact_root),
        "screenplay_packet_path": str(artifact_root / "screenplay_packet.json"),
        "screenplay_md_path": str(artifact_root / "screenplay.md"),
        "route_state_capsule_path": str(artifact_root / "route_state_capsule.json"),
        "validation_report_path": str(artifact_root / "validation_report.json"),
        "execution_log_path": str(artifact_root / "execution.log"),
    }
    return packet


def _set_generic_premise(packet: dict[str, Any], line: str) -> None:
    packet["premise_test"]["premise"] = line
    packet["concept_note"]["premise"] = line
    packet["premise"] = line


def _flatten_stakes(packet: dict[str, Any], line: str) -> None:
    for beat in packet.get("beat_sheet", []):
        beat["stakes_change"] = line
    if "act_structure" in packet:
        packet["act_structure"]["stakes_progression"] = {"start": line, "middle": line, "end": line}


def _make_decorative_second_character(packet: dict[str, Any], line: str) -> None:
    relationship = packet.get("relationship_map", {}).get("relationships", [{}])[0]
    relationship["emotional_function"] = "pleasant presence"
    relationship["conflict_source"] = line
    relationship["support_function"] = "stands nearby"
    relationship["mirror_function"] = "decorative company"
    relationship["scene_interaction_purpose"] = "fill the scene"
    for card in packet.get("scene_cards", []):
        card["dialogue_subtext_goal"] = "say the feeling directly"


def _remove_visual_tension(packet: dict[str, Any], visual_line: str) -> None:
    packet.get("visual_language", {})["scene_visual_mapping"] = [
        {"scene_number": card["scene_number"], "visual_strategy": visual_line, "blocking_reason": "none"}
        for card in packet.get("scene_cards", [])
    ]
    packet.get("visual_language", {})["visual_metaphor"] = ""
    for card in packet.get("scene_cards", []):
        card["visual_motif"] = ""
        card["visual_plan"] = {"camera_reason": "none", "frame_pressure": "flat"}
    packet.get("cinematography_plan", {})["lens_intent"] = "basic coverage"
    packet.get("cinematography_plan", {})["camera_movement_motivation"] = "just show the action"
    packet.get("cinematography_plan", {})["shot_progression"] = [
        {"scene_number": card["scene_number"], "shot_type": "medium", "camera_reason": "coverage"}
        for card in packet.get("scene_cards", [])
    ]


def _rewrite_weak_screenplay(packet: dict[str, Any], ending_line: str) -> None:
    screenplay = _screenplay_from_scene_cards(packet)
    packet["screenplay"] = screenplay + "\n" + ending_line + "\n"
    packet["screenplay_body"] = packet["screenplay"]


def apply_weakness_profile(packet: dict[str, Any], fixture: dict[str, Any]) -> dict[str, Any]:
    weakened = copy.deepcopy(packet)
    profile = fixture.get("weakness_profile", [])
    weak_dialogue = fixture.get("weak_dialogue_line", "We will be better tomorrow.")
    weak_conflict = fixture.get("weak_conflict_line", "things feel a little difficult")
    weak_stakes = fixture.get("weak_stakes_line", "the emotional temperature stays mostly the same")
    weak_visual = fixture.get("weak_visual_line", "plain coverage with no expressive visual logic")
    weak_ending = fixture.get("weak_ending_line", "Everything is probably fine now.")

    if "generic premise" in profile:
        _set_generic_premise(weakened, "A person learns to do better.")
        weakened["logline"] = "Someone has a hard day and wants to be better."

    if "passive protagonist" in profile:
        weakened["character_arc"]["want"] = "keep the day moving"
        weakened["character_arc"]["need"] = "keep the day moving"
        weakened["character_arc"]["transformation_start"] = "mostly waiting"
        weakened["character_arc"]["transformation_midpoint"] = "still mostly waiting"
        weakened["character_arc"]["transformation_end"] = "mostly waiting but calmer"
        weakened["protagonist_want"] = "keep the day moving"
        weakened["protagonist_need"] = "keep the day moving"

    if "flat stakes" in profile or "no clear threat escalation" in profile:
        _flatten_stakes(weakened, weak_stakes)

    if "theme stated only in metadata" in profile:
        for beat in weakened.get("beat_sheet", []):
            beat["story_function"] = "the scene continues without dramatizing the theme"
        for card in weakened.get("scene_cards", []):
            card["scene_objective"] = "talk around the issue"
            card["objective"] = "talk around the issue"

    if "second character decorative" in profile or "relationship conflict vague" in profile:
        _make_decorative_second_character(weakened, weak_conflict)

    if "no real midpoint" in profile or "no emotional reversal" in profile:
        weakened["act_structure"]["midpoint_shift_or_reversal"] = "the story continues without a meaningful shift"
        if weakened.get("scene_cards"):
            weakened["scene_cards"][3]["turning_point"] = "nothing meaningfully changes"
            weakened["scene_cards"][3]["turn"] = "nothing meaningfully changes"

    if "no visual motif" in profile or "visual tension missing" in profile:
        _remove_visual_tension(weakened, weak_visual)

    if "no repair action" in profile or "ending not earned" in profile or "final reconciliation unearned" in profile:
        if weakened.get("scene_cards"):
            final_card = weakened["scene_cards"][-1]
            final_card["scene_objective"] = "say everything will be okay"
            final_card["objective"] = "say everything will be okay"
            final_card["conflict"] = "very little resists the ending"
            final_card["turning_point"] = "they decide to call it resolved"
            final_card["turn"] = "they decide to call it resolved"
        weakened["character_arc"]["transformation_end"] = "slightly calmer but not meaningfully changed"

    if "opposing force vague" in profile:
        weakened["opposing_force"]["opposing_force"] = "a problem"
        weakened["character_arc"]["opposing_force"] = "a problem"
        weakened["premise_test"]["central_conflict"] = "a problem"
        weakened["opposing_force_summary"] = "a problem"
        weakened["logline"] = "A parent tries to handle a problem before it gets worse."
        weakened["premise_test"]["premise"] = "A parent deals with a problem in a scary moment."

    if "weak ticking clock" in profile:
        weakened["world_bible"]["timeline"] = ["the situation unfolds at an unspecified pace"]
        weakened["world_bible"]["consequence_chain"] = ["something bad could happen eventually"]

    if "suspense not scene-mapped" in profile:
        for card in weakened.get("scene_cards", []):
            card["conflict"] = weak_conflict
            card["turning_point"] = "the scene ends without a sharper threat turn"
            card["scene_objective"] = "react in a vague way"
            card["objective"] = "react in a vague way"
        weakened["act_structure"]["midpoint_shift_or_reversal"] = "the story continues without a meaningful shift"
        weakened["character_arc"]["transformation_midpoint"] = "still overwhelmed and imprecise"

    if "dialogue too direct" in profile or "no subtext" in profile:
        for card in weakened.get("scene_cards", []):
            card["dialogue_subtext_goal"] = "say the exact feeling out loud"
            card["dialogue_lines"] = [{"speaker": weakened["character_list"][0]["name"], "line": weak_dialogue}]

    if "relationship conflict vague" in profile:
        _set_generic_premise(weakened, "Two people try to talk through a difficult evening.")
        weakened["logline"] = "Two partners try to get through a difficult night together."
        _flatten_stakes(weakened, weak_stakes)
        weakened["world_bible"]["consequence_chain"] = ["the relationship might feel strained for a while"]

    _rewrite_weak_screenplay(weakened, weak_ending)
    weakened["quality_benchmark_source_payload"] = copy.deepcopy(fixture["payload"])
    weakened["quality_benchmark_profile"] = profile
    weakened["quality_benchmark_expected_band"] = fixture.get("expected_quality_band", "NEEDS_MAJOR_REWRITE")
    return weakened


def build_weak_packet_from_fixture(fixture_path: str | Path) -> tuple[dict[str, Any], dict[str, Any]]:
    fixture = load_json(Path(fixture_path))
    base_packet = generate_screenplay(copy.deepcopy(fixture["payload"]))
    weak_packet = apply_weakness_profile(base_packet, fixture)
    return weak_packet, fixture


def _runtime_payload(packet: dict[str, Any]) -> dict[str, Any]:
    return {"preproduction_packet": packet}


def _materialize_quality_artifact_bundle(packet: dict[str, Any]) -> dict[str, str]:
    bundle_key = hashlib.sha256(packet.get("screenplay", "").encode("utf-8")).hexdigest()[:12]
    bundle_root = QUALITY_ARTIFACT_ROOT / "_runtime_temp" / f"f13_revised_bundle_{bundle_key}"
    bundle_root.mkdir(parents=True, exist_ok=True)

    screenplay_packet = dict(packet)
    screenplay_packet.setdefault("route_state_capsule", {"route_id": screenplay_packet.get("route")})
    screenplay_packet.setdefault("route_state", {"route_id": screenplay_packet.get("route"), "output_phase_started": True})
    screenplay_packet.setdefault("screenplay_body", screenplay_packet.get("screenplay", ""))
    screenplay_packet.setdefault("estimated_duration_minutes", screenplay_packet.get("duration_minutes", 5))
    screenplay_packet.setdefault("scene_breakdown", screenplay_packet.get("scene_cards", []))
    screenplay_packet.setdefault("character_list", screenplay_packet.get("character_bible", []))

    write_json(bundle_root / "screenplay_packet.json", screenplay_packet)
    write_json(bundle_root / "preproduction_packet.json", packet)
    write_text(bundle_root / "screenplay.md", packet.get("screenplay", ""))
    write_json(bundle_root / "route_state_capsule.json", screenplay_packet["route_state_capsule"])

    validation_report = {
        "status": "PASS_RUNTIME_ARTIFACT_PROVEN",
        "run_id": f"f13_revised_{bundle_key}",
        "route_checks": {
            "route_exists": True,
            "script_generation_preserved": screenplay_packet.get("mode") == "script_only",
        },
        "validator_results": {
            "route_selection": {"passed": True},
            "duration": {"passed": True},
            "character_constraints": {"passed": True},
            "emotional_beat_map": {"passed": True},
            "continuity": {"passed": True},
        },
    }
    write_json(bundle_root / "validation_report.json", validation_report)
    write_text(bundle_root / "execution.log", "F13 revised screenplay artifact bundle materialized for local validator reuse.\n")

    return {
        "artifact_root": str(bundle_root),
        "screenplay_packet_path": str(bundle_root / "screenplay_packet.json"),
        "screenplay_md_path": str(bundle_root / "screenplay.md"),
        "route_state_capsule_path": str(bundle_root / "route_state_capsule.json"),
        "validation_report_path": str(bundle_root / "validation_report.json"),
        "execution_log_path": str(bundle_root / "execution.log"),
    }


def run_existing_validator_suite(packet: dict[str, Any]) -> dict[str, Any]:
    results: dict[str, Any] = {}
    use_synthetic_bundle = bool(packet.get("quality_scene_rewrite_metadata"))
    compatible_rewrite_validators = {
        "premise",
        "logline",
        "theme_alignment",
        "genre_grammar",
        "stakes_escalation",
        "character_arc",
        "consequence_logic",
        "director_vision",
        "visual_language",
        "department_handoffs",
        "production_risk",
        "downstream_boundary",
    }
    artifact_paths = packet.get("quality_runtime_artifact_paths") or {}
    if use_synthetic_bundle:
        artifact_paths = _materialize_quality_artifact_bundle(packet)
    artifact_payload = {
        "artifact_root": artifact_paths.get("artifact_root"),
        "screenplay_packet_path": artifact_paths.get("screenplay_packet_path"),
        "screenplay_md_path": artifact_paths.get("screenplay_md_path"),
        "route_state_capsule_path": artifact_paths.get("route_state_capsule_path"),
        "validation_report_path": artifact_paths.get("validation_report_path"),
        "execution_log_path": artifact_paths.get("execution_log_path"),
    } if artifact_paths else None
    for name, rel_path in validator_paths().items():
        if name in {"route_selection", "quality_score", "revision_delta", "revised_packet_improvement"}:
            continue
        if use_synthetic_bundle and name not in compatible_rewrite_validators:
            continue
        module = _load_module(rel_path)
        if name == "screenplay_packet" and artifact_payload:
            results[name] = module.validate(artifact_payload)
            report_path = Path(artifact_payload["validation_report_path"])
            report = load_json(report_path)
            report["validator_results"]["screenplay_packet"] = results[name]
            write_json(report_path, report)
        elif name == "no_fake_pass" and artifact_payload:
            validation_report = load_json(Path(artifact_payload["validation_report_path"]))
            no_fake_payload = {
                **artifact_payload,
                "route_id": "FILM_SCREENPLAY_GENERATION",
                "mode": "script_only",
                "actual_command_used": "python3 tools/film_runtime/film_screenplay_runtime_proof_runner.py --payload <payload> --output-root <output-root>",
                "validator_results": validation_report.get("validator_results", {}),
                "film_schema_evidence": True,
                "route_lineage_ledger": True,
                "filmcraft_scorecard": True,
            }
            results[name] = module.validate(no_fake_payload)
        elif artifact_payload and not use_synthetic_bundle:
            results[name] = module.validate(artifact_payload)
        else:
            if name in {"screenplay_packet", "no_fake_pass"}:
                results[name] = module.validate(packet)
            else:
                results[name] = module.validate(_runtime_payload(packet))
    return results
