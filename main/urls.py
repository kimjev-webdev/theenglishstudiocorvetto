from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]
