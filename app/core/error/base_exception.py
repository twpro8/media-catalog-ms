"""
Base exception module.
"""


class BaseError(Exception):
    status_code: int = 500
    detail: str = "Unexpected error"

    def __init__(
        self,
        detail: str | None = None,
        status_code: int | None = None,
        *args: object,
    ):
        self.status_code = status_code or self.status_code
        self.detail = detail or self.detail
        super().__init__(self.detail, *args)

    def __str__(self) -> str:
        return self.detail


class NotFoundError(BaseError):
    status_code = 404
    detail = "Not Found Error"


class ConflictError(BaseError):
    status_code = 409
    detail = "Already Exists Error"
