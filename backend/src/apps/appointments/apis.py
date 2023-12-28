from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.apps.users.authentication import CustomUserAuthentication
from .serializers import AppointmentSerializer
from .services import *


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
def get_appointments_by_date(request, date):
    try:
        appointments = fetch_appointments_by_date(date)
    except NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(data=serializer.data)


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
def get_total_appointments_by_professional(request, professional_id):
    total = count_appointments_by_professional(professional_id)
    return Response({"total_appointments_by_professional": total})


@api_view(["GET"])
@authentication_classes((CustomUserAuthentication,))
@permission_classes((IsAuthenticated,))
def get_total_appointments_by_date_range(request, date_range):
    total = count_appointments_by_date_range(date_range)
    return Response({"total_appointments_by_date_range": total})


# @api_view(["GET"])
# @authentication_classes((CustomUserAuthentication,))
# @permission_classes((IsAuthenticated,))
# def get_daily_report(request):
#     professional = request.user
#     today = timezone.now().date()
#     appointments_collection = Appointment.objects.filter(
#         professional=professional, attendance_date=today, attended=True
#     )
#     serializer = AppointmentSerializer(appointments_collection, many=True)
#     return Response(serializer.data)
