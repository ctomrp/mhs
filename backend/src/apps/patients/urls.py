from django.urls import path
from rest_framework import routers
from .apis import (
    get_patient_by_dni,
    get_patient_by_medical_record,
    get_patients_by_name,
    get_patients_with_suicide_attempt,
    get_total_attempts,
    get_patients_ges,
    get_total_ges,
    get_patients_in_psychiatric_care,
    get_total_in_psychiatric_care,
    get_patients_pregnants,
    get_total_pregnants,
    get_patients_by_diagnosis,
    get_patients_by_age,
)
from .views import PatientViewSet

patients_router = routers.DefaultRouter()
patients_router.register(r"", PatientViewSet, "patients")

urlpatterns = [
    path("dni/<str:patient_dni>/", get_patient_by_dni, name="patient-by-dni"),
    path(
        "medical-record/<int:medical_record_id>/",
        get_patient_by_medical_record,
        name="patient-by-medical-record",
    ),
    path("name/<str:patient_name>/", get_patients_by_name, name="patient-by-name"),
    path(
        "suicide-attempt/",
        get_patients_with_suicide_attempt,
        name="patient-by-suicide-attempt",
    ),
    path("total-attempts/", get_total_attempts, name="total-attempts"),
    path("ges/", get_patients_ges, name="patient-by-ges"),
    path("total-ges/", get_total_ges, name="total-ges"),
    path(
        "psychiatric-care/",
        get_patients_in_psychiatric_care,
        name="patient-by-psychiatric_care",
    ),
    path(
        "total-psychiatric-care/",
        get_total_in_psychiatric_care,
        name="total-in-psychiatric-care",
    ),
    path(
        "pregnants/",
        get_patients_pregnants,
        name="pregnants",
    ),
    path(
        "total-pregnants/",
        get_total_pregnants,
        name="total-pregnants",
    ),
    path(
        "diagnosis/<int:diagnosis_id>",
        get_patients_by_diagnosis,
        name="patients-by-diagnosis",
    ),
    path(
        "age/<int:age>",
        get_patients_by_age,
        name="patients-by-age",
    ),
]

urlpatterns += patients_router.urls
