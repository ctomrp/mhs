from django.db.models import Q
from django.db import connection
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Patient
from src.apps.diagnostics.models import Diagnosis
from src.apps.groups.models import Group


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
    if diagnosis_id is not None:
        diagnosis = Diagnosis.objects.get(pk=diagnosis_id)
        patients = Patient.objects.filter(diagnostics=diagnosis)
    else:
        patients = Patient.objects.filter(Q(diagnostics__isnull=True))

    return [patient for patient in patients]


def count_diagnostics(diagnosis_id) -> int:
    total = Patient.objects.filter(diagnostics=diagnosis_id).count()
    return total


def fetch_patients_by_age(age):
    query = """SELECT *  FROM patients_patient WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) = %s;"""
    # mysql
    # SELECT * FROM patients_patient WHERE TIMESTAMPDIFF(YEAR, birthdate, NOW()) = %s;
    # postgresql
    # SELECT * FROM patients_patient WHERE EXTRACT(YEAR FROM age(current_date, birthdate)) = %s;
    results = Patient.objects.raw(query, [age])
    patients = list(results)
    return patients


def fetch_patients_by_age_range(age_range):
    min_age, max_age = map(int, age_range.split("-"))
    query = """SELECT * FROM patients_patient WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) BETWEEN %s AND %s;"""
    # mysql
    # SELECT * FROM patients_patient WHERE TIMESTAMPDIFF(YEAR, birthdate, NOW()) = %s;
    # postgresql
    # SELECT * FROM patients_patient WHERE EXTRACT(YEAR FROM age(current_date, birthdate)) = %s;
    results = Patient.objects.raw(query, [min_age, max_age])
    patients = list(results)
    return patients


def count_patients_by_age_range(age_range):
    min_age, max_age = map(int, age_range.split("-"))
    query = """
        SELECT COUNT(*) as count
        FROM patients_patient
        WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) BETWEEN %s AND %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [min_age, max_age])
        result = cursor.fetchone()

    return result[0] if result else 0


def fetch_patients_by_gender(gender):
    patients = Patient.objects.filter(gender=gender.upper())
    return [patient for patient in patients]


def fetch_patients_by_sector(sector_id):
    if sector_id is not None:
        patients = Patient.objects.filter(sector=sector_id)
    else:
        patients = Patient.objects.filter(Q(sector__isnull=True))

    return [patient for patient in patients]


def fetch_patients_by_groups(group_id) -> "Patient":
    if group_id is not None:
        group = Group.objects.get(pk=group_id)
        patients = Patient.objects.filter(groups=group)
    else:
        patients = Patient.objects.filter(Q(groups__isnull=True))

    return [patient for patient in patients]
