from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from common import ROOT, output


BRIDGE = ROOT / "registries/local_media_factory_bridge.yaml"
CONTRACT = ROOT / "runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md"
MEDIA_FACTORY_ROOT = Path("/Users/apple/ShadowMediaFactory")
CONTROL_PANEL = MEDIA_FACTORY_ROOT / "control_panel"
CLI = CONTROL_PANEL / "bin/shadow_factory_ctl.py"
CAPABILITY_MAP = CONTROL_PANEL / "config/capability_map.json"
PROOFS_DIR = CONTROL_PANEL / "proofs"
REGISTRY_DIR = CONTROL_PANEL / "registry"
JOBS_DIR = CONTROL_PANEL / "jobs"
EXPORTS_DIR = MEDIA_FACTORY_ROOT / "08_EXPORTS"
COMFYUI_ROOT = MEDIA_FACTORY_ROOT / "apps/ComfyUI"

SYNC_BEGIN = "# BEGIN AUTO-GENERATED MEDIA FACTORY SYNC STATE"
SYNC_END = "# END AUTO-GENERATED MEDIA FACTORY SYNC STATE"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))


def run_cmd(cmd: list[str], timeout: int = 20) -> dict:
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        stdout = proc.stdout.strip()
        parsed = None
        if stdout.startswith("{"):
            try:
                parsed = json.loads(stdout)
            except json.JSONDecodeError:
                parsed = None
        return {
            "callable": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout_excerpt": stdout[:2000],
            "json": parsed,
        }
    except Exception as exc:
        return {
            "callable": False,
            "returncode": None,
            "stdout_excerpt": str(exc),
            "json": None,
        }


def latest_file(path: Path, pattern: str) -> Path | None:
    if not path.exists():
        return None
    files = [p for p in path.glob(pattern) if p.is_file()]
    return max(files, key=lambda p: p.stat().st_mtime) if files else None


def jsonl_summary(path: Path) -> dict:
    if not path.exists():
        return {"exists": False, "line_count": 0, "valid_jsonl": False, "hash": None}
    valid = True
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    for line in lines:
        if not line.strip():
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError:
            valid = False
            break
    return {
        "exists": True,
        "line_count": len([line for line in lines if line.strip()]),
        "valid_jsonl": valid,
        "hash": sha256(path),
    }


def collect_snapshot(runtime_check: bool) -> dict:
    latest_proof = latest_file(PROOFS_DIR, "*.json")
    capability = read_json(CAPABILITY_MAP)
    registry_files = {
        name: jsonl_summary(REGISTRY_DIR / name)
        for name in [
            "assets.jsonl",
            "scene_contracts.jsonl",
            "route_decisions.jsonl",
            "retry_state.jsonl",
        ]
    }
    snapshot = {
        "snapshot_at": now_iso(),
        "paths": {
            "media_factory_root_exists": MEDIA_FACTORY_ROOT.exists(),
            "control_panel_exists": CONTROL_PANEL.exists(),
            "control_panel_cli_exists": CLI.exists(),
            "capability_map_exists": CAPABILITY_MAP.exists(),
            "proofs_dir_exists": PROOFS_DIR.exists(),
            "registry_dir_exists": REGISTRY_DIR.exists(),
            "jobs_dir_exists": JOBS_DIR.exists(),
            "exports_dir_exists": EXPORTS_DIR.exists(),
            "comfyui_root_exists": COMFYUI_ROOT.exists(),
        },
        "hashes": {
            "control_panel_cli_sha256": sha256(CLI),
            "capability_map_sha256": sha256(CAPABILITY_MAP),
            "latest_proof_sha256": sha256(latest_proof) if latest_proof else None,
        },
        "latest_proof": str(latest_proof) if latest_proof else None,
        "registry_files": registry_files,
        "capability_map": capability,
        "runtime_check_enabled": runtime_check,
        "status": None,
        "doctor": None,
    }
    if runtime_check and CLI.exists():
        snapshot["status"] = run_cmd(["python3", str(CLI), "status"])
        snapshot["doctor"] = run_cmd(["python3", str(CLI), "doctor"], timeout=45)
    return snapshot


def bridge_text() -> str:
    return BRIDGE.read_text(encoding="utf-8-sig", errors="replace") if BRIDGE.exists() else ""


def bridge_contains_required_paths(text: str) -> bool:
    required = [
        "/Users/apple/ShadowMediaFactory",
        "/Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py",
        "/Users/apple/ShadowMediaFactory/control_panel/config/capability_map.json",
    ]
    return all(item in text for item in required)


def bridge_has_stale_hashes(text: str, snapshot: dict) -> bool:
    if SYNC_BEGIN not in text:
        return True
    for key, value in snapshot.get("hashes", {}).items():
        if not value:
            continue
        unquoted = f"{key}: {value}"
        quoted = f'{key}: "{value}"'
        if unquoted not in text and quoted not in text:
            return True
    return False


