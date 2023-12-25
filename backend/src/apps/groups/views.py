from rest_framework.viewsets import ModelViewSet

from .models import Group
from .serializers import GroupSerializer


class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
