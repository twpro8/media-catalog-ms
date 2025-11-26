"""
Delete season use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.core.error.season_exception import (
    SeasonAlreadyDeletedError,
    SeasonNotFoundError,
)
from app.core.use_cases.use_case import BaseUseCase
from app.features.season.domain.entities.season_entity import SeasonEntity
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.repositories.season_unit_of_work import SeasonUnitOfWork


class DeleteSeasonUseCase(BaseUseCase[tuple[UUID], SeasonReadModel]):
    """
    DeleteSeasonUseCase defines a command use case interface related to the Season entity.
    """

    unit_of_work: SeasonUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> SeasonReadModel: ...


class DeleteSeasonUseCaseImpl(DeleteSeasonUseCase):
    """
    DeleteSeasonUseCaseImpl implements a command use case related to the Season entity.
    """

    def __init__(self, unit_of_work: SeasonUnitOfWork):
        self.unit_of_work: SeasonUnitOfWork = unit_of_work

    async def __call__(self, args: tuple[UUID]) -> SeasonReadModel:
        (id_,) = args

        existing_season = await self.unit_of_work.seasons.find_by_id(id_)
        if existing_season is None:
            raise SeasonNotFoundError

        try:
            marked_season = existing_season.mark_entity_as_deleted()
        except InvalidOperationError:
            raise SeasonAlreadyDeletedError

        deleted_season = await self.unit_of_work.seasons.update(marked_season)

        await self.unit_of_work.commit()

        return SeasonReadModel.from_entity(cast(SeasonEntity, deleted_season))
