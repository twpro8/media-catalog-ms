"""
Director exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.director.domain.exceptions import (
    DirectorNotFoundError,
    DirectorAlreadyExistsError,
    DirectorAlreadyDeletedError,
)


def register_director_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DirectorNotFoundError)
    async def director_not_active_handler(
        request: Request,
        exc: DirectorNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(DirectorAlreadyExistsError)
    async def director_already_exists_handler(
        request: Request,
        exc: DirectorAlreadyExistsError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(DirectorAlreadyDeletedError)
    async def director_already_deleted_handler(
        request: Request,
        exc: DirectorAlreadyDeletedError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
