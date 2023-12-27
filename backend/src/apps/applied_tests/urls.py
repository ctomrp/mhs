from rest_framework import routers

from .views import TestViewSet


applied_tests_router = routers.DefaultRouter()
applied_tests_router.register(r"", TestViewSet, "tests")
urlpatterns = applied_tests_router.urls
