from rest_framework.viewsets import ModelViewSet

from .models import Diagnosis
from .serializers import DiagnosisSerializer


class DiagnosisViewSet(ModelViewSet):
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
