"""
Create show use case module.
"""

from abc import abstractmethod
from typing import cast

from app.features.show.domain.exceptions import ShowAlreadyExistsError
from app.core.use_cases.use_case import BaseUseCase
from app.features.show.domain.entities.show_entity import ShowEntity
from app.features.show.domain.entities.show_command_model import ShowCreateModel
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.repositories.show_unit_of_work import ShowUnitOfWork


class CreateShowUseCase(BaseUseCase[tuple[ShowCreateModel], ShowReadModel]):
    """
    CreateShowUseCase defines a command use case interface related to the Show entity.
    """

    unit_of_work: ShowUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[ShowCreateModel]) -> ShowReadModel: ...


class CreateShowUseCaseImpl(CreateShowUseCase):
    """
    CreateShowUseCaseImpl implements a command use case related to the Show entity.
    """

    def __init__(self, unit_of_work: ShowUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[ShowCreateModel]) -> ShowReadModel:
        (data,) = args

        show = ShowEntity(None, **data.model_dump())
        existing_show = await self.unit_of_work.shows.find_by_title_and_date(
            title=data.title,
            release_date=data.release_date,
        )

        if existing_show:
            if existing_show.is_deleted:
                unmarked_show = existing_show.unmark_entity_as_deleted()
                created_show = await self.unit_of_work.shows.update(unmarked_show)
            else:
                raise ShowAlreadyExistsError
        else:
            created_show = await self.unit_of_work.shows.create(show)

        await self.unit_of_work.commit()

        return ShowReadModel.from_entity(cast(ShowEntity, created_show))
