"""
Update actor use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.features.actor.domain.exceptions import ActorNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.actor.domain.entities.actor_command_model import (
    ActorUpdateModel,
)
from app.features.actor.domain.entities.actor_entity import ActorEntity
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.repositories.actor_unit_of_work import (
    ActorUnitOfWork,
)


class UpdateActorUseCase(BaseUseCase[tuple[UUID, ActorUpdateModel], ActorReadModel]):
    """
    UpdateActorUseCase defines a query use case interface related to the Actor Entity.
    """

    unit_of_work: ActorUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID, ActorUpdateModel]) -> ActorReadModel: ...


class UpdateActorUseCaseImpl(UpdateActorUseCase):
    """
    UpdateActorUseCaseImpl implements a query use case related to the Actor entity.
    """

    def __init__(self, unit_of_work: ActorUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[UUID, ActorUpdateModel]) -> ActorReadModel:
        id_, update_data = args

        existing_actor = await self.unit_of_work.actors.find_by_id(id_)
        if not existing_actor or existing_actor.is_deleted:
            raise ActorNotFoundError

        update_entity = existing_actor.update_entity(
            update_data,
            lambda actor_data: update_data.model_dump(exclude_unset=True),
        )

        updated_actor = await self.unit_of_work.actors.update(update_entity)
        await self.unit_of_work.commit()

        return ActorReadModel.from_entity(cast(ActorEntity, updated_actor))
