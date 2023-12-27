from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Appointment
from .serializers import AppointmentSerializer
from src.apps.users.authentication import CustomUserAuthentication


class AppointmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
