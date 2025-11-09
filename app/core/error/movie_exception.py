"""
Movie exception module.
"""

from app.core.error.base_exception import NotFoundError, ConflictError


class MovieNotFoundError(NotFoundError):
    detail = "Movie not found"


class MovieAlreadyExistsError(ConflictError):
    detail = "Movie already exists"


class MovieAlreadyDeletedError(ConflictError):
    detail = "Movie already deleted"
