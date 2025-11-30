"""
Get director use case module.
"""

from abc import abstractmethod
from uuid import UUID

from app.core.error.director_exception import DirectorNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.services.director_query_service import (
    DirectorQueryService,
)


class GetDirectorUseCase(BaseUseCase[tuple[UUID], DirectorReadModel]):
    """
    GetDirectorUseCase defines a query use case interface related to the Director Entity.
    """

    service: DirectorQueryService

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> DirectorReadModel: ...


class GetDirectorUseCaseImpl(GetDirectorUseCase):
    """
    GetDirectorUseCaseImpl implements a query use case related to the Director entity.
    """

    def __init__(self, service: DirectorQueryService):
        self.service: DirectorQueryService = service

    async def __call__(self, args: tuple[UUID]) -> DirectorReadModel:
        (id_,) = args

        director = await self.service.find_by_id(id_)
        if director is None or director.is_deleted:
            raise DirectorNotFoundError

        return director
