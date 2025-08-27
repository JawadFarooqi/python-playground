#!/usr/bin/env bash
set -euo pipefail

# Simple bootstrap for absolute beginners.
# Usage: bash scripts/bootstrap.sh

if [ ! -d .venv ]; then
  python -m venv .venv
  echo "[bootstrap] Created virtual environment .venv"
fi
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install notebook
echo
echo "✅ Environment ready. Start Jupyter with: jupyter notebook"
