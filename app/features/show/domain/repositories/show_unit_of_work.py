"""
Show unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.show.domain.repositories.show_repository import ShowRepository


class ShowUnitOfWork(AbstractUnitOfWork):
    """
    ShowUnitOfWork defines an interface based on Unit of Work.
    """

    shows: ShowRepository
