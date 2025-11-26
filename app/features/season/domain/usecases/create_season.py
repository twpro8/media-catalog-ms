"""
Create season use case module.
"""

from abc import abstractmethod
from typing import cast

from app.core.error.season_exception import SeasonAlreadyExistsError
from app.core.error.show_exception import ShowNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.season.domain.entities.season_entity import SeasonEntity
from app.features.season.domain.entities.season_command_model import SeasonCreateModel
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.repositories.season_unit_of_work import SeasonUnitOfWork


class CreateSeasonUseCase(BaseUseCase[tuple[SeasonCreateModel], SeasonReadModel]):
    """
    CreateSeasonUseCase defines a command use case interface related to the Season entity.
    """

    unit_of_work: SeasonUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[SeasonCreateModel]) -> SeasonReadModel: ...


class CreateSeasonUseCaseImpl(CreateSeasonUseCase):
    """
    CreateSeasonUseCaseImpl implements a command use case related to the Season entity.
    """

    def __init__(self, unit_of_work: SeasonUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[SeasonCreateModel]) -> SeasonReadModel:
        (data,) = args

        show = await self.unit_of_work.shows.find_by_id(data.show_id)
        if not show or show.is_deleted:
            raise ShowNotFoundError

        existing_season = await self.unit_of_work.seasons.find_by_show_and_number(
            show_id=data.show_id,
            season_number=data.season_number,
        )

        if existing_season:
            if existing_season.is_deleted:
                unmarked_season = existing_season.unmark_as_deleted()
                created_season = await self.unit_of_work.seasons.update(unmarked_season)
            else:
                raise SeasonAlreadyExistsError
        else:
            season = SeasonEntity(None, **data.model_dump())
            created_season = await self.unit_of_work.seasons.create(season)

        await self.unit_of_work.commit()

        return SeasonReadModel.from_entity(cast(SeasonEntity, created_season))
