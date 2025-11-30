"""
Show-Actor association orm model module.
"""

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base


class ShowActor(Base):
    __tablename__ = "show_actor_associations"

    show_id: Mapped[UUID] = mapped_column(
        ForeignKey("shows.id_", ondelete="CASCADE"),
        primary_key=True,
    )
    actor_id: Mapped[UUID] = mapped_column(
        ForeignKey("actors.id_", ondelete="CASCADE"),
        primary_key=True,
    )
