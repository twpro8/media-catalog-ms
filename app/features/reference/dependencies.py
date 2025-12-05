"""
Language dependencies module.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.reference.data.services.language_query_service_impl import (
    LanguageQueryServiceImpl,
)
from app.features.reference.domain.services.language.language_query_service import (
    LanguageQueryService,
)
from app.features.reference.domain.usecases.language.get_languages import (
    GetLanguagesUseCase,
    GetLanguagesUseCaseImpl,
)


def get_language_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> LanguageQueryService:
    return LanguageQueryServiceImpl(session)


def get_languages_use_case(
    language_query_service: Annotated[
        LanguageQueryService, Depends(get_language_query_service)
    ],
) -> GetLanguagesUseCase:
    return GetLanguagesUseCaseImpl(language_query_service)
