import importlib.util
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "validators/film/validate_film_route_post_binding_state.py"
PROMOTION_CHECKER_PATH = ROOT / "validators/film/validate_film_route_promotion_gate.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("post_binding_checker", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_post_binding_checker_reports_ready_for_current_repo_state():
    checker = load_checker()
    status, details = checker.evaluate(ROOT)

    assert status == "POST_BINDING_FILM_ROUTE_STATE_READY"
    assert "selector_mode=film_screenplay_generation" in details
    assert "selector_allowed_route_id=FILM_SCREENPLAY_GENERATION" in details
    assert "default_mode=script_only" in details
    assert "manifest_bound_to_route_selector=true" in details
    assert "slice_bound_to_route_selector=true" in details
    assert "script_generation_preserved=true" in details
    assert "pass_claimed=false" in details
    assert "governed_runtime_proof_claimed=false" in details


def test_post_binding_checker_cli_reports_ready_and_no_runtime_proof():
    result = subprocess.run(
        ["python3", str(CHECKER_PATH)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )

    assert "POST_BINDING_FILM_ROUTE_STATE_CHECKER_REPORT" in result.stdout
    assert "status=POST_BINDING_FILM_ROUTE_STATE_READY" in result.stdout
    assert "runtime_behavior_changed=false" in result.stdout
    assert "pass_claimed=false" in result.stdout
    assert "governed_runtime_proof_claimed=false" in result.stdout


def test_pre_promotion_checker_remains_unmodified_and_pre_binding_only():
    text = PROMOTION_CHECKER_PATH.read_text(encoding="utf-8")
    assert "PROMOTION_GATE_BLOCKED_ACTIVE_FILE_ALREADY_EXISTS" in text
    assert "PROMOTION_GATE_BLOCKED_SELECTOR_ALREADY_REFERENCES_FILM_ROUTE" in text
    assert "POST_BINDING_FILM_ROUTE_STATE_READY" not in text


def test_post_binding_manifest_documents_unbound_read_only_checker():
    manifest = (ROOT / "validators/film/phase_13e30_post_binding_checker_manifest.json").read_text(
        encoding="utf-8"
    )
    assert '"phase": "13E_30"' in manifest
    assert '"status": "post_binding_checker_unbound_read_only"' in manifest
    assert '"runtime_behavior_changed": false' in manifest
    assert '"route_selector_modified": false' in manifest
    assert '"pass_claimed": false' in manifest
    assert '"governed_runtime_proof_claimed": false' in manifest


if __name__ == "__main__":
    test_post_binding_checker_reports_ready_for_current_repo_state()
    test_post_binding_checker_cli_reports_ready_and_no_runtime_proof()
    test_pre_promotion_checker_remains_unmodified_and_pre_binding_only()
    test_post_binding_manifest_documents_unbound_read_only_checker()
    print("phase_13e30_film_route_post_binding_state_checker_ok")
