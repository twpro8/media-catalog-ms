"""
Show domain exceptions module.
"""

from app.core.error.base_exception import (
    BaseError,
    EntityNotFoundError,
    EntityAlreadyExistsError,
)


class ShowNotFoundError(EntityNotFoundError):
    detail = "Show not found"


class ShowAlreadyExistsError(EntityAlreadyExistsError):
    detail = "Show already exists"


class ShowAlreadyDeletedError(BaseError):
    detail = "Show already deleted"
