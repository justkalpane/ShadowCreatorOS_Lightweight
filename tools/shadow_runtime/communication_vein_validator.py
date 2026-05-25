from __future__ import annotations
import argparse
from common import parse_pointer_registry, output
from route_graph_builder import build_route


def validate(route_id: str):
    graph=build_route(route_id)
    ptrs=parse_pointer_registry()
    issues=[]; contract_only=0; validated=0
    if not graph.get('pass'):
        return {'pass':False,'route_id':route_id,'issues':['route_graph_invalid']+graph.get('issues',[]),'contract_only_veins_remaining':None,'dag_connected_veins':0}
    for node in graph.get('ordered_nodes',[]):
        for pid in node.get('communication_pointer_ids',[]):
            if pid not in ptrs:
                issues.append(f'missing_pointer:{pid}')
                continue
            rec=ptrs[pid]
            required=['source_component_layer','target_component_layer','trigger_condition','required_input_packet','required_output_packet','validation_rule','fallback_behavior','lineage_required']
            missing=[k for k in required if not str(rec.get(k,'')).strip()]
            if missing:
                contract_only += 1
                issues.append(f'contract_only_pointer:{pid}:{"|".join(missing)}')
            validated += 1
    return {'pass':len(issues)==0,'route_id':route_id,'veins_validated':validated,'contract_only_veins_remaining':contract_only,'dag_connected_veins':validated-contract_only,'issues':issues}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--route', required=True)
    ap.add_argument('--out')
    args=ap.parse_args()
    result=validate(args.route)
    output(result,args.out)
    raise SystemExit(0 if result['pass'] else 1)

if __name__=='__main__':
    main()
