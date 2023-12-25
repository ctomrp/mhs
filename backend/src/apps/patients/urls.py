from django.urls import path
from rest_framework import routers
from .apis import PatientByDNIAPI
from .views import PatientViewSet

patients_router = routers.DefaultRouter()
patients_router.register(r"", PatientViewSet, "patients")

urlpatterns = [
    path("by-dni/<str:patient_dni>/", PatientByDNIAPI.as_view(), name="patient-by-dni"),
]

urlpatterns += patients_router.urls
print(patients_router.urls)
