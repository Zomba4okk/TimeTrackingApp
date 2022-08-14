from django.contrib import admin

from apps.time_tracking.models import Timestamp


@admin.register(Timestamp)
class TimestampAdmin(admin.ModelAdmin):
    pass
