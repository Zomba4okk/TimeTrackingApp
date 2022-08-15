from datetime import date

from django.db.models import Sum
from rest_framework.exceptions import ValidationError

from apps.time_tracking.models import Timestamp


class TimestampService:
    @staticmethod
    def check_if_log_is_valid(log_date: date, time: int, user_id: int) -> bool:
        result = Timestamp.objects.filter(date=log_date, user_id=user_id).aggregate(
            total_time=Sum("time")
        )

        total_time = result.get("total_time") or 0

        return total_time + time <= 24

    def log_time(self, log_date: date, time: int, project_id: int, user_id: int) -> Timestamp:
        if not self.check_if_log_is_valid(log_date=log_date, time=time, user_id=user_id):
            raise ValidationError("Time per day exceeded 24 hours")

        return Timestamp.objects.create(
            date=log_date, time=time, project_id=project_id, user_id=user_id
        )
