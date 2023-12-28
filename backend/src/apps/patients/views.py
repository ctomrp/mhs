from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Patient, PatientQuestionnaire, PatientStatus, ECICEPScore, Sex
from .serializers import (
    PatientSerializer,
    PatientQuestionnaireSerializer,
    PatientStatusSerializer,
    ECICEPScoreSerializer,
    SexSerializer,
)
from src.apps.users.authentication import CustomUserAuthentication


class PatientViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientQuestionnaireViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = PatientQuestionnaire.objects.all()
    serializer_class = PatientQuestionnaireSerializer


class PatientStatusViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = PatientStatus.objects.all()
    serializer_class = PatientStatusSerializer


class ECICEPScoreViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ECICEPScore.objects.all()
    serializer_class = ECICEPScoreSerializer


class SexViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Sex.objects.all()
    serializer_class = SexSerializer
