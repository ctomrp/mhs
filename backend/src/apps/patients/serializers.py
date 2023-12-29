from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Patient, PatientQuestionnaire, PatientStatus, ECICEPScore, Sex


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def validate_sex(self, value):
        if value is None:
            raise serializers.ValidationError(_("Sex field is required."))
        return value

    def validate_sector(self, value):
        if value is None:
            raise serializers.ValidationError(_("Sector field is required."))
        return value

    def validate_patient_status(self, value):
        if value is None:
            raise serializers.ValidationError(_("Patient status field is required."))
        return value

    def validate_ecicep_score(self, value):
        if value is None:
            raise serializers.ValidationError(_("ECICEP score field is required."))
        return value


class PatientQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientQuestionnaire
        fields = "__all__"


class PatientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientStatus
        fields = "__all__"


class ECICEPScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECICEPScore
        fields = "__all__"


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"
