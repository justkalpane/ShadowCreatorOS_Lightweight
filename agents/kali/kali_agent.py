from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
from agents.common.production_agent_base import ProductionAgentBase, print_run


class KaliAgent(ProductionAgentBase):
    def __init__(
        self,
        timeout_seconds: float = 8.0,
        max_retries: int = 2,
        backoff_seconds: float = 0.4,
    ) -> None:
        super().__init__(
            agent_slug="kali",
            director_binding="Kali",
            artifact_family="kali-agent-packet",
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
        )


if __name__ == "__main__":
    print_run(KaliAgent())


# PHASE 13E_6 NAMED AGENT 24-CRAFT CINEMA ALIGNMENT
# phase_13e_6_status: NAMED_AGENT_24_CRAFT_CINEMA_ALIGNMENT
# runtime_behavior_changed: false
# selector_modified: false
# active_route_registry_modified: false
# runtime_proof_claimed: false
# pass_claimed: false
# script_generation_preserved: true
# film_screenplay_generation_preserved: true
# cinema_craft_authority: 07 dramatic_conflict_and_stakes; 22 post_production_and_finishing
# mythology_fidelity_lock: rupture, moral cleansing, decisive cut, protective destruction, and fearless confrontation
# cinema_department_execution_role: Execute decisive revision, moral rupture, conflict pressure, and severance of false or weak dramatic material.
# downstream_boundary: Shock value, outrage, controversy, rage-bait, thumbnail provocation, shorts virality, and platform conflict are not film-core authority.
# content_platform_drift_not_marked_as_film_core_authority: true
