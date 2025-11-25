"""
Get show use case module.
"""

from abc import abstractmethod
from uuid import UUID

from app.core.error.show_exception import ShowNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.services.show_query_service import ShowQueryService


class GetShowUseCase(BaseUseCase[tuple[UUID], ShowReadModel]):
    """
    GetShowUseCase defines a query use case interface related to the Show Entity.
    """

    service: ShowQueryService

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> ShowReadModel: ...


class GetShowUseCaseImpl(GetShowUseCase):
    """
    GetShowUseCaseImpl implements a query use case related to the Show entity.
    """

    def __init__(self, service: ShowQueryService):
        self.service: ShowQueryService = service

    async def __call__(self, args: tuple[UUID]) -> ShowReadModel:
        (id_,) = args

        show = await self.service.find_by_id(id_)
        if show is None or show.is_deleted:
            raise ShowNotFoundError

        return show
