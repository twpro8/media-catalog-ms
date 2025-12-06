"""
Country orm model module.
"""

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.postgres.models import Base
from app.features.reference.domain.entities.country.country_entity import (
    CountryEntity,
)
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)


class Country(Base):
    __tablename__ = "countries"

    code: Mapped[str] = mapped_column(String(2), primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    def to_entity(self):
        return CountryEntity(
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

    def to_read_model(self) -> CountryReadModel:
        return CountryReadModel(code=self.code, name=self.name)
