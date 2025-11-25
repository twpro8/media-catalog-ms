"""
Show exception module.
"""

from app.core.error.base_exception import NotFoundError, ConflictError


class ShowNotFoundError(NotFoundError):
    detail = "Show not found"


class ShowAlreadyExistsError(ConflictError):
    detail = "Show already exists"


class ShowAlreadyDeletedError(ConflictError):
    detail = "Show already deleted"
