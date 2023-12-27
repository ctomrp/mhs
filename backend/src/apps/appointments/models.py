from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.patients.models import Patient


class Appointment(models.Model):
    attendance_date = models.DateField(verbose_name=_("Attendance date"))
    attendance_recorded = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Attendance recorded")
    )
    attended = models.BooleanField(verbose_name=_("Attended"))
    professional = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        verbose_name=_("Profesional"),
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        verbose_name=_("Patient"),
    )
    observations = models.TextField(null=True, verbose_name=_("Observations"))
