from django.shortcuts import render
from flyers.models import Flyer  # ✅ Corrected import from the new app


def home(request):
    flyers = Flyer.objects.order_by("sort_order", "event_date")
    return render(request, "index.html", {"flyers": flyers})


def courses(request):
    return render(request, 'courses.html')


def about(request):
    return render(request, 'about.html')


def calendar(request):
    return render(request, 'calendar.html')


def contact(request):
    return render(request, 'contact.html')
