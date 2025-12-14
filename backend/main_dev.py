"""API main for local development"""

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from src.api.accident_types import router as accident_types_router
from src.api.accidents import router as accidents_router
from src.api.injury_types import router as injury_types_router
from src.api.persons import router as persons_router
from src.api.roles import router as roles_router
from src.api.sites import router as sites_router

api = FastAPI(title="SafetySuite API")

api.include_router(
    accidents_router,
    prefix="/api/v1/accidents",
    tags=["accidents"],
)

api.include_router(
    accident_types_router,
    prefix="/api/v1/accident_types",
    tags=["accident_types"],
)

api.include_router(
    injury_types_router,
    prefix="/api/v1/injury_types",
    tags=["injury_types"],
)

api.include_router(
    persons_router,
    prefix="/api/v1/persons",
    tags=["persons"],
)

api.include_router(
    roles_router,
    prefix="/api/v1/roles",
    tags=["roles"],
)

api.include_router(
    sites_router,
    prefix="/api/v1/sites",
    tags=["sites"],
)
