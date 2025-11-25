"""
Show unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.show.domain.repositories.show_unit_of_work import ShowUnitOfWork
from app.features.show.domain.repositories.show_repository import ShowRepository


class ShowUnitOfWorkImpl(SQLAlchemyUnitOfWork, ShowUnitOfWork):
    """
    Show unit of work implementation.
    """

    def __init__(
        self,
        session: AsyncSession,
        show_repository: ShowRepository,
    ):
        super().__init__(session)
        self.shows: ShowRepository = show_repository
