"""
Language orm model module.
"""

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base


class Language(Base):
    __tablename__ = "languages"

    code: Mapped[str] = mapped_column(String(2), primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    active: Mapped[bool] = mapped_column(Boolean, default=True)
