from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.utils import formats
from django.db import models
from datetime import time
from django.contrib.postgres.fields import ArrayField


class Class(models.Model):
    name_en = models.CharField(
        max_length=100,
        verbose_name=_("Class Name (EN)")
    )
    name_it = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Class Name (IT)")
    )
    emoji = models.CharField(
        max_length=10,
        verbose_name=_("Emoji"),
        help_text=_("Use a single emoji to represent this class")
    )

    def __str__(self):
        lang = get_language()
        name = (
            self.name_it
            if lang == 'it' and self.name_it
            else self.name_en
        )
        return f"{self.emoji} {name}"

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class Recurrence(models.TextChoices):
    NONE = 'none', _('One-time only')
    WEEKLY = 'weekly', _('Weekly')
    BIWEEKLY = 'biweekly', _('Every 2 weeks')
    MONTHLY = 'monthly', _('Monthly')
    CUSTOM_DAYS = 'custom_days', _('Custom weekdays')


class Event(models.Model):
    class_instance = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name=_("Class")
    )
    date = models.DateField(verbose_name=_("Date"))
    start_time = models.TimeField(
        verbose_name=_("Start Time"),
        default=time(11, 0)
    )
    end_time = models.TimeField(
        verbose_name=_("End Time"),
        default=time(12, 0)
    )
    recurrence = models.CharField(
        max_length=20,
        choices=Recurrence.choices,
        default=Recurrence.NONE,
        verbose_name=_("Repeats")
    )
    days_of_week = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Days of the Week"),
        help_text=_("For custom repeat, enter days like 'Mon,Wed,Fri'")
    )
    recurrence_exceptions = ArrayField(
        base_field=models.DateField(),
        blank=True,
        default=list,
        verbose_name=_("Recurrence Exceptions"),
        help_text=_("Dates on which this recurring event should be skipped")
    )
    repeat_until = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Repeat Until"),
        help_text=_("Last day this event should occur")
    )

    def __str__(self):
        return (
            f"{self.class_instance} – "
            f"{formats.date_format(self.date, 'DATE_FORMAT')}, "
            f"{formats.time_format(self.start_time, 'TIME_FORMAT')} to "
            f"{formats.time_format(self.end_time, 'TIME_FORMAT')}"
        )
