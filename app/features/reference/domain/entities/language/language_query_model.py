"""
Language query model module.
"""

from pydantic import ConfigDict

from app.features.reference.domain.entities.language.language_entity import (
    LanguageEntity,
)
from app.features.reference.domain.entities.language.language_common_model import (
    LanguageBaseModel,
)


class LanguageReadModel(LanguageBaseModel):
    """
    LanguageReadModel represents data structure as a read model
    """

    active: bool

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: LanguageEntity) -> "LanguageReadModel":
        assert entity.active is not None

        return LanguageReadModel(
            code=entity.code,
            name=entity.name,
            active=entity.active,
        )
