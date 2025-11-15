from polyfactory.factories.pydantic_factory import ModelFactory

from app.features.movie.domain.entities.movie_command_model import (
    MovieCreateModel,
    MovieUpdateModel,
)


class MovieCreateModelFactory(ModelFactory[MovieCreateModel]): ...


class MovieUpdateModelFactory(ModelFactory[MovieUpdateModel]): ...
