from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.projects.models import Project
from apps.time_tracking.models import Timestamp
from apps.time_tracking.serializers import LogTimeSerializer
from apps.time_tracking.services import TimestampService
from apps.users.permissions import IsAdminPermission


class LogTimeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogTimeSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def check_permission(self, project_id: int):
        if self.request.user.is_staff:
            return

        if not Project.objects.filter(
            id=project_id, users__id__contains=self.request.user.id
        ).exists():
            raise PermissionDenied("You are not assigned on this project")

    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.check_permission(project_id=serializer.data["project"])

        TimestampService().log_time(
            log_date=serializer.data["date"],
            time=serializer.data["time"],
            project_id=serializer.data["project"],
            user_id=request.user.id,
        )

        return Response(status=status.HTTP_201_CREATED)


class TimestampDetailsView(DestroyAPIView):
    permission_classes = (IsAdminPermission,)
    queryset = Timestamp.objects.all()
    lookup_url_kwarg = "timestamp_id"
    lookup_field = "id"
