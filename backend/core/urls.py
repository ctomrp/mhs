from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from src.apps.applied_tests.urls import applied_tests_router
from src.apps.diagnostics.urls import diagnostics_router
from src.apps.groups.urls import groups_router
from src.apps.sectors.urls import sectors_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("src.apps.users.urls")),
    path("api/appointments/", include("src.apps.appointments.urls")),
    path("api/diagnostics/", include(diagnostics_router.urls)),
    path("api/groups/", include(groups_router.urls)),
    path("api/patients/", include("src.apps.patients.urls")),
    path("api/sectors/", include(sectors_router.urls)),
    path("api/tests/", include(applied_tests_router.urls)),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/docs/yaml/", SpectacularAPIView.as_view(), name="schema"),
]
