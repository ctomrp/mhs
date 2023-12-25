# from django.db.models import Q

# from .models import Patient


# def get_patient_by_dni(dni):
#     return Patient.objects.get(dni=dni)


# def get_patient_by_medical_record_id(medical_record_id):
#     return Patient.objects.get(medical_record_id=medical_record_id)


# def get_patients_by_name(name):
#     patients = Patient.objects.filter(
#         Q(first_name__icontains=name)
#         | Q(middle_name__icontains=name)
#         | Q(last_name__icontains=name)
#         | Q(second_last_name__icontains=name)
#     )
#     return patients


# def get_patients_with_suicide_attempt():
#     patients = Patient.objects.filter(suicide_attempt=True)
#     return patients


# def get_patients_ges():
#     patients = Patient.objects.filter(is_ges=True)
#     return patients


# def get_patients_in_psychiatric_care():
#     patients = Patient.objects.filter(in_psychiatric_care=True)
#     return patients


# def get_patients_is_pregnant():
#     patients = Patient.objects.filter(is_pregnant=True)
#     return patients
