"""
Episode entity module.
"""

import copy
from datetime import datetime, date
from typing import Any, Callable, TYPE_CHECKING
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError

if TYPE_CHECKING:
    from app.features.episode.domain.entities.episode_command_model import (
        EpisodeUpdateModel,
    )


class EpisodeEntity(object):
    """
    Episode represents your collection of episodes as an entity.
    """

    def __init__(
        self,
        id_: UUID | None,
        season_id: UUID,
        title: str,
        episode_number: int,
        release_date: date,
        duration: int | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.title = title
        self.episode_number = episode_number
        self.season_id = season_id
        self.release_date = release_date
        self.duration = duration
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def update_entity(
        self,
        entity_update_model: "EpisodeUpdateModel",
        get_update_data_fn: Callable[["EpisodeUpdateModel"], dict[str, Any]],
    ) -> "EpisodeEntity":
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> "EpisodeEntity":
        if self.is_deleted:
            raise InvalidOperationError("Episode is already marked as deleted")

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def unmark_entity_as_deleted(self) -> "EpisodeEntity":
        if not self.is_deleted:
            raise InvalidOperationError("Episode is already unmarked as deleted.")

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = False

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, EpisodeEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
