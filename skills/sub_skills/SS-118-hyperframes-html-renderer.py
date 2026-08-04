from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


HYPERFRAMES_BIN = "/Users/apple/ShadowMediaFactory/07_PROJECTS/hyperframes/node_modules/.bin/hyperframes"
CONTROL_PANEL_CLI = "/Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py"
HYPERFRAMES_PROVIDER_ID = "hyperframes_cli_local"
HYPERFRAMES_CONNECTOR_CONTRACT = "runtime_contracts/HYPERFRAMES_CONNECTOR_INTEGRATION_CONTRACT.md"
HYPERFRAMES_ORIGINAL_SKILL_PATHS = [
    "/Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes/SKILL.md",
    "/Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes-cli/SKILL.md",
    "/Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes-registry/SKILL.md",
]


def build_hyperframes_render_plan(project_root: str, output_path: str, use_alpha: bool = False, execute: bool = False) -> dict:
    """Emit an honest HyperFrames render handoff packet without claiming media creation."""
    project = Path(project_root).expanduser()
    output = Path(output_path).expanduser()
    command = [HYPERFRAMES_BIN, "render", str(project), "--output", str(output)]
    if use_alpha:
        command.append("--alpha")
    if not project.exists() or not project.is_dir():
        status = "NEEDS_CONFIRMATION"
        status_reason = "HyperFrames project root does not exist yet; plan cannot be treated as ready for execution."
    elif execute:
        status = "NEEDS_USER_APPROVAL"
        status_reason = "Execution was requested, but local engine execution still requires explicit user approval."
    else:
        status = "PASS"
        status_reason = "Dry-run plan is structurally valid for an existing project root; no execution was performed."

    return {
        "packet_family": "hyperframes_render_plan_packet",
        "sub_skill_id": "SS-118",
        "sub_skill_name": "HyperFrames HTML Renderer",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "status_reason": status_reason,
        "execution_mode": "dry_run_plan_only",
        "local_engine_execution_used": False,
        "provider_execution_allowed": False,
        "provider_id": HYPERFRAMES_PROVIDER_ID,
        "connector_assessment_required": True,
        "connector_assessment_contract": HYPERFRAMES_CONNECTOR_CONTRACT,
        "project_root": str(project),
        "project_root_exists": project.exists(),
        "output_path": str(output),
        "alpha_export_requested": use_alpha,
        "original_skill_paths": HYPERFRAMES_ORIGINAL_SKILL_PATHS,
        "supported_layouts": ["split_card_horizontal", "fullscreen_text_center", "notebook_dual_panel"],
        "tool_role": "deterministic HTML/CSS/GSAP render planning for NotebookLM slides, programmatic cards, kinetic text, and WebM alpha overlays",
        "boundary": "HyperFrames does not replace DaVinci Resolve for 2.5D parallax or final assembly.",
        "planned_command": command,
        "control_panel_command": ["python3", CONTROL_PANEL_CLI, "run-hyperframes"],
        "execution_note": "This wrapper produces a handoff plan. Run execution only after explicit user approval and local engine preflight proof.",
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 SS-118-hyperframes-html-renderer.py <project_root> <output_path> [--alpha] [--execute]")
        sys.exit(1)

    packet = build_hyperframes_render_plan(
        sys.argv[1],
        sys.argv[2],
        use_alpha="--alpha" in sys.argv,
        execute="--execute" in sys.argv,
    )
    print(json.dumps(packet, indent=2))
