from django.urls import path

from apps.time_tracking.views import LogTimeView, TimestampDetailsView


urlpatterns = [
    path("", LogTimeView.as_view(), name="log-time"),
    path(
        "timestamps/<int:timestamp_id>/", TimestampDetailsView.as_view(), name="timestamp-details"
    ),
]
