from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Diagnosis
from .serializers import DiagnosisSerializer
from src.apps.users.authentication import CustomUserAuthentication


class DiagnosisViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
