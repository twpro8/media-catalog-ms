"""
Delete show use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.features.show.domain.exceptions import (
    ShowNotFoundError,
    ShowAlreadyDeletedError,
)
from app.core.use_cases.use_case import BaseUseCase
from app.features.show.domain.entities.show_entity import ShowEntity
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.repositories.show_unit_of_work import ShowUnitOfWork


class DeleteShowUseCase(BaseUseCase[tuple[UUID], ShowReadModel]):
    """
    DeleteShowUseCase defines a command use case interface related to the Show entity.
    """

    unit_of_work: ShowUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> ShowReadModel: ...


class DeleteShowUseCaseImpl(DeleteShowUseCase):
    """
    DeleteShowUseCaseImpl implements a command use case related to the Show entity.
    """

    def __init__(self, unit_of_work: ShowUnitOfWork):
        self.unit_of_work: ShowUnitOfWork = unit_of_work

    async def __call__(self, args: tuple[UUID]) -> ShowReadModel:
        (id_,) = args

        existing_show = await self.unit_of_work.shows.find_by_id(id_)
        if existing_show is None:
            raise ShowNotFoundError

        try:
            marked_show = existing_show.mark_entity_as_deleted()
        except InvalidOperationError:
            raise ShowAlreadyDeletedError

        deleted_show = await self.unit_of_work.shows.update(marked_show)

        await self.unit_of_work.commit()

        return ShowReadModel.from_entity(cast(ShowEntity, deleted_show))
