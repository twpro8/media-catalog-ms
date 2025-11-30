from polyfactory.factories.pydantic_factory import ModelFactory

from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
    DirectorUpdateModel,
)


class DirectorCreateModelFactory(ModelFactory[DirectorCreateModel]): ...


class DirectorUpdateModelFactory(ModelFactory[DirectorUpdateModel]): ...
