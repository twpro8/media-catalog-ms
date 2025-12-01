"""
Base exception module.
"""


class BaseError(Exception):
    detail: str = "Unexpected error"

    def __init__(
        self,
        detail: str | None = None,
        *args: object,
    ):
        self.detail = detail or self.detail
        super().__init__(self.detail, *args)

    def __str__(self) -> str:
        return self.detail


class EntityNotFoundError(BaseError):
    detail = "Entity Not Found Error"


class EntityAlreadyExistsError(BaseError):
    detail = "Entity Already Exists Error"
