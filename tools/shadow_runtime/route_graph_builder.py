from __future__ import annotations
import argparse, json
from pathlib import Path
from common import ROOT, load_route_dag_registry, load_component_lifecycle, parse_pointer_registry, output


PLACEHOLDER_VALUES = {"", "placeholder", "tbd", "unknown", "unknown_needs_review", "none", "null"}


def _bad_value(value):
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip().lower() in PLACEHOLDER_VALUES
    return False


def _load_dag_override(path):
    if not path:
        return load_route_dag_registry()
    return json.loads(Path(path).read_text(encoding="utf-8-sig", errors="replace"))


def _load_lifecycle_override(path):
    if not path:
        return load_component_lifecycle()
    data = json.loads(Path(path).read_text(encoding="utf-8-sig", errors="replace"))
    by_path = {c["component_path"]: c for c in data.get("components", []) if "component_path" in c}
    by_id = {c["component_id"]: c for c in data.get("components", []) if "component_id" in c}
    return data, by_path, by_id


def build_route(route_id: str, dag_path: str | None = None, lifecycle_path: str | None = None):
    dag=_load_dag_override(dag_path)
    route=next((r for r in dag.get('route_dags',[]) if r.get('route_id')==route_id), None)
    issues=[]
    if not route:
        return {'pass':False,'route_id':route_id,'issues':['route_not_found']}
    if "ordered_nodes" not in route:
        return {'pass':False,'route_id':route_id,'issues':['ordered_nodes_missing']}
    ordered=route.get('ordered_nodes')
    if ordered is None:
        return {'pass':False,'route_id':route_id,'issues':['ordered_nodes_null']}
    if not isinstance(ordered, list):
        return {'pass':False,'route_id':route_id,'issues':['ordered_nodes_not_list']}
    if not ordered:
        return {'pass':False,'route_id':route_id,'issues':['ordered_nodes_empty']}
    _, by_path, _ = _load_lifecycle_override(lifecycle_path)
    ptrs=parse_pointer_registry()
    produced=set(route.get('initial_packets',[]))
    node_ids=[n.get('node_id') for n in ordered if isinstance(n, dict)]
    if len(node_ids) != len(set(node_ids)):
        issues.append('duplicate_node_ids')
    for i,node in enumerate(ordered):
        if not isinstance(node, dict):
            issues.append(f'node_not_object:{i}')
            continue
        for key in ['node_id','component_id','component_path','component_layer']:
            if _bad_value(node.get(key)):
                issues.append(f'placeholder_or_missing_{key}:{i}')
        p=node.get('component_path','')
        if p not in by_path:
            issues.append(f'component_not_in_lifecycle:{p}')
        if p and not (ROOT / p).exists():
            issues.append(f'component_path_missing:{p}')
        if p not in by_path:
            continue
        st=by_path[p].get('lifecycle_status')
        if st not in {'ACTIVE_CORE','ACTIVE_SUPPORT'}:
            issues.append(f'invalid_lifecycle:{p}:{st}')
        if not isinstance(node.get('required_input_packets'), list) or not node.get('required_input_packets'):
            issues.append(f'required_input_packets_missing:{node.get("node_id")}')
        if not isinstance(node.get('emitted_output_packets'), list) or not node.get('emitted_output_packets'):
            issues.append(f'emitted_output_packets_missing:{node.get("node_id")}')
        for req in node.get('required_input_packets',[]):
            if req not in produced:
                issues.append(f'packet_continuity_missing:{node.get("node_id")}:{req}')
            if _bad_value(req):
                issues.append(f'placeholder_input_packet:{node.get("node_id")}')
        if not isinstance(node.get('communication_pointer_ids'), list) or not node.get('communication_pointer_ids'):
            issues.append(f'communication_pointer_ids_missing:{node.get("node_id")}')
        for pid in node.get('communication_pointer_ids',[]):
            if pid not in ptrs:
                issues.append(f'pointer_missing:{pid}')
            if _bad_value(pid):
                issues.append(f'placeholder_pointer_id:{node.get("node_id")}')
        if not node.get('validator_rules'):
            issues.append(f'validator_rules_missing:{node.get("node_id")}')
        if not node.get('quality_gates'):
            issues.append(f'quality_gates_missing:{node.get("node_id")}')
        if _bad_value(node.get('provider_boundary')):
            issues.append(f'provider_boundary_missing:{node.get("node_id")}')
        for outp in node.get('emitted_output_packets',[]):
            if _bad_value(outp):
                issues.append(f'placeholder_output_packet:{node.get("node_id")}')
            produced.add(outp)
        nxt=node.get('next_nodes',[])
        if not isinstance(nxt, list):
            issues.append(f'next_nodes_not_list:{node.get("node_id")}')
            nxt=[]
        for target in nxt:
            if target not in node_ids:
                issues.append(f'next_node_target_missing:{node.get("node_id")}->{target}')
        if i < len(ordered)-1:
            if ordered[i+1].get('node_id') not in nxt:
                issues.append(f'next_node_link_missing:{node.get("node_id")}->{ordered[i+1].get("node_id")}')
    return {'pass':len(issues)==0,'route_id':route_id,'issues':issues,'ordered_nodes':ordered,'packets_produced':sorted(produced)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--route', required=True)
    ap.add_argument('--dag-file')
    ap.add_argument('--lifecycle-file')
    ap.add_argument('--out')
    args=ap.parse_args()
    result=build_route(args.route,args.dag_file,args.lifecycle_file)
    output(result,args.out)
    raise SystemExit(0 if result['pass'] else 1)

if __name__=='__main__':
    main()
