"""
Director orm model module.
"""

from datetime import date, datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import String, UniqueConstraint, text, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.postgres.models import Base

if TYPE_CHECKING:
    from app.features.movie.data.models.movie import Movie
    from app.features.show.data.models.show import Show


class Director(Base):
    __tablename__ = "directors"
    __table_args__ = (
        UniqueConstraint(
            "first_name",
            "last_name",
            "birth_date",
            name="uq_director",
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
        secondary="movie_director_associations",
        back_populates="directors",
    )
    shows: Mapped[list["Show"]] = relationship(
        secondary="show_director_associations",
        back_populates="directors",
    )
