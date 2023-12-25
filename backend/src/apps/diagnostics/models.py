from django.db import models
from django.utils.translation import gettext_lazy as _


class Diagnosis(models.Model):
    name = models.CharField(
        verbose_name=_("Diagnosis"), max_length=255, default=None, unique=True
    )
    is_ges = models.BooleanField(verbose_name=_("GES"), default=False)
    is_active = models.BooleanField(verbose_name=_("Active"), default=True)

    def __str__(self):
        return _(self.name)
