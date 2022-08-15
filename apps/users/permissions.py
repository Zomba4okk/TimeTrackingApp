from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


class IsAdminPermission(IsAuthenticated):
    def has_permission(self, request: Request, view):
        return super().has_permission(request, view) and request.user.is_staff
