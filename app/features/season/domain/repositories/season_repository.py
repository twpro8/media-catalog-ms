"""
Season repository module.
"""

from abc import abstractmethod
from uuid import UUID

from app.core.repositories.base_repository import BaseRepository
from app.features.season.domain.entities.season_entity import SeasonEntity


class SeasonRepository(BaseRepository[SeasonEntity]):
    """
    SeasonRepository defines a repositories interface for Season entity.
    """

    @abstractmethod
    async def find_by_show_and_number(
        self, show_id: UUID, season_number: int
    ) -> SeasonEntity | None: ...
