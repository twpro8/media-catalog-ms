"""
Show exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.show.domain.exceptions import (
    ShowNotFoundError,
    ShowAlreadyExistsError,
    ShowAlreadyDeletedError,
)


def register_show_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ShowNotFoundError)
    async def show_not_active_handler(
        request: Request,
        exc: ShowNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(ShowAlreadyExistsError)
    async def show_already_exists_handler(
        request: Request,
        exc: ShowAlreadyExistsError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(ShowAlreadyDeletedError)
    async def show_already_deleted_handler(
        request: Request,
        exc: ShowAlreadyDeletedError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
