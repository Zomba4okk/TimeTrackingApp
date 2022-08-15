from datetime import date

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.projects.services import ProjectAssigmentsService
from apps.projects.tests.factories import ProjectFactory
from apps.time_tracking.services import TimestampService
from apps.users.tests.factories import UserFactory


class Command(BaseCommand):
    help = "Generate data for local develpoment"

    @transaction.atomic
    def handle(self, *args, **options):
        user_1 = UserFactory()
        user_2 = UserFactory()
        user_3 = UserFactory()
        UserFactory()

        project_1 = ProjectFactory()
        project_2 = ProjectFactory()
        ProjectFactory()

        ProjectAssigmentsService.assign_users_to_project(
            project_id=project_1.id, user_ids=[user_1.id, user_2.id]
        )
        ProjectAssigmentsService.assign_users_to_project(
            project_id=project_2.id, user_ids=[user_2.id, user_3.id]
        )

        TimestampService().log_time(
            log_date=date.today(), time=4, project_id=project_1.id, user_id=user_1.id
        )
        TimestampService().log_time(
            log_date=date.today(), time=4, project_id=project_1.id, user_id=user_2.id
        )

        TimestampService().log_time(
            log_date=date.today(), time=6, project_id=project_2.id, user_id=user_2.id
        )
        TimestampService().log_time(
            log_date=date.today(), time=8, project_id=project_2.id, user_id=user_3.id
        )
