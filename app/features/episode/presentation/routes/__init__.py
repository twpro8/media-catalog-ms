"""
Initialize episode router.
"""

from app.features.episode.presentation.routes.create_episode_route import create_episode
from app.features.episode.presentation.routes.get_episode_route import get_episode
from app.features.episode.presentation.routes.get_episodes_route import get_episodes
from app.features.episode.presentation.routes.update_episode_route import update_episode
from app.features.episode.presentation.routes.delete_episode_route import (
    delete_episode,
    router,
)

episode_router = router
