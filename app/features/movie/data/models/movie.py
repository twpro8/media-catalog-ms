"""
Movie orm model module.
"""

from decimal import Decimal
from datetime import date, datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    DECIMAL,
    String,
    UniqueConstraint,
    CheckConstraint,
    DateTime,
    text,
    Boolean,
)

from app.core.models.postgres.models import Base
from app.features.movie.domain.entities.movie_query_model import MovieReadModel

if TYPE_CHECKING:
    from app.features.director.data.models.director import Director


class Movie(Base):
    __tablename__ = "movies"
    __table_args__ = (
        UniqueConstraint("title", "release_date", name="uq_movie"),
        CheckConstraint("rating >= 0 AND rating <= 10"),
    )

    id_: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuidv7()"),
    )
    title: Mapped[str] = mapped_column(String(length=256))
    description: Mapped[str] = mapped_column(String(length=1024))
    release_date: Mapped[date]
    rating: Mapped[Decimal] = mapped_column(DECIMAL(3, 1), default=Decimal("0.0"))
    duration: Mapped[int | None]
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
    directors: Mapped[list["Director"]] = relationship(
        secondary="movie_director_associations",
        back_populates="movies",
    )

    def to_dict(self):
        return {
            "id_": self.id_,
            "title": self.title,
            "description": self.description,
            "release_date": self.release_date,
            "rating": self.rating,
            "duration": self.duration,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
        }

    def to_read_model(self) -> MovieReadModel:
        return MovieReadModel(
            id_=self.id_,
            title=self.title,
            description=self.description,
            release_date=self.release_date,
            rating=self.rating,
            duration=self.duration,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )
