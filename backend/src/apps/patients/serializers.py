from rest_framework import serializers

from .models import Patient, PatientTest


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTest
        fields = "__all__"
