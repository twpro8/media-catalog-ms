"""
Director exception module.
"""

from app.core.error.base_exception import NotFoundError, ConflictError


class DirectorNotFoundError(NotFoundError):
    detail = "Director not found"


class DirectorAlreadyExistsError(ConflictError):
    detail = "Director already exists"


class DirectorAlreadyDeletedError(ConflictError):
    detail = "Director already deleted"
