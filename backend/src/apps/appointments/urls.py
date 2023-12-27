from django.urls import path
from rest_framework import routers

from .apis import (
    get_appointments_by_professional,
    get_total_appointments_by_professional,
    get_appointments_by_date_range,
    get_total_appointments_by_date_range,
)
from .views import AppointmentViewSet


appointments_router = routers.DefaultRouter()
appointments_router.register(r"", AppointmentViewSet, "appointments")

urlpatterns = [
    path(
        "professional/<int:professional_id>",
        get_appointments_by_professional,
        name="appointments-by-professional",
    ),
    path(
        "total-appointments/<int:professional_id>",
        get_total_appointments_by_professional,
        name="total-appointments",
    ),
    path(
        "date-range/<str:date_range>",
        get_appointments_by_date_range,
        name="appointments-date-range",
    ),
    path(
        "date-range-total/<str:date_range>",
        get_total_appointments_by_date_range,
        name="total-appointments-by-date-range",
    ),
]
urlpatterns += appointments_router.urls
