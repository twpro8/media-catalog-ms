"""
Episode exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.episode.domain.exceptions import (
    EpisodeNotFoundError,
    EpisodeAlreadyExistsError,
    EpisodeAlreadyDeletedError,
)


def register_episode_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(EpisodeNotFoundError)
    async def episode_not_active_handler(
        request: Request,
        exc: EpisodeNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(EpisodeAlreadyExistsError)
    async def episode_already_exists_handler(
        request: Request,
        exc: EpisodeAlreadyExistsError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(EpisodeAlreadyDeletedError)
    async def episode_already_deleted_handler(
        request: Request,
        exc: EpisodeAlreadyDeletedError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
