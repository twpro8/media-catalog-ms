"""
Language entity module.
"""

import copy

from app.features.reference.domain.exceptions.language_error import (
    LanguageAlreadyActiveError,
    LanguageAlreadyInactiveError,
)


class LanguageEntity(object):
    """
    Language represents your collection of languages as an entity.
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

    def mark_entity_as_active(self) -> "LanguageEntity":
        if self.active:
            raise LanguageAlreadyActiveError

        marked_entity = copy.deepcopy(self)
        marked_entity.active = True

        return marked_entity

    def mark_entity_as_inactive(self) -> "LanguageEntity":
        if not self.active:
            raise LanguageAlreadyInactiveError

        marked_entity = copy.deepcopy(self)
        marked_entity.active = False

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, LanguageEntity):
            return self.code == other.code

        return False

    def to_popo(self) -> object:
        return self.__dict__
