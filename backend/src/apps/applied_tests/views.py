from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Test
from .serializers import TestSerializer
from src.apps.users.authentication import CustomUserAuthentication


class TestViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = TestSerializer
    queryset = Test.objects.all()
