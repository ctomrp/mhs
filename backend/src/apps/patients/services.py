from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from .models import Patient
from src.apps.diagnostics.models import Diagnosis


def fetch_patient_by_dni(dni) -> "Patient":
    return Patient.objects.get(dni=dni)


def fetch_patient_by_medical_record(medical_record_id) -> list["Patient"]:
    patients = Patient.objects.filter(medical_record_id=medical_record_id)
    return [patient for patient in patients]


def fetch_patients_by_name(name) -> list["Patient"]:
    patients = Patient.objects.filter(
        Q(first_name__icontains=name)
        | Q(middle_name__icontains=name)
        | Q(last_name__icontains=name)
        | Q(second_last_name__icontains=name)
    )
    return [patient for patient in patients]


def fetch_patients_with_suicide_attempt() -> list["Patient"]:
    patients = Patient.objects.filter(suicide_attempt=True)
    return [patient for patient in patients]


def count_suicide_attempts() -> int:
    total = Patient.objects.filter(suicide_attempt=True).count()
    return total


def fetch_patients_ges() -> list["Patient"]:
    patients = Patient.objects.filter(is_ges=True)
    return [patient for patient in patients]


def count_ges() -> int:
    total = Patient.objects.filter(is_ges=True).count()
    return total


def fetch_patients_in_psychiatric_care() -> list["Patient"]:
    patients = Patient.objects.filter(in_psychiatric_care=True)
    return [patient for patient in patients]


def count_in_psychiatric_care() -> int:
    total = Patient.objects.filter(in_psychiatric_care=True).count()
    return total


def fetch_patients_pregnants() -> list["Patient"]:
    patients = Patient.objects.filter(is_pregnant=True)
    return [patient for patient in patients]


def count_pregnants() -> int:
    total = Patient.objects.filter(is_pregnant=True).count()
    return total


def fetch_patients_by_diagnosis(diagnosis_id) -> "Patient":
    diagnosis = Diagnosis.objects.get(pk=diagnosis_id)
    patients = Patient.objects.filter(diagnostics=diagnosis)
    return [patient for patient in patients]


def fetch_patients_by_age(age):
    query = """SELECT *  FROM patients_patient WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) = %s;"""
    # mysql
    # SELECT * FROM patients_patient WHERE TIMESTAMPDIFF(YEAR, birthdate, NOW()) = %s;
    # postgresql
    # SELECT * FROM patients_patient WHERE EXTRACT(YEAR FROM age(current_date, birthdate)) = %s;
    results = Patient.objects.raw(query, [age])
    patients = list(results)
    return patients
