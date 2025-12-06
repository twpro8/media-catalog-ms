"""
Country repository module.
"""

from abc import ABC, abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.features.reference.domain.entities.country.country_entity import (
    CountryEntity,
)


class CountryRepository(BaseRepository[CountryEntity], ABC):
    """
    CountryRepository defines a repository interface for Country entity.
    """

    @abstractmethod
    async def find_by_code(self, code: str) -> CountryEntity | None: ...
