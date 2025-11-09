"""
Initialize movie router.
"""

from app.features.movie.presentation.routes.get_movie_route import get_movie
from app.features.movie.presentation.routes.get_movies_route import get_movies
from app.features.movie.presentation.routes.update_movie_route import update_movie
from app.features.movie.presentation.routes.delete_movie_route import delete_movie
from app.features.movie.presentation.routes.create_movie_route import (
    create_movie,
    router,
)

movie_router = router
