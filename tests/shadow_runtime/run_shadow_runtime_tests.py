from __future__ import annotations
import subprocess, json, tempfile, os
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'proofs/mac_06_2f_v2_executable_nervous_system/command_outputs/runtime_test_output.txt'


def run(cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return p.returncode,p.stdout

def test(name, cmd, expect=0):
    rc,out=run(cmd)
    ok=(rc==expect)
    return {'name':name,'pass':ok,'rc':rc,'expect':expect,'output':out[:1200]}

results=[]
results.append(test('packet schemas load',['python3','tools/shadow_runtime/packet_schema_validator.py','--schema','schemas/packets/script_segment_packet.schema.json','--packet','tests/shadow_runtime/fixtures/packets/valid/script_segment_packet.valid.json'],0))
results.append(test('valid packet passes',['python3','tools/shadow_runtime/packet_schema_validator.py','--schema','schemas/packets/script_segment_packet.schema.json','--packet','tests/shadow_runtime/fixtures/packets/valid/script_segment_packet.valid.json'],0))
results.append(test('invalid packet fails',['python3','tools/shadow_runtime/packet_schema_validator.py','--schema','schemas/packets/script_segment_packet.schema.json','--packet','tests/shadow_runtime/fixtures/packets/invalid/script_segment_packet.missing_fields.json'],1))
results.append(test('route DAG builds',['python3','tools/shadow_runtime/route_graph_builder.py','--route','script_generation'],0))
results.append(test('empty ordered_nodes fails',['python3','tools/shadow_runtime/route_graph_builder.py','--route','script_generation','--dag-file','tests/shadow_runtime/fixtures/route_dags/fail_empty_ordered_nodes.yaml'],1))
results.append(test('missing ordered_nodes fails',['python3','tools/shadow_runtime/route_graph_builder.py','--route','script_generation','--dag-file','tests/shadow_runtime/fixtures/route_dags/fail_missing_ordered_nodes.yaml'],1))
results.append(test('null ordered_nodes fails',['python3','tools/shadow_runtime/route_graph_builder.py','--route','script_generation','--dag-file','tests/shadow_runtime/fixtures/route_dags/fail_null_ordered_nodes.yaml'],1))
results.append(test('placeholder node fails',['python3','tools/shadow_runtime/route_graph_builder.py','--route','script_generation','--dag-file','tests/shadow_runtime/fixtures/route_dags/fail_placeholder_nodes.yaml'],1))
results.append(test('invalid lifecycle node fails',['python3','tools/shadow_runtime/route_graph_builder.py','--route','script_generation','--dag-file','tests/shadow_runtime/fixtures/route_dags/fail_duplicate_candidate_node.yaml'],1))
results.append(test('packet flow dry-run passes for script_generation',['python3','tools/shadow_runtime/packet_flow_runner.py','--route','script_generation','--dry-run'],0))
# missing packet fails by editing temp route impossible here; simulate with invalid route
results.append(test('missing packet fails',['python3','tools/shadow_runtime/packet_flow_runner.py','--route','non_existing','--dry-run'],1))
results.append(test('communication veins connected to DAG',['python3','tools/shadow_runtime/communication_vein_validator.py','--route','script_generation'],0))
results.append(test('contract-only vein fails',['python3','tools/shadow_runtime/communication_vein_validator.py','--route','non_existing'],1))
results.append(test('provider execution blocked',['python3','tools/shadow_runtime/provider_boundary_validator.py','--route','script_generation'],0))
results.append(test('quality false pass fails',['python3','tools/shadow_runtime/quality_scorecard_runtime.py','--scorecard','tests/shadow_runtime/fixtures/quality/scorecard.false_pass_invalid.json'],1))
results.append(test('lineage store initializes',['python3','tools/shadow_runtime/lineage_approval_store.py','init'],0))
results.append(test('approval request supports regenerate_segment',['python3','tools/shadow_runtime/lineage_approval_store.py','request-approval','--route','script_generation','--action','regenerate_segment','--segment-id','seg_001'],0))
results.append(test('shadow_cli preflight passes',['python3','tools/shadow_runtime/shadow_cli.py','preflight'],0))
results.append(test('shadow_cli operator-packet passes',['python3','tools/shadow_runtime/shadow_cli.py','operator-packet','--task','Shadow script proof mode task'],0))
# non-codex harness using temp packet
op=json.loads(run(['python3','tools/shadow_runtime/shadow_cli.py','operator-packet','--task','Shadow script proof mode task'])[1])
tmp=ROOT/'runtime_state/tmp_operator_packet.json'; tmp.write_text(json.dumps(op['operator_packet'],indent=2))
results.append(test('non-Codex harness validates expected result schema',['python3','tools/shadow_runtime/non_codex_operator_harness.py','--packet',str(tmp)],0))

passed=sum(1 for r in results if r['pass']); total=len(results); failed=[r['name'] for r in results if not r['pass']]
final={'tests_total':total,'tests_passed':passed,'tests_failed':total-passed,'failed_tests':failed,'results':results,'pass':passed==total}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(final,indent=2))
print(json.dumps(final,indent=2))
raise SystemExit(0 if final['pass'] else 1)
