import calendar
import json
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.utils.formats import date_format
from django.db.models import Q  # ✅ required for combined query logic

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

    events = (
        Event.objects
        .filter(
            Q(date__lte=last_day) | Q(repeat_until__gte=first_day)
        )
        .select_related('class_instance')
        .distinct()
    )
    events_by_day = {}

    print("📆 CALENDAR VIEW:", first_day, "to", last_day)

    for event in events:
        print("\n🧠 Processing Event ID:", event.id)
        print("📘 Class:", event.class_instance.name_en)
        print("🗓️ Date:", event.date)
        print("🔁 Recurrence:", event.recurrence)
        print("⛔ Exceptions:", event.recurrence_exceptions)
        print("📅 Repeat until:", event.repeat_until)

        exceptions = set(event.recurrence_exceptions or [])
        if event.repeat_until:
            end_boundary = min(last_day, event.repeat_until)
        else:
            end_boundary = (
                last_day
            )

        if event.recurrence == 'none':
            if (
                first_day <= event.date <= last_day
                and event.date not in exceptions
            ):
                print("✅ Adding one-time event on:", event.date)
                events_by_day.setdefault(event.date, []).append(event)

        elif event.recurrence == 'weekly':
            current = event.date
            while current <= end_boundary:
                print("🔄 Weekly check:", current)
                if (
                    current >= first_day
                    and current.weekday() == event.date.weekday()
                    and current not in exceptions
                ):
                    print("✅ Adding weekly event on:", current)
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(weeks=1)

        elif event.recurrence == 'biweekly':
            current = event.date
            while current <= end_boundary:
                print("🔄 Biweekly check:", current)
                if (
                    current >= first_day
                    and current.weekday() == event.date.weekday()
                    and current not in exceptions
                ):
                    print("✅ Adding biweekly event on:", current)
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(weeks=2)

        elif event.recurrence == 'monthly':
            current = event.date
            while current <= end_boundary:
                print("🔄 Monthly check:", current)
                if current >= first_day and current not in exceptions:
                    print("✅ Adding monthly event on:", current)
                    events_by_day.setdefault(current, []).append(event)
                try:
                    current += relativedelta(months=1)
                except ValueError:
                    print("❌ Error incrementing monthly")
                    break

        elif event.recurrence == 'custom_days':
            if not event.days_of_week:
                print("⚠️ Skipping custom_days with no days defined")
                continue
            weekday_map = {
                'mon': 0,
                'tue': 1,
                'wed': 2,
                'thu': 3,
                'fri': 4,
                'sat': 5,
                'sun': 6
            }
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
                    print("✅ Adding custom-day event on:", current)
                    events_by_day.setdefault(current, []).append(event)
                current += timedelta(days=1)

    prev_year, prev_month = get_adjacent_month(year, month, -1)
    next_year, next_month = get_adjacent_month(year, month, 1)
    return render(
        request,
        'schedule/calendar.html',
        {
            'year': year,
            'month': date_format(
                date(year, month, 1),
                "F",
                use_l10n=True
            ),
            'month_number': month,
            'weeks': weeks,
            'events_by_day': events_by_day,
            'prev_year': prev_year,
            'prev_month': prev_month,
            'next_year': next_year,
            'next_month': next_month,
        }
    )


def event_list_view(request):
    classes = Class.objects.all()
    events = Event.objects.all().select_related('class_instance')
    return render(request, 'schedule/event_list.html', {
        'classes': classes,
        'events': events
    })


@csrf_exempt
@require_POST
def create_event(request):
    data = json.loads(request.body)
    cls = get_object_or_404(Class, id=data['class_id'])
    exceptions_str = data.get('recurrence_exceptions', '')
    exceptions = [d.strip() for d in exceptions_str.split(',') if d.strip()]
    repeat_until = data.get('repeat_until') or None

    event = Event.objects.create(
        class_instance=cls,
        date=data['date'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        recurrence=data.get('recurrence', 'none'),
        days_of_week=data.get('days_of_week', ''),
        recurrence_exceptions=exceptions,
        repeat_until=repeat_until
    )
    return JsonResponse(model_to_dict(event))


@csrf_exempt
@require_POST
def update_event(request, event_id):
    data = json.loads(request.body)
    event = get_object_or_404(Event, id=event_id)
    event.class_instance = get_object_or_404(Class, id=data['class_id'])
    event.date = data['date']
    event.start_time = data['start_time']
    event.end_time = data['end_time']
    event.recurrence = data.get('recurrence', 'none')
    event.days_of_week = data.get('days_of_week', '')
    exceptions_str = data.get('recurrence_exceptions', '')
    event.recurrence_exceptions = [
        d.strip() for d in exceptions_str.split(',') if d.strip()
    ]
    event.repeat_until = data.get('repeat_until') or None
    event.save()
    return JsonResponse(model_to_dict(event))


@csrf_exempt
@require_POST
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
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
