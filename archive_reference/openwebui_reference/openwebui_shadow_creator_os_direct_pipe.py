"""
title: Shadow Creator OS Direct Router
author: ShadowEmpire
version: 1.0.0
required_open_webui_version: 0.9.4
description: Deterministic Open WebUI pipe for Shadow Creator OS. User surface is Open WebUI on localhost:3000; internal Operator API routing is handled automatically.
"""

import json
import re
import time
from pathlib import Path
from typing import Optional, Any

import requests
from pydantic import BaseModel, Field

from open_webui.utils.misc import get_last_user_message


class Pipe:
    class Valves(BaseModel):
        OPERATOR_BASE_URL: str = Field(default="http://localhost:5002")
        REQUEST_TIMEOUT_SEC: int = Field(default=30)
        POLL_INTERVAL_SEC: float = Field(default=2.0)
        POLL_MAX_ATTEMPTS: int = Field(default=15)
        DEFAULT_ROUTE_ID: str = Field(default="ROUTE_PHASE1_STANDARD")
        DEFAULT_MODE: str = Field(default="creator")
        DATA_ROOT: str = Field(default="C:/ShadowEmpire-Git_Restore_01/data")

    def __init__(self):
        self.type = "pipe"
        self.name = "Shadow Creator OS Direct"
        self.valves = self.Valves()

    def _api(self, method: str, endpoint: str, body: Optional[dict] = None) -> dict:
        url = f"{self.valves.OPERATOR_BASE_URL}{endpoint}"
        try:
            if method.upper() == "GET":
                response = requests.get(url, timeout=self.valves.REQUEST_TIMEOUT_SEC)
            else:
                response = requests.post(url, json=body or {}, timeout=self.valves.REQUEST_TIMEOUT_SEC)

            text = response.text or ""
            payload = {}
            if text:
                try:
                    payload = response.json()
                except Exception:
                    payload = {"raw_text": text}

            payload["_http_status"] = response.status_code
            if response.status_code >= 400:
                payload.setdefault("status", "FAILED")
                payload.setdefault("error", f"HTTP {response.status_code}")
            return payload
        except Exception as exc:
            return {
                "status": "FAILED_CONTROLLED",
                "error_code": "OPERATOR_API_UNAVAILABLE",
                "error_class": "CONNECTION_RESET_10054" if "10054" in str(exc) else "OPERATOR_API_UNAVAILABLE",
                "error": str(exc),
                "operator_route_reached": False,
                "n8n_route_reached": False,
                "wf001_dossier_created": False,
                "wf010_reached": False,
                "provider_used": "gemini",
                "model_used": "gemini-2.5-flash",
                "cloud_provider_used": False,
                "content_generation_executed": False,
                "controlled_failure": True,
                "runtime_error_packet_count": 1,
                "message": "Operator API is temporarily unavailable. Retry once service stabilizes.",
                "_http_status": 0,
            }

    def _extract_dossier_id(self, text: str) -> Optional[str]:
        if not text:
            return None
        match = re.search(r"(DOSSIER-[A-Z0-9-]+)", text, flags=re.IGNORECASE)
        return match.group(1).upper() if match else None

    def _extract_director_requested(self, text: str) -> Optional[str]:
        if not text:
            return None
        directors = [
            "chanakya", "krishna", "narada", "vyasa", "ravana",
            "shakuni", "saraswati", "agni", "yama", "kubera",
            "ganesha", "vayu", "aruna",
        ]
        lower = text.lower()
        for d in directors:
            if re.search(rf"\\b{re.escape(d)}\\b", lower):
                return d.title()
        return None

    def _latest_dossier_from_index(self) -> Optional[str]:
        try:
            idx_path = Path(self.valves.DATA_ROOT) / "se_dossier_index.json"
            if not idx_path.exists():
                return None
            doc = json.loads(idx_path.read_text(encoding="utf-8"))
            rows = doc.get("records") or doc.get("dossiers") or []
            if not rows:
                return None
            rows = [r for r in rows if r.get("dossier_id")]
            if not rows:
                return None
            rows.sort(key=lambda r: r.get("created_at", ""))
            return rows[-1]["dossier_id"]
        except Exception:
            return None

    def _extract_text_snippet(self, payload: Any, keyword_hints: list[str]) -> Optional[str]:
        best = None

        def walk(node: Any, parent_key: str = ""):
            nonlocal best
            if best:
                return
            if isinstance(node, dict):
                for k, v in node.items():
                    if isinstance(v, str) and any(h in k.lower() for h in keyword_hints):
                        val = v.strip()
                        if len(val) > 20:
                            best = val
                            return
                    if isinstance(v, list) and any(h in k.lower() for h in keyword_hints):
                        parts = [str(x).strip() for x in v if isinstance(x, str) and str(x).strip()]
                        if parts:
                            best = "\n- " + "\n- ".join(parts[:4])
                            return
                    walk(v, k.lower())
            elif isinstance(node, list):
                for item in node:
                    walk(item, parent_key)
            elif isinstance(node, str):
                val = node.strip()
                if len(val) > 20 and any(h in parent_key for h in keyword_hints):
                    best = val

        walk(payload)
        return best

    def _packet_families(self, outputs: dict) -> list[str]:
        families = []
        for packet in outputs.get("packets", []) or []:
            fam = packet.get("artifact_family")
            if fam and fam not in families:
                families.append(fam)
        return families

    def _format_controlled_failure(self, payload: dict, fallback_dossier_id: Optional[str] = None) -> str:
        dossier_id = payload.get("dossier_id") or fallback_dossier_id
        error_code = payload.get("error_code") or payload.get("status") or "OPERATOR_API_UNAVAILABLE"
        error_class = payload.get("error_class") or payload.get("error") or "OPERATOR_API_UNAVAILABLE"
        lines = [
            "Shadow route reached but content generation is currently blocked.",
            f"status: {payload.get('status', 'FAILED_CONTROLLED')}",
            f"error_code: {error_code}",
            f"error_class: {error_class}",
            f"dossier_id: {dossier_id or 'null'}",
            f"operator_route_reached: {payload.get('operator_route_reached', True)}",
            f"n8n_route_reached: {payload.get('n8n_route_reached', False)}",
            f"wf001_dossier_created: {payload.get('wf001_dossier_created', bool(dossier_id))}",
            f"wf010_reached: {payload.get('wf010_reached', False)}",
            f"provider_used: {payload.get('provider_used', 'gemini')}",
            f"model_used: {payload.get('model_used', 'gemini-2.5-flash')}",
            f"cloud_provider_used: {payload.get('cloud_provider_used', False)}",
            f"controlled_failure: {payload.get('controlled_failure', True)}",
            f"runtime_error_packet_count: {payload.get('runtime_error_packet_count', 1)}",
            "",
            f"message: {payload.get('message', 'Provider unavailable or route degraded. Retry after provider/API recovery.')}",
            "",
            "operator_surface: Open WebUI (http://localhost:3000)",
            "operator_api_link: internal-only",
        ]
        return "\n".join(lines)

    def _format_summary(self, dossier_id: str, start_resp: dict, timeline: dict, outputs: dict) -> str:
        families = self._packet_families(outputs)

        refined_script = self._extract_text_snippet(outputs, ["refined_script", "final_script", "script"])
        thumbnail = self._extract_text_snippet(outputs, ["thumbnail"])
        metadata = self._extract_text_snippet(outputs, ["metadata", "description", "hashtags", "title"])

        wf001_status = ((start_resp.get("wf001") or {}).get("status")) or "unknown"
        wf010_status = ((start_resp.get("wf010") or {}).get("status")) or "unknown"

        lines = [
            "Shadow job executed via Direct Router.",
            f"dossier_id: {dossier_id}",
            f"workflow route summary: WF-001={wf001_status}, WF-010={wf010_status}",
            "operator_surface: Open WebUI (http://localhost:3000)",
            "operator_api_link: internal-only",
            f"timeline_count: {timeline.get('timeline_count', 'n/a')}",
            f"packets_count: {outputs.get('packets_count', 'n/a')}",
            f"packet_families: {', '.join(families) if families else 'none'}",
            "",
            "final refined script:",
            refined_script or "not materialized in current packet payloads",
            "",
            "thumbnail ideas:",
            thumbnail or "not materialized in current packet payloads",
            "",
            "metadata:",
            metadata or "not materialized in current packet payloads",
            "",
            "next actions:",
            f"- inspect dossier: Inspect dossier {dossier_id}",
            f"- replay stage: Replay WF-200 for dossier {dossier_id} with your change request",
        ]
        return "\n".join(lines)

    def _poll_until_ready(self, dossier_id: str) -> tuple[dict, dict]:
        timeline = {}
        outputs = {}
        required = {
            "research_packet",
            "script_packet",
            "refined_script_packet",
            "context_packet",
            "thumbnail_packet",
            "metadata_packet",
        }
        for _ in range(self.valves.POLL_MAX_ATTEMPTS):
            timeline = self._api("GET", f"/operator/dossier/{dossier_id}/timeline")
            outputs = self._api("GET", f"/operator/outputs/{dossier_id}")
            families = set(self._packet_families(outputs))
            if required.issubset(families):
                break
            time.sleep(self.valves.POLL_INTERVAL_SEC)
        return timeline, outputs

    def pipe(self, body: dict, __user__: Optional[dict] = None) -> str:
        last_user_message = get_last_user_message(body.get("messages", [])) or ""
        prompt = str(last_user_message).strip()
        prompt_lc = prompt.lower()

        # Health path
        if any(k in prompt_lc for k in ["health", "status check", "health_check"]):
            health = self._api("GET", "/operator/health")
            return json.dumps(health, ensure_ascii=False, indent=2)

        # Dossier inspect path
        if any(k in prompt_lc for k in ["inspect dossier", "inspect output", "show outputs", "timeline"]):
            dossier_id = self._extract_dossier_id(prompt) or self._latest_dossier_from_index()
            if not dossier_id:
                return "No dossier_id found. Provide a dossier_id like DOSSIER-... or create a new content job first."
            timeline = self._api("GET", f"/operator/dossier/{dossier_id}/timeline")
            outputs = self._api("GET", f"/operator/outputs/{dossier_id}")
            return self._format_summary(dossier_id, {}, timeline, outputs)

        # Replay/remodify path
        if any(k in prompt_lc for k in ["replay", "remodify", "improve the hook", "sharper intro", "request changes"]):
            dossier_id = self._extract_dossier_id(prompt) or self._latest_dossier_from_index()
            if not dossier_id:
                return "No dossier_id found for replay. Provide dossier_id explicitly."
            replay = self._api(
                "POST",
                f"/operator/replay/{dossier_id}",
                {
                    "dossier_id": dossier_id,
                    "stage": "WF-200",
                    "instructions": prompt,
                    "checkpoint": "latest",
                },
            )
            timeline, outputs = self._poll_until_ready(dossier_id)
            summary = self._format_summary(dossier_id, {}, timeline, outputs)
            return summary + "\n\nreplay_response:\n" + json.dumps(replay, ensure_ascii=False, indent=2)

        # Default: create content job path
        cleaned_topic = re.sub(r"(?i)use shadow creator os tools\\.?\\s*", "", prompt).strip()
        if not cleaned_topic:
            cleaned_topic = "Create a YouTube script about AI vs Human with hook, intro, research summary, debate/critique, refined script, context packet, thumbnail plan, and metadata."

        channel_id = body.get("chat_id") or body.get("id") or "openwebui-chat"
        explicit_dossier = self._extract_dossier_id(prompt)
        reference_dossier_id = explicit_dossier
        if not reference_dossier_id and re.search(r"(?i)\\b(above|latest|previous|that script|this script)\\b", prompt):
            reference_dossier_id = self._latest_dossier_from_index()

        director_requested = self._extract_director_requested(prompt)

        start = self._api(
            "POST",
            "/operator/new-content-job",
            {
                "topic": cleaned_topic,
                "context": "YouTube video",
                "mode": self.valves.DEFAULT_MODE,
                "route_id": self.valves.DEFAULT_ROUTE_ID,
                "mission_text": cleaned_topic,
                "message": cleaned_topic,
                "request_id": f"OWUI-{int(time.time() * 1000)}",
                "creator_id": (__user__ or {}).get("id") or (__user__ or {}).get("email") or "openwebui-user",
                "channel_id": channel_id,
                "route_mode": "production",
                "provider_preference": "gemini",
                "cloud_llm_required": True,
                "source_surface": "openwebui",
                "reference_dossier_id": reference_dossier_id,
                "director_requested": director_requested,
                "openwebui_chat_id": channel_id,
            },
        )

        if start.get("status") == "FAILED_CONTROLLED" or start.get("controlled_failure"):
            return self._format_controlled_failure(start)

        dossier_id = start.get("dossier_id") or self._extract_dossier_id(json.dumps(start))
        if not dossier_id:
            fallback = {
                "status": "FAILED_CONTROLLED",
                "error_code": start.get("error_code") or "MISSING_DOSSIER_ID",
                "error_class": start.get("error_class") or start.get("error") or "MISSING_DOSSIER_ID",
                "dossier_id": None,
                "operator_route_reached": bool(start.get("_http_status", 0) >= 200 and start.get("_http_status", 0) < 600),
                "n8n_route_reached": bool((start.get("wf001") or {}).get("workflow_id") or (start.get("wf010") or {}).get("workflow_id")),
                "wf001_dossier_created": False,
                "wf010_reached": bool(start.get("wf010")),
                "provider_used": "gemini",
                "model_used": "gemini-2.5-flash",
                "cloud_provider_used": False,
                "content_generation_executed": False,
                "controlled_failure": True,
                "runtime_error_packet_count": 1,
                "message": "Operator API route returned without dossier_id. Request was handled in controlled failure mode.",
            }
            return self._format_controlled_failure(fallback)

        timeline, outputs = self._poll_until_ready(dossier_id)
        return self._format_summary(dossier_id, start, timeline, outputs)
