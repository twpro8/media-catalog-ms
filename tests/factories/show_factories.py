from polyfactory.factories.pydantic_factory import ModelFactory

from app.features.show.domain.entities.show_command_model import (
    ShowCreateModel,
    ShowUpdateModel,
)


class ShowCreateModelFactory(ModelFactory[ShowCreateModel]): ...


class ShowUpdateModelFactory(ModelFactory[ShowUpdateModel]): ...
