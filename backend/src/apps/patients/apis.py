from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .services import get_patient_by_dni

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
