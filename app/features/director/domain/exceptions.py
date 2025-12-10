"""
Director domain exceptions module.
"""

from app.core.error.base_exception import (
    BaseError,
    EntityNotFoundError,
    EntityAlreadyExistsError,
)


class DirectorNotFoundError(EntityNotFoundError):
    detail = "Director not found"


class DirectorAlreadyExistsError(EntityAlreadyExistsError):
    detail = "Director already exists"


class DirectorAlreadyDeletedError(BaseError):
    detail = "Director already deleted"
