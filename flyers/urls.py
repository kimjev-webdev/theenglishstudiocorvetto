from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.flyer_list,
        name='flyer_list'
    ),
]
