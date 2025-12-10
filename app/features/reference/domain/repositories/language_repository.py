"""
Language repository module.
"""

from abc import ABC, abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.features.reference.domain.entities.language.language_entity import (
    LanguageEntity,
)


class LanguageRepository(BaseRepository[LanguageEntity], ABC):
    """
    LanguageRepository defines a repository interface for Language entity.
    """

    @abstractmethod
    async def find_by_code(self, code: str) -> LanguageEntity | None: ...
