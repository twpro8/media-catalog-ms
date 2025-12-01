"""
Create actor use case module.
"""

from abc import abstractmethod
from typing import cast

from app.features.actor.domain.exceptions import ActorAlreadyExistsError
from app.core.use_cases.use_case import BaseUseCase
from app.features.actor.domain.entities.actor_entity import ActorEntity
from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.repositories.actor_unit_of_work import (
    ActorUnitOfWork,
)


class CreateActorUseCase(BaseUseCase[tuple[ActorCreateModel], ActorReadModel]):
    """
    CreateActorUseCase defines a command use case interface related to the Actor entity.
    """

    unit_of_work: ActorUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[ActorCreateModel]) -> ActorReadModel: ...


class CreateActorUseCaseImpl(CreateActorUseCase):
    """
    CreateActorUseCaseImpl implements a command use case related to the Actor entity.
    """

    def __init__(self, unit_of_work: ActorUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[ActorCreateModel]) -> ActorReadModel:
        (data,) = args

        actor = ActorEntity(None, **data.model_dump())
        existing_actor = await self.unit_of_work.actors.find_one(
            first_name=data.first_name,
            last_name=data.last_name,
            birth_date=data.birth_date,
        )

        if existing_actor:
            if existing_actor.is_deleted:
                unmarked_actor = existing_actor.unmark_entity_as_deleted()
                created_actor = await self.unit_of_work.actors.update(unmarked_actor)
            else:
                raise ActorAlreadyExistsError
        else:
            created_actor = await self.unit_of_work.actors.create(actor)

        await self.unit_of_work.commit()

        return ActorReadModel.from_entity(cast(ActorEntity, created_actor))
