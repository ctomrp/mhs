from django.urls import path
from rest_framework import routers
from .apis import (
    get_patient_by_dni,
    get_patient_by_medical_record,
    get_patient_by_name,
    get_patient_by_diagnosis,
    get_patient_by_age,
    get_patient_by_age_range,
    get_patient_by_gender,
    get_patient_by_sector,
    get_patient_by_groups,
    get_patient_with_suicide_attempt,
    get_patient_ges,
    get_patient_in_psychiatric_care,
    get_patient_pregnants,
    get_total_diagnostics,
    get_total_patients_by_age_range,
    get_total_attempts,
    get_total_ges,
    get_total_in_psychiatric_care,
    get_total_pregnants,
)
from .views import PatientViewSet, PatientTestViewSet

patients_router = routers.DefaultRouter()
patients_router.register(r"records", PatientViewSet, "patients")
patients_router.register(r"tests", PatientTestViewSet, "patienttests")


urlpatterns = [
    path("dni/<str:patient_dni>/", get_patient_by_dni, name="patient_by_dni"),
    path(
        "medical-record/<int:patient_medical_record_id>/",
        get_patient_by_medical_record,
        name="patient_by_medical_record",
    ),
    path("name/<str:patient_name>/", get_patient_by_name, name="patient-by-name"),
    path(
        "diagnosis/<int:diagnosis_id>",
        get_patient_by_diagnosis,
        name="patient_by_diagnosis",
    ),
    path("age/<int:age>", get_patient_by_age, name="patient-by-age"),
    path(
        "age-range/<str:age_range>",
        get_patient_by_age_range,
        name="patient-by-age-range",
    ),
    path("gender/<int:gender_id>", get_patient_by_gender, name="patient-by-gender"),
    path("sector/<int:sector_id>", get_patient_by_sector, name="patient-by-sector"),
    path("group/<int:group_id>", get_patient_by_groups, name="patient-by-group"),
    path(
        "suicide-attempt/",
        get_patient_with_suicide_attempt,
        name="patient_with_suicide_attempt",
    ),
    path("ges/", get_patient_ges, name="patient_ges"),
    path(
        "psychiatric-care/",
        get_patient_in_psychiatric_care,
        name="patient_in_psychiatric_care",
    ),
    path("pregnants/", get_patient_pregnants, name="patient_pregnants"),
    path(
        "diagnosis-total/<int:diagnosis_id>",
        get_total_diagnostics,
        name="total_diagnostics",
    ),
    path(
        "age-range-total/<str:age_range>",
        get_total_patients_by_age_range,
        name="total_patients_by_age_range",
    ),
    path("attempts-total/", get_total_attempts, name="total-attempts"),
    path("ges-total/", get_total_ges, name="total-ges"),
    path(
        "psychiatric-care-total/",
        get_total_in_psychiatric_care,
        name="total_in_psychiatric_care",
    ),
    path("pregnants-total/", get_total_pregnants, name="total-pregnants"),
]

urlpatterns += patients_router.urls
