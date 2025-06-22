from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='schedule'),
    path(
        '<int:year>/<int:month>/',
        views.calendar_view,
        name='calendar_by_date'
    ),

    path('calendar/', views.calendar_view, name='calendar_view'),
    path('schedule/', views.event_list_view, name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
    path(
        'events/<int:event_id>/edit/',
        views.update_event,
        name='update_event'
    ),
    path(
        'events/<int:event_id>/delete/',
        views.delete_event,
        name='delete_event'
    ),

    path('classes/create/', views.create_class, name='create_class'),
    path(
        'classes/<int:class_id>/edit/',
        views.update_class,
        name='update_class'
    ),
    path(
        'classes/<int:class_id>/delete/',
        views.delete_class,
        name='delete_class'
    ),
]
