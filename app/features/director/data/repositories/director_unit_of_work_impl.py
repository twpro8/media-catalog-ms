"""
Director unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.director.domain.repositories.director_unit_of_work import (
    DirectorUnitOfWork,
)
from app.features.director.domain.repositories.director_repository import (
    DirectorRepository,
)


class DirectorUnitOfWorkImpl(SQLAlchemyUnitOfWork, DirectorUnitOfWork):
    """
    Director unit of work implementation.
    """

    def __init__(
        self,
        session: AsyncSession,
        director_repository: DirectorRepository,
    ):
        super().__init__(session)
        self.directors: DirectorRepository = director_repository
