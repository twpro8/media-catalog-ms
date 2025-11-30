"""
Movie-Actor association orm model module.
"""

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base


class MovieActor(Base):
    __tablename__ = "movie_actor_associations"

    movie_id: Mapped[UUID] = mapped_column(
        ForeignKey("movies.id_", ondelete="CASCADE"),
        primary_key=True,
    )
    actor_id: Mapped[UUID] = mapped_column(
        ForeignKey("actors.id_", ondelete="CASCADE"),
        primary_key=True,
    )
