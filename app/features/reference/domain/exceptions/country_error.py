"""
Country domain exceptions module.
"""

from app.core.error.base_exception import BaseError, EntityNotFoundError


class CountryNotFoundError(EntityNotFoundError):
    detail = "Country not found"


class CountryAlreadyActiveError(BaseError):
    detail = "Country already active"


class CountryAlreadyInactiveError(BaseError):
    detail = "Country already inactive"
