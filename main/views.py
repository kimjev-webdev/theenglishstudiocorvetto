from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def events(request):
    return render(request, 'events.html')


def calendar(request):
    return render(request, 'calendar.html')
