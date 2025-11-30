"""
Create episode use case module.
"""

from abc import abstractmethod
from typing import cast

from app.core.error.episode_exception import EpisodeAlreadyExistsError
from app.core.error.season_exception import SeasonNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.episode.domain.entities.episode_entity import EpisodeEntity
from app.features.episode.domain.entities.episode_command_model import (
    EpisodeCreateModel,
)
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.repositories.episode_unit_of_work import (
    EpisodeUnitOfWork,
)


class CreateEpisodeUseCase(BaseUseCase[tuple[EpisodeCreateModel], EpisodeReadModel]):
    """
    CreateEpisodeUseCase defines a command use case interface related to the Episode entity.
    """

    unit_of_work: EpisodeUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[EpisodeCreateModel]) -> EpisodeReadModel: ...


class CreateEpisodeUseCaseImpl(CreateEpisodeUseCase):
    """
    CreateEpisodeUseCaseImpl implements a command use case related to the Episode entity.
    """

    def __init__(self, unit_of_work: EpisodeUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[EpisodeCreateModel]) -> EpisodeReadModel:
        (data,) = args

        season = await self.unit_of_work.seasons.find_by_id(data.season_id)
        if not season or season.is_deleted:
            raise SeasonNotFoundError

        existing_episode = await self.unit_of_work.episodes.find_by_season_and_number(
            season_id=data.season_id,
            episode_number=data.episode_number,
        )

        if existing_episode:
            if existing_episode.is_deleted:
                unmarked_episode = existing_episode.unmark_entity_as_deleted()
                created_episode = await self.unit_of_work.episodes.update(
                    unmarked_episode
                )
            else:
                raise EpisodeAlreadyExistsError
        else:
            episode = EpisodeEntity(None, **data.model_dump())
            created_episode = await self.unit_of_work.episodes.create(episode)

        await self.unit_of_work.commit()

        return EpisodeReadModel.from_entity(cast(EpisodeEntity, created_episode))
