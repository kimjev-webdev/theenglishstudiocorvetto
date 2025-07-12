from django.shortcuts import render
from .models import Flyer  # ✅ Import the Flyer model
from django.utils import timezone


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
