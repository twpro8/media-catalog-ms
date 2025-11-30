from app.core.repositories.data_mapper import DataMapper
from app.features.actor.data.models.actor import Actor
from app.features.actor.domain.entities.actor_entity import ActorEntity


class ActorDataMapper(DataMapper):
    model = Actor
    entity = ActorEntity
