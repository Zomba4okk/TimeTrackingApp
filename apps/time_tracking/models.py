from django.db import models
from django_extensions.db.models import TimeStampedModel


class Timestamp(TimeStampedModel):
    date = models.DateField(
        verbose_name="Date",
        null=False,
        blank=False,
        help_text="Date for which the timestamp is registered",
    )
    time = models.PositiveIntegerField(
        verbose_name="Time", null=False, blank=False, help_text="Number of registered hours"
    )
    project = models.ForeignKey(
        "projects.Project",
        related_name="timestamps",
        on_delete=models.CASCADE,
        verbose_name="Project",
        null=False,
        blank=False,
        help_text="Project for which the timestamp is registered",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="User",
        null=False,
        blank=False,
        help_text="User whose time was registered",
    )

    def __str__(self):
        return f"{self.id} -- {self.date}"
