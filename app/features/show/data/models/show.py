"""
Show orm model module.
"""

from decimal import Decimal
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DECIMAL, String, UniqueConstraint, CheckConstraint

from app.core.models.postgres.models import Base
from app.features.show.domain.entities.show_entity import ShowEntity
from app.features.show.domain.entities.show_query_model import ShowReadModel


class Show(Base):
    __tablename__ = "shows"
    __table_args__ = (
        UniqueConstraint("title", "release_date", name="uq_show"),
        CheckConstraint("rating >= 0 AND rating <= 10"),
    )

    title: Mapped[str] = mapped_column(String(length=256))
    description: Mapped[str] = mapped_column(String(length=1024))
    release_date: Mapped[date]
    rating: Mapped[Decimal] = mapped_column(DECIMAL(3, 1), default=Decimal("0.0"))

    def to_entity(self) -> ShowEntity:
        return ShowEntity(
            id_=self.id_,
            title=self.title,
            description=self.description,
            release_date=self.release_date,
            rating=self.rating,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )

    def to_dict(self):
        return {
            "id_": self.id_,
            "title": self.title,
            "description": self.description,
            "release_date": self.release_date,
            "rating": self.rating,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
        }

    def to_read_model(self) -> ShowReadModel:
        return ShowReadModel(
            id_=self.id_,
            title=self.title,
            description=self.description,
            release_date=self.release_date,
            rating=self.rating,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )

    @staticmethod
    def from_entity(show: ShowEntity) -> "Show":
        return Show(
            id_=show.id_,
            title=show.title,
            description=show.description,
            release_date=show.release_date,
            rating=show.rating,
            created_at=show.created_at,
            updated_at=show.updated_at,
            is_deleted=show.is_deleted,
        )