def capability_drift(text: str, capability: dict) -> list[str]:
    issues: list[str] = []
    if not capability:
        issues.append("capability_map_missing_or_unreadable")
        return issues
    animatic = capability.get("local_animatic_lane", {})
    wan = capability.get("wan_lane", {})
    assembly = capability.get("assembly_lane", {})
    expected_pairs = {
        "supports_canny": animatic.get("supports_canny"),
        "supports_openpose": animatic.get("supports_openpose"),
        "supports_depth": animatic.get("supports_depth"),
        "supports_lineart": animatic.get("supports_lineart"),
        "supports_ipadapter": animatic.get("supports_ipadapter"),
        "supports_true_camera_motion": animatic.get("supports_true_camera_motion"),
        "wan_technical_pass": wan.get("technical_pass"),
        "wan_production_quality_pass": wan.get("production_quality_pass"),
        "supports_audio_mix": assembly.get("supports_audio_mix"),
        "supports_per_scene_sfx": assembly.get("supports_per_scene_sfx"),
    }
    for key, value in expected_pairs.items():
        if value is None:
            continue
        yaml_key = key
        if key.startswith("wan_"):
            yaml_key = key.replace("wan_", "")
        needle = f"{yaml_key}: {str(value).lower()}"
        if needle not in text:
            issues.append(f"bridge_missing_or_stale:{key}={str(value).lower()}")
    return issues


def analyze(snapshot: dict) -> dict:
    text = bridge_text()
    issues: list[str] = []
    if not BRIDGE.exists():
        issues.append("bridge_registry_missing")
    if not CONTRACT.exists():
        issues.append("bridge_contract_missing")
    if not bridge_contains_required_paths(text):
        issues.append("bridge_missing_required_paths")
    if bridge_has_stale_hashes(text, snapshot):
        issues.append("bridge_sync_state_missing_or_stale")
    issues.extend(capability_drift(text, snapshot.get("capability_map", {})))
    missing_paths = [k for k, v in snapshot["paths"].items() if not v]
    for missing in missing_paths:
        issues.append(f"media_factory_path_missing:{missing}")
    if snapshot.get("runtime_check_enabled"):
        if not (snapshot.get("status") or {}).get("callable"):
            issues.append("media_factory_status_failed")
        if not (snapshot.get("doctor") or {}).get("callable"):
            issues.append("media_factory_doctor_failed")
    changed = any(
        issue.startswith("bridge_sync_state_missing_or_stale")
        or issue.startswith("bridge_missing_or_stale")
        or issue.startswith("capability_map")
        for issue in issues
    )
    in_sync = not issues
    return {
        "bridge_in_sync": in_sync,
        "media_factory_changed": changed,
        "repo_bridge_update_required": bool(issues),
        "issues": issues,
        "safe_to_update_bridge": BRIDGE.exists() and not missing_paths,
    }


