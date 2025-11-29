"""
Episode exception module.
"""

from app.core.error.base_exception import ConflictError, NotFoundError


class EpisodeNotFoundError(NotFoundError):
    detail = "Episode not found"


class EpisodeAlreadyExistsError(ConflictError):
    detail = "Episode already exists"
