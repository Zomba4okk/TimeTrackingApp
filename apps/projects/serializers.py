from rest_framework.serializers import ModelSerializer

from apps.projects.models import Project


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name")
