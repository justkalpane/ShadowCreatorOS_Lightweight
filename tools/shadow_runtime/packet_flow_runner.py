from __future__ import annotations
import argparse, json
from pathlib import Path
from common import ROOT, output, schema_for_packet
from route_graph_builder import build_route
from packet_schema_validator import validate_packet


def _mk_packet(packet_name, route_id, producer):
    p={
      'packet_id':packet_name,'route_id':route_id,'producer_component_id':producer,
      'consumer_component_ids':['next_node'],'lineage':{'upstream':[]},'validation_status':'PASS'
    }
    # fill known required extras
    if packet_name=='topic_intake_packet': p.update({'topic':'x','audience':'x','intent':'x'})
    if packet_name=='trend_signal_packet': p.update({'signals':['signal'], 'freshness_date':'2026-05-25'})
    if packet_name=='source_evidence_packet': p.update({'sources':['https://example.com'], 'claims':['claim']})
    if packet_name=='research_brief_packet': p.update({'brief':'x','source_evidence_refs':['x']})
    if packet_name=='script_strategy_packet': p.update({'strategy':'x','duration_target_sec':60})
    if packet_name=='script_v1_packet': p.update({'script_text':'x','hook':'x'})
    if packet_name=='debate_critique_packet': p.update({'critique_points':['point'], 'line_refs':['L1']})
    if packet_name=='refinement_delta_packet': p.update({'changes':['change'], 'rationale':'improve clarity'})
    if packet_name=='final_script_packet': p.update({'final_script_text':'final', 'cta':'comment'})
    if packet_name=='script_segment_packet': p.update({'segments':['x'],'total_duration_sec':60})
    if packet_name=='voice_context_packet': p.update({'voice_persona':'neutral', 'pace':'medium', 'emotion_map':'steady'})
    if packet_name=='visual_context_packet': p.update({'style_bible':'clean', 'scene_prompts':['scene']})
    if packet_name=='video_context_packet': p.update({'scene_plan':['scene_1'], 'camera_moves':['static']})
    if packet_name=='music_sfx_packet': p.update({'music_mood':'uplifting', 'sfx_cues':['whoosh']})
    if packet_name=='editing_timeline_packet': p.update({'timeline_segments':['seg_1'], 'cut_points':['00:03']})
    if packet_name in {'voice_context_packet','visual_context_packet','video_context_packet','music_sfx_packet','editing_timeline_packet'}:
        p.update({'provider_execution_allowed':False,'approval_required':True})
    if packet_name=='provider_handoff_packet':
        p.update({
            'provider_type':'planning_only',
            'typed_input':'script_segment_packet',
            'provider_execution_allowed':False,
            'approval_required':True
        })
    if packet_name=='media_quality_gate_packet': p.update({'scores':{'script_score':80},'final_pass_fail':False})
    if packet_name=='lineage_packet': p.update({'upstream_packet_ids':['x'],'decision_log':'x'})
    if packet_name=='approval_packet': p.update({'approval_action':'review','approved_by':'user'})
    return p


def run_flow(route_id: str):
    graph=build_route(route_id)
    trace={'route_id':route_id,'pass':False,'steps':[],'issues':[]}
    if not graph.get('pass'):
        trace['issues']=['route_graph_invalid']+graph.get('issues',[])
        return trace
    available=set(['topic_intake_packet'])
    temp_dir=ROOT/'runtime_state/tmp_packets'
    temp_dir.mkdir(parents=True,exist_ok=True)
    for node in graph.get('ordered_nodes',[]):
        nid=node.get('node_id')
        missing=[r for r in node.get('required_input_packets',[]) if r not in available]
        if missing:
            trace['issues'].append(f'missing_input:{nid}:{"|".join(missing)}')
            break
        emitted=[]
        for outp in node.get('emitted_output_packets',[]):
            pkt=_mk_packet(outp, route_id, node.get('component_id','component'))
            pkt_path=temp_dir/f'{nid}.{outp}.json'
            pkt_path.write_text(json.dumps(pkt,indent=2))
            sch=schema_for_packet(outp)
            if not sch.exists():
                trace['issues'].append(f'missing_schema:{outp}')
                continue
            v=validate_packet(sch,pkt_path)
            if not v['pass']:
                trace['issues'].append(f'invalid_packet:{nid}:{outp}:{"|".join(v["errors"])}')
            else:
                available.add(outp)
                emitted.append(outp)
        trace['steps'].append({'node_id':nid,'component_id':node.get('component_id'),'consumed':node.get('required_input_packets',[]),'emitted':emitted})
    trace['packets_available']=sorted(available)
    trace['pass']=len(trace['issues'])==0
    return trace


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--route', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--out')
    args=ap.parse_args()
    result=run_flow(args.route)
    result['mode']='dry-run' if args.dry_run else 'run'
    output(result,args.out)
    raise SystemExit(0 if result['pass'] else 1)

if __name__=='__main__':
    main()
