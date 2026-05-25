
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path('/Users/apple/Documents/ShadowCreatorOS_Lightweight')/'tools/shadow_runtime'))
import route_graph_builder as rgb
import communication_vein_validator as cvv
root=Path('/Users/apple/Documents/ShadowCreatorOS_Lightweight')
dag=json.loads((root/'registries/route_dag_registry.yaml').read_text())
for r in dag['route_dags']:
    if r['route_id']=='script_generation':
        r['ordered_nodes'][0]['communication_pointer_ids']=['PTR_DOES_NOT_EXIST']
life=json.loads((root/'registries/component_lifecycle_registry.yaml').read_text())
rgb.load_route_dag_registry=lambda: dag
rgb.load_component_lifecycle=lambda: (life, {c['component_path']:c for c in life['components']}, {c['component_id']:c for c in life['components']})
cvv.build_route=rgb.build_route
res=cvv.validate('script_generation')
print(json.dumps(res))
sys.exit(0 if res.get('pass') else 1)
