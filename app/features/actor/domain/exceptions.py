"""
Actor domain exceptions module.
"""

from app.core.error.base_exception import (
    BaseError,
    EntityNotFoundError,
    EntityAlreadyExistsError,
)


class ActorNotFoundError(EntityNotFoundError):
    detail = "Actor not found"


class ActorAlreadyExistsError(EntityAlreadyExistsError):
    detail = "Actor already exists"


class ActorAlreadyDeletedError(BaseError):
    detail = "Actor already deleted"
