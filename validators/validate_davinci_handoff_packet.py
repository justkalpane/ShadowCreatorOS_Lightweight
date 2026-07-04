#!/usr/bin/env python3
from __future__ import annotations

from lib.batch3_validator_core import execute_from_config
from lib.batch3_validator_configs import CONFIGS

if __name__ == "__main__":
    raise SystemExit(execute_from_config(CONFIGS['davinci_handoff_packet']))
