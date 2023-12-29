from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = [
            "attendance_recorded",
            "professional",
        ]

    def validate_patient(self, value):
        if value is None:
            raise serializers.ValidationError("Patient field is required.")
        return value