def yaml_scalar(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def render_sync_state(snapshot: dict, analysis: dict) -> str:
    hashes = snapshot.get("hashes", {})
    paths = snapshot.get("paths", {})
    capability = snapshot.get("capability_map", {})
    animatic = capability.get("local_animatic_lane", {})
    wan = capability.get("wan_lane", {})
    assembly = capability.get("assembly_lane", {})
    lines = [
        SYNC_BEGIN,
        "sync_state:",
        f"  last_sync_at: {yaml_scalar(snapshot.get('snapshot_at'))}",
        f"  bridge_in_sync: {yaml_scalar(analysis.get('bridge_in_sync'))}",
        f"  media_factory_changed: {yaml_scalar(analysis.get('media_factory_changed'))}",
        f"  repo_bridge_update_required: {yaml_scalar(analysis.get('repo_bridge_update_required'))}",
        f"  control_panel_cli_sha256: {yaml_scalar(hashes.get('control_panel_cli_sha256'))}",
        f"  capability_map_sha256: {yaml_scalar(hashes.get('capability_map_sha256'))}",
        f"  latest_proof_sha256: {yaml_scalar(hashes.get('latest_proof_sha256'))}",
        f"  latest_proof_path: {yaml_scalar(snapshot.get('latest_proof'))}",
        "  path_status:",
    ]
    for key in sorted(paths):
        lines.append(f"    {key}: {yaml_scalar(paths[key])}")
    lines.extend(
        [
            "  lane_truth:",
            f"    local_animatic_engine: {yaml_scalar(animatic.get('engine'))}",
            f"    local_animatic_role: {yaml_scalar(animatic.get('production_role'))}",
            f"    local_animatic_supports_canny: {yaml_scalar(animatic.get('supports_canny'))}",
            f"    local_animatic_supports_openpose: {yaml_scalar(animatic.get('supports_openpose'))}",
            f"    local_animatic_supports_depth: {yaml_scalar(animatic.get('supports_depth'))}",
            f"    local_animatic_supports_lineart: {yaml_scalar(animatic.get('supports_lineart'))}",
            f"    local_animatic_supports_ipadapter: {yaml_scalar(animatic.get('supports_ipadapter'))}",
            f"    local_animatic_supports_true_camera_motion: {yaml_scalar(animatic.get('supports_true_camera_motion'))}",
            f"    wan_engine: {yaml_scalar(wan.get('engine'))}",
            f"    wan_technical_pass: {yaml_scalar(wan.get('technical_pass'))}",
            f"    wan_production_quality_pass: {yaml_scalar(wan.get('production_quality_pass'))}",
            f"    assembly_engine: {yaml_scalar(assembly.get('engine'))}",
            f"    assembly_supports_audio_mix: {yaml_scalar(assembly.get('supports_audio_mix'))}",
            f"    assembly_supports_per_scene_sfx: {yaml_scalar(assembly.get('supports_per_scene_sfx'))}",
            "  registry_files:",
        ]
    )
    for name, summary in snapshot.get("registry_files", {}).items():
        lines.append(f"    {name}:")
        lines.append(f"      exists: {yaml_scalar(summary.get('exists'))}")
        lines.append(f"      line_count: {yaml_scalar(summary.get('line_count'))}")
        lines.append(f"      valid_jsonl: {yaml_scalar(summary.get('valid_jsonl'))}")
        lines.append(f"      hash: {yaml_scalar(summary.get('hash'))}")
    lines.append("  issues:")
    for issue in analysis.get("issues", []):
        lines.append(f"    - {yaml_scalar(issue)}")
    if not analysis.get("issues"):
        lines.append("    []")
    lines.append(SYNC_END)
    return "\n".join(lines) + "\n"


def apply_sync_state(snapshot: dict, analysis: dict) -> bool:
    original = bridge_text()
    block = render_sync_state(snapshot, analysis)
    if SYNC_BEGIN in original and SYNC_END in original:
        pattern = re.compile(
            re.escape(SYNC_BEGIN) + r".*?" + re.escape(SYNC_END) + r"\n?",
            re.DOTALL,
        )
        updated = pattern.sub(block, original)
    else:
        updated = original.rstrip() + "\n\n" + block
    updated = re.sub(
        r'^updated_at:\s*".*?"\s*$',
        f'updated_at: "{snapshot.get("snapshot_at", now_iso())[:10]}"',
        updated,
        flags=re.MULTILINE,
    )
    BRIDGE.write_text(updated, encoding="utf-8")
    return bridge_text() == updated


def run(runtime_check: bool, apply: bool) -> dict:
    snapshot = collect_snapshot(runtime_check=runtime_check)
    analysis = analyze(snapshot)
    applied = False
    if apply:
        applied = apply_sync_state(snapshot, analysis)
        refreshed = collect_snapshot(runtime_check=False)
        analysis = analyze(refreshed)
        snapshot = refreshed
    return {
        "pass": True,
        "BRIDGE_DRIFT_SYNC_DONE": True,
        "APPLY_MODE": apply,
        "SYNC_STATE_WRITTEN": applied,
        "BRIDGE_IN_SYNC": analysis.get("bridge_in_sync"),
        "MEDIA_FACTORY_CHANGED": analysis.get("media_factory_changed"),
        "REPO_BRIDGE_UPDATE_REQUIRED": analysis.get("repo_bridge_update_required"),
        "SAFE_TO_UPDATE_BRIDGE": analysis.get("safe_to_update_bridge"),
        "MEDIA_FACTORY_ROOT": str(MEDIA_FACTORY_ROOT),
        "BRIDGE_REGISTRY": str(BRIDGE),
        "BRIDGE_CONTRACT": str(CONTRACT),
        "CONTROL_PANEL_CLI": str(CLI),
        "CAPABILITY_MAP": str(CAPABILITY_MAP),
        "LATEST_PROOF": snapshot.get("latest_proof"),
        "ISSUES": analysis.get("issues", []),
        "SNAPSHOT": snapshot,
    }


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Audit and optionally sync ShadowCreatorOS local Media Factory bridge state."
    )
    ap.add_argument("--runtime-check", action="store_true", help="Run Media Factory status and doctor.")
    ap.add_argument("--apply", action="store_true", help="Write sync_state back into the bridge registry.")
    ap.add_argument("--out", help="Optional JSON output path.")
    args = ap.parse_args()
    result = run(runtime_check=args.runtime_check, apply=args.apply)
    output(result, args.out)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
