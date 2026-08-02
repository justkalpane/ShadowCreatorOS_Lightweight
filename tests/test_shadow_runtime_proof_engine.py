import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF_ENGINE_PATH = ROOT / "tools/shadow_runtime/proof_engine.py"


def build_film_mission() -> dict:
    return {
        "schema_version": "1.0.0",
        "mission_id": "MISSION-FILM-GOVERNED-RUNTIME-EXECUTION-TEST",
        "mission_semantic_hash": "sha256:film_governed_runtime_execution_test_placeholder",
        "client": {
            "client_id": "codex-film-executor-test",
            "platform": "GENERIC_OPENAPI_CLIENT",
            "platform_version": "unknown",
            "adapter_id": "shadow-openapi-agentic-gateway",
            "transport": "HTTPS_OPENAPI",
            "session_id": "SESSION-FILM-EXEC-TEST",
            "authenticated_subject": "authorized-agent",
        },
        "request": {
            "intent": "governed_runtime_executor_phase_film_runtime_proof",
            "inputs": [
                {
                    "kind": "text",
                    "value": "Execute the governed runtime executor path for FILM_SCREENPLAY_GENERATION under bounded scope.",
                },
                {
                    "kind": "text",
                    "value": "Preserve SCRIPT_GENERATION and default_mode=script_only.",
                },
            ],
            "requested_capabilities": ["mission.submit", "mission.status", "certificate.read"],
            "requested_output_contract": "FILM_GOVERNED_RUNTIME_EXECUTION_PLAN",
            "priority": "normal",
            "deadline": None,
        },
        "authorization": {
            "scopes": ["mission:submit", "mission:read"],
            "approval_mode": "founder_required_for_state_change",
            "founder_authority_present": False,
        },
        "repository_binding": {
            "repository_id": "ShadowCreatorOS_Lightweight",
            "worktree": str(ROOT),
            "branch": "codex/shadow-prod-recovery",
            "repository_lock_id": "REPOSITORY_LOCK_REQUIRED_AT_RUNTIME",
        },
        "metadata": {
            "correlation_id": "CORR-FILM-EXEC-TEST",
            "submitted_at": "2026-08-02T14:20:00Z",
            "locale": "en-US",
            "timezone": "Asia/Kolkata",
        },
    }


def test_proof_engine_generate_accepts_supplied_mission() -> None:
    mission = build_film_mission()
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        mission_path = Path(handle.name)
        json.dump(mission, handle, indent=2)
        handle.write("\n")

    try:
        result = subprocess.run(
            ["python3", str(PROOF_ENGINE_PATH), "generate", "--mission", str(mission_path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        assert result.returncode == 0, result.stdout + result.stderr
        assert "REAL_PROOF_ENGINE=PASS" in result.stdout
        assert "status=COMPONENT_RUNTIME_PROTOTYPE_HARDENED" in result.stdout
        assert "mission_id=MISSION-FILM-GOVERNED-RUNTIME-EXECUTION-TEST" in result.stdout
    finally:
        mission_path.unlink(missing_ok=True)


if __name__ == "__main__":
    test_proof_engine_generate_accepts_supplied_mission()
    print("test_shadow_runtime_proof_engine_ok")
