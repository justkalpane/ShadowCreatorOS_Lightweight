"""Script-only downstream adapter boundary stub for the film route."""

from __future__ import annotations

from typing import Any


ALLOWED_FUTURE_TARGETS = [
    "Nomi",
    "OpenMontage",
    "LTX",
    "DaVinci Resolve MCP",
]


def build_downstream_boundary(route_state: dict[str, Any], artifact_root: str) -> dict[str, Any]:
    return {
        "route_mode": route_state.get("mode"),
        "route_id": route_state.get("route"),
        "preproduction_only": True,
        "downstream_execution_triggered": False,
        "media_provider_triggered": False,
        "paid_api_triggered": False,
        "allowed_future_targets": ALLOWED_FUTURE_TARGETS,
        "handoff_packet_schema_required_before_activation": True,
        "artifact_root": artifact_root,
    }
