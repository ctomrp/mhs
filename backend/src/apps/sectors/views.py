from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Sector
from .serializers import SectorSerializer
from src.apps.users.authentication import CustomUserAuthentication


class SectorViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
