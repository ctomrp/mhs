from django.utils.translation import gettext_lazy as _
from django.db import models

from src.apps.diagnostics.models import Diagnosis
from src.apps.groups.models import Group
from src.apps.sectors.models import Sector


class Patient(models.Model):
    GENDER_CHOICES = [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("I", "Intersexual"),
    ]

    # datos de identificación del paciente
    dni = models.CharField(max_length=10, unique=True, verbose_name=_("DNI"))
    medical_record_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_("Medical record number")
    )
    first_name = models.CharField(max_length=20, verbose_name=_("First name"))
    middle_name = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Middle name")
    )
    last_name = models.CharField(max_length=20, verbose_name=_("Last name"))
    second_last_name = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Second last name")
    )
    birthdate = models.DateField(verbose_name=_("Birthdate"))
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name=_("Gender")
    )
    # datos de contacto del paciente
    phone = models.BigIntegerField(
        null=True, blank=True, verbose_name=_("Phone number")
    )
    address = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Address")
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Sector"),
    )
    # otros datos relevantes
    suicide_attempt = models.BooleanField(
        default=False, verbose_name=_("Suicide attempt")
    )
    attempt_date = models.DateField(
        null=True, blank=True, verbose_name=_("Attempt date")
    )
    diagnostics = models.ManyToManyField(
        Diagnosis, blank=True, related_name="patients", verbose_name=_("Diagnostics")
    )
    groups = models.ManyToManyField(
        Group, blank=True, related_name="patients", verbose_name=_("Groups")
    )
    is_ges = models.BooleanField(default=False, verbose_name=_("Is GES"))
    signed_ges = models.BooleanField(default=False, verbose_name=_("Signed GES"))
    has_pci = models.BooleanField(default=False, verbose_name=_("Has PCI"))
    signed_consent = models.BooleanField(
        default=False, verbose_name=_("Signed consent")
    )
    in_psychiatric_care = models.BooleanField(
        default=False, verbose_name=_("In psychiatric care")
    )
    seen_in_consulting = models.BooleanField(
        default=False, verbose_name=_("Seen in consulting")
    )
    ecicep_score = models.CharField(
        max_length=2, null=True, blank=True, verbose_name=_("ECICEP score")
    )
    # datos solo para mujeres
    is_pregnant = models.BooleanField(default=False, verbose_name=_("Is pregnant"))
    due_date = models.DateField(null=True, blank=True, verbose_name=_("Due date"))
    has_child_under_five = models.BooleanField(
        default=False, verbose_name=_("Has child under five years old")
    )
    child_birthdate = models.DateField(
        null=True, blank=True, verbose_name=_("Child birthdate")
    )
