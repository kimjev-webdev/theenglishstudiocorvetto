# schedule/views.py
import calendar
import json
from datetime import date, timedelta, time as dtime

from dateutil.relativedelta import relativedelta

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.utils.formats import date_format
from django.db.models import Q
from django.utils.dateparse import parse_date, parse_time

from django.contrib.auth.decorators import login_required, user_passes_test
from portal.authz import is_portal_owner
from portal.authz import in_group  # reuse your portal auth helpers

from .models import Event, Class


# ---- auth guard for schedule admin endpoints ----
def _schedule_guard(user):
    return (
        user.is_authenticated and (
            user.is_staff or
            is_portal_owner(user) or
            in_group(user, "SCHEDULE")
        )
    )


def get_adjacent_month(year, month, offset):
    new_month = month + offset
    new_year = year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1
    return new_year, new_month


# ===== Public calendar page =====
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
        .filter(
            Q(date__lte=last_day) | Q(repeat_until__gte=first_day)
        )
        .select_related('class_instance')
        .distinct()
    )
    events_by_day = {}

    # ---- expand events into the month, clamped to repeat_until if set ----
    for event in events:
        exceptions = set(event.recurrence_exceptions or [])
        end_boundary = (
            min(last_day, event.repeat_until)
            if event.repeat_until else last_day
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


# If this list is an admin page, lock it down.
# If it's public, drop the decorators.
@login_required
@user_passes_test(_schedule_guard)
def event_list_view(request):
    classes = Class.objects.all()
    events = Event.objects.all().select_related('class_instance')
    return render(
        request,
        'schedule/event_list.html',
        {
            'classes': classes,
            'events': events
        }
    )


# ---------- helpers for JSON endpoints ----------
def _json_bad_request(msg, status=400):
    return JsonResponse({"ok": False, "error": msg}, status=status)


def _parse_exceptions(value):
    # Accept list OR comma-separated string
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(v).strip() for v in value if str(v).strip()]
    return [s.strip() for s in str(value).split(',') if s.strip()]


# ----------------------------- CREATE EVENT ---------------------------------
@login_required
@user_passes_test(_schedule_guard)
@require_POST
def create_event(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return _json_bad_request("Invalid JSON payload")

    cls = get_object_or_404(Class, id=data.get('class_id'))

    d = parse_date(data.get('date'))
    st = parse_time(data.get('start_time'))
    et = parse_time(data.get('end_time'))
    if not d or not st or not et:
        return _json_bad_request(
            "Missing or invalid date/start_time/end_time "
            "(use ISO e.g. 2025-08-25, 14:30:00)"
        )

    # ensure end after start (simple check; adjust if events can span midnight)
    if isinstance(st, dtime) and isinstance(et, dtime) and et <= st:
        return _json_bad_request("end_time must be after start_time")

    rec = data.get('recurrence', 'none')
    days_of_week = data.get('days_of_week', '')
    exceptions = _parse_exceptions(data.get('recurrence_exceptions'))
    ru = data.get('repeat_until')
    repeat_until = parse_date(ru) if ru else None

    event = Event.objects.create(
        class_instance=cls,
        date=d,
        start_time=st,
        end_time=et,
        recurrence=rec,
        days_of_week=days_of_week,
        recurrence_exceptions=exceptions,
        repeat_until=repeat_until,
    )
    return JsonResponse(
        {
            "ok": True,
            "message": "Event created.",
            "data": model_to_dict(event)
        },
        status=201
    )


# ----------------------------- UPDATE EVENT ---------------------------------
@login_required
@user_passes_test(_schedule_guard)
@require_POST
def update_event(request, event_id):
    ev = get_object_or_404(Event, id=event_id)
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return _json_bad_request("Invalid JSON payload")

    if 'class_id' in data:
        ev.class_instance = get_object_or_404(Class, id=data['class_id'])

    if 'date' in data:
        d = parse_date(data['date'])
        if not d:
            return _json_bad_request("Invalid date")
        ev.date = d

    if 'start_time' in data:
        st = parse_time(data['start_time'])
        if not st:
            return _json_bad_request("Invalid start_time")
        ev.start_time = st

    if 'end_time' in data:
        et = parse_time(data['end_time'])
        if not et:
            return _json_bad_request("Invalid end_time")
        ev.end_time = et

    if 'recurrence' in data:
        ev.recurrence = data['recurrence']

    if 'days_of_week' in data:
        ev.days_of_week = data['days_of_week']

    if 'recurrence_exceptions' in data:
        ev.recurrence_exceptions = _parse_exceptions(
            data.get('recurrence_exceptions')
        )

    if 'repeat_until' in data:
        ru = data['repeat_until']
        ev.repeat_until = parse_date(ru) if ru else None

    # validate times if both present
    if ev.start_time and ev.end_time and ev.end_time <= ev.start_time:
        return _json_bad_request("end_time must be after start_time")

    ev.save()
    return JsonResponse({
        "ok": True,
        "message": "Event updated.",
        "data": model_to_dict(ev)
    })


# ----------------------------- DELETE EVENT ---------------------------------
@login_required
@user_passes_test(_schedule_guard)
@require_POST
def delete_event(request, event_id):
    ev = get_object_or_404(Event, id=event_id)
    ev.delete()
    return JsonResponse({
        "ok": True,
        "message": "Event deleted.",
        "data": {"id": event_id}
    })


# ----------------------------- CREATE CLASS ---------------------------------
@login_required
@user_passes_test(_schedule_guard)
@require_POST
def create_class(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return _json_bad_request("Invalid JSON payload")

    name_en = (data.get('name_en') or "").strip()
    if not name_en:
        return _json_bad_request("name_en is required")

    cls = Class.objects.create(
        name_en=name_en,
        name_it=data.get('name_it', '').strip(),
        emoji=data.get('emoji', '').strip()
    )
    return JsonResponse(
        {
            "ok": True,
            "message": "Class created.",
            "data": model_to_dict(cls)
        },
        status=201
    )


# ----------------------------- UPDATE CLASS ---------------------------------
@login_required
@user_passes_test(_schedule_guard)
@require_POST
def update_class(request, class_id):
    cls = get_object_or_404(Class, id=class_id)
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return _json_bad_request("Invalid JSON payload")

    if 'name_en' in data:
        name_en = (data.get('name_en') or "").strip()
        if not name_en:
            return _json_bad_request("name_en is required")
        cls.name_en = name_en

    if 'name_it' in data:
        cls.name_it = (data.get('name_it') or "").strip()

    if 'emoji' in data:
        cls.emoji = (data.get('emoji') or "").strip()

    cls.save()
    return JsonResponse({
        "ok": True,
        "message": "Class updated.",
        "data": model_to_dict(cls)
    })


# ----------------------------- DELETE CLASS ---------------------------------
@login_required
@user_passes_test(_schedule_guard)
@require_POST
def delete_class(request, class_id):
    cls = get_object_or_404(Class, id=class_id)
    cls.delete()
    return JsonResponse({
        "ok": True,
        "message": "Class deleted.",
        "data": {"id": class_id}
    })
