from rest_framework import serializers

from apps.projects.models import Project
from apps.time_tracking.serializers import TimestampListSerializer


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name")


class ProjectDetailsSerializer(serializers.ModelSerializer):
    timestamps = TimestampListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ("id", "name", "description", "timestamps")
        read_only_fields = ("id", "timestamps")


class ProjectAssigmentsSerializer(serializers.Serializer):
    user_ids = serializers.ListField(
        child=serializers.IntegerField(allow_null=False, min_value=1),
        required=True,
        allow_empty=False,
        allow_null=False,
    )
