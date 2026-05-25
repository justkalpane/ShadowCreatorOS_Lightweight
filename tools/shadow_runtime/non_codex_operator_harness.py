from __future__ import annotations
import argparse, json
from pathlib import Path
from common import ROOT, output

REQUIRED_PROOF=['shadow_command_alias_detected','route_manifest_loaded','internal_wrapper_applied','route_dag_validation_pass','packet_schema_validation_pass','packet_flow_validation_pass','communication_vein_validation_pass','lifecycle_validation_pass','quality_scorecard_validation_pass','provider_boundary_validation_pass']

def validate(packet_path: Path):
    pkt=json.loads(packet_path.read_text(encoding='utf-8-sig', errors='replace'))
    issues=[]
    for k in ['packet_id','route_id','proof_fields','provider_execution_allowed']:
        if k not in pkt: issues.append(f'missing:{k}')
    pf=pkt.get('proof_fields',{}) if isinstance(pkt.get('proof_fields',{}),dict) else {}
    for k in REQUIRED_PROOF:
        if pf.get(k) is not True: issues.append(f'proof_field_missing_or_false:{k}')
    if pkt.get('provider_execution_allowed') is True: issues.append('provider_execution_not_allowed')
    if pkt.get('external_calls') is True or pkt.get('content_generation') is True: issues.append('external_or_content_generation_claimed')
    ok=len(issues)==0
    return {'pass':ok,'validation_status':'PASS' if ok else 'FAIL','issues':issues,'safe_to_run_only_after_local_enforcement':True}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--packet', required=True)
    ap.add_argument('--out')
    args=ap.parse_args()
    res=validate(Path(args.packet))
    output(res,args.out)
    raise SystemExit(0 if res['pass'] else 1)

if __name__=='__main__':
    main()
