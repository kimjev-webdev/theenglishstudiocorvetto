from django.shortcuts import render
from django.utils import timezone
from flyers.models import Flyer  # ✅ Corrected import from the new app


def home(request):
    flyers = (
        Flyer.objects
        .filter(event_date__gte=timezone.now().date())
        .order_by('event_date')
    )
    return render(request, 'index.html', {'flyers': flyers})


def courses(request):
    return render(request, 'courses.html')


def about(request):
    return render(request, 'about.html')


def calendar(request):
    return render(request, 'calendar.html')


def contact(request):
    return render(request, 'contact.html')
