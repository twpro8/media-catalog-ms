"""
Reference unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.reference.domain.repositories.country_repository import (
    CountryRepository,
)
from app.features.reference.domain.repositories.language_repository import (
    LanguageRepository,
)
from app.features.reference.domain.repositories.reference_unit_of_work import (
    ReferenceUnitOfWork,
)


class ReferenceUnitOfWorkImpl(SQLAlchemyUnitOfWork, ReferenceUnitOfWork):
    """
    ReferenceUnitOfWorkImpl implements Unit of Work pattern for Reference features.
    """

    def __init__(
        self,
        session: AsyncSession,
        country_repository: CountryRepository,
        language_repository: LanguageRepository,
    ):
        super().__init__(session)
        self.countries = country_repository
        self.languages = language_repository
