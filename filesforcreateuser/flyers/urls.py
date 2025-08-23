from django.urls import path
from .views import flyer_list  # or use views.flyer_list if importing views

urlpatterns = [
    path('', flyer_list, name='flyer_list'),
]
