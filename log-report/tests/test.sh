#!/bin/bash
set -uo pipefail
# Deps (pytest, pytest-json-ctrf) are baked into environment/Dockerfile —
# no installs at verify time.

pytest /tests/test_outputs.py -rA --ctrf=/app/ctrf.json
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > /app/reward.txt
else
  echo 0 > /app/reward.txt
fi

exit 0
