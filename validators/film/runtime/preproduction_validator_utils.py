"""Shared helpers for film preproduction runtime validators."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet
except ModuleNotFoundError:  # pragma: no cover
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


PHASE = "13D_F7"
REPO_ROOT = Path(__file__).resolve().parents[3]


def result(name: str, passed: bool, errors: list[str]) -> dict[str, Any]:
    return {
        "validator": name,
        "phase": PHASE,
        "status": "VALIDATION_PASSED" if passed else "VALIDATION_FAILED",
        "passed": passed,
        "enforced": True,
        "runtime_behavior_changed": False,
        "route_selector_modified": False,
        "validator_bound_to_runtime": True,
        "governed_runtime_proof_claimed": False,
        "errors": errors,
        "message": f"{name} {'passed' if passed else 'failed'}.",
    }


def packet(payload: dict[str, Any]) -> dict[str, Any]:
    data = load_screenplay_packet(payload)
    if "preproduction_packet" in data and isinstance(data["preproduction_packet"], dict):
        return data["preproduction_packet"]
    return data


def require_fields(data: dict[str, Any], fields: list[str]) -> list[str]:
    return [f"missing field: {field}" for field in fields if field not in data or data.get(field) in ({}, [], "", None)]


def contains_forbidden_media_terms(data: dict[str, Any]) -> bool:
    text = json.dumps(data).lower()
    return any(term in text for term in ["provider_call_triggered\": true", "media_generation_triggered\": true", "paid_api_triggered\": true"])


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def normalized_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip().lower()
    return json.dumps(value, ensure_ascii=True).lower()


def contains_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def missing_or_empty(data: dict[str, Any], field: str) -> bool:
    return field not in data or data.get(field) in ({}, [], "", None)


def list_of_dicts(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, dict) for item in value)


def read_json_file(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def schema_path(rel_path: str) -> Path:
    return REPO_ROOT / rel_path


def _check_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return True


def validate_against_schema(
    value: Any,
    schema: dict[str, Any],
    *,
    base_dir: Path | None = None,
    path: str = "$",
) -> list[str]:
    base_dir = base_dir or REPO_ROOT
    errors: list[str] = []

    if "$ref" in schema:
        ref_path = (base_dir / schema["$ref"]).resolve()
        target = read_json_file(ref_path)
        return validate_against_schema(value, target, base_dir=ref_path.parent, path=path)

    expected_type = schema.get("type")
    if expected_type and not _check_type(value, expected_type):
        return [f"{path} expected {expected_type}"]

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path} must equal {schema['const']}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path} must be one of {schema['enum']}")

    if expected_type == "object":
        if not isinstance(value, dict):
            return errors
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}.{key} missing")
        properties = schema.get("properties", {})
        for key, sub_schema in properties.items():
            if key in value:
                errors.extend(validate_against_schema(value[key], sub_schema, base_dir=base_dir, path=f"{path}.{key}"))

    if expected_type == "array":
        if not isinstance(value, list):
            return errors
        min_items = schema.get("minItems")
        if min_items is not None and len(value) < min_items:
            errors.append(f"{path} must contain at least {min_items} items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(validate_against_schema(item, item_schema, base_dir=base_dir, path=f"{path}[{index}]"))

    return errors


def validate_schema_file(value: Any, rel_path: str) -> list[str]:
    path = schema_path(rel_path)
    schema = read_json_file(path)
    return validate_against_schema(value, schema, base_dir=path.parent)
