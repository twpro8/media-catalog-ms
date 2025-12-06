"""
Language data mapper module.
"""

from app.core.repositories.data_mapper import DataMapper
from app.features.reference.data.models.language import Language
from app.features.reference.domain.entities.language.language_entity import (
    LanguageEntity,
)


class LanguageDataMapper(DataMapper[Language, LanguageEntity]):
    """
    LanguageDataMapper implements DataMapper.
    """

    model = Language
    entity = LanguageEntity
