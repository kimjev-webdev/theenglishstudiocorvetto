# main/views.py
from django.shortcuts import render
from django.db.models import F
from flyers.models import Flyer  # ✅ from the flyers app


def home(request):
    # Include undated flyers; keep a predictable order
    flyers = Flyer.objects.order_by(
        "sort_order",
        F("event_date").asc(nulls_last=True),
        "pk",
    )
    return render(request, "index.html", {"flyers": flyers})


def courses(request):
    return render(request, "courses.html")


def about(request):
    return render(request, "about.html")


def calendar(request):
    return render(request, "calendar.html")


def contact(request):
    return render(request, "contact.html")


def privacy(request):
    return render(request, "privacy.html")
