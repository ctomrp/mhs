from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .services import *

from .models import Patient
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
        patient = fetch_patient_by_dni(dni=patient_dni)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patient)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patient_by_medical_record(request, medical_record_id):
    try:
        patient = fetch_patient_by_medical_record(medical_record_id=medical_record_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patient, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_by_name(request, patient_name):
    try:
        patients = fetch_patients_by_name(name=patient_name)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_with_suicide_attempt(request):
    try:
        patients = fetch_patients_with_suicide_attempt()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_attempts(request):
    total = count_suicide_attempts()
    return Response({"total_attempts": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_ges(request):
    try:
        patients = fetch_patients_ges()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_ges(request):
    total = count_ges()
    return Response({"total_ges": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_in_psychiatric_care(request):
    try:
        patients = fetch_patients_in_psychiatric_care()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_in_psychiatric_care(request):
    total = count_in_psychiatric_care()
    return Response({"total_in_psychiatric_care": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_pregnants(request):
    try:
        patients = fetch_patients_pregnants()
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_pregnants(request):
    total = count_pregnants()
    return Response({"total_pregnants": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_by_diagnosis(request, diagnosis_id=None):
    try:
        patients = fetch_patients_by_diagnosis(diagnosis_id)
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
def get_patients_by_age(request, age):
    try:
        patients = fetch_patients_by_age(age)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_by_age_range(request, age_range):
    try:
        patients = fetch_patients_by_age_range(age_range)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_by_age_range(request, age_range):
    total = count_patients_by_age_range(age_range)
    return Response({"total_age_range": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_by_gender(request, gender):
    try:
        patients = fetch_patients_by_gender(gender)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_by_sector(request, sector_id=None):
    try:
        patients = fetch_patients_by_sector(sector_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_patients_by_groups(request, group_id=None):
    try:
        patients = fetch_patients_by_groups(group_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patients, many=True)
    return Response(data=serializer.data)
