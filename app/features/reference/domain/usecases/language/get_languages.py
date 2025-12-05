"""
Get languages use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.domain.services.language.language_query_service import (
    LanguageQueryService,
)


class GetLanguagesUseCase(BaseUseCase[None, Sequence[LanguageReadModel]]):
    """
    GetLanguagesUseCase defines a query use case interface related to the Language Entity.
    """

    service = LanguageQueryService

    async def __call__(self, args: None) -> Sequence[LanguageReadModel]: ...


class GetLanguagesUseCaseImpl(GetLanguagesUseCase):
    """
    GetLanguagesUseCaseImpl implements a query use case related to the Language entity.
    """

    def __init__(self, service: LanguageQueryService):
        self.service: LanguageQueryService = service

    async def __call__(self, args: None) -> Sequence[LanguageReadModel]:
        languages = await self.service.findall()
        return languages
