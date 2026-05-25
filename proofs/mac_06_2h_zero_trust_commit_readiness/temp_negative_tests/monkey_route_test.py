
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path('/Users/apple/Documents/ShadowCreatorOS_Lightweight')/'tools/shadow_runtime'))
import route_graph_builder as rgb
root=Path('/Users/apple/Documents/ShadowCreatorOS_Lightweight')
dag=json.loads((root/'registries/route_dag_registry.yaml').read_text())
life=json.loads((root/'registries/component_lifecycle_registry.yaml').read_text())

first=next(r for r in dag['route_dags'] if r['route_id']=='script_generation')['ordered_nodes'][0]['component_path']
for c in life['components']:
    if c['component_path']==first: c['lifecycle_status']='QUARANTINE_REVIEW'

rgb.load_route_dag_registry=lambda: dag
rgb.load_component_lifecycle=lambda: (life, {c['component_path']:c for c in life['components']}, {c['component_id']:c for c in life['components']})
res=rgb.build_route('script_generation')
print(json.dumps(res))
sys.exit(0 if res.get('pass') else 1)
