"""
Initialize season router.
"""

from app.features.season.presentation.routes.get_season_route import get_season
from app.features.season.presentation.routes.get_seasons_route import get_seasons
from app.features.season.presentation.routes.update_season_route import update_season
from app.features.season.presentation.routes.delete_season_route import delete_season
from app.features.season.presentation.routes.create_season_route import (
    create_season,
    router,
)

season_router = router
