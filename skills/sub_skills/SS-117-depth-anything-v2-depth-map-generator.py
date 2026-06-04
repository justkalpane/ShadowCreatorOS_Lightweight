from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


DEPTH_INFER_SCRIPT = "depth_anything_v2_infer.py"


def build_depth_map_plan(input_dir: str, output_dir: str, execute: bool = False) -> dict:
    """Emit an honest DA-V2 handoff packet without claiming local execution."""
    in_path = Path(input_dir).expanduser()
    out_path = Path(output_dir).expanduser()
    image_candidates = []
    if in_path.exists() and in_path.is_dir():
        image_candidates = [
            str(p)
            for p in sorted(in_path.iterdir())
            if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        ]

    command = [
        "python3",
        DEPTH_INFER_SCRIPT,
        "--img-path",
        str(in_path),
        "--outdir",
        str(out_path),
    ]
    if not in_path.exists() or not in_path.is_dir():
        status = "NEEDS_CONFIRMATION"
        status_reason = "Input image directory does not exist yet; plan cannot be treated as ready for execution."
    elif execute:
        status = "NEEDS_USER_APPROVAL"
        status_reason = "Execution was requested, but local engine execution still requires explicit user approval."
    else:
        status = "PASS"
        status_reason = "Dry-run plan is structurally valid for an existing input directory; no execution was performed."
    return {
        "packet_family": "depth_map_plan_packet",
        "sub_skill_id": "SS-117",
        "sub_skill_name": "Depth Anything V2 Depth Map Generator",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "status_reason": status_reason,
        "execution_mode": "dry_run_plan_only",
        "local_engine_execution_used": False,
        "provider_execution_allowed": False,
        "input_dir": str(in_path),
        "output_dir": str(out_path),
        "input_dir_exists": in_path.exists(),
        "image_candidates": image_candidates,
        "recommended_model": "Depth-Anything-V2-Small for CPU/Mac safety; Large only when GPU/RAM headroom is confirmed",
        "tool_role": "depth_mask_generation_only",
        "boundary": "DA-V2 creates depth masks only. It does not generate images, videos, cinematic B-roll, or DaVinci composites.",
        "davinci_handoff": "Use generated depth_map_png in DaVinci Resolve Fusion for foreground/midground/background 2.5D parallax.",
        "planned_command": command,
        "execution_note": "This wrapper produces a handoff plan. Run execution only after explicit user approval and local engine preflight proof.",
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 SS-117-depth-anything-v2-depth-map-generator.py <input_dir> <output_dir> [--execute]")
        sys.exit(1)

    packet = build_depth_map_plan(sys.argv[1], sys.argv[2], execute="--execute" in sys.argv)
    print(json.dumps(packet, indent=2))
