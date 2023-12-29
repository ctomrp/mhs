from django.utils.translation import gettext_lazy as _
from django.db import models

from src.apps.diagnostics.models import Diagnosis
from src.apps.groups.models import Group
from src.apps.sectors.models import Sector
from src.apps.questionnaires.models import Questionnaire


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
    sex = models.ForeignKey(
        "Sex",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Sex"),
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Sector"),
    )
    address = models.CharField(max_length=255, null=True, verbose_name=_("Address"))
    phone = models.BigIntegerField(null=True, verbose_name=_("Phone number"))
    patient_status = models.ForeignKey(
        "PatientStatus",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Patient status"),
    )
    suicide_attempt = models.BooleanField(verbose_name=_("Suicide attempt"))
    attempt_date = models.DateField(null=True, verbose_name=_("Attempt date"))
    diagnostics = models.ManyToManyField(
        Diagnosis, related_name="patients", verbose_name=_("Diagnostics"), blank=True
    )
    groups = models.ManyToManyField(
        Group, related_name="patients", verbose_name=_("Groups"), blank=True
    )
    ecicep_score = models.ForeignKey(
        "ECICEPScore",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("ECICEP score"),
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
        return f"{self.first_name} {self.middle_name} {self.last_name} {self.second_last_name}"


class Sex(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=_("Sex"))

    def __str__(self):
        return self.name


class PatientStatus(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name=_("Patient status")
    )

    def __str__(self):
        return self.name


class ECICEPScore(models.Model):
    name = models.CharField(max_length=2, unique=True, verbose_name=_("ECICEP score"))

    def __str__(self):
        return self.name


class PatientQuestionnaire(models.Model):
    patient = models.ForeignKey(
        "Patient", on_delete=models.CASCADE, verbose_name=_("Patient")
    )
    questionnaire = models.ForeignKey(
        Questionnaire, on_delete=models.CASCADE, verbose_name=_("Questionnaire")
    )
    score = models.CharField(max_length=255, verbose_name=_("Score"))
    observations = models.TextField(verbose_name=_("Observations"))
    evaluation_date = models.DateField(
        null=True, auto_now_add=True, verbose_name=_("Evaluation date")
    )
