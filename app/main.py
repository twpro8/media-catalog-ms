"""
Main module.
"""

from contextlib import asynccontextmanager
from typing import Sequence

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.error.base_exception_handler import register_base_exception_handlers
from app.dependencies import get_settings
from app.features.actor.presentation.exception_handlers import (
    register_actor_exception_handlers,
)
from app.features.actor.presentation.routes import actor_router
from app.features.director.presentation.exception_handlers import (
    register_director_exception_handlers,
)
from app.features.director.presentation.routes import director_router
from app.features.episode.presentation.exception_handlers import (
    register_episode_exception_handlers,
)
from app.features.movie.presentation.exception_handlers import (
    register_movie_exception_handlers,
)
from app.features.movie.presentation.routes import movie_router
from app.features.season.presentation.exception_handlers import (
    register_season_exception_handlers,
)
from app.features.show.presentation.exception_handlers import (
    register_show_exception_handlers,
)
from app.features.show.presentation.routes import show_router
from app.features.season.presentation.routes import season_router
from app.features.episode.presentation.routes import episode_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown


def _setup_middleware(app: FastAPI, origins: Sequence[str]):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def _setup_exception_handlers(app: FastAPI):
    register_base_exception_handlers(app)
    register_movie_exception_handlers(app)
    register_show_exception_handlers(app)
    register_season_exception_handlers(app)
    register_episode_exception_handlers(app)
    register_director_exception_handlers(app)
    register_actor_exception_handlers(app)


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
    _setup_middleware(app, settings.ALLOWED_ORIGINS)
    _setup_exception_handlers(app)
    _setup_routes(app)

    return app


app = create_app()
