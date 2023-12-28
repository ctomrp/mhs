from rest_framework import serializers

from .models import (
    DailyReport,
    MonthlyReportMen,
    MonthlyReportWomen,
    MonthlyReportIntersex,
)


class DailyReportSerializer(serializers.Serializer):
    class Meta:
        model = DailyReport
        fields = "__all__"


class MonthlyReportMenSerializer(serializers.Serializer):
    class Meta:
        model = MonthlyReportMen
        fields = "__all__"


class MonthlyReportWomenSerializer(serializers.Serializer):
    class Meta:
        model = MonthlyReportWomen
        fields = "__all__"


class MonthlyReportIntersexSerializer(serializers.Serializer):
    class Meta:
        model = MonthlyReportIntersex
        fields = "__all__"
