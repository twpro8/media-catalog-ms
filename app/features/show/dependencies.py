"""
Show dependencies module.
"""

from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.show.data.repositories.show_repository_impl import (
    ShowRepositoryImpl,
)
from app.features.show.data.repositories.show_unit_of_work_impl import (
    ShowUnitOfWorkImpl,
)
from app.features.show.data.services.show_query_service_impl import (
    ShowQueryServiceImpl,
)
from app.features.show.domain.repositories.show_repository import ShowRepository
from app.features.show.domain.repositories.show_unit_of_work import ShowUnitOfWork
from app.features.show.domain.services.show_query_service import ShowQueryService
from app.features.show.domain.usecases.create_show import (
    CreateShowUseCase,
    CreateShowUseCaseImpl,
)
from app.features.show.domain.usecases.delete_show import (
    DeleteShowUseCase,
    DeleteShowUseCaseImpl,
)
from app.features.show.domain.usecases.get_show import (
    GetShowUseCase,
    GetShowUseCaseImpl,
)
from app.features.show.domain.usecases.get_shows import (
    GetShowsUseCase,
    GetShowsUseCaseImpl,
)
from app.features.show.domain.usecases.update_show import (
    UpdateShowUseCase,
    UpdateShowUseCaseImpl,
)


def get_show_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ShowQueryService:
    return ShowQueryServiceImpl(session)


def get_show_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ShowRepository:
    return ShowRepositoryImpl(session)


async def get_show_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    show_repository: Annotated[ShowRepository, Depends(get_show_repository)],
) -> AsyncGenerator[ShowUnitOfWork, None]:
    async with ShowUnitOfWorkImpl(session, show_repository) as uow:
        yield uow


def get_create_show_use_case(
    unit_of_work: Annotated[ShowUnitOfWork, Depends(get_show_unit_of_work)],
) -> CreateShowUseCase:
    return CreateShowUseCaseImpl(unit_of_work)


def get_show_use_case(
    show_query_service: Annotated[ShowQueryService, Depends(get_show_query_service)],
) -> GetShowUseCase:
    return GetShowUseCaseImpl(show_query_service)


def get_shows_use_case(
    show_query_service: Annotated[ShowQueryService, Depends(get_show_query_service)],
) -> GetShowsUseCase:
    return GetShowsUseCaseImpl(show_query_service)


def get_update_show_use_case(
    unit_of_work: Annotated[ShowUnitOfWork, Depends(get_show_unit_of_work)],
) -> UpdateShowUseCase:
    return UpdateShowUseCaseImpl(unit_of_work)


def get_delete_show_use_case(
    unit_of_work: Annotated[ShowUnitOfWork, Depends(get_show_unit_of_work)],
) -> DeleteShowUseCase:
    return DeleteShowUseCaseImpl(unit_of_work)
