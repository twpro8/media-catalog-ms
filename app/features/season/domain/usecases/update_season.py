"""
Update season use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.season_exception import SeasonNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.season.domain.entities.season_command_model import SeasonUpdateModel
from app.features.season.domain.entities.season_entity import SeasonEntity
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.repositories.season_unit_of_work import SeasonUnitOfWork


class UpdateSeasonUseCase(BaseUseCase[tuple[UUID, SeasonUpdateModel], SeasonReadModel]):
    """
    UpdateSeasonUseCase defines a query use case interface related to the Season Entity.
    """

    unit_of_work: SeasonUnitOfWork

    @abstractmethod
    async def __call__(
        self, args: tuple[UUID, SeasonUpdateModel]
    ) -> SeasonReadModel: ...


class UpdateSeasonUseCaseImpl(UpdateSeasonUseCase):
    """
    UpdateSeasonUseCaseImpl implements a query use case related to the Season entity.
    """

    def __init__(self, unit_of_work: SeasonUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[UUID, SeasonUpdateModel]) -> SeasonReadModel:
        id_, update_data = args

        existing_season = await self.unit_of_work.seasons.find_by_id(id_)
        if not existing_season or existing_season.is_deleted:
            raise SeasonNotFoundError

        update_entity = existing_season.update_entity(
            update_data, lambda season_data: update_data.model_dump(exclude_unset=True)
        )

        updated_season = await self.unit_of_work.seasons.update(update_entity)
        await self.unit_of_work.commit()

        return SeasonReadModel.from_entity(cast(SeasonEntity, updated_season))
