"""
Update show use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.show_exception import ShowNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.show.domain.entities.show_command_model import ShowUpdateModel
from app.features.show.domain.entities.show_entity import ShowEntity
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.repositories.show_unit_of_work import ShowUnitOfWork


class UpdateShowUseCase(BaseUseCase[tuple[UUID, ShowUpdateModel], ShowReadModel]):
    """
    UpdateShowUseCase defines a query use case interface related to the Show Entity.
    """

    unit_of_work: ShowUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID, ShowUpdateModel]) -> ShowReadModel: ...


class UpdateShowUseCaseImpl(UpdateShowUseCase):
    """
    UpdateShowUseCaseImpl implements a query use case related to the Show entity.
    """

    def __init__(self, unit_of_work: ShowUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[UUID, ShowUpdateModel]) -> ShowReadModel:
        id_, update_data = args

        existing_show = await self.unit_of_work.shows.find_by_id(id_)
        if not existing_show or existing_show.is_deleted:
            raise ShowNotFoundError

        update_entity = existing_show.update_entity(
            update_data, lambda show_data: update_data.model_dump(exclude_unset=True)
        )

        updated_show = await self.unit_of_work.shows.update(update_entity)
        await self.unit_of_work.commit()

        return ShowReadModel.from_entity(cast(ShowEntity, updated_show))
