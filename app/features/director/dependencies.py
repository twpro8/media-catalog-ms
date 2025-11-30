"""
Director dependencies module.
"""

from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.director.data.repositories.director_repository_impl import (
    DirectorRepositoryImpl,
)
from app.features.director.data.repositories.director_unit_of_work_impl import (
    DirectorUnitOfWorkImpl,
)
from app.features.director.data.services.director_query_service_impl import (
    DirectorQueryServiceImpl,
)
from app.features.director.domain.repositories.director_repository import (
    DirectorRepository,
)
from app.features.director.domain.repositories.director_unit_of_work import (
    DirectorUnitOfWork,
)
from app.features.director.domain.services.director_query_service import (
    DirectorQueryService,
)
from app.features.director.domain.usecases.create_director import (
    CreateDirectorUseCase,
    CreateDirectorUseCaseImpl,
)
from app.features.director.domain.usecases.delete_director import (
    DeleteDirectorUseCase,
    DeleteDirectorUseCaseImpl,
)
from app.features.director.domain.usecases.get_director import (
    GetDirectorUseCase,
    GetDirectorUseCaseImpl,
)
from app.features.director.domain.usecases.get_directors import (
    GetDirectorsUseCase,
    GetDirectorsUseCaseImpl,
)
from app.features.director.domain.usecases.update_director import (
    UpdateDirectorUseCase,
    UpdateDirectorUseCaseImpl,
)


def get_director_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> DirectorQueryService:
    return DirectorQueryServiceImpl(session)


def get_director_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> DirectorRepository:
    return DirectorRepositoryImpl(session)


async def get_director_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    director_repository: Annotated[
        DirectorRepository, Depends(get_director_repository)
    ],
) -> AsyncGenerator[DirectorUnitOfWork]:
    async with DirectorUnitOfWorkImpl(session, director_repository) as uow:
        yield uow


def get_create_director_use_case(
    unit_of_work: Annotated[DirectorUnitOfWork, Depends(get_director_unit_of_work)],
) -> CreateDirectorUseCase:
    return CreateDirectorUseCaseImpl(unit_of_work)


def get_director_use_case(
    director_query_service: Annotated[
        DirectorQueryService, Depends(get_director_query_service)
    ],
) -> GetDirectorUseCase:
    return GetDirectorUseCaseImpl(director_query_service)


def get_directors_use_case(
    director_query_service: Annotated[
        DirectorQueryService, Depends(get_director_query_service)
    ],
) -> GetDirectorsUseCase:
    return GetDirectorsUseCaseImpl(director_query_service)


def get_update_director_use_case(
    unit_of_work: Annotated[DirectorUnitOfWork, Depends(get_director_unit_of_work)],
) -> UpdateDirectorUseCase:
    return UpdateDirectorUseCaseImpl(unit_of_work)


def get_delete_director_use_case(
    unit_of_work: Annotated[DirectorUnitOfWork, Depends(get_director_unit_of_work)],
) -> DeleteDirectorUseCase:
    return DeleteDirectorUseCaseImpl(unit_of_work)
