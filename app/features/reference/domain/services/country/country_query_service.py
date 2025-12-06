"""
Country query service module.
"""

from abc import ABC, abstractmethod

from app.core.services.base_query_service import QueryService
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)


class CountryQueryService(QueryService[CountryReadModel], ABC):
    """
    CountryQueryService defines a query service interface.
    """

    @abstractmethod
    async def find_by_code(self, code: str) -> CountryReadModel | None: ...
