"""
Season unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.season.domain.repositories.season_unit_of_work import SeasonUnitOfWork
from app.features.season.domain.repositories.season_repository import SeasonRepository
from app.features.show.domain.repositories.show_repository import ShowRepository


class SeasonUnitOfWorkImpl(SQLAlchemyUnitOfWork, SeasonUnitOfWork):
    """
    Season unit of work implementation.
    """

    def __init__(
        self,
        session: AsyncSession,
        season_repository: SeasonRepository,
        show_repository: ShowRepository,
    ):
        super().__init__(session)
        self.seasons: SeasonRepository = season_repository
        self.shows: ShowRepository = show_repository
