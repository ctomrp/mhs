from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .services import *

from .models import Patient
from .serializers import AppointmentSerializer
from src.apps.users.authentication import CustomUserAuthentication

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_appointments_by_professional(request, professional_id):
    try:
        appointments = fetch_appointments_by_professional(professional_id)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AppointmentSerializer(appointments, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_appointments_by_professional(request, professional_id):
    total = count_appointments_by_professional(professional_id)
    return Response({"total_appointments": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_appointments_by_date_range(request, date_range):
    try:
        appointments = fetch_appointments_by_date_range(date_range)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AppointmentSerializer(appointments, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_appointments_by_date_range(request, date_range):
    total = count_appointments_by_date_range(date_range)
    return Response({"total_appointments_by_date_range": total})
