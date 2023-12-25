from django.db import models
from django.utils.translation import gettext_lazy as _


class Sector(models.Model):
    name = models.CharField(
        verbose_name=_("Sector"), max_length=255, default=None, unique=True
    )

    def __str__(self):
        return self.name
