"""
Update director use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.features.director.domain.exceptions import DirectorNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.director.domain.entities.director_command_model import (
    DirectorUpdateModel,
)
from app.features.director.domain.entities.director_entity import DirectorEntity
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.repositories.director_unit_of_work import (
    DirectorUnitOfWork,
)


class UpdateDirectorUseCase(
    BaseUseCase[tuple[UUID, DirectorUpdateModel], DirectorReadModel]
):
    """
    UpdateDirectorUseCase defines a query use case interface related to the Director Entity.
    """

    unit_of_work: DirectorUnitOfWork

    @abstractmethod
    async def __call__(
        self, args: tuple[UUID, DirectorUpdateModel]
    ) -> DirectorReadModel: ...


class UpdateDirectorUseCaseImpl(UpdateDirectorUseCase):
    """
    UpdateDirectorUseCaseImpl implements a query use case related to the Director entity.
    """

    def __init__(self, unit_of_work: DirectorUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(
        self, args: tuple[UUID, DirectorUpdateModel]
    ) -> DirectorReadModel:
        id_, update_data = args

        existing_director = await self.unit_of_work.directors.find_by_id(id_)
        if not existing_director or existing_director.is_deleted:
            raise DirectorNotFoundError

        update_entity = existing_director.update_entity(
            update_data,
            lambda director_data: update_data.model_dump(exclude_unset=True),
        )

        updated_director = await self.unit_of_work.directors.update(update_entity)
        await self.unit_of_work.commit()

        return DirectorReadModel.from_entity(cast(DirectorEntity, updated_director))
