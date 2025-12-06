"""
Country data mapper module.
"""

from app.core.repositories.data_mapper import DataMapper
from app.features.reference.data.models.country import Country
from app.features.reference.domain.entities.country.country_entity import (
    CountryEntity,
)


class CountryDataMapper(DataMapper[Country, CountryEntity]):
    """
    CountryDataMapper implements DataMapper.
    """

    model = Country
    entity = CountryEntity
