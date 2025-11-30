from app.core.repositories.data_mapper import DataMapper
from app.features.director.data.models.director import Director
from app.features.director.domain.entities.director_entity import DirectorEntity


class DirectorDataMapper(DataMapper):
    model = Director
    entity = DirectorEntity
