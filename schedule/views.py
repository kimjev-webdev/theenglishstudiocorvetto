import calendar
from datetime import date
from django.shortcuts import render
from django.utils.formats import date_format  # NEW import
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

    # Get all events in the month
    events = Event.objects.filter(date__year=year, date__month=month)
    events_by_day = {}
    for event in events:
        events_by_day.setdefault(event.date, []).append(event)

    # Determine previous/next month for navigation
    prev_year, prev_month = get_adjacent_month(year, month, -1)
    next_year, next_month = get_adjacent_month(year, month, 1)

    context = {
        'year': year,
        # Localized full month name
        'month': date_format(
            date(year, month, 1),
            "F",
            use_l10n=True
        ),
        'weeks': weeks,
        'events_by_day': events_by_day,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }

    return render(request, 'schedule/calendar.html', context)
