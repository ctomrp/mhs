from django.urls import path
from rest_framework import routers
from .apis import (
    PatientByDNIAPI,
    PatientByMedicalRecordIdAPI,
    PatientByNameAPI,
    PatientByAttemptApi,
    TotalAttemptsApi,
)
from .views import PatientViewSet

patients_router = routers.DefaultRouter()
patients_router.register(r"", PatientViewSet, "patients")

urlpatterns = [
    path("by-dni/<str:patient_dni>/", PatientByDNIAPI.as_view(), name="patient-by-dni"),
    path(
        "by-medical-record-id/<int:medical_record_id>/",
        PatientByMedicalRecordIdAPI.as_view(),
        name="patient-by-medical-record",
    ),
    path(
        "by-name/<str:patient_name>/",
        PatientByNameAPI.as_view(),
        name="patient-by-name",
    ),
    path(
        "by-suicide-attempt/",
        PatientByAttemptApi.as_view(),
        name="patient-by-suicide-attempt",
    ),
    path(
        "total-attempts/",
        TotalAttemptsApi.as_view(),
        name="total-attempts",
    ),
]

urlpatterns += patients_router.urls
print(patients_router.urls)
