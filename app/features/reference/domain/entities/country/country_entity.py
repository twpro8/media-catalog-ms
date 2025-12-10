"""
Country entity module.
"""

import copy

from app.features.reference.domain.exceptions.country_error import (
    CountryAlreadyActiveError,
    CountryAlreadyInactiveError,
)


class CountryEntity(object):
    """
    Country represents your collection of countries as an entity.
    """

    def __init__(
        self,
        code: str,
        name: str,
        active: bool | None = True,
    ):
        self.code = code
        self.name = name
        self.active = active

    def mark_entity_as_active(self) -> "CountryEntity":
        if self.active:
            raise CountryAlreadyActiveError

        marked_entity = copy.deepcopy(self)
        marked_entity.active = True

        return marked_entity

    def mark_entity_as_inactive(self) -> "CountryEntity":
        if not self.active:
            raise CountryAlreadyInactiveError

        marked_entity = copy.deepcopy(self)
        marked_entity.active = False

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CountryEntity):
            return self.code == other.code

        return False

    def to_popo(self) -> object:
        return self.__dict__
