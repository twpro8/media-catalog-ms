"""
Actor exception module.
"""

from app.core.error.base_exception import NotFoundError, ConflictError


class ActorNotFoundError(NotFoundError):
    detail = "Actor not found"


class ActorAlreadyExistsError(ConflictError):
    detail = "Actor already exists"


class ActorAlreadyDeletedError(ConflictError):
    detail = "Actor already deleted"
