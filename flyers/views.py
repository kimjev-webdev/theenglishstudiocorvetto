from django.shortcuts import render
from .models import Flyer
from django.utils import timezone


def flyer_list(request):
    flyers = Flyer.objects.filter(
        event_date__gte=timezone.now().date()
    ).order_by('event_date')
    return render(
        request,
        'flyers/flyer_list.html',
        {'flyers': flyers}
    )
