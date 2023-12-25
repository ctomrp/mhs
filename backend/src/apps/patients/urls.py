from rest_framework import routers

from .views import PatientViewSet


patients_router = routers.DefaultRouter()
patients_router.register(r"", PatientViewSet, "patients")
urlpatterns = patients_router.urls
