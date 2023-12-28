from django.urls import path
from rest_framework import routers

from .apis import (
    get_appointments_by_professional,
    get_appointments_by_date,
    get_appointments_by_date_range,
    get_total_appointments_by_professional,
    get_total_appointments_by_date_range,
    # get_daily_report,
)
from .views import AppointmentViewSet


appointments_router = routers.DefaultRouter()
appointments_router.register(r"", AppointmentViewSet, "appointments")
urlpatterns = [
    path(
        "professional/<int:professional_id>",
        get_appointments_by_professional,
        name="appointments_by_professional",
    ),
    path(
        "date/<str:date>",
        get_appointments_by_date,
        name="appointments_by_date",
    ),
    path(
        "date-range/<str:date_range>",
        get_appointments_by_date_range,
        name="appointments_by_date_range",
    ),
    path(
        "professional-total/<int:professional_id>",
        get_total_appointments_by_professional,
        name="total_appointments_by_professional",
    ),
    path(
        "date-range-total/<str:date_range>",
        get_total_appointments_by_date_range,
        name="total_appointments_by_date_range",
    ),
    # path("daily-report/", get_daily_report, name="daily_report"),
]
urlpatterns += appointments_router.urls
