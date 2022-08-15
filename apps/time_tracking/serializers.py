from rest_framework import serializers

from apps.time_tracking.models import Timestamp


class LogTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestamp
        fields = ("date", "time", "project")


class TimestampListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Timestamp
        fields = ("id", "date", "time", "user")
        read_only_fields = ("id", "date", "time", "user")
