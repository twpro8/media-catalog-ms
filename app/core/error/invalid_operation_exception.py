from app.core.error.base_exception import BaseError


class InvalidOperationError(BaseError):
    detail = "Invalid Operation on entity"
