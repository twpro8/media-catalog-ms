"""
Movie domain exceptions module.
"""

from app.core.error.base_exception import (
    BaseError,
    EntityNotFoundError,
    EntityAlreadyExistsError,
)


class MovieNotFoundError(EntityNotFoundError):
    detail = "Movie not found"


class MovieAlreadyExistsError(EntityAlreadyExistsError):
    detail = "Movie already exists"


class MovieAlreadyDeletedError(BaseError):
    detail = "Movie already deleted"
