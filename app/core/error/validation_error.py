from app.core.error.base_exception import BaseError


class ValidationError(BaseError):
    status_code = 422
    detail = "Validation Error"


class FieldRequiredError(ValidationError):
    detail = "At least one field is required"
