"""
Delete actor use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.core.error.actor_exception import (
    ActorAlreadyDeletedError,
    ActorNotFoundError,
)
from app.core.use_cases.use_case import BaseUseCase
from app.features.actor.domain.entities.actor_entity import ActorEntity
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.repositories.actor_unit_of_work import (
    ActorUnitOfWork,
)


class DeleteActorUseCase(BaseUseCase[tuple[UUID], ActorReadModel]):
    """
    DeleteActorUseCase defines a command use case interface related to the Actor entity.
    """

    unit_of_work: ActorUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> ActorReadModel: ...


class DeleteActorUseCaseImpl(DeleteActorUseCase):
    """
    DeleteActorUseCaseImpl implements a command use case related to the Actor entity.
    """

    def __init__(self, unit_of_work: ActorUnitOfWork):
        self.unit_of_work: ActorUnitOfWork = unit_of_work

    async def __call__(self, args: tuple[UUID]) -> ActorReadModel:
        (id_,) = args

        existing_actor = await self.unit_of_work.actors.find_by_id(id_)
        if existing_actor is None:
            raise ActorNotFoundError

        try:
            marked_actor = existing_actor.mark_entity_as_deleted()
        except InvalidOperationError:
            raise ActorAlreadyDeletedError

        deleted_actor = await self.unit_of_work.actors.update(marked_actor)

        await self.unit_of_work.commit()

        return ActorReadModel.from_entity(cast(ActorEntity, deleted_actor))
