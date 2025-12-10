"""
Language query service module.
"""

from abc import ABC, abstractmethod

from app.core.services.base_query_service import QueryService
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)


class LanguageQueryService(QueryService[LanguageReadModel], ABC):
    """
    LanguageQueryService defines a query service interface.
    """

    @abstractmethod
    async def find_by_code(self, code: str) -> LanguageReadModel | None: ...
