from rest_framework import routers

from .views import TestViewSet


test_router = routers.DefaultRouter()
test_router.register(r"", TestViewSet, "tests")
urlpatterns = test_router.urls
