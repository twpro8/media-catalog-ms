"""
Season unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.season.domain.repositories.season_repository import SeasonRepository
from app.features.show.domain.repositories.show_repository import ShowRepository


class SeasonUnitOfWork(AbstractUnitOfWork):
    """
    SeasonUnitOfWork defines an interface based on Unit of Work.
    """

    seasons: SeasonRepository
    shows: ShowRepository
