from django.test import TestCase

from apps.projects.services import ProjectAssigmentsService
from apps.projects.tests.factories import ProjectFactory
from apps.users.tests.factories import UserFactory


class TestProjectAssigmentsService(TestCase):
    def test_should_assign_users_on_project(self):
        # assemble
        user_1 = UserFactory()
        user_2 = UserFactory()

        project = ProjectFactory()
        assert project.users.count() == 0

        # act
        ProjectAssigmentsService.assign_users_to_project(
            project_id=project.id, user_ids=[user_1.id, user_2.id]
        )

        # assert
        assert list(project.users.order_by("id")) == [user_1, user_2]

    def test_should_should_finish_successfully_when_user_already_assigned(self):
        # assemble
        user_1 = UserFactory()
        user_2 = UserFactory()

        project = ProjectFactory()
        project.users.add(user_1)

        # act
        ProjectAssigmentsService.assign_users_to_project(
            project_id=project.id, user_ids=[user_1.id, user_2.id]
        )

        # assert
        assert list(project.users.order_by("id")) == [user_1, user_2]

    def test_should_should_unassign_users_from_project(self):
        # assemble
        user_1 = UserFactory()
        user_2 = UserFactory()

        project = ProjectFactory()
        project.users.add(user_1, user_2)

        # act
        ProjectAssigmentsService.unassign_users_from_project(
            project_id=project.id, user_ids=[user_1.id, user_2.id]
        )

        # assert
        assert project.users.count() == 0

    def test_should_should_finish_successfully_when_user_not_assigned(self):
        # assemble
        user_1 = UserFactory()
        user_2 = UserFactory()

        project = ProjectFactory()
        project.users.add(user_1)

        # act
        ProjectAssigmentsService.unassign_users_from_project(
            project_id=project.id, user_ids=[user_1.id, user_2.id]
        )

        # assert
        assert project.users.count() == 0
