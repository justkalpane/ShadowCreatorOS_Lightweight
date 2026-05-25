from __future__ import annotations
import argparse, json
from pathlib import Path
from common import ROOT, load_route_dag_registry, output


def validate(packet_path: Path|None=None, route: str='script_generation'):
    issues=[]
    provider_execution_disabled=True
    unauthorized_blocked=True
    false_claim_detected=False
    if packet_path and packet_path.exists():
        pkt=json.loads(packet_path.read_text(encoding='utf-8-sig', errors='replace'))
        if pkt.get('provider_execution_allowed') is True and (
            not pkt.get('approval_required')
            or pkt.get('approval_authorized') is not True
            or not pkt.get('approval_packet_id')
        ):
            issues.append('provider_execution_without_explicit_approval_packet')
            provider_execution_disabled=False
            unauthorized_blocked=False
    dag=load_route_dag_registry()
    rt=next((r for r in dag.get('route_dags',[]) if r.get('route_id')==route),None)
    if rt:
        for n in rt.get('ordered_nodes',[]):
            pb=str(n.get('provider_boundary','')).lower()
            if 'provider_execution_allowed=false' not in pb:
                issues.append(f'provider_boundary_missing_on_node:{n.get("node_id")}')
                provider_execution_disabled=False
    # scan runtime/proof outputs for false claims
    for p in (ROOT/'proofs').rglob('*.txt'):
        t=p.read_text(encoding='utf-8-sig', errors='ignore').lower()
        if 'providers_called=true' in t or 'media_created=true' in t or 'n8n_started=true' in t:
            false_claim_detected=True
            issues.append(f'false_execution_claim:{p}')
            break
    ok=len(issues)==0
    return {'pass':ok,'provider_execution_disabled':provider_execution_disabled,'unauthorized_provider_execution_blocked':unauthorized_blocked,'false_execution_claim_detected':false_claim_detected,'issues':issues}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--packet')
    ap.add_argument('--route', default='script_generation')
    ap.add_argument('--out')
    args=ap.parse_args()
    pp=Path(args.packet) if args.packet else None
    res=validate(pp,args.route)
    output(res,args.out)
    raise SystemExit(0 if res['pass'] else 1)

if __name__=='__main__':
    main()
