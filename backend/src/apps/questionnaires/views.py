from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Questionnaire
from .serializers import QuestionnaireSerializer
from src.apps.users.authentication import CustomUserAuthentication


class QuestionnaireViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()
