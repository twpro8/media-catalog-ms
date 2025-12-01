"""
Update episode use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.features.episode.domain.exceptions import EpisodeNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.episode.domain.entities.episode_command_model import (
    EpisodeUpdateModel,
)
from app.features.episode.domain.entities.episode_entity import EpisodeEntity
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.repositories.episode_unit_of_work import (
    EpisodeUnitOfWork,
)


class UpdateEpisodeUseCase(
    BaseUseCase[tuple[UUID, EpisodeUpdateModel], EpisodeReadModel]
):
    """
    UpdateEpisodeUseCase defines a query use case interface related to the Episode Entity.
    """

    unit_of_work: EpisodeUnitOfWork

    @abstractmethod
    async def __call__(
        self, args: tuple[UUID, EpisodeUpdateModel]
    ) -> EpisodeReadModel: ...


class UpdateEpisodeUseCaseImpl(UpdateEpisodeUseCase):
    """
    UpdateEpisodeUseCaseImpl implements a query use case related to the Episode entity.
    """

    def __init__(self, unit_of_work: EpisodeUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[UUID, EpisodeUpdateModel]) -> EpisodeReadModel:
        id_, update_data = args

        existing_episode = await self.unit_of_work.episodes.find_by_id(id_)
        if not existing_episode or existing_episode.is_deleted:
            raise EpisodeNotFoundError

        update_entity = existing_episode.update_entity(
            update_data, lambda episode_data: update_data.model_dump(exclude_unset=True)
        )

        updated_episode = await self.unit_of_work.episodes.update(update_entity)
        await self.unit_of_work.commit()

        return EpisodeReadModel.from_entity(cast(EpisodeEntity, updated_episode))
