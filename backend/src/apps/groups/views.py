from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Group
from .serializers import GroupSerializer
from src.apps.users.authentication import CustomUserAuthentication


class GroupViewSet(ModelViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
