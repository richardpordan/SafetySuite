#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 '<revision comment>'" >&2
  exit 1
fi

# Alembic revision
uv run alembic revision --autogenerate -m "$1"
