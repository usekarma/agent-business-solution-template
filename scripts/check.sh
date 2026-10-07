#!/usr/bin/env bash
set -euo pipefail

PYTHON="${PYTHON:-python3}"

if [[ -x .venv/bin/python ]]; then
  PYTHON=.venv/bin/python
fi

"$PYTHON" -m pytest
"$PYTHON" -m ruff check .
"$PYTHON" -m mypy src
