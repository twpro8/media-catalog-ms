"""
Movie orm model module.
"""

from decimal import Decimal
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DECIMAL, String, UniqueConstraint, CheckConstraint

from app.core.models.postgres.models import Base
from app.features.movie.domain.entities.movie_query_model import MovieReadModel


class Movie(Base):
    __tablename__ = "movies"
    __table_args__ = (
        UniqueConstraint("title", "release_date", name="uq_movie"),
        CheckConstraint("rating >= 0 AND rating <= 10"),
    )

    title: Mapped[str] = mapped_column(String(length=256))
    description: Mapped[str] = mapped_column(String(length=1024))
    release_date: Mapped[date]
    rating: Mapped[Decimal] = mapped_column(DECIMAL(3, 1), default=Decimal("0.0"))
    duration: Mapped[int | None]

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
