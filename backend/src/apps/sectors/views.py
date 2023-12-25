from rest_framework.viewsets import ModelViewSet

from .models import Sector
from .serializers import SectorSerializer


class SectorViewSet(ModelViewSet):
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
