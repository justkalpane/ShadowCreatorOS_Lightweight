from __future__ import annotations
import argparse, json
from pathlib import Path
from common import output

CRITICAL=['script_score','hook_score','retention_score','voice_score','visual_score','video_score','audio_score','editing_score','platform_score','lineage_score']
THRESHOLD=70


def validate(score_path: Path):
    data=json.loads(score_path.read_text(encoding='utf-8-sig', errors='replace'))
    missing=[k for k in CRITICAL+['final_pass_fail','approval_readiness_score','provider_handoff_score','emotional_score'] if k not in data]
    low=[k for k in CRITICAL if isinstance(data.get(k),(int,float)) and data[k] < THRESHOLD]
    errors=[]
    if missing: errors.append('missing_fields:'+','.join(missing))
    if low: errors.append('critical_below_threshold:'+','.join(low))
    if data.get('final_pass_fail') is True and low:
        errors.append('false_pass_with_low_critical_scores')
    status='PASS' if not errors else 'FAIL'
    return {'pass':status=='PASS','status':status,'errors':errors,'low_scores':low,'threshold':THRESHOLD}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scorecard', required=True)
    ap.add_argument('--out')
    args=ap.parse_args()
    res=validate(Path(args.scorecard))
    output(res,args.out)
    raise SystemExit(0 if res['pass'] else 1)

if __name__=='__main__':
    main()
