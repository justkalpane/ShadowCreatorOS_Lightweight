# Native Agent Capability Inventory Contract

This contract defines how any coding agent or LLM app must declare capabilities before task execution claims.

## Required Inventory Record

```text
NATIVE_AGENT_CAPABILITY
- capability_name
- capability_type = repo_read / repo_write / shell / git / github / web_search / web_fetch / file_search / image_input / document_read / code_execution / package_install / browser_automation / api_call / connector / plugin / provider / local_app / cloud_app
- current_status = ACTIVE / AVAILABLE_BY_APPROVAL / PLANNED / NOT_ACTIVE / NEEDS_CONFIRMATION
- source_of_truth = environment_inspection / repo_contract / user_confirmation / historical_reference / unknown
- approval_required = true/false
- safe_for_default_use = true/false
- allowed_in_chat_only_mode = true/false
- allowed_in_repo_write_mode = true/false
- allowed_in_execution_bus_mode = true/false
- security_risk = LOW / MEDIUM / HIGH
- notes
```

## Classification Rules

- Chat reasoning is `ACTIVE` only when the current session can respond.
- Repo read is `ACTIVE` only when repo files are accessible.
- Repo write is `ACTIVE` only when filesystem write access exists and user approves.
- Git push is `AVAILABLE_BY_APPROVAL` by default.
- Web research is `ACTIVE` only if environment can fetch/use web sources.
- Provider APIs are `NOT_ACTIVE` unless credentials and approval exist.
- n8n workflows are `NOT_ACTIVE` unless runtime is explicitly started and approved.
- Browser automation is `NOT_ACTIVE` unless explicitly available and approved.

## Security Rule

No secrets, tokens, credentials, or private raw exports may be exposed in capability output.
