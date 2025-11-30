"""
Director repository module.
"""

from app.core.repositories.base_repository import BaseRepository
from app.features.director.domain.entities.director_entity import DirectorEntity


class DirectorRepository(BaseRepository[DirectorEntity]):
    """
    DirectorRepository defines a repositories interface for Director entity.
    """

    pass
