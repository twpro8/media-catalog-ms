"""
Episode orm model module.
"""

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint, ForeignKey

from app.core.models.postgres.models import Base

if TYPE_CHECKING:
    from app.features.season.data.models.season import Season


class Episode(Base):
    __tablename__ = "episodes"
    __table_args__ = (
        UniqueConstraint(
            "season_id",
            "episode_number",
            name="uq_episode",
        ),
    )

    season_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("seasons.id_", ondelete="CASCADE"),
    )
    title: Mapped[str] = mapped_column(String(length=256))
    episode_number: Mapped[int]
    duration: Mapped[int | None]
    release_date: Mapped[date]

    # Relationships
    season: Mapped["Season"] = relationship(back_populates="episodes")

    def to_dict(self):
        return {
            "id_": self.id_,
            "season_id": self.season_id,
            "title": self.title,
            "episode_number": self.episode_number,
            "duration": self.duration,
            "release_date": self.release_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
        }
