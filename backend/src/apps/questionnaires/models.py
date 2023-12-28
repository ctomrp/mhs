from django.db import models
from django.utils.translation import gettext_lazy as _


class Questionnaire(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name=_("Questionnaire name")
    )

    def __str__(self):
        return self.name
