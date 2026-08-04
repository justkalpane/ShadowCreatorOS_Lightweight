"""Shared helpers for local film runtime artifact validation."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]


def _resolve_path(value: str | Path, repo_root: Path | None = None) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (repo_root or REPO_ROOT) / path


def load_json_value(value: Any, repo_root: Path | None = None) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if isinstance(value, (str, Path)):
        path = _resolve_path(value, repo_root=repo_root)
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def load_text_value(value: Any, repo_root: Path | None = None) -> str:
    if isinstance(value, str) and value and "\n" in value:
        return value
    if isinstance(value, (str, Path)):
        path = _resolve_path(value, repo_root=repo_root)
        if path.is_file():
            return path.read_text(encoding="utf-8")
    return ""


def artifact_bundle(payload: dict[str, Any], repo_root: Path | None = None) -> dict[str, Any]:
    bundle: dict[str, Any] = dict(payload)
    if "artifact_root" in payload:
        root = _resolve_path(payload["artifact_root"], repo_root=repo_root)
        bundle.setdefault("screenplay_packet_path", root / "screenplay_packet.json")
        bundle.setdefault("screenplay_md_path", root / "screenplay.md")
        bundle.setdefault("route_state_capsule_path", root / "route_state_capsule.json")
        bundle.setdefault("validation_report_path", root / "validation_report.json")
        bundle.setdefault("execution_log_path", root / "execution.log")
    return bundle


def load_screenplay_packet(payload: dict[str, Any], repo_root: Path | None = None) -> dict[str, Any]:
    if "screenplay_packet" in payload and isinstance(payload["screenplay_packet"], dict):
        return payload["screenplay_packet"]
    if "screenplay_packet_path" in payload:
        return load_json_value(payload["screenplay_packet_path"], repo_root=repo_root)
    if "artifact_root" in payload:
        root = _resolve_path(payload["artifact_root"], repo_root=repo_root)
        return json.loads((root / "screenplay_packet.json").read_text(encoding="utf-8"))
    return payload


def load_route_state(payload: dict[str, Any], repo_root: Path | None = None) -> dict[str, Any]:
    if "route_state" in payload and isinstance(payload["route_state"], dict):
        return payload["route_state"]
    if "route_state_capsule_path" in payload:
        return load_json_value(payload["route_state_capsule_path"], repo_root=repo_root)
    if "artifact_root" in payload:
        root = _resolve_path(payload["artifact_root"], repo_root=repo_root)
        return json.loads((root / "route_state_capsule.json").read_text(encoding="utf-8"))
    return {}


def load_validation_report(payload: dict[str, Any], repo_root: Path | None = None) -> dict[str, Any]:
    if "validation_report" in payload and isinstance(payload["validation_report"], dict):
        return payload["validation_report"]
    if "validation_report_path" in payload:
        return load_json_value(payload["validation_report_path"], repo_root=repo_root)
    if "artifact_root" in payload:
        root = _resolve_path(payload["artifact_root"], repo_root=repo_root)
        return json.loads((root / "validation_report.json").read_text(encoding="utf-8"))
    return {}


def screenplay_text(packet: dict[str, Any], payload: dict[str, Any] | None = None, repo_root: Path | None = None) -> str:
    payload = payload or {}
    if "screenplay" in packet and isinstance(packet["screenplay"], str):
        return packet["screenplay"]
    if "screenplay_body" in packet and isinstance(packet["screenplay_body"], str):
        return packet["screenplay_body"]
    if "screenplay_md_path" in payload:
        return load_text_value(payload["screenplay_md_path"], repo_root=repo_root)
    if "artifact_root" in payload:
        root = _resolve_path(payload["artifact_root"], repo_root=repo_root)
        return (root / "screenplay.md").read_text(encoding="utf-8")
    return ""


def scene_heading_count(screenplay: str) -> int:
    matches = re.findall(r"(?m)^(?:INT|EXT|INT/EXT)\.[^\n]*$", screenplay.strip())
    return len(matches)


def named_characters(packet: dict[str, Any]) -> list[str]:
    characters = packet.get("character_list") or []
    names: list[str] = []
    if isinstance(characters, list):
        for item in characters:
            if isinstance(item, str):
                names.append(item)
            elif isinstance(item, dict):
                for key in ("name", "character_name", "label", "role"):
                    value = item.get(key)
                    if isinstance(value, str) and value:
                        names.append(value)
                        break
    return names


def contains_any(text: str, terms: list[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def has_required_artifacts(payload: dict[str, Any]) -> list[str]:
    required = [
        "screenplay_packet_path",
        "screenplay_md_path",
        "route_state_capsule_path",
        "validation_report_path",
        "execution_log_path",
    ]
    missing: list[str] = []
    for key in required:
        raw = payload.get(key)
        if not raw:
            missing.append(key)
            continue
        path = _resolve_path(raw)
        if not path.is_file():
            missing.append(key)
    return missing

