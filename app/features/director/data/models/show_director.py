"""
Show-Director association orm model module.
"""

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base


class ShowDirector(Base):
    __tablename__ = "show_director_associations"

    show_id: Mapped[UUID] = mapped_column(
        ForeignKey("shows.id_", ondelete="CASCADE"),
        primary_key=True,
    )
    director_id: Mapped[UUID] = mapped_column(
        ForeignKey("directors.id_", ondelete="CASCADE"),
        primary_key=True,
    )
