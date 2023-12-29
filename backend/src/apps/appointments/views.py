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

    def perform_create(self, serializer):
        if self.request.user:
            serializer.validated_data["professional"] = self.request.user
        serializer.save()
