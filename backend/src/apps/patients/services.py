from django.db.models import Q
from django.db import connection

from .models import Patient
from src.apps.diagnostics.models import Diagnosis
from src.apps.groups.models import Group


def fetch_patient_by_dni(patient_dni) -> "Patient":
    return Patient.objects.get(dni=patient_dni)


def fetch_patient_by_medical_record(patient_medical_record_id) -> "Patient":
    return Patient.objects.get(medical_record_id=patient_medical_record_id)


def fetch_patient_by_name(patient_name) -> list["Patient"]:
    patient_collection = Patient.objects.filter(
        Q(first_name__icontains=patient_name)
        | Q(middle_name__icontains=patient_name)
        | Q(last_name__icontains=patient_name)
        | Q(second_last_name__icontains=patient_name)
    )
    return [patient for patient in patient_collection]


def fetch_patient_by_diagnosis(diagnosis_id) -> list["Patient"]:
    diagnosis = Diagnosis.objects.get(pk=diagnosis_id)
    patient_collection = Patient.objects.filter(diagnostics=diagnosis)
    return [patient for patient in patient_collection]


def fetch_patient_by_age(age) -> list["Patient"]:
    query = """SELECT *  FROM patients_patient WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) = %s;"""
    patient_collection = Patient.objects.raw(query, [age])
    return [patient for patient in patient_collection]


def fetch_patient_by_age_range(age_range) -> list["Patient"]:
    min_age, max_age = map(int, age_range.split(","))
    query = """SELECT * FROM patients_patient WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) BETWEEN %s AND %s;"""
    patient_collection = Patient.objects.raw(query, [min_age, max_age])
    return [patient for patient in patient_collection]


def fetch_patient_by_sex(sex_id) -> list["Patient"]:
    patient_collection = Patient.objects.filter(sex=sex_id)
    return [patient for patient in patient_collection]


def fetch_patient_by_sector(sector_id) -> list["Patient"]:
    patient_collection = Patient.objects.filter(sector=sector_id)
    return [patient for patient in patient_collection]


def fetch_patient_by_groups(group_id) -> list["Patient"]:
    group = Group.objects.get(pk=group_id)
    patient_collection = Patient.objects.filter(groups=group)
    return [patient for patient in patient_collection]


def fetch_patient_with_suicide_attempt() -> list["Patient"]:
    patient_collection = Patient.objects.filter(suicide_attempt=True)
    return [patient for patient in patient_collection]


def fetch_patient_ges() -> list["Patient"]:
    patient_collection = Patient.objects.filter(is_ges=True)
    return [patient for patient in patient_collection]


def fetch_patient_in_psychiatric_care() -> list["Patient"]:
    patient_collection = Patient.objects.filter(in_psychiatric_care=True)
    return [patient for patient in patient_collection]


def fetch_patient_pregnants() -> list["Patient"]:
    patient_collection = Patient.objects.filter(is_pregnant=True)
    return [patient for patient in patient_collection]


def count_diagnostics(diagnosis_id) -> int:
    total = Patient.objects.filter(diagnostics=diagnosis_id).count()
    return total


def count_diagnostics_by_group(diagnosis_id_and_group_id) -> int:
    diagnosis_id, group_id = map(int, diagnosis_id_and_group_id.split(","))
    total = Patient.objects.filter(diagnostics=diagnosis_id, groups=group_id).count()
    return total


def count_patients_by_age_range(age_range) -> int:
    min_age, max_age = map(int, age_range.split(","))
    query = """SELECT COUNT(*) as count FROM patients_patient WHERE CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER) BETWEEN %s AND %s;"""
    with connection.cursor() as cursor:
        cursor.execute(query, [min_age, max_age])
        total = cursor.fetchone()
    return total[0] if total else 0


def count_suicide_attempts() -> int:
    total = Patient.objects.filter(suicide_attempt=True).count()
    return total


def count_ges() -> int:
    total = Patient.objects.filter(is_ges=True).count()
    return total


def count_in_psychiatric_care() -> int:
    total = Patient.objects.filter(in_psychiatric_care=True).count()
    return total


def count_pregnants() -> int:
    total = Patient.objects.filter(is_pregnant=True).count()
    return total
