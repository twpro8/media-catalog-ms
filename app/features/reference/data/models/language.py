"""
Language orm model module.
"""

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base
from app.features.reference.domain.entities.language.language_entity import (
    LanguageEntity,
)
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)


class Language(Base):
    __tablename__ = "languages"

    code: Mapped[str] = mapped_column(String(2), primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    def to_entity(self):
        return LanguageEntity(
            code=self.code,
            name=self.name,
            active=self.active,
        )

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "active": self.active,
        }

    def to_read_model(self) -> LanguageReadModel:
        return LanguageReadModel(code=self.code, name=self.name, active=self.active)
