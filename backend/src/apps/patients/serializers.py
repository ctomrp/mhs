from rest_framework import serializers

from .models import Patient, PatientQuestionnaire, PatientStatus, ECICEPScore, Sex


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


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
