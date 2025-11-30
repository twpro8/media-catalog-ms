"""
Main module.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.dependencies import get_settings
from app.core.error.base_exception import BaseError
from app.core.error.exception_handler import app_exception_handler
from app.features.actor.presentation.routes import actor_router
from app.features.director.presentation.routes import director_router
from app.features.movie.presentation.routes import movie_router
from app.features.show.presentation.routes import show_router
from app.features.season.presentation.routes import season_router
from app.features.episode.presentation.routes import episode_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown


def _setup_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


def _setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(BaseError, app_exception_handler)


def _setup_routes(app: FastAPI):
    app.include_router(movie_router)
    app.include_router(show_router)
    app.include_router(season_router)
    app.include_router(episode_router)
    app.include_router(director_router)
    app.include_router(actor_router)


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )
    _setup_middleware(app)
    _setup_exception_handlers(app)
    _setup_routes(app)

    return app


app = create_app()
