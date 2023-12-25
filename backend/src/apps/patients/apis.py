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


class PatientByDNIAPI(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, patient_dni):
        patient = get_patient_by_dni(dni=patient_dni)
        serializer = PatientSerializer(patient)
        return Response(data=serializer.data)


class PatientByMedicalRecordIdAPI(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, medical_record_id):
        patient = get_patient_by_medical_record_id(medical_record_id=medical_record_id)
        serializer = PatientSerializer(patient, many=True)
        return Response(data=serializer.data)


class PatientByNameAPI(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, patient_name):
        patients = get_patients_by_name(name=patient_name)
        serializer = PatientSerializer(patients, many=True)
        return Response(data=serializer.data)


class PatientByAttemptApi(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        patients = get_patients_with_suicide_attempt()
        serializer = PatientSerializer(patients, many=True)
        return Response(data=serializer.data)


class TotalAttemptsApi(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        total_attempts = count_suicide_attempts()
        return Response({"total_attempts": total_attempts})
