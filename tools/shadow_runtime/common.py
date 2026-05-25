from __future__ import annotations
import json,re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))


def output(obj, out_path=None):
    text=json.dumps(obj, indent=2, sort_keys=True)
    if out_path:
        p=Path(out_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    print(text)


def load_component_lifecycle():
    p=ROOT/'registries/component_lifecycle_registry.yaml'
    data=load_json(p)
    by_path={c['component_path']:c for c in data.get('components',[])}
    by_id={c['component_id']:c for c in data.get('components',[])}
    return data, by_path, by_id


def load_route_dag_registry():
    p=ROOT/'registries/route_dag_registry.yaml'
    return load_json(p)


def load_pointer_registry_text():
    p=ROOT/'registries/communication_pointer_registry.yaml'
    return p.read_text(encoding='utf-8-sig', errors='replace') if p.exists() else ''


def parse_pointer_registry():
    text=load_pointer_registry_text()
    recs={}
    cur=None
    for line in text.splitlines():
        m=re.match(r'\s*-\s*pointer_id\s*:\s*([^\s#]+)', line)
        if m:
            cur={'pointer_id':m.group(1).strip().strip('"')}
            recs[cur['pointer_id']]=cur
            continue
        if cur:
            m2=re.match(r'\s+([A-Za-z0-9_]+)\s*:\s*(.*)$', line)
            if m2:
                cur[m2.group(1)] = m2.group(2).strip().strip('"')
    return recs


def schema_for_packet(packet_name: str):
    return ROOT/'schemas/packets'/f"{packet_name}.schema.json"
