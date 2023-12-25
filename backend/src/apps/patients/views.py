from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Patient
from .serializers import PatientSerializer
from src.apps.users.authentication import CustomUserAuthentication


class PatientViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
