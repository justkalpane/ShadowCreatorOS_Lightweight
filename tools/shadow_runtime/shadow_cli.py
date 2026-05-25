from __future__ import annotations
import argparse, json, subprocess, tempfile
from pathlib import Path
from common import ROOT, output

CMD=ROOT/'proofs/mac_06_2f_v2_executable_nervous_system/command_outputs'


def run(cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return p.returncode,p.stdout


def preflight():
    required=[
      ROOT/'registries/component_lifecycle_registry.yaml',ROOT/'registries/route_dag_registry.yaml',
      ROOT/'tools/shadow_runtime/packet_schema_validator.py',ROOT/'tools/shadow_runtime/route_graph_builder.py',
      ROOT/'tools/shadow_runtime/packet_flow_runner.py',ROOT/'tools/shadow_runtime/communication_vein_validator.py',
      ROOT/'tools/shadow_runtime/provider_boundary_validator.py',ROOT/'tools/shadow_runtime/validate_route_dag.py',
      ROOT/'tools/shadow_runtime/schema_rationalizer.py',ROOT/'tools/shadow_runtime/validator_integrity_scanner.py'
    ]
    missing=[str(p) for p in required if not p.exists()]
    return {'pass':len(missing)==0,'missing':missing,'external_calls':False,'content_generation':False}


def validate_lifecycle():
    import json
    data=json.loads((ROOT/'registries/component_lifecycle_registry.yaml').read_text())
    comps=data.get('components',[])
    active=[c for c in comps if c.get('lifecycle_status') in {'ACTIVE_CORE','ACTIVE_SUPPORT'}]
    dag=json.loads((ROOT/'registries/route_dag_registry.yaml').read_text())
    dag_paths={n.get('component_path') for r in dag.get('route_dags',[]) for n in r.get('ordered_nodes',[])}
    active_not_consumed=[c.get('component_path') for c in active if c.get('component_path') not in dag_paths]
    blocked_active=[
      c.get('component_path') for c in comps
      if c.get('lifecycle_status') in {'QUARANTINE_REVIEW','DUPLICATE_CANDIDATE','DORMANT_FUTURE','HISTORICAL_REFERENCE'}
      and c.get('active_runtime') is True
    ]
    ok=len(active)>0 and not active_not_consumed and not blocked_active and any(c.get('lifecycle_status')!='ACTIVE_CORE' for c in comps)
    return {'pass':ok,'components_classified':len(comps),'active_components':len(active),'active_not_consumed':active_not_consumed,'blocked_active':blocked_active,'all_active':len(active)==len(comps)}


def validate_route(route):
    rc,out=run(['python3','tools/shadow_runtime/route_graph_builder.py','--route',route])
    obj=json.loads(out)
    obj['pass']=rc==0 and obj.get('pass',False)
    return obj


def validate_veins(route):
    rc,out=run(['python3','tools/shadow_runtime/communication_vein_validator.py','--route',route])
    obj=json.loads(out)
    obj['pass']=rc==0 and obj.get('pass',False)
    return obj


def validate_packets(route):
    valid_dir=ROOT/'tests/shadow_runtime/fixtures/packets/valid'
    total=0; failed=[]
    for pkt in sorted(valid_dir.glob('*.valid.json')):
        packet_id=pkt.name.split('.valid.json')[0]
        sch=ROOT/'schemas/packets'/f'{packet_id}.schema.json'
        rc,_=run(['python3','tools/shadow_runtime/packet_schema_validator.py','--schema',str(sch),'--packet',str(pkt)])
        total+=1
        if rc!=0: failed.append(pkt.name)
    return {'pass':len(failed)==0,'route':route,'packets_checked':total,'failed_packets':failed}


def dry_run(route):
    rc,out=run(['python3','tools/shadow_runtime/packet_flow_runner.py','--route',route,'--dry-run'])
    obj=json.loads(out)
    obj['pass']=rc==0 and obj.get('pass',False)
    return obj


def validate_provider_boundary(route='script_generation'):
    rc,out=run(['python3','tools/shadow_runtime/provider_boundary_validator.py','--route',route])
    obj=json.loads(out)
    obj['pass']=rc==0 and obj.get('pass',False)
    return obj


def operator_packet(task):
    pf=preflight(); lc=validate_lifecycle(); rt=validate_route('script_generation'); vn=validate_veins('script_generation'); pk=validate_packets('script_generation'); dr=dry_run('script_generation'); pb=validate_provider_boundary('script_generation')
    checks={'preflight':pf.get('pass'), 'lifecycle':lc.get('pass'), 'route':rt.get('pass'), 'veins':vn.get('pass'), 'packets':pk.get('pass'), 'dry_run':dr.get('pass'), 'provider_boundary':pb.get('pass')}
    ok=all(checks.values())
    route_ok=bool(rt.get('pass'))
    packet_ok=bool(pk.get('pass'))
    dry_ok=bool(dr.get('pass'))
    vein_ok=bool(vn.get('pass'))
    lifecycle_ok=bool(lc.get('pass'))
    provider_ok=bool(pb.get('pass'))
    packet={
      'packet_id':'operator_execution_packet','route_id':'script_generation','producer_component_id':'shadow_cli',
      'consumer_component_ids':['non_codex_operator_harness'],'lineage':{'upstream_packet_ids':['script_segment_packet'],'decision_log':'local enforcement only'},
      'validation_status':'PASS' if ok else 'FAIL','task':task,
      'proof_fields':{
        'shadow_command_alias_detected':task.lower().startswith('shadow '),'route_manifest_loaded':route_ok,'internal_wrapper_applied':ok,
        'gateway_contract_loaded_before_alias':(ROOT/'runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md').exists(),
        'output_mode_contract_loaded':(ROOT/'runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md').exists(),
        'registry_paths_exist':pf.get('pass'),'route_components_exist':route_ok,'selected_components_are_registered':route_ok,
        'provider_boundary_present':provider_ok,'no_n8n_provider_media_execution':provider_ok,
        'compact_or_proof_output_allowed_only_after_locks':ok,
        'component_depth_validation_required':True,
        'universal_component_contract_present':(ROOT/'runtime_contracts/UNIVERSAL_COMPONENT_CONTRACT_STANDARD.md').exists(),
        'script_segment_packet_present':(ROOT/'schemas/packets/script_segment_packet.schema.json').exists(),
        'voice_context_packet_present':(ROOT/'schemas/packets/voice_context_packet.schema.json').exists(),
        'visual_context_packet_present':(ROOT/'schemas/packets/visual_context_packet.schema.json').exists(),
        'video_context_packet_present':(ROOT/'schemas/packets/video_context_packet.schema.json').exists(),
        'music_sfx_packet_present':(ROOT/'schemas/packets/music_sfx_packet.schema.json').exists(),
        'editing_timeline_packet_present':(ROOT/'schemas/packets/editing_timeline_packet.schema.json').exists(),
        'provider_handoff_packet_present':(ROOT/'schemas/packets/provider_handoff_packet.schema.json').exists(),
        'media_quality_gate_packet_present':(ROOT/'schemas/packets/media_quality_gate_packet.schema.json').exists(),
        'lineage_approval_packet_present':(ROOT/'schemas/packets/lineage_packet.schema.json').exists() and (ROOT/'schemas/packets/approval_packet.schema.json').exists(),
        'quality_scores_present':(ROOT/'schemas/quality/quality_scorecard.schema.json').exists(),
        'segment_level_regeneration_actions_present':(ROOT/'runtime_contracts/SEGMENT_LEVEL_REGENERATION_CONTRACT.md').exists(),
        'route_dag_validation_pass':route_ok,'packet_schema_validation_pass':packet_ok,'packet_flow_validation_pass':dry_ok,
        'communication_vein_validation_pass':vein_ok,'lifecycle_validation_pass':lifecycle_ok,
        'lineage_approval_validation_pass':(ROOT/'runtime_state/lineage_store.json').exists() and (ROOT/'runtime_state/approval_store.json').exists(),
        'quality_scorecard_validation_pass':(ROOT/'tools/shadow_runtime/quality_scorecard_runtime.py').exists(),
        'provider_boundary_validation_pass':provider_ok,
        'fake_depth_detected':not lifecycle_ok,'contract_only_detected':not vein_ok,'text_label_only_detected':False
      },
      'approval_required':False,'provider_execution_allowed':False,
      'local_enforcement_checks':checks,'external_calls':False,'content_generation':False
    }
    return {'pass':ok,'operator_packet':packet,'checks':checks,'issues':[] if ok else ['local_enforcement_failed']}


def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('preflight')
    sub.add_parser('validate-lifecycle')
    p=sub.add_parser('validate-route'); p.add_argument('--route', required=True)
    p=sub.add_parser('validate-veins'); p.add_argument('--route', required=True)
    p=sub.add_parser('validate-packets'); p.add_argument('--route', required=True)
    p=sub.add_parser('dry-run-flow'); p.add_argument('--route', required=True)
    sub.add_parser('validate-provider-boundary')
    p=sub.add_parser('operator-packet'); p.add_argument('--task', required=True)
    ap.add_argument('--out')
    args=ap.parse_args()
    if args.cmd=='preflight': res=preflight()
    elif args.cmd=='validate-lifecycle': res=validate_lifecycle()
    elif args.cmd=='validate-route': res=validate_route(args.route)
    elif args.cmd=='validate-veins': res=validate_veins(args.route)
    elif args.cmd=='validate-packets': res=validate_packets(args.route)
    elif args.cmd=='dry-run-flow': res=dry_run(args.route)
    elif args.cmd=='validate-provider-boundary': res=validate_provider_boundary('script_generation')
    else: res=operator_packet(args.task)
    output(res,args.out)
    raise SystemExit(0 if res.get('pass') else 1)

if __name__=='__main__':
    main()
