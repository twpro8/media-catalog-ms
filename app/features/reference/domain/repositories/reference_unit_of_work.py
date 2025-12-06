"""
Reference unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.reference.domain.repositories.country_repository import (
    CountryRepository,
)
from app.features.reference.domain.repositories.language_repository import (
    LanguageRepository,
)


class ReferenceUnitOfWork(AbstractUnitOfWork):
    """
    ReferenceUnitOfWork defines an interface based on Unit of Work.
    """

    countries: CountryRepository
    languages: LanguageRepository
