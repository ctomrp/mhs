# from django.contrib import admin
from django.urls import path, include

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from src.apps.questionnaires.urls import questionnaire_router
from src.apps.diagnostics.urls import diagnostics_router
from src.apps.groups.urls import groups_router
from src.apps.sectors.urls import sectors_router


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/appointments/", include("src.apps.appointments.urls")),
    path("api/diagnostics/", include(diagnostics_router.urls)),
    path("api/groups/", include(groups_router.urls)),
    path("api/patients/", include("src.apps.patients.urls")),
    path("api/questionnaires/", include(questionnaire_router.urls)),
    path("api/sectors/", include(sectors_router.urls)),
    path("api/users/", include("src.apps.users.urls")),
    # path(
    #     "",
    #     SpectacularSwaggerView.as_view(url_name="schema"),
    #     name="swagger-ui",
    # ),
    # path("api/docs/yaml/", SpectacularAPIView.as_view(), name="schema"),
]
