"""
Season entity module.
"""

import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError

if TYPE_CHECKING:
    from app.features.season.domain.entities.season_command_model import (
        SeasonUpdateModel,
    )


class SeasonEntity(object):
    """
    Season represents your collection of seasons as an entity.
    """

    def __init__(
        self,
        id_: UUID | None,
        show_id: UUID,
        title: str,
        season_number: int,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.show_id = show_id
        self.title = title
        self.season_number = season_number
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def update_entity(
        self,
        entity_update_model: "SeasonUpdateModel",
        get_update_data_fn: Callable[["SeasonUpdateModel"], dict[str, Any]],
    ) -> "SeasonEntity":
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> "SeasonEntity":
        if self.is_deleted:
            raise InvalidOperationError("Season is already marked as deleted")

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def unmark_as_deleted(self) -> "SeasonEntity":
        if not self.is_deleted:
            raise InvalidOperationError("Season is already unmarked as deleted.")

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = False

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SeasonEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
