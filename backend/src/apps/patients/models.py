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
    dni = models.CharField(max_length=10, unique=True, verbose_name="DNI")
    medical_record_number = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Medical record number"
    )
    first_name = models.CharField(max_length=20, verbose_name="First name")
    middle_name = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Middle name"
    )
    last_name = models.CharField(max_length=20, verbose_name="Last name")
    second_last_name = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Second last name"
    )
    birthdate = models.DateField(verbose_name="Birthdate")
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name="Gender"
    )
    # datos de contacto del paciente
    phone = models.BigIntegerField(null=True, blank=True, verbose_name="Phone number")
    address = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Address"
    )
    sector = models.ForeignKey(
        Sector, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Sector"
    )
    # otros datos relevantes
    suicide_attempt = models.BooleanField(
        default=False, verbose_name=("Suicide attempt")
    )
    attempt_date = models.DateField(
        null=True, blank=True, verbose_name=("Attempt date")
    )
    diagnostics = models.ManyToManyField(
        Diagnosis, blank=True, verbose_name="Diagnostics"
    )
    groups = models.ManyToManyField(Group, blank=True, verbose_name="Groups")
    is_ges = models.BooleanField(default=False, verbose_name="Is GES")
    signed_ges = models.BooleanField(default=False, verbose_name="Signed GES")
    has_pci = models.BooleanField(default=False, verbose_name="Has PCI")
    signed_consent = models.BooleanField(default=False, verbose_name="Signed consent")
    in_psychiatric_care = models.BooleanField(
        default=False, verbose_name="In psychiatric care"
    )
    seen_in_consulting = models.BooleanField(
        default=False, verbose_name="Seen in consulting"
    )
    ecicep_score = models.CharField(
        max_length=2, null=True, blank=True, verbose_name="ECICEP score"
    )
    # datos solo para mujeres
    is_pregnant = models.BooleanField(default=False, verbose_name="Is pregnant")
    due_date = models.DateField(null=True, blank=True, verbose_name="Due date")
    has_child_under_five = models.BooleanField(
        default=False, verbose_name="Has child under five years old"
    )
    child_birthdate = models.DateField(
        null=True, blank=True, verbose_name="Child birthdate"
    )
