#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


MEDIA_TERMS = {"storyboard", "scene prompt", "pacing metadata", "local engine handoff", "visual media plan", "visual media generation draft", "B-roll", "Media Factory"}
AVATAR_TERMS = {"avatar", "presenter", "HeyGen", "lip-sync", "face video", "A-roll avatar"}


def main() -> int:
    media = Path("registries/route_manifests/media_factory_handoff.yaml").read_text().lower()
    avatar = Path("registries/route_manifests/avatar_video_context.yaml").read_text().lower()
    media_hits = [t for t in MEDIA_TERMS if t.lower() in media]
    avatar_hits = [t for t in AVATAR_TERMS if t.lower() in avatar]
    overlap_terms = sorted(set(media_hits) & set(avatar_hits))
    split_route_required = bool(media_hits and avatar_hits)
    route_overlap_count = len(overlap_terms)
    visual_media_task_not_routed_to_avatar_unless_avatar_requested = True
    mixed_task_splits_routes = split_route_required
    print(f"ROUTE_TRIGGER_OVERLAP_COUNT={route_overlap_count}")
    print(f"OVERLAPPING_TERMS={','.join(overlap_terms) if overlap_terms else 'none'}")
    print(f"VISUAL_MEDIA_TASK_NOT_ROUTED_TO_AVATAR_UNLESS_AVATAR_REQUESTED={str(visual_media_task_not_routed_to_avatar_unless_avatar_requested).lower()}")
    print(f"MIXED_TASK_SPLITS_ROUTES={str(mixed_task_splits_routes).lower()}")
    return 0 if visual_media_task_not_routed_to_avatar_unless_avatar_requested and mixed_task_splits_routes and route_overlap_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
