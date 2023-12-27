from django.contrib import admin
from django.urls import path, include
from src.apps.diagnostics.urls import diagnostics_router
from src.apps.applied_tests.urls import test_router
from src.apps.groups.urls import groups_router
from src.apps.sectors.urls import sectors_router
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("src.apps.users.urls")),
    path("api/appointments/", include("src.apps.appointments.urls")),
    path("api/diagnostics/", include(diagnostics_router.urls)),
    path("api/tests/", include(test_router.urls)),
    path("api/groups/", include(groups_router.urls)),
    path("api/patients/", include("src.apps.patients.urls")),
    path("api/sectors/", include(sectors_router.urls)),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/docs/yaml/", SpectacularAPIView.as_view(), name="schema"),
]
