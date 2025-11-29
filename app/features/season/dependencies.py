"""
Season dependencies module.
"""

from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.season.data.repositories.season_repository_impl import (
    SeasonRepositoryImpl,
)
from app.features.season.data.repositories.season_unit_of_work_impl import (
    SeasonUnitOfWorkImpl,
)
from app.features.season.data.services.season_query_service_impl import (
    SeasonQueryServiceImpl,
)
from app.features.season.domain.repositories.season_repository import SeasonRepository
from app.features.season.domain.repositories.season_unit_of_work import SeasonUnitOfWork
from app.features.season.domain.services.season_query_service import SeasonQueryService
from app.features.season.domain.usecases.create_season import (
    CreateSeasonUseCase,
    CreateSeasonUseCaseImpl,
)
from app.features.season.domain.usecases.delete_season import (
    DeleteSeasonUseCase,
    DeleteSeasonUseCaseImpl,
)
from app.features.season.domain.usecases.get_season import (
    GetSeasonUseCase,
    GetSeasonUseCaseImpl,
)
from app.features.season.domain.usecases.get_seasons import (
    GetSeasonsUseCase,
    GetSeasonsUseCaseImpl,
)
from app.features.season.domain.usecases.update_season import (
    UpdateSeasonUseCase,
    UpdateSeasonUseCaseImpl,
)
from app.features.show.dependencies import get_show_repository
from app.features.show.domain.repositories.show_repository import ShowRepository


def get_season_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> SeasonQueryService:
    return SeasonQueryServiceImpl(session)


def get_season_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> SeasonRepository:
    return SeasonRepositoryImpl(session)


async def get_season_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    season_repository: Annotated[SeasonRepository, Depends(get_season_repository)],
    show_repository: Annotated[ShowRepository, Depends(get_show_repository)],
) -> AsyncGenerator[SeasonUnitOfWork, None]:
    async with SeasonUnitOfWorkImpl(session, season_repository, show_repository) as uow:
        yield uow


def get_create_season_use_case(
    unit_of_work: Annotated[SeasonUnitOfWork, Depends(get_season_unit_of_work)],
) -> CreateSeasonUseCase:
    return CreateSeasonUseCaseImpl(unit_of_work)


def get_season_use_case(
    season_query_service: Annotated[
        SeasonQueryService, Depends(get_season_query_service)
    ],
) -> GetSeasonUseCase:
    return GetSeasonUseCaseImpl(season_query_service)


def get_seasons_use_case(
    season_query_service: Annotated[
        SeasonQueryService, Depends(get_season_query_service)
    ],
) -> GetSeasonsUseCase:
    return GetSeasonsUseCaseImpl(season_query_service)


def get_update_season_use_case(
    unit_of_work: Annotated[SeasonUnitOfWork, Depends(get_season_unit_of_work)],
) -> UpdateSeasonUseCase:
    return UpdateSeasonUseCaseImpl(unit_of_work)


def get_delete_season_use_case(
    unit_of_work: Annotated[SeasonUnitOfWork, Depends(get_season_unit_of_work)],
) -> DeleteSeasonUseCase:
    return DeleteSeasonUseCaseImpl(unit_of_work)
