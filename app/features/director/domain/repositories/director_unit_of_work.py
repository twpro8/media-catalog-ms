"""
Director unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.director.domain.repositories.director_repository import (
    DirectorRepository,
)


class DirectorUnitOfWork(AbstractUnitOfWork):
    """
    DirectorUnitOfWork defines an interface based on Unit of Work.
    """

    directors: DirectorRepository
