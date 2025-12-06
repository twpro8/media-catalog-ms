"""
Language dependencies module.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.reference.data.repositories.country_repository_impl import (
    CountryRepositoryImpl,
)
from app.features.reference.data.repositories.language_repository_impl import (
    LanguageRepositoryImpl,
)
from app.features.reference.data.services.language_query_service_impl import (
    LanguageQueryServiceImpl,
)
from app.features.reference.domain.repositories.country_repository import (
    CountryRepository,
)
from app.features.reference.domain.repositories.language_repository import (
    LanguageRepository,
)
from app.features.reference.domain.services.language_query_service import (
    LanguageQueryService,
)
from app.features.reference.domain.usecases.language.get_languages import (
    GetLanguagesUseCase,
    GetLanguagesUseCaseImpl,
)
from app.features.reference.data.services.country_query_service_impl import (
    CountryQueryServiceImpl,
)
from app.features.reference.domain.services.country_query_service import (
    CountryQueryService,
)
from app.features.reference.domain.usecases.country.get_countries import (
    GetCountriesUseCase,
    GetCountriesUseCaseImpl,
)
from app.features.reference.data.repositories.reference_unit_of_work_impl import (
    ReferenceUnitOfWorkImpl,
)
from app.features.reference.domain.repositories.reference_unit_of_work import (
    ReferenceUnitOfWork,
)
from app.features.reference.domain.usecases.language.get_language import (
    GetLanguageUseCase,
    GetLanguageUseCaseImpl,
)
from app.features.reference.domain.usecases.language.activate_language import (
    ActivateLanguageUseCase,
    ActivateLanguageUseCaseImpl,
)
from app.features.reference.domain.usecases.language.deactivate_language import (
    DeactivateLanguageUseCase,
    DeactivateLanguageUseCaseImpl,
)
from app.features.reference.domain.usecases.country.get_country import (
    GetCountryUseCase,
    GetCountryUseCaseImpl,
)
from app.features.reference.domain.usecases.country.activate_country import (
    ActivateCountryUseCase,
    ActivateCountryUseCaseImpl,
)
from app.features.reference.domain.usecases.country.deactivate_country import (
    DeactivateCountryUseCase,
    DeactivateCountryUseCaseImpl,
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


def get_country_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> CountryRepository:
    return CountryRepositoryImpl(session)


def get_language_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> LanguageRepository:
    return LanguageRepositoryImpl(session)


def get_reference_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    country_repository: Annotated[CountryRepository, Depends(get_country_repository)],
    language_repository: Annotated[
        LanguageRepository, Depends(get_language_repository)
    ],
) -> ReferenceUnitOfWork:
    return ReferenceUnitOfWorkImpl(
        session,
        country_repository,
        language_repository,
    )


def get_language_use_case(
    language_query_service: Annotated[
        LanguageQueryService, Depends(get_language_query_service)
    ],
) -> GetLanguageUseCase:
    return GetLanguageUseCaseImpl(language_query_service)


def get_activate_language_use_case(
    unit_of_work: Annotated[ReferenceUnitOfWork, Depends(get_reference_unit_of_work)],
) -> ActivateLanguageUseCase:
    return ActivateLanguageUseCaseImpl(unit_of_work)


def get_deactivate_language_use_case(
    unit_of_work: Annotated[ReferenceUnitOfWork, Depends(get_reference_unit_of_work)],
) -> DeactivateLanguageUseCase:
    return DeactivateLanguageUseCaseImpl(unit_of_work)


def get_country_use_case(
    country_query_service: Annotated[
        CountryQueryService, Depends(get_country_query_service)
    ],
) -> GetCountryUseCase:
    return GetCountryUseCaseImpl(country_query_service)


def get_activate_country_use_case(
    unit_of_work: Annotated[ReferenceUnitOfWork, Depends(get_reference_unit_of_work)],
) -> ActivateCountryUseCase:
    return ActivateCountryUseCaseImpl(unit_of_work)


def get_deactivate_country_use_case(
    unit_of_work: Annotated[ReferenceUnitOfWork, Depends(get_reference_unit_of_work)],
) -> DeactivateCountryUseCase:
    return DeactivateCountryUseCaseImpl(unit_of_work)
