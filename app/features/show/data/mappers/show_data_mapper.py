from app.core.repositories.data_mapper import DataMapper
from app.features.show.data.models.show import Show
from app.features.show.domain.entities.show_entity import ShowEntity


class ShowDataMapper(DataMapper):
    model = Show
    entity = ShowEntity
