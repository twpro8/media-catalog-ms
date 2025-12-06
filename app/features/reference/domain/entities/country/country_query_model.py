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

    active: bool

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: CountryEntity) -> "CountryReadModel":
        assert entity.active is not None

        return CountryReadModel(
            code=entity.code,
            name=entity.name,
            active=entity.active,
        )
