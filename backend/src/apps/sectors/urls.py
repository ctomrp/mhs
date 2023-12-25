from rest_framework import routers

from .views import SectorViewSet


sectors_router = routers.DefaultRouter()
sectors_router.register(r"", SectorViewSet, "sectors")
urlpatterns = sectors_router.urls
