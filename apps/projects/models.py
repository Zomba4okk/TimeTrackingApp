from typing import Iterable

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Project(TimeStampedModel):
    name = models.CharField(
        verbose_name="Name",
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        help_text="Project name",
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        null=True,
        blank=True,
        help_text="Short project description",
    )

    def assign_users(self, user_ids: Iterable[int]) -> None:
        self.users.add(*user_ids)

    def unassign_users(self, user_ids: Iterable[int]) -> None:
        self.users.remove(*user_ids)

    def __str__(self):
        return self.name
