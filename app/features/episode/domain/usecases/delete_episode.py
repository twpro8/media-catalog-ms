"""
Delete episode use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.core.error.episode_exception import (
    EpisodeAlreadyDeletedError,
    EpisodeNotFoundError,
)
from app.core.use_cases.use_case import BaseUseCase
from app.features.episode.domain.entities.episode_entity import EpisodeEntity
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.repositories.episode_unit_of_work import (
    EpisodeUnitOfWork,
)


class DeleteEpisodeUseCase(BaseUseCase[tuple[UUID], EpisodeReadModel]):
    """
    DeleteEpisodeUseCase defines a command use case interface related to the Episode entity.
    """

    unit_of_work: EpisodeUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> EpisodeReadModel: ...


class DeleteEpisodeUseCaseImpl(DeleteEpisodeUseCase):
    """
    DeleteEpisodeUseCaseImpl implements a command use case related to the Episode entity.
    """

    def __init__(self, unit_of_work: EpisodeUnitOfWork):
        self.unit_of_work: EpisodeUnitOfWork = unit_of_work

    async def __call__(self, args: tuple[UUID]) -> EpisodeReadModel:
        (id_,) = args

        existing_episode = await self.unit_of_work.episodes.find_by_id(id_)
        if existing_episode is None:
            raise EpisodeNotFoundError

        try:
            marked_episode = existing_episode.mark_entity_as_deleted()
        except InvalidOperationError:
            raise EpisodeAlreadyDeletedError

        deleted_episode = await self.unit_of_work.episodes.update(marked_episode)

        await self.unit_of_work.commit()

        return EpisodeReadModel.from_entity(cast(EpisodeEntity, deleted_episode))
