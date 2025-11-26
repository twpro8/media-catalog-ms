from app.core.repositories.data_mapper import DataMapper
from app.features.season.data.models.season import Season
from app.features.season.domain.entities.season_entity import SeasonEntity


class SeasonDataMapper(DataMapper):
    model = Season
    entity = SeasonEntity
