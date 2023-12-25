from rest_framework.viewsets import ModelViewSet

from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
