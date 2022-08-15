from rest_framework.serializers import ModelSerializer

from apps.projects.serializers import ProjectListSerializer
from apps.users.models import User


class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")


class UserDetailsSerializer(ModelSerializer):
    projects = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "projects")
        read_only_fields = ("email", "projects")
