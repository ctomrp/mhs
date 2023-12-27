from django.db import models
from django.utils.translation import gettext_lazy as _


class Diagnosis(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Diagnosis"))
    is_ges = models.BooleanField(verbose_name=_("GES"))
    is_active = models.BooleanField(verbose_name=_("Active"))

    def __str__(self):
        return self.name
