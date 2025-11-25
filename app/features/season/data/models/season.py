"""
Season orm model module.
"""

from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint, ForeignKey, String

from app.core.models.postgres.models import Base

if TYPE_CHECKING:
    from app.features.show.data.models.show import Show
    from app.features.episode.data.models.episode import Episode


class Season(Base):
    __tablename__ = "seasons"
    __table_args__ = (
        UniqueConstraint(
            "show_id",
            "season_number",
            name="uq_season",
        ),
    )

    show_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("shows.id_", ondelete="CASCADE"),
    )
    title: Mapped[str] = mapped_column(String(length=256))
    season_number: Mapped[int]

    # Relationships
    show: Mapped["Show"] = relationship(back_populates="seasons")
    episodes: Mapped[list["Episode"]] = relationship(back_populates="season")

    def to_dict(self):
        return {
            "id_": self.id_,
            "title": self.title,
            "season_number": self.season_number,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
        }
