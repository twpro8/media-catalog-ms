"""
Exception handler module.
"""

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from starlette import status

from app.core.error.validation_exception import FieldRequiredError


def register_base_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(FieldRequiredError)
    async def show_not_active_handler(
        request: Request,
        exc: FieldRequiredError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exc.detail},
        )
