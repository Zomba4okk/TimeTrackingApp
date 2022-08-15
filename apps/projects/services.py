from typing import Iterable

from apps.projects.models import Project


class ProjectAssigmentsService:
    @staticmethod
    def assign_users_to_project(project_id: int, user_ids: Iterable[int]) -> None:
        project = Project.objects.get(id=project_id)
        project.assign_users(user_ids=user_ids)

    @staticmethod
    def unassign_users_from_project(project_id: int, user_ids: Iterable[int]) -> None:
        project = Project.objects.get(id=project_id)
        project.unassign_users(user_ids=user_ids)
