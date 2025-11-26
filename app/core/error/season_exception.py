"""
Season exception module.
"""

from app.core.error.base_exception import NotFoundError, ConflictError


class SeasonNotFoundError(NotFoundError):
    detail = "Season not found"


class SeasonAlreadyExistsError(ConflictError):
    detail = "Season already exists"


class SeasonAlreadyDeletedError(ConflictError):
    detail = "Season already deleted"
