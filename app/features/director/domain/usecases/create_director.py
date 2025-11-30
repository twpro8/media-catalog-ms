"""
Create director use case module.
"""

from abc import abstractmethod
from typing import cast

from app.core.error.director_exception import DirectorAlreadyExistsError
from app.core.use_cases.use_case import BaseUseCase
from app.features.director.domain.entities.director_entity import DirectorEntity
from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.repositories.director_unit_of_work import (
    DirectorUnitOfWork,
)


class CreateDirectorUseCase(BaseUseCase[tuple[DirectorCreateModel], DirectorReadModel]):
    """
    CreateDirectorUseCase defines a command use case interface related to the Director entity.
    """

    unit_of_work: DirectorUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[DirectorCreateModel]) -> DirectorReadModel: ...


class CreateDirectorUseCaseImpl(CreateDirectorUseCase):
    """
    CreateDirectorUseCaseImpl implements a command use case related to the Director entity.
    """

    def __init__(self, unit_of_work: DirectorUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[DirectorCreateModel]) -> DirectorReadModel:
        (data,) = args

        director = DirectorEntity(None, **data.model_dump())
        existing_director = await self.unit_of_work.directors.find_one(
            first_name=data.first_name,
            last_name=data.last_name,
            birth_date=data.birth_date,
        )

        if existing_director:
            if existing_director.is_deleted:
                unmarked_director = existing_director.unmark_entity_as_deleted()
                created_director = await self.unit_of_work.directors.update(
                    unmarked_director
                )
            else:
                raise DirectorAlreadyExistsError
        else:
            created_director = await self.unit_of_work.directors.create(director)

        await self.unit_of_work.commit()

        return DirectorReadModel.from_entity(cast(DirectorEntity, created_director))
