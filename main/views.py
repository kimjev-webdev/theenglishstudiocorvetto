from django.shortcuts import render
from .models import Flyer  # ✅ Import the Flyer model


def home(request):
    flyers = Flyer.objects.order_by('-event_date')[:6]
    return render(
        request,
        'index.html',
        {'flyers': flyers}
    )


def courses(request):
    return render(request, 'courses.html')


def about(request):
    return render(request, 'about.html')


def calendar(request):
    return render(request, 'calendar.html')


def contact(request):
    return render(request, 'contact.html')
