#!/usr/bin/env python3
from __future__ import annotations

import sys

from lib.batch3_validator_core import execute_from_config
from lib.batch3_validator_configs import CONFIGS
from lib.batch8j_validator_core import run_single_target_cli


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and ("batch8i" in args[0] or "batch8j" in args[0]):
        raise SystemExit(run_single_target_cli("evidence_bundle", args))
    raise SystemExit(execute_from_config(CONFIGS["evidence_bundle"]))
