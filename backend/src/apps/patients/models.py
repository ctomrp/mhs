from django.utils.translation import gettext_lazy as _
from django.db import models

from .choices import ECICEP_SCORE_CHOICES, GENDER_CHOICES, PATIENT_STATUS_CHOICES
from src.apps.diagnostics.models import Diagnosis
from src.apps.groups.models import Group
from src.apps.sectors.models import Sector
from src.apps.applied_tests.models import Test


class Patient(models.Model):
    dni = models.CharField(max_length=10, unique=True, verbose_name=_("DNI"))
    medical_record_id = models.PositiveIntegerField(
        unique=True, verbose_name=_("Medical record id")
    )
    first_name = models.CharField(max_length=20, verbose_name=_("First name"))
    middle_name = models.CharField(
        max_length=20, null=True, verbose_name=_("Middle name")
    )
    last_name = models.CharField(max_length=20, verbose_name=_("Last name"))
    second_last_name = models.CharField(
        max_length=20, null=True, verbose_name=_("Second last name")
    )
    birthdate = models.DateField(verbose_name=_("Birthdate"))
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name=_("Gender"))
    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_DEFAULT,
        default=_("Unassigned"),
        verbose_name=_("Sector"),
    )
    address = models.CharField(max_length=255, null=True, verbose_name=_("Address"))
    phone = models.BigIntegerField(null=True, verbose_name=_("Phone number"))
    patient_status = models.IntegerField(
        choices=PATIENT_STATUS_CHOICES, verbose_name=_("Patient status")
    )
    suicide_attempt = models.BooleanField(verbose_name=_("Suicide attempt"))
    attempt_date = models.DateField(null=True, verbose_name=_("Attempt date"))
    diagnostics = models.ManyToManyField(
        Diagnosis, related_name="patients", verbose_name=_("Diagnostics")
    )
    groups = models.ManyToManyField(
        Group, related_name="patients", verbose_name=_("Groups")
    )
    ecicep_score = models.IntegerField(
        choices=ECICEP_SCORE_CHOICES, verbose_name=_("ECICEP score")
    )
    is_ges = models.BooleanField(verbose_name=_("Is GES"))
    signed_ges = models.BooleanField(verbose_name=_("Signed GES"))
    has_pci = models.BooleanField(verbose_name=_("Has PCI"))
    signed_consent = models.BooleanField(verbose_name=_("Signed consent"))
    in_psychiatric_care = models.BooleanField(verbose_name=_("In psychiatric care"))
    seen_in_consulting = models.BooleanField(verbose_name=_("Seen in consulting"))
    # datos solo para mujeres
    is_pregnant = models.BooleanField(verbose_name=_("Is pregnant"))
    due_date = models.DateField(null=True, verbose_name=_("Due date"))
    has_child_under_five = models.BooleanField(
        verbose_name=_("Has child under five years old")
    )
    child_birthdate = models.DateField(null=True, verbose_name=_("Child birthdate"))

    def __str__(self):
        name = (
            self.first_name + self.middle_name + self.last_name + self.second_last_name
        )
        return f"{self.dni}, {name}"


class PatientTest(models.Model):
    patient = models.ForeignKey(
        "Patient", on_delete=models.CASCADE, verbose_name=_("Patient")
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"))
    score = models.CharField(max_length=255, verbose_name=_("Score"))
    observations = models.TextField(verbose_name=_("Observations"))
