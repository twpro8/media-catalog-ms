"""
Reference exception handlers module.
"""

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from app.features.reference.domain.exceptions.country_error import (
    CountryNotFoundError,
    CountryAlreadyActiveError,
    CountryAlreadyInactiveError,
)
from app.features.reference.domain.exceptions.language_error import (
    LanguageNotFoundError,
    LanguageAlreadyActiveError,
    LanguageAlreadyInactiveError,
)


def register_country_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(CountryNotFoundError)
    async def country_not_found_handler(
        request: Request,
        exc: CountryNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(CountryAlreadyActiveError)
    async def country_already_active(
        request: Request,
        exc: CountryAlreadyActiveError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(CountryAlreadyInactiveError)
    async def country_already_inactive(
        request: Request,
        exc: CountryAlreadyInactiveError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )


def register_language_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(LanguageNotFoundError)
    async def language_not_found_handler(
        request: Request,
        exc: LanguageNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail},
        )

    @app.exception_handler(LanguageAlreadyActiveError)
    async def language_already_active(
        request: Request,
        exc: LanguageAlreadyActiveError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )

    @app.exception_handler(LanguageAlreadyInactiveError)
    async def language_already_inactive(
        request: Request,
        exc: LanguageAlreadyInactiveError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail},
        )
