from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .services import *

from .serializers import PatientSerializer
from src.apps.users.authentication import CustomUserAuthentication

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_dni(request, patient_dni):
    try:
        patient = fetch_patient_by_dni(patient_dni=patient_dni)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patient)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_medical_record(request, patient_medical_record_id):
    try:
        patient = fetch_patient_by_medical_record(
            patient_medical_record_id=patient_medical_record_id
        )
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patient)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_name(request, patient_name):
    try:
        patients = fetch_patient_by_name(patient_name=patient_name)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_diagnosis(request, diagnosis_id):
    try:
        patients = fetch_patient_by_diagnosis(diagnosis_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_age(request, age):
    try:
        patients = fetch_patient_by_age(age)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_age_range(request, age_range):
    try:
        patients = fetch_patient_by_age_range(age_range)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_sex(request, sex_id):
    try:
        patients = fetch_patient_by_sex(sex_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_sector(request, sector_id):
    try:
        patients = fetch_patient_by_sector(sector_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_groups(request, group_id):
    try:
        patients = fetch_patient_by_groups(group_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_with_suicide_attempt(request):
    try:
        patients = fetch_patient_with_suicide_attempt()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_ges(request):
    try:
        patients = fetch_patient_ges()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_in_psychiatric_care(request):
    try:
        patients = fetch_patient_in_psychiatric_care()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_pregnants(request):
    try:
        patients = fetch_patient_pregnants()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_diagnostics(request, diagnosis_id):
    total = count_diagnostics(diagnosis_id)
    return Response({"total_diagnostics": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_diagnostics_by_group(request, diagnosis_id_and_group_id):
    total = count_diagnostics_by_group(diagnosis_id_and_group_id)
    return Response({"total_diagnostics": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_patients_by_age_range(request, age_range):
    total = count_patients_by_age_range(age_range)
    return Response({"total_patients_by_age_range": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_attempts(request):
    total = count_suicide_attempts()
    return Response({"total_attempts": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_ges(request):
    total = count_ges()
    return Response({"total_ges": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_in_psychiatric_care(request):
    total = count_in_psychiatric_care()
    return Response({"total_in_psychiatric_care": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_pregnants(request):
    total = count_pregnants()
    return Response({"total_pregnants": total})
