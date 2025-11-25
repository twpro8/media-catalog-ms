"""
Initialize show router.
"""

from app.features.show.presentation.routes.get_show_route import get_show
from app.features.show.presentation.routes.get_shows_route import get_shows
from app.features.show.presentation.routes.update_show_route import update_show
from app.features.show.presentation.routes.delete_show_route import delete_show
from app.features.show.presentation.routes.create_show_route import (
    create_show,
    router,
)

show_router = router
