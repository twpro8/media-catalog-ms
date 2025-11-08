"""
Exception handler module.
"""

from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse

from app.core.error.base_exception import BaseError


async def app_exception_handler(
    request: Request,
    exc: Exception,
) -> Response:
    if isinstance(exc, BaseError):
        status_code = exc.status_code
        detail = exc.detail
    else:
        status_code = 500
        detail = "Internal Server Error"

    return JSONResponse(
        status_code=status_code,
        content={"detail": detail},
    )
