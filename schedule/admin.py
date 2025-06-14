from django.contrib import admin
from .models import Class, Event


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name_en", "emoji")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "class_instance",
        "date",
        "start_time",
        "end_time",
        "recurrence",
    )
    list_filter = ("date", "class_instance", "recurrence")

    fieldsets = (
        (None, {
            'fields': ('class_instance', 'date', 'start_time', 'end_time')
        }),
        ('Recurrence', {
            'fields': ('recurrence', 'days_of_week'),
            'description': (
                'Optional: Set how often this event repeats. '
                'Leave as "One-time only" if not repeating.'
            )
        }),
    )
