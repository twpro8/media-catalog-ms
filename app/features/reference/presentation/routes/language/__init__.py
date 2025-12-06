"""
Initialize language router.
"""

from app.features.reference.presentation.routes.language.get_language_route import (
    get_language,
)
from app.features.reference.presentation.routes.language.activate_language_route import (
    activate_language,
)
from app.features.reference.presentation.routes.language.deactivate_language_route import (
    deactivate_language,
)
from app.features.reference.presentation.routes.language.get_languages_route import (
    get_languages,
    router,
)

language_router = router
