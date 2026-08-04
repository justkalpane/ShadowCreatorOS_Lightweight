from __future__ import annotations

from pathlib import Path

from validators.film.runtime.preproduction_validator_utils import packet, result


REPO_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = REPO_ROOT / "runtime_contracts/FILM_DOWNSTREAM_MEDIA_ADAPTER_BOUNDARY_CONTRACT.md"


def validate(payload: dict) -> dict:
    data = packet(payload)
    boundary = data.get("downstream_adapter_boundary") or {}
    errors = []
    if not CONTRACT_PATH.is_file():
        errors.append("downstream boundary contract missing")
    if data.get("mode") != "script_only":
        errors.append("downstream boundary requires script_only mode")
    if boundary.get("route_mode") != "script_only":
        errors.append("route mode must remain script_only in boundary packet")
    if not boundary.get("preproduction_only"):
        errors.append("downstream boundary must mark film output as preproduction only")
    if boundary.get("downstream_execution_triggered") is not False:
        errors.append("downstream execution must remain false")
    if boundary.get("media_provider_triggered") is not False:
        errors.append("media provider trigger must remain false")
    if boundary.get("paid_api_triggered") is not False:
        errors.append("paid api trigger must remain false")
    if set(boundary.get("allowed_future_targets") or []) != {"Nomi", "OpenMontage", "LTX", "DaVinci Resolve MCP"}:
        errors.append("allowed future targets list is incomplete")
    return result("validate_film_downstream_boundary", not errors, errors)
