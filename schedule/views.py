import calendar
from datetime import date, timedelta
from django.shortcuts import render
from django.utils.formats import date_format
from .models import Event


def get_adjacent_month(year, month, offset):
    """Returns (year, month) offset months from the given month."""
    new_month = month + offset
    new_year = year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1
    return new_year, new_month


def calendar_view(request, year=None, month=None):
    today = date.today()
    year = int(year) if year else today.year
    month = int(month) if month else today.month

    cal = calendar.Calendar(firstweekday=0)  # Monday = 0
    weeks = cal.monthdatescalendar(year, month)

    # Calculate first and last visible day of the month
    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])

    # Fetch events whose date could affect this month
    events = Event.objects.filter(date__lte=last_day)
    events_by_day = {}

    for event in events:
        if event.recurrence == 'none':
            if first_day <= event.date <= last_day:
                events_by_day.setdefault(event.date, []).append(event)

        elif event.recurrence == 'weekly':
            current = event.date
            while current <= last_day:
                if (
                    current >= first_day and
                    current.weekday() == event.date.weekday()
                ):
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(weeks=1)

        elif event.recurrence == 'biweekly':
            current = event.date
            while current <= last_day:
                if (
                    current >= first_day and
                    current.weekday() == event.date.weekday()
                ):
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(weeks=2)

        elif event.recurrence == 'monthly':
            try:
                recur_date = date(year, month, event.date.day)
                if first_day <= recur_date <= last_day:
                    events_by_day.setdefault(recur_date, []).append(event)
            except ValueError:
                pass  # e.g. no Feb 30

        elif event.recurrence == 'custom_days':
            if not event.days_of_week:
                continue
            weekday_map = {
                'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3,
                'fri': 4, 'sat': 5, 'sun': 6
            }
            selected_days = [
                weekday_map[d.strip().lower()]
                for d in event.days_of_week.split(',')
                if d.strip().lower() in weekday_map
            ]
            current = first_day
            while current <= last_day:
                if (
                    current.weekday() in selected_days and
                    current >= event.date
                ):
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(days=1)

    # Determine previous/next month for navigation
    prev_year, prev_month = get_adjacent_month(year, month, -1)
    next_year, next_month = get_adjacent_month(year, month, 1)

    context = {
        'year': year,
        'month': date_format(date(year, month, 1), "F", use_l10n=True),
        'weeks': weeks,
        'events_by_day': events_by_day,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }

    return render(request, 'schedule/calendar.html', context)
