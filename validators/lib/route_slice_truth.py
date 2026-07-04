#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from lib.claim_normalizer import normalize_task_mode


REPO_ROOT = Path(__file__).resolve().parents[2]


def _clean(value: object) -> str:
    return str(value or "").strip().strip("`").strip()


def _upper(value: object) -> str:
    return _clean(value).upper()


def parse_yaml_scalar_any_indent(text: str, key: str) -> str | None:
    match = re.search(rf"(?im)^\s*{re.escape(key)}:\s*(.+?)\s*$", text)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith("[") and value.endswith("]"):
        return value
    return value.strip("'\"")


def parse_yaml_list_any_indent(text: str, key: str) -> list[str]:
    inline = re.search(rf"(?im)^\s*{re.escape(key)}:\s*\[(.*?)\]\s*$", text)
    if inline:
        items = [item.strip().strip("'\"") for item in inline.group(1).split(",")]
        return [item for item in items if item]
    block = re.search(
        rf"(?ims)^\s*{re.escape(key)}:\s*\n((?:^\s*-\s*.+\n?)*)",
        text,
    )
    if not block:
        return []
    return [
        line.strip()[2:].strip().strip("'\"")
        for line in block.group(1).splitlines()
        if line.strip().startswith("- ")
    ]


def route_slice_inventory(repo_root: Path | None = None) -> tuple[dict[str, list[dict[str, object]]], dict[str, dict[str, object]]]:
    root = repo_root or REPO_ROOT
    slice_root = root / "registries/route_slices"
    by_route_id: dict[str, list[dict[str, object]]] = {}
    by_path: dict[str, dict[str, object]] = {}
    if not slice_root.is_dir():
        return by_route_id, by_path
    for path in sorted(slice_root.glob("*.registry_slice.yaml")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        item = {
            "path": rel,
            "slice_id": parse_yaml_scalar_any_indent(text, "slice_id") or "",
            "route_id": parse_yaml_scalar_any_indent(text, "route_id") or "",
            "task_mode": parse_yaml_scalar_any_indent(text, "task_mode") or "",
            "default_task_mode": parse_yaml_scalar_any_indent(text, "default_task_mode") or "",
            "source_manifest": parse_yaml_scalar_any_indent(text, "source_manifest") or "",
            "output_contracts": parse_yaml_list_any_indent(text, "output_contracts"),
        }
        by_path[rel] = item
        route_id = _upper(item["route_id"])
        if route_id:
            by_route_id.setdefault(route_id, []).append(item)
    return by_route_id, by_path


def resolve_route_slice_claim(
    route_id: str | None,
    task_mode: str | None,
    route_manifest_path: str | None,
    route_slice_path: str | None,
    repo_root: Path | None = None,
) -> dict[str, object]:
    root = repo_root or REPO_ROOT
    by_route_id, by_path = route_slice_inventory(root)
    route_id_upper = _upper(route_id)
    normalized_mode = normalize_task_mode(_clean(task_mode))
    manifest_path = _clean(route_manifest_path)
    slice_path = _clean(route_slice_path)
    selected: dict[str, object] | None = None

    if slice_path:
        selected = by_path.get(slice_path)
    elif route_id_upper:
        candidates = by_route_id.get(route_id_upper, [])
        for candidate in candidates:
            candidate_mode = normalize_task_mode(
                _clean(candidate.get("task_mode")) or _clean(candidate.get("default_task_mode"))
            )
            candidate_manifest = _clean(candidate.get("source_manifest"))
            if normalized_mode and candidate_mode == normalized_mode:
                selected = candidate
                break
            if manifest_path and candidate_manifest == manifest_path:
                selected = candidate
                break
        if selected is None and candidates:
            selected = candidates[0]

    slice_exists = bool(selected)
    source_manifest_matches = (
        not slice_exists or not manifest_path or _clean(selected.get("source_manifest")) == manifest_path
    )
    route_id_matches = (
        not slice_exists or not route_id_upper or _upper(selected.get("route_id")) == route_id_upper
    )
    task_mode_matches = (
        not slice_exists
        or not normalized_mode
        or normalize_task_mode(
            _clean(selected.get("task_mode")) or _clean(selected.get("default_task_mode"))
        ) == normalized_mode
    )

    return {
        "expected": bool(route_id_upper or manifest_path or slice_path),
        "slice_exists": slice_exists,
        "slice_path": _clean(selected.get("path")) if selected else "",
        "slice_id": _clean(selected.get("slice_id")) if selected else "",
        "route_id": _clean(selected.get("route_id")) if selected else "",
        "task_mode": (
            _clean(selected.get("task_mode")) or _clean(selected.get("default_task_mode"))
        ) if selected else "",
        "source_manifest": _clean(selected.get("source_manifest")) if selected else "",
        "output_contracts": list(selected.get("output_contracts", [])) if selected else [],
        "route_id_matches": route_id_matches,
        "task_mode_matches": task_mode_matches,
        "source_manifest_matches": source_manifest_matches,
        "path_matches_claim": not slice_path or (slice_exists and _clean(selected.get("path")) == slice_path),
    }
