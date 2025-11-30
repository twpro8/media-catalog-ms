"""
Movie-Director association orm model module.
"""

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base


class MovieDirector(Base):
    __tablename__ = "movie_director_associations"

    movie_id: Mapped[UUID] = mapped_column(
        ForeignKey("movies.id_", ondelete="CASCADE"),
        primary_key=True,
    )
    director_id: Mapped[UUID] = mapped_column(
        ForeignKey("directors.id_", ondelete="CASCADE"),
        primary_key=True,
    )
