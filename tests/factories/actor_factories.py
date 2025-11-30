from polyfactory.factories.pydantic_factory import ModelFactory

from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
    ActorUpdateModel,
)


class ActorCreateModelFactory(ModelFactory[ActorCreateModel]): ...


class ActorUpdateModelFactory(ModelFactory[ActorUpdateModel]): ...
