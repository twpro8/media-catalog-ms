"""
Actor orm model module.
"""

from datetime import date, datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import String, UniqueConstraint, text, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.postgres.models import Base
from app.features.actor.domain.entities.actor_query_model import ActorReadModel

if TYPE_CHECKING:
    from app.features.movie.data.models.movie import Movie
    from app.features.show.data.models.show import Show


class Actor(Base):
    __tablename__ = "actors"
    __table_args__ = (
        UniqueConstraint(
            "first_name",
            "last_name",
            "birth_date",
            name="uq_actor",
        ),
    )

    id_: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuidv7()"),
    )
    first_name: Mapped[str] = mapped_column(String(48))
    last_name: Mapped[str] = mapped_column(String(48))
    birth_date: Mapped[date]
    bio: Mapped[str | None] = mapped_column(String(1024))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('UTC', now())"),
    )
    # Add a trigger on update updated_at for this entity.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('UTC', now())"),
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationships
    movies: Mapped[list["Movie"]] = relationship(
        secondary="movie_actor_associations",
        back_populates="actors",
    )
    shows: Mapped[list["Show"]] = relationship(
        secondary="show_actor_associations",
        back_populates="actors",
    )

    def to_dict(self) -> dict:
        return {
            "id_": self.id_,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "bio": self.bio,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
        }

    def to_read_model(self) -> ActorReadModel:
        return ActorReadModel(
            id_=self.id_,
            first_name=self.first_name,
            last_name=self.last_name,
            birth_date=self.birth_date,
            bio=self.bio,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )
