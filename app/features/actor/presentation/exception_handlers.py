"""
Actor exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.actor.domain.exceptions import (
    ActorNotFoundError,
    ActorAlreadyExistsError,
    ActorAlreadyDeletedError,
)


def register_actor_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ActorNotFoundError)
    async def actor_not_active_handler(
        request: Request,
        exc: ActorNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(ActorAlreadyExistsError)
    async def actor_already_exists_handler(
        request: Request,
        exc: ActorAlreadyExistsError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(ActorAlreadyDeletedError)
    async def actor_already_deleted_handler(
        request: Request,
        exc: ActorAlreadyDeletedError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
