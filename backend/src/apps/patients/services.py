from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Patient


def get_patient_by_dni(dni) -> "Patient":
    return Patient.objects.get(dni=dni)


def get_patient_by_medical_record_id(medical_record_id) -> list["Patient"]:
    patients = Patient.objects.filter(medical_record_id=medical_record_id)
    return [patient for patient in patients]


def get_patients_by_name(name) -> list["Patient"]:
    patients = Patient.objects.filter(
        Q(first_name__icontains=name)
        | Q(middle_name__icontains=name)
        | Q(last_name__icontains=name)
        | Q(second_last_name__icontains=name)
    )
    return [patient for patient in patients]


def get_patients_with_suicide_attempt() -> list["Patient"]:
    patients = Patient.objects.filter(suicide_attempt=True)
    return [patient for patient in patients]


def count_suicide_attempts() -> int:
    total = Patient.objects.filter(suicide_attempt=True).count()
    return total


def get_patients_ges() -> list["Patient"]:
    patients = Patient.objects.filter(is_ges=True)
    return [patient for patient in patients]


def get_patients_in_psychiatric_care() -> list["Patient"]:
    patients = Patient.objects.filter(in_psychiatric_care=True)
    return [patient for patient in patients]


def get_patients_is_pregnant() -> list["Patient"]:
    patients = Patient.objects.filter(is_pregnant=True)
    return [patient for patient in patients]
