from app.core.error.base_exception import BaseError


class FieldRequiredError(BaseError):
    detail = "At least one field is required"
