import calendar
import json
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.utils.formats import date_format
from django.db.models import Q

from .models import Event, Class


def get_adjacent_month(year, month, offset):
    new_month = month + offset
    new_year = year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1
    return new_year, new_month


def calendar_view(request, year=None, month=None):
    today = date.today()
    year = int(year) if year else today.year
    month = int(month) if month else today.month

    cal = calendar.Calendar(firstweekday=0)
    weeks = cal.monthdatescalendar(year, month)

    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])

    # Pull anything that could touch this month (starts before month ends OR
    # ends after month starts)
    events = (
        Event.objects
        .filter(Q(date__lte=last_day) | Q(repeat_until__gte=first_day))
        .select_related('class_instance')
        .distinct()
    )
    events_by_day = {}

    # ---- expand events into the month, clamped to repeat_until if set ----
    for event in events:
        exceptions = set(
            event.recurrence_exceptions or []
        )
        end_boundary = (
            (
                min(last_day, event.repeat_until)
                if event.repeat_until else last_day
            )
        )

        if event.recurrence == 'none':
            if (
                first_day <= event.date <= last_day
                and event.date not in exceptions
            ):
                events_by_day.setdefault(
                    event.date, []
                ).append(event)

        elif event.recurrence == 'weekly':
            current = event.date
            while current <= end_boundary:
                if (
                    current >= first_day
                    and current.weekday() == event.date.weekday()
                    and current not in exceptions
                ):
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(weeks=1)

        elif event.recurrence == 'biweekly':
            current = event.date
            while current <= end_boundary:
                if (
                    current >= first_day
                    and current.weekday() == event.date.weekday()
                    and current not in exceptions
                ):
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(weeks=2)

        elif event.recurrence == 'monthly':
            current = event.date
            while current <= end_boundary:
                if current >= first_day and current not in exceptions:
                    events_by_day.setdefault(current, []).append(event)
                try:
                    current += relativedelta(months=1)
                except ValueError:
                    break

        elif event.recurrence == 'custom_days':
            if not event.days_of_week:
                continue
            weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
            weekday_map = dict(zip(weekdays, range(7)))
            selected_days = [
                weekday_map[d.strip().lower()]
                for d in event.days_of_week.split(',')
                if d.strip().lower() in weekday_map
            ]
            current = first_day
            while current <= end_boundary:
                if (
                    current.weekday() in selected_days
                    and current >= event.date
                    and current not in exceptions
                ):
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(days=1)

    prev_year, prev_month = get_adjacent_month(year, month, -1)
    next_year, next_month = get_adjacent_month(year, month, 1)

    return render(request, 'schedule/calendar.html', {
        'year': year,
        'month': date_format(date(year, month, 1), "F", use_l10n=True),
        'month_number': month,
        'weeks': weeks,
        'events_by_day': events_by_day,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    })


def event_list_view(request):
    classes = Class.objects.all()
    events = Event.objects.all().select_related('class_instance')
    return render(
        request,
        'schedule/event_list.html',
        {'classes': classes, 'events': events}
    )


# ----------------------------- CREATE ---------------------------------
@csrf_exempt
@require_POST
def create_event(request):
    data = json.loads(request.body)
    cls = get_object_or_404(Class, id=data['class_id'])

    exceptions = [
        d.strip()
        for d in data.get('recurrence_exceptions', '').split(',')
        if d.strip()
    ]

    # Accept missing repeat_until as None; parse "YYYY-MM-DD" when provided
    repeat_until_str = data.get('repeat_until')
    repeat_until = (
        datetime.strptime(repeat_until_str, '%Y-%m-%d').date()
        if repeat_until_str else None
    )

    event = Event.objects.create(
        class_instance=cls,
        date=data['date'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        recurrence=data.get('recurrence', 'none'),
        days_of_week=data.get('days_of_week', ''),
        recurrence_exceptions=exceptions,
        repeat_until=repeat_until,
    )
    return JsonResponse(model_to_dict(event))


# ----------------------------- UPDATE ---------------------------------
@csrf_exempt
@require_POST
def update_event(request, event_id):
    data = json.loads(request.body)
    ev = get_object_or_404(Event, id=event_id)

    # Only update fields that were actually sent
    if 'class_id' in data:
        ev.class_instance = get_object_or_404(Class, id=data['class_id'])
    if 'date' in data:
        ev.date = data['date']
    if 'start_time' in data:
        ev.start_time = data['start_time']
    if 'end_time' in data:
        ev.end_time = data['end_time']
    if 'recurrence' in data:
        ev.recurrence = data['recurrence']
    if 'days_of_week' in data:
        ev.days_of_week = data['days_of_week']

    if 'recurrence_exceptions' in data:
        ev.recurrence_exceptions = [
            d.strip()
            for d in data.get('recurrence_exceptions', '').split(',')
            if d.strip()
        ]

    # Critical: only change repeat_until if the client sent the key
    if 'repeat_until' in data:
        ru = data['repeat_until']  # may be "", null, or "YYYY-MM-DD"
        ev.repeat_until = (
            datetime.strptime(ru, '%Y-%m-%d').date() if ru else None
        )

    ev.save()
    return JsonResponse(model_to_dict(ev))


@csrf_exempt
@require_POST
def delete_event(request, event_id):
    ev = get_object_or_404(Event, id=event_id)
    ev.delete()
    return JsonResponse({'deleted': True})


@csrf_exempt
@require_POST
def create_class(request):
    data = json.loads(request.body)
    cls = Class.objects.create(
        name_en=data['name_en'],
        name_it=data.get('name_it', ''),
        emoji=data.get('emoji', '')
    )
    return JsonResponse(model_to_dict(cls))


@csrf_exempt
@require_POST
def update_class(request, class_id):
    data = json.loads(request.body)
    cls = get_object_or_404(Class, id=class_id)
    cls.name_en = data['name_en']
    cls.name_it = data.get('name_it', '')
    cls.emoji = data.get('emoji', '')
    cls.save()
    return JsonResponse(model_to_dict(cls))


@csrf_exempt
@require_POST
def delete_class(request, class_id):
    cls = get_object_or_404(Class, id=class_id)
    cls.delete()
    return JsonResponse({'deleted': True})
