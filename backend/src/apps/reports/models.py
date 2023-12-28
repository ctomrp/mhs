from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.patients.models import Patient
from src.apps.patients.services import *


class DailyReport(models.Model):
    date_report = models.DateField(auto_now_add=True, verbose_name=_("Date report"))
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_("Patient"),
    )
    professional = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Professional"),
    )
    pass


class MonthlyReportMen(models.Model):
    date_report = models.DateField(auto_now_add=True, verbose_name=_("Date report"))
    from_0_to_4 = models.IntegerField(null=True, verbose_name=_("0 to 4"))
    from_5_to_9 = models.IntegerField(null=True, verbose_name=_("5 to 9"))
    from_10_to_14 = models.IntegerField(null=True, verbose_name=_("10 to 14"))
    from_15_to_19 = models.IntegerField(null=True, verbose_name=_("15 to 19"))
    from_20_to_24 = models.IntegerField(null=True, verbose_name=_("20 to 24"))
    from_25_to_29 = models.IntegerField(null=True, verbose_name=_("25 to 29"))
    from_30_to_34 = models.IntegerField(null=True, verbose_name=_("30 to 34"))
    from_35_to_39 = models.IntegerField(null=True, verbose_name=_("35 to 39"))
    from_40_to_44 = models.IntegerField(null=True, verbose_name=_("40 to 44"))
    from_45_to_49 = models.IntegerField(null=True, verbose_name=_("45 to 49"))
    from_50_to_54 = models.IntegerField(null=True, verbose_name=_("50 to 54"))
    from_55_to_59 = models.IntegerField(null=True, verbose_name=_("55 to 59"))
    from_60_to_64 = models.IntegerField(null=True, verbose_name=_("60 to 64"))
    from_65_to_69 = models.IntegerField(null=True, verbose_name=_("65 to 69"))
    from_70_to_74 = models.IntegerField(null=True, verbose_name=_("70 to 74"))
    from_75_to_79 = models.IntegerField(null=True, verbose_name=_("75 to 79"))
    more_than_80 = models.IntegerField(null=True, verbose_name=_("More than 80"))


class MonthlyReportWomen(models.Model):
    date_report = models.DateField(auto_now_add=True, verbose_name=_("Date report"))
    from_0_to_4 = models.IntegerField(null=True, verbose_name=_("0 to 4"))
    from_5_to_9 = models.IntegerField(null=True, verbose_name=_("5 to 9"))
    from_10_to_14 = models.IntegerField(null=True, verbose_name=_("10 to 14"))
    from_15_to_19 = models.IntegerField(null=True, verbose_name=_("15 to 19"))
    from_20_to_24 = models.IntegerField(null=True, verbose_name=_("20 to 24"))
    from_25_to_29 = models.IntegerField(null=True, verbose_name=_("25 to 29"))
    from_30_to_34 = models.IntegerField(null=True, verbose_name=_("30 to 34"))
    from_35_to_39 = models.IntegerField(null=True, verbose_name=_("35 to 39"))
    from_40_to_44 = models.IntegerField(null=True, verbose_name=_("40 to 44"))
    from_45_to_49 = models.IntegerField(null=True, verbose_name=_("45 to 49"))
    from_50_to_54 = models.IntegerField(null=True, verbose_name=_("50 to 54"))
    from_55_to_59 = models.IntegerField(null=True, verbose_name=_("55 to 59"))
    from_60_to_64 = models.IntegerField(null=True, verbose_name=_("60 to 64"))
    from_65_to_69 = models.IntegerField(null=True, verbose_name=_("65 to 69"))
    from_70_to_74 = models.IntegerField(null=True, verbose_name=_("70 to 74"))
    from_75_to_79 = models.IntegerField(null=True, verbose_name=_("75 to 79"))
    more_than_80 = models.IntegerField(null=True, verbose_name=_("More than 80"))
    pregnants = models.IntegerField(null=True, verbose_name=_("Pregnants"))
    has_child_under_5 = models.IntegerField(
        null=True, verbose_name=_("Has child under 5 years old")
    )


class MonthlyReportIntersex(models.Model):
    date_report = models.DateField(auto_now_add=True, verbose_name=_("Date report"))
    from_0_to_4 = models.IntegerField(null=True, verbose_name=_("0 to 4"))
    from_5_to_9 = models.IntegerField(null=True, verbose_name=_("5 to 9"))
    from_10_to_14 = models.IntegerField(null=True, verbose_name=_("10 to 14"))
    from_15_to_19 = models.IntegerField(null=True, verbose_name=_("15 to 19"))
    from_20_to_24 = models.IntegerField(null=True, verbose_name=_("20 to 24"))
    from_25_to_29 = models.IntegerField(null=True, verbose_name=_("25 to 29"))
    from_30_to_34 = models.IntegerField(null=True, verbose_name=_("30 to 34"))
    from_35_to_39 = models.IntegerField(null=True, verbose_name=_("35 to 39"))
    from_40_to_44 = models.IntegerField(null=True, verbose_name=_("40 to 44"))
    from_45_to_49 = models.IntegerField(null=True, verbose_name=_("45 to 49"))
    from_50_to_54 = models.IntegerField(null=True, verbose_name=_("50 to 54"))
    from_55_to_59 = models.IntegerField(null=True, verbose_name=_("55 to 59"))
    from_60_to_64 = models.IntegerField(null=True, verbose_name=_("60 to 64"))
    from_65_to_69 = models.IntegerField(null=True, verbose_name=_("65 to 69"))
    from_70_to_74 = models.IntegerField(null=True, verbose_name=_("70 to 74"))
    from_75_to_79 = models.IntegerField(null=True, verbose_name=_("75 to 79"))
    more_than_80 = models.IntegerField(null=True, verbose_name=_("More than 80"))
    pregnants = models.IntegerField(null=True, verbose_name=_("Pregnants"))
    has_child_under_5 = models.IntegerField(
        null=True, verbose_name=_("Has child under 5 years old")
    )
