"""
Language domain exceptions module.
"""

from app.core.error.base_exception import EntityNotFoundError, BaseError


class LanguageNotFoundError(EntityNotFoundError):
    detail = "Language not found"


class LanguageAlreadyActiveError(BaseError):
    detail = "Language already active"


class LanguageAlreadyInactiveError(BaseError):
    detail = "Language already inactive"
