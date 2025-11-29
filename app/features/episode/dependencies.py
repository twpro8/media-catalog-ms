"""
Episode dependencies module.
"""

from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.postgres.database import get_session
from app.features.episode.data.repositories.episode_repository_impl import (
    EpisodeRepositoryImpl,
)
from app.features.episode.data.repositories.episode_unit_of_work_impl import (
    EpisodeUnitOfWorkImpl,
)
from app.features.episode.data.services.episode_query_service_impl import (
    EpisodeQueryServiceImpl,
)
from app.features.episode.domain.repositories.episode_repository import (
    EpisodeRepository,
)
from app.features.episode.domain.repositories.episode_unit_of_work import (
    EpisodeUnitOfWork,
)
from app.features.episode.domain.services.episode_query_service import (
    EpisodeQueryService,
)
from app.features.episode.domain.usecases.create_episode import (
    CreateEpisodeUseCase,
    CreateEpisodeUseCaseImpl,
)
from app.features.episode.domain.usecases.delete_episode import (
    DeleteEpisodeUseCase,
    DeleteEpisodeUseCaseImpl,
)
from app.features.episode.domain.usecases.get_episode import (
    GetEpisodeUseCase,
    GetEpisodeUseCaseImpl,
)
from app.features.episode.domain.usecases.get_episodes import (
    GetEpisodesUseCase,
    GetEpisodesUseCaseImpl,
)
from app.features.episode.domain.usecases.update_episode import (
    UpdateEpisodeUseCase,
    UpdateEpisodeUseCaseImpl,
)
from app.features.season.dependencies import get_season_repository
from app.features.season.domain.repositories.season_repository import SeasonRepository


def get_episode_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> EpisodeQueryService:
    return EpisodeQueryServiceImpl(session)


def get_episode_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> EpisodeRepository:
    return EpisodeRepositoryImpl(session)


async def get_episode_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    episode_repository: Annotated[EpisodeRepository, Depends(get_episode_repository)],
    season_repository: Annotated[SeasonRepository, Depends(get_season_repository)],
) -> AsyncGenerator[EpisodeUnitOfWork]:
    async with EpisodeUnitOfWorkImpl(
        session,
        episode_repository,
        season_repository,
    ) as uow:
        yield uow


def get_create_episode_use_case(
    unit_of_work: Annotated[EpisodeUnitOfWork, Depends(get_episode_unit_of_work)],
) -> CreateEpisodeUseCase:
    return CreateEpisodeUseCaseImpl(unit_of_work)


def get_episode_use_case(
    episode_query_service: Annotated[
        EpisodeQueryService, Depends(get_episode_query_service)
    ],
) -> GetEpisodeUseCase:
    return GetEpisodeUseCaseImpl(episode_query_service)


def get_episodes_use_case(
    episode_query_service: Annotated[
        EpisodeQueryService, Depends(get_episode_query_service)
    ],
) -> GetEpisodesUseCase:
    return GetEpisodesUseCaseImpl(episode_query_service)


def get_update_episode_use_case(
    unit_of_work: Annotated[EpisodeUnitOfWork, Depends(get_episode_unit_of_work)],
) -> UpdateEpisodeUseCase:
    return UpdateEpisodeUseCaseImpl(unit_of_work)


def get_delete_episode_use_case(
    unit_of_work: Annotated[EpisodeUnitOfWork, Depends(get_episode_unit_of_work)],
) -> DeleteEpisodeUseCase:
    return DeleteEpisodeUseCaseImpl(unit_of_work)
