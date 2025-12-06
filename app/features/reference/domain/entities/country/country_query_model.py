"""
Country query model module.
"""

from pydantic import ConfigDict

from app.features.reference.domain.entities.country.country_entity import (
    CountryEntity,
)
from app.features.reference.domain.entities.country.country_common_model import (
    CountryBaseModel,
)


class CountryReadModel(CountryBaseModel):
    """
    CountryReadModel represents data structure as a read model
    """

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: CountryEntity) -> "CountryReadModel":
        return CountryReadModel(code=entity.code, name=entity.name)
