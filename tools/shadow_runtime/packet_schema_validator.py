from __future__ import annotations
import argparse, json
from pathlib import Path
from common import output


def _check_type(val, t):
    if t=='string': return isinstance(val, str)
    if t=='array': return isinstance(val, list)
    if t=='object': return isinstance(val, dict)
    if t=='boolean': return isinstance(val, bool)
    if t=='number': return isinstance(val, (int,float)) and not isinstance(val, bool)
    return True


def validate_packet(schema_path: Path, packet_path: Path):
    schema=json.loads(schema_path.read_text(encoding='utf-8-sig', errors='replace'))
    packet=json.loads(packet_path.read_text(encoding='utf-8-sig', errors='replace'))
    errors=[]
    for req in schema.get('required',[]):
        if req not in packet:
            errors.append(f"missing_required:{req}")
    props=schema.get('properties',{})
    for k,v in packet.items():
        if k not in props and not schema.get('additionalProperties',True):
            errors.append(f"unknown_property:{k}")
            continue
        if k in props:
            t=props[k].get('type')
            if t and not _check_type(v,t):
                errors.append(f"invalid_type:{k}:{t}")
            if 'const' in props[k] and v != props[k]['const']:
                errors.append(f"const_violation:{k}:{props[k]['const']}")
            if 'enum' in props[k] and v not in props[k]['enum']:
                errors.append(f"enum_violation:{k}")
    if packet.get('provider_execution_allowed') is True and (
        not packet.get('approval_required')
        or packet.get('approval_authorized') is not True
        or not packet.get('approval_packet_id')
    ):
        errors.append('provider_execution_allowed_without_explicit_approval_packet')
    ok=not errors
    return {'validator':'packet_schema_validator','schema':str(schema_path),'packet':str(packet_path),'pass':ok,'errors':errors}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--schema', required=True)
    ap.add_argument('--packet', required=True)
    ap.add_argument('--out')
    args=ap.parse_args()
    result=validate_packet(Path(args.schema), Path(args.packet))
    output(result, args.out)
    raise SystemExit(0 if result['pass'] else 1)

if __name__=='__main__':
    main()
