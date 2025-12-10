"""
Season exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.season.domain.exceptions import (
    SeasonNotFoundError,
    SeasonAlreadyExistsError,
    SeasonAlreadyDeletedError,
)


def register_season_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(SeasonNotFoundError)
    async def season_not_found_handler(
        request: Request,
        exc: SeasonNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(SeasonAlreadyExistsError)
    async def season_already_exists_handler(
        request: Request,
        exc: SeasonAlreadyExistsError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(SeasonAlreadyDeletedError)
    async def season_already_deleted_handler(
        request: Request,
        exc: SeasonAlreadyDeletedError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
