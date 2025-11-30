"""
Actor entity module.
"""

import copy
from datetime import date, datetime
from typing import TYPE_CHECKING, Any, Callable
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError

if TYPE_CHECKING:
    from app.features.actor.domain.entities.actor_command_model import (
        ActorUpdateModel,
    )


class ActorEntity(object):
    """
    Actor represents your collection of actors as an entity.
    """

    def __init__(
        self,
        id_: UUID | None,
        first_name: str,
        last_name: str,
        birth_date: date,
        bio: str | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.bio = bio
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def update_entity(
        self,
        entity_update_model: "ActorUpdateModel",
        get_update_data_fn: Callable[["ActorUpdateModel"], dict[str, Any]],
    ) -> "ActorEntity":
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> "ActorEntity":
        if self.is_deleted:
            raise InvalidOperationError("Actor is already marked as deleted")

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def unmark_entity_as_deleted(self) -> "ActorEntity":
        if not self.is_deleted:
            raise InvalidOperationError("Actor is already unmarked as deleted.")

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = False

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ActorEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
