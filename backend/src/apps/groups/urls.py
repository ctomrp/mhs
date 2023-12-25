from rest_framework import routers

from .views import GroupViewSet


groups_router = routers.DefaultRouter()
groups_router.register(r"", GroupViewSet, "groups")
urlpatterns = groups_router.urls
