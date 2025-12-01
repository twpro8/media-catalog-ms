"""
Movie exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.movie.domain.exceptions import (
    MovieNotFoundError,
    MovieAlreadyExistsError,
    MovieAlreadyDeletedError,
)


def register_movie_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(MovieNotFoundError)
    async def movie_not_active_handler(
        request: Request,
        exc: MovieNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(MovieAlreadyExistsError)
    async def movie_already_exists_handler(
        request: Request,
        exc: MovieAlreadyExistsError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(MovieAlreadyDeletedError)
    async def movie_already_deleted_handler(
        request: Request,
        exc: MovieAlreadyDeletedError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
