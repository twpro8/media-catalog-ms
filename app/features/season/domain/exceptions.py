"""
Season domain exceptions module.
"""

from app.core.error.base_exception import (
    BaseError,
    EntityNotFoundError,
    EntityAlreadyExistsError,
)


class SeasonNotFoundError(EntityNotFoundError):
    detail = "Season not found"


class SeasonAlreadyExistsError(EntityAlreadyExistsError):
    detail = "Season already exists"


class SeasonAlreadyDeletedError(BaseError):
    detail = "Season already deleted"
