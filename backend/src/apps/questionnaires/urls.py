from rest_framework import routers

from .views import QuestionnaireViewSet


questionnaire_router = routers.DefaultRouter()
questionnaire_router.register(r"", QuestionnaireViewSet, "questionnaires")
urlpatterns = questionnaire_router.urls
