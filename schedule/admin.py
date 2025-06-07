# schedule/admin.py
from django.contrib import admin
from .models import Class, Event

admin.site.register(Class)
admin.site.register(Event)


class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "emoji")


class EventAdmin(admin.ModelAdmin):
    list_display = ("class_ref", "date", "time")
    list_filter = ("date", "class_ref")
