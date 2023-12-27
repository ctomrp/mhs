from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    name = models.CharField(verbose_name=_("Group"), max_length=255, unique=True)

    def __str__(self):
        return self.name
