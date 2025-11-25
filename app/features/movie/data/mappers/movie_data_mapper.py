from app.core.repositories.data_mapper import DataMapper
from app.features.movie.data.models.movie import Movie
from app.features.movie.domain.entities.movie_entity import MovieEntity


class MovieDataMapper(DataMapper):
    model = Movie
    entity = MovieEntity
