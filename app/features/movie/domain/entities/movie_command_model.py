"""
Movie command model module.
"""

from datetime import date

from pydantic import BaseModel

from app.features.movie.domain.entities.movie_common_model import MovieBaseModel


class MovieCreateModel(MovieBaseModel):
    """
    MovieCreateModel represents a write model to create a movie.
    """


class MovieUpdateModel(BaseModel):
    """
    MovieUpdateModel represents a write model to update a movie.
    """

    title: str | None
    description: str | None
    release_date: date | None
    duration: int | None
