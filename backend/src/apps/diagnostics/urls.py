from rest_framework import routers

from .views import DiagnosisViewSet


diagnostics_router = routers.DefaultRouter()
diagnostics_router.register(r"", DiagnosisViewSet, "diagnostics")
urlpatterns = diagnostics_router.urls
