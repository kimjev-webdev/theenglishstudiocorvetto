from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })


def courses(request):
    return render(request, 'courses.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def events(request):
    return render(request, 'events.html')
