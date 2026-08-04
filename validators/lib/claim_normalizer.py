#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from typing import Iterable


URL_RE = re.compile(r"https?://[^\s)>\"']+")
TRUNCATION_RE = re.compile(r"<truncated[^>]*>", re.IGNORECASE)
KV_RE = re.compile(r"^\s*(?:[-*]\s*)?`?([A-Za-z0-9_.\-/]+)`?\s*=\s*(.+?)\s*$")
COLON_RE = re.compile(r"^\s*(?:[-*]\s*)?`?([A-Za-z0-9_.\-/]+)`?\s*:\s*(.+?)\s*$")

PASS_STATUS_KEYS = [
    "status",
    "final_status",
    "FINAL_PROOF_STATUS",
    "validation_result",
    "source_research_lock_status",
    "consumption_lock_status",
    "duration_fit_status",
    "quality_lock_status",
    "governance_lock_status",
    "production_pass_allowed",
    "final_deliverable_generated",
    "route_scope_status",
]

WEB_USED_KEYS = [
    "web_used",
    "web_access_used",
    "web_search_conducted",
    "real_time_sources_used",
]

SOURCE_URL_COUNT_KEYS = [
    "source_ledger_urls_count",
    "ledger_urls_count",
    "url_count",
    "urls_count",
]

ARTIFACT_PRESENT_KEYS = [
    "artifacts_present",
    "artifact_present",
    "media_artifacts_claimed",
]

PROOF_PRESENT_KEYS = [
    "proof_json_present",
    "proof_present",
    "production_proof_present",
]

ROUTE_MODE_ALIASES = {
    "standard_script": "INVALID_STANDARD_SCRIPT",
    "script": "script_only",
    "script_only": "script_only",
    "visual_media_generator_draft": "script_plus_visual_generation_draft",
    "visual_media_generation_draft": "script_plus_visual_generation_draft",
}


def normalize_key(key: object) -> str:
    return str(key or "").strip().strip("`").lower()


def clean_value(value: object) -> str:
    return str(value or "").strip().strip("`").strip()


def _append(claims: dict[str, list[str]], key: object, value: object) -> None:
    normalized = normalize_key(key)
    if normalized:
        claims.setdefault(normalized, []).append(clean_value(value))


def _parse_table_row(line: str, claims: dict[str, list[str]]) -> bool:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return False
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if len(cells) < 2:
        return False
    if all(set(cell) <= {"-", ":"} for cell in cells if cell):
        return True
    key, value = cells[0], cells[1]
    if normalize_key(key) in {"key", "field", "claim", "property", "name", "layer"}:
        return True
    if key and value:
        _append(claims, key, value)
    return True


def parse_claims(text: str) -> dict[str, list[str]]:
    claims: dict[str, list[str]] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if _parse_table_row(line, claims):
            continue
        match = KV_RE.match(line) or COLON_RE.match(line)
        if match:
            _append(claims, match.group(1), match.group(2))
    return claims


def all_values(claims: dict[str, list[str]], keys: Iterable[str]) -> list[str]:
    values: list[str] = []
    for key in keys:
        values.extend(claims.get(normalize_key(key), []))
    return values


def first_value(claims: dict[str, list[str]], keys: list[str], default: str = "") -> str:
    values = all_values(claims, keys)
    return values[0] if values else default


def _token(value: object) -> str:
    text = clean_value(value).lower()
    return re.sub(r"[^a-z0-9_ -].*$", "", text).strip()


def is_truthy(value: object) -> bool:
    return _token(value) in {"true", "yes", "1", "pass", "passed", "ready", "present", "complete", "completed"}


def is_falsey(value: object) -> bool:
    return _token(value) in {"false", "no", "0", "fail", "failed", "blocked", "missing", "absent", "incomplete"}


def is_pass_value(value: object) -> bool:
    token = _token(value)
    return token in {"pass", "passed", "true", "ready", "complete", "completed", "allowed"}


def is_blocked_value(value: object) -> bool:
    token = _token(value)
    return token in {"blocked", "fail", "failed", "false", "needs_confirmation", "needs_user_approval"}


def has_pass_claim(claims: dict[str, list[str]], keys: list[str] | None = None) -> bool:
    target_keys = keys or PASS_STATUS_KEYS
    return any(is_pass_value(value) for value in all_values(claims, target_keys))


def has_blocked_claim(claims: dict[str, list[str]], keys: list[str] | None = None) -> bool:
    target_keys = keys or PASS_STATUS_KEYS
    return any(is_blocked_value(value) for value in all_values(claims, target_keys))


def count_urls(text: str) -> int:
    return len(URL_RE.findall(text))


def truncation_markers(text: str) -> list[str]:
    return TRUNCATION_RE.findall(text)


def has_truncation_marker(text: str) -> bool:
    return bool(truncation_markers(text))


def normalize_task_mode(value: str) -> str:
    token = clean_value(value).lower()
    return ROUTE_MODE_ALIASES.get(token, token)

