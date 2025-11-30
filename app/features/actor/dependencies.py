"""
Actor dependencies module.
"""

from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.actor.data.repositories.actor_repository_impl import (
    ActorRepositoryImpl,
)
from app.features.actor.data.repositories.actor_unit_of_work_impl import (
    ActorUnitOfWorkImpl,
)
from app.features.actor.data.services.actor_query_service_impl import (
    ActorQueryServiceImpl,
)
from app.features.actor.domain.repositories.actor_repository import (
    ActorRepository,
)
from app.features.actor.domain.repositories.actor_unit_of_work import (
    ActorUnitOfWork,
)
from app.features.actor.domain.services.actor_query_service import (
    ActorQueryService,
)
from app.features.actor.domain.usecases.create_actor import (
    CreateActorUseCase,
    CreateActorUseCaseImpl,
)
from app.features.actor.domain.usecases.delete_actor import (
    DeleteActorUseCase,
    DeleteActorUseCaseImpl,
)
from app.features.actor.domain.usecases.get_actor import (
    GetActorUseCase,
    GetActorUseCaseImpl,
)
from app.features.actor.domain.usecases.get_actors import (
    GetActorsUseCase,
    GetActorsUseCaseImpl,
)
from app.features.actor.domain.usecases.update_actor import (
    UpdateActorUseCase,
    UpdateActorUseCaseImpl,
)


def get_actor_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ActorQueryService:
    return ActorQueryServiceImpl(session)


def get_actor_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ActorRepository:
    return ActorRepositoryImpl(session)


async def get_actor_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    actor_repository: Annotated[ActorRepository, Depends(get_actor_repository)],
) -> AsyncGenerator[ActorUnitOfWork]:
    async with ActorUnitOfWorkImpl(session, actor_repository) as uow:
        yield uow


def get_create_actor_use_case(
    unit_of_work: Annotated[ActorUnitOfWork, Depends(get_actor_unit_of_work)],
) -> CreateActorUseCase:
    return CreateActorUseCaseImpl(unit_of_work)


def get_actor_use_case(
    actor_query_service: Annotated[ActorQueryService, Depends(get_actor_query_service)],
) -> GetActorUseCase:
    return GetActorUseCaseImpl(actor_query_service)


def get_actors_use_case(
    actor_query_service: Annotated[ActorQueryService, Depends(get_actor_query_service)],
) -> GetActorsUseCase:
    return GetActorsUseCaseImpl(actor_query_service)


def get_update_actor_use_case(
    unit_of_work: Annotated[ActorUnitOfWork, Depends(get_actor_unit_of_work)],
) -> UpdateActorUseCase:
    return UpdateActorUseCaseImpl(unit_of_work)


def get_delete_actor_use_case(
    unit_of_work: Annotated[ActorUnitOfWork, Depends(get_actor_unit_of_work)],
) -> DeleteActorUseCase:
    return DeleteActorUseCaseImpl(unit_of_work)
