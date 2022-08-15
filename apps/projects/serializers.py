from rest_framework import serializers

from apps.projects.models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name")


class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description")
        read_only_fields = ("id",)


class ProjectAssigmentsSerializer(serializers.Serializer):
    user_ids = serializers.ListField(
        child=serializers.IntegerField(allow_null=False, min_value=1),
        required=True,
        allow_empty=False,
        allow_null=False,
    )
