from __future__ import annotations
import argparse, json
from pathlib import Path
from common import ROOT, output

STATE=ROOT/'runtime_state'
LFILE=STATE/'lineage_store.json'
AFILE=STATE/'approval_store.json'


def init_state():
    STATE.mkdir(parents=True,exist_ok=True)
    if not LFILE.exists(): LFILE.write_text(json.dumps({'lineages':[]},indent=2))
    if not AFILE.exists(): AFILE.write_text(json.dumps({'approvals':[]},indent=2))
    ok=LFILE.exists() and AFILE.exists()
    return {'pass':ok,'lineage_store':str(LFILE),'approval_store':str(AFILE)}


def add_lineage(route, packet):
    init_state()
    data=json.loads(LFILE.read_text())
    rec={'route_id':route,'packet_id':packet,'component_id':'shadow_cli','upstream_packet_ids':[],'downstream_packet_ids':[]}
    data['lineages'].append(rec)
    LFILE.write_text(json.dumps(data,indent=2))
    written=json.loads(LFILE.read_text())
    return {'pass':rec in written.get('lineages',[]),'added':rec}


def request_approval(route, action, segment_id):
    init_state()
    data=json.loads(AFILE.read_text())
    rec={'route_id':route,'action':action,'segment_id':segment_id,'state':'REQUESTED','approval_required':True,'provider_execution_allowed':False}
    data['approvals'].append(rec)
    AFILE.write_text(json.dumps(data,indent=2))
    written=json.loads(AFILE.read_text())
    return {'pass':rec in written.get('approvals',[]),'approval_request':rec}


def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('init')
    p1=sub.add_parser('add-lineage'); p1.add_argument('--route',required=True); p1.add_argument('--packet',required=True)
    p2=sub.add_parser('request-approval'); p2.add_argument('--route',required=True); p2.add_argument('--action',required=True); p2.add_argument('--segment-id',required=True)
    ap.add_argument('--out')
    args=ap.parse_args()
    if args.cmd=='init': res=init_state()
    elif args.cmd=='add-lineage': res=add_lineage(args.route,args.packet)
    else: res=request_approval(args.route,args.action,args.segment_id)
    output(res,args.out)
    raise SystemExit(0 if res.get('pass') else 1)

if __name__=='__main__':
    main()
