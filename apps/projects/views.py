from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.projects.models import Project
from apps.projects.serializers import (
    ProjectAssigmentsSerializer,
    ProjectDetailsSerializer,
    ProjectListSerializer,
)
from apps.projects.services import ProjectAssigmentsService
from apps.users.permissions import IsAdminPermission


class ProjectsView(ListCreateAPIView):
    permission_classes = (IsAdminPermission,)
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectListSerializer
        return ProjectDetailsSerializer


class ProjectDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminPermission,)
    serializer_class = ProjectDetailsSerializer
    queryset = Project.objects.prefetch_related("timestamps__user").all()
    lookup_field = "id"
    lookup_url_kwarg = "project_id"


class ProjectAssigmentsView(APIView):
    permission_classes = (IsAdminPermission,)
    serializer_class = ProjectAssigmentsSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request: Request, project_id: int, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ProjectAssigmentsService.assign_users_to_project(
            project_id=project_id, user_ids=serializer.data["user_ids"]
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request: Request, project_id: int, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ProjectAssigmentsService.unassign_users_from_project(
            project_id=project_id, user_ids=serializer.data["user_ids"]
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
