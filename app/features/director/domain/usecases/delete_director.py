"""
Delete director use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.core.error.director_exception import (
    DirectorAlreadyDeletedError,
    DirectorNotFoundError,
)
from app.core.use_cases.use_case import BaseUseCase
from app.features.director.domain.entities.director_entity import DirectorEntity
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.repositories.director_unit_of_work import (
    DirectorUnitOfWork,
)


class DeleteDirectorUseCase(BaseUseCase[tuple[UUID], DirectorReadModel]):
    """
    DeleteDirectorUseCase defines a command use case interface related to the Director entity.
    """

    unit_of_work: DirectorUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> DirectorReadModel: ...


class DeleteDirectorUseCaseImpl(DeleteDirectorUseCase):
    """
    DeleteDirectorUseCaseImpl implements a command use case related to the Director entity.
    """

    def __init__(self, unit_of_work: DirectorUnitOfWork):
        self.unit_of_work: DirectorUnitOfWork = unit_of_work

    async def __call__(self, args: tuple[UUID]) -> DirectorReadModel:
        (id_,) = args

        existing_director = await self.unit_of_work.directors.find_by_id(id_)
        if existing_director is None:
            raise DirectorNotFoundError

        try:
            marked_director = existing_director.mark_entity_as_deleted()
        except InvalidOperationError:
            raise DirectorAlreadyDeletedError

        deleted_director = await self.unit_of_work.directors.update(marked_director)

        await self.unit_of_work.commit()

        return DirectorReadModel.from_entity(cast(DirectorEntity, deleted_director))
