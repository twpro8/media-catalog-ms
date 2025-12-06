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
from app.features.reference.data.services.country_query_service_impl import (
    CountryQueryServiceImpl,
)
from app.features.reference.domain.services.country.country_query_service import (
    CountryQueryService,
)
from app.features.reference.domain.usecases.country.get_countries import (
    GetCountriesUseCase,
    GetCountriesUseCaseImpl,
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


def get_country_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> CountryQueryService:
    return CountryQueryServiceImpl(session)


def get_countries_use_case(
    country_query_service: Annotated[
        CountryQueryService, Depends(get_country_query_service)
    ],
) -> GetCountriesUseCase:
    return GetCountriesUseCaseImpl(country_query_service)
