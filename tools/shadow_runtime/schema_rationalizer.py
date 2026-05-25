from __future__ import annotations
import argparse, csv, json
from pathlib import Path
from common import ROOT, load_route_dag_registry, output


CANONICAL_ACTIVE = [
    "topic_intake_packet",
    "trend_signal_packet",
    "source_evidence_packet",
    "research_brief_packet",
    "script_strategy_packet",
    "script_v1_packet",
    "debate_critique_packet",
    "refinement_delta_packet",
    "final_script_packet",
    "script_segment_packet",
    "voice_context_packet",
    "visual_context_packet",
    "video_context_packet",
    "music_sfx_packet",
    "editing_timeline_packet",
    "provider_handoff_packet",
    "media_quality_gate_packet",
    "lineage_packet",
    "approval_packet",
    "operator_execution_packet",
]

PROVIDER_RELEVANT = {
    "provider_handoff_packet",
    "video_context_packet",
    "voice_context_packet",
    "visual_context_packet",
    "music_sfx_packet",
    "editing_timeline_packet",
    "operator_execution_packet",
}

BASE_REQUIRED = {
    "packet_id",
    "route_id",
    "producer_component_id",
    "consumer_component_ids",
    "lineage",
    "validation_status",
}


def classify_schema(packet_id: str, used_by_dag: bool) -> str:
    if packet_id in CANONICAL_ACTIVE:
        return "CANONICAL_ACTIVE"
    if used_by_dag:
        return "CANONICAL_SUPPORT"
    if packet_id.endswith("_alias_packet"):
        return "GENERATED_ALIAS"
    if "duplicate" in packet_id:
        return "DUPLICATE_CANDIDATE"
    if any(token in packet_id for token in ["future", "provider", "media"]) and packet_id not in CANONICAL_ACTIVE:
        return "DORMANT_FUTURE"
    return "GENERATED_ALIAS"


def rationalize(out_csv: str | None = None):
    schema_dir = ROOT / "schemas/packets"
    dag = load_route_dag_registry()
    dag_packets = {
        packet
        for route in dag.get("route_dags", [])
        for node in route.get("ordered_nodes", [])
        for packet in node.get("required_input_packets", []) + node.get("emitted_output_packets", [])
    }
    rows = []
    counts = {}
    missing_for_dags = []
    issues = []
    for packet in sorted(dag_packets):
        if not (schema_dir / f"{packet}.schema.json").exists():
            missing_for_dags.append(packet)
    for path in sorted(schema_dir.glob("*.schema.json")):
        packet_id = path.name.removesuffix(".schema.json")
        valid_json = False
        data = {}
        gap = []
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))
            valid_json = data.get("type") == "object" and isinstance(data.get("properties"), dict)
        except Exception as exc:
            gap.append(f"invalid_json:{exc}")
        props = data.get("properties", {}) if isinstance(data, dict) else {}
        required = set(data.get("required", [])) if isinstance(data.get("required", []), list) else set()
        used = packet_id in dag_packets
        classification = classify_schema(packet_id, used)
        provider_default_false = True
        approval_required_present = "approval_required" in props or packet_id == "approval_packet"
        if packet_id in PROVIDER_RELEVANT:
            provider = props.get("provider_execution_allowed", {})
            provider_default_false = provider.get("default") is False and provider.get("const") is False
            if not provider_default_false:
                gap.append("provider_execution_allowed_default_false_missing")
            if "approval_required" not in props:
                gap.append("approval_required_missing")
        if used and classification not in {"CANONICAL_ACTIVE", "CANONICAL_SUPPORT"}:
            gap.append("dag_schema_not_canonical")
        if used and not BASE_REQUIRED.issubset(required):
            gap.append("base_required_fields_missing")
        if not valid_json:
            gap.append("not_valid_json_schema")
        status = "PASS" if not gap else "FAIL"
        if gap:
            issues.append(f"{path.name}:{'|'.join(gap)}")
        counts[classification] = counts.get(classification, 0) + 1
        rows.append(
            {
                "schema_file": str(path.relative_to(ROOT)),
                "packet_id": packet_id,
                "classification": classification,
                "used_by_active_dag": used,
                "valid_json_schema": valid_json,
                "provider_default_false_present": provider_default_false,
                "approval_required_present": approval_required_present,
                "lineage_present": "lineage" in props,
                "canonical_target": packet_id if classification.startswith("CANONICAL") else "",
                "status": status,
                "gap": ";".join(gap),
            }
        )

    index = {
        "schema_governance_status": "PASS" if not issues and not missing_for_dags else "FAIL",
        "canonical_active_packets": CANONICAL_ACTIVE,
        "dag_packets": sorted(dag_packets),
        "classification_counts": counts,
        "schema_count_justified": not issues and not missing_for_dags,
        "overgenerated_schema_risk_resolved": not issues and not missing_for_dags,
        "missing_for_dags": missing_for_dags,
    }
    (schema_dir / "CANONICAL_PACKET_SCHEMA_INDEX.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    (schema_dir / "SCHEMA_RATIONALIZATION_REPORT.md").write_text(
        "# Schema Rationalization Report\n\n"
        f"schemas_found={len(rows)}\n"
        f"canonical_active_schemas={counts.get('CANONICAL_ACTIVE', 0)}\n"
        f"schema_count_justified={str(index['schema_count_justified']).lower()}\n"
        f"overgenerated_schema_risk_resolved={str(index['overgenerated_schema_risk_resolved']).lower()}\n"
        f"schemas_missing_for_dags={missing_for_dags}\n"
        f"issues={issues[:20]}\n",
        encoding="utf-8",
    )
    if out_csv:
        p = Path(out_csv)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
            if rows:
                w.writeheader()
                w.writerows(rows)
    result = {
        "pass": not issues and not missing_for_dags,
        "schemas_found": len(rows),
        "canonical_active_schemas": counts.get("CANONICAL_ACTIVE", 0),
        "canonical_support_schemas": counts.get("CANONICAL_SUPPORT", 0),
        "generated_alias_schemas": counts.get("GENERATED_ALIAS", 0),
        "dormant_future_schemas": counts.get("DORMANT_FUTURE", 0),
        "duplicate_candidate_schemas": counts.get("DUPLICATE_CANDIDATE", 0),
        "quarantine_schemas": counts.get("QUARANTINE_SCHEMA", 0),
        "schemas_used_by_dags": len(dag_packets),
        "schemas_missing_for_dags": len(missing_for_dags),
        "schema_count_justified": not issues and not missing_for_dags,
        "overgenerated_schema_risk_resolved": not issues and not missing_for_dags,
        "issues": issues,
    }
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--csv")
    args = ap.parse_args()
    result = rationalize(args.csv)
    output(result, args.out)
    raise SystemExit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
