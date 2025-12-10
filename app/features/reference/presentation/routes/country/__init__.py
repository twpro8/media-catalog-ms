"""
Initialize country router.
"""

from app.features.reference.presentation.routes.country.get_country_route import (
    get_country,
)
from app.features.reference.presentation.routes.country.activate_country_route import (
    activate_country,
)
from app.features.reference.presentation.routes.country.deactivate_country_route import (
    deactivate_country,
)
from app.features.reference.presentation.routes.country.get_countries_route import (
    get_countries,
    router,
)

country_router = router
