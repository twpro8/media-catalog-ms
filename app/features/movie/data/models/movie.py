"""
Movie orm model module.
"""

from decimal import Decimal
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DECIMAL, String, UniqueConstraint, CheckConstraint

from app.core.models.postgres.models import Base


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
