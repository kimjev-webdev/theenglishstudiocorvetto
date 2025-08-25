from django.shortcuts import render
from .models import Flyer
from django.utils import timezone


def flyer_list(request):
    flyers = Flyer.objects.filter(
        event_date__gte=timezone.now().date()
    ).order_by('sort_order', 'event_date', 'pk')  # ✅ respects your drag order
    return render(request, 'flyers/flyers_list.html', {'flyers': flyers})
