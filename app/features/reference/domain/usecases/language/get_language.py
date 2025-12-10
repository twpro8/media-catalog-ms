"""
Get language use case module.
"""

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.domain.exceptions.language_error import (
    LanguageNotFoundError,
)
from app.features.reference.domain.services.language_query_service import (
    LanguageQueryService,
)


class GetLanguageUseCase(BaseUseCase[str, LanguageReadModel]):
    """
    GetLanguageUseCase defines a query use case interface related to the Language Entity.
    """

    service = LanguageQueryService

    async def __call__(self, code: str) -> LanguageReadModel: ...


class GetLanguageUseCaseImpl(GetLanguageUseCase):
    """
    GetLanguageUseCaseImpl implements a query use case related to the Language entity.
    """

    def __init__(self, service: LanguageQueryService):
        self.service = service

    async def __call__(self, code: str) -> LanguageReadModel:
        language = await self.service.find_by_code(code)
        if not language:
            raise LanguageNotFoundError

        return language
