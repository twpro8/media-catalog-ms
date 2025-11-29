"""
Episode orm model module.
"""

from datetime import date, datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint, ForeignKey, text, DateTime, Boolean

from app.core.models.postgres.models import Base
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel

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

    id_: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuidv7()"),
    )
    season_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("seasons.id_", ondelete="CASCADE"),
    )
    title: Mapped[str] = mapped_column(String(length=256))
    episode_number: Mapped[int]
    duration: Mapped[int | None]
    release_date: Mapped[date]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('UTC', now())"),
    )
    # Add triggers on update updated_at for each entity.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('UTC', now())"),
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

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

    def to_read_model(self) -> EpisodeReadModel:
        return EpisodeReadModel(
            id_=self.id_,
            season_id=self.season_id,
            title=self.title,
            episode_number=self.episode_number,
            duration=self.duration,
            release_date=self.release_date,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )
