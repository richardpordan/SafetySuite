#!/usr/bin/env bash

set -eou pipefail

uv run alembic upgrade head

uv run uvicorn main:api --host 0.0.0.0 --port 8000
