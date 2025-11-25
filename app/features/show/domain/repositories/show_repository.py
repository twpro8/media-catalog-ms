"""
Show repository module.
"""

from abc import abstractmethod
from datetime import date

from app.core.repositories.base_repository import BaseRepository
from app.features.show.domain.entities.show_entity import ShowEntity


class ShowRepository(BaseRepository[ShowEntity]):
    """
    ShowRepository defines a repositories interface for Show entity.
    """

    @abstractmethod
    async def find_by_title_and_date(
        self, title: str, release_date: date
    ) -> ShowEntity | None: ...
