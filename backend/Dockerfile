# ===============================
# SafetySuite Backend Dockerfile
# ===============================
FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

WORKDIR /api

# Install build dependencies for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python3-dev \
    gcc

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev

COPY ./src ./src
COPY main.py ./
COPY ./alembic ./alembic
COPY alembic.ini ./

COPY ./scripts ./scripts
RUN chmod +x ./scripts/entrypoint.sh

CMD ["./scripts/entrypoint.sh"]
