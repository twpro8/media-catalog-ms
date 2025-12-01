"""
Episode domain exceptions module.
"""

from app.core.error.base_exception import (
    BaseError,
    EntityNotFoundError,
    EntityAlreadyExistsError,
)


class EpisodeNotFoundError(EntityNotFoundError):
    detail = "Episode not found"


class EpisodeAlreadyExistsError(EntityAlreadyExistsError):
    detail = "Episode already exists"


class EpisodeAlreadyDeletedError(BaseError):
    detail = "Episode already deleted"
