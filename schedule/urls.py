from django.urls import path
from . import views

urlpatterns = [
    # Main views
    path('calendar/', views.calendar_view, name='calendar_view'),
    path(
        'calendar/<int:year>/<int:month>/',
        views.calendar_view,
        name='calendar_by_date'
    ),
    path('schedule/', views.event_list_view, name='schedule'),

    # Event AJAX endpoints
    path('schedule/events/create/', views.create_event, name='create_event'),
    path(
        'schedule/events/<int:event_id>/edit/',
        views.update_event,
        name='update_event'
    ),
    path(
        'schedule/events/<int:event_id>/delete/',
        views.delete_event,
        name='delete_event'
    ),

    # Class AJAX endpoints
    path('schedule/classes/create/', views.create_class, name='create_class'),
    path(
        'schedule/classes/<int:class_id>/edit/',
        views.update_class,
        name='update_class'
    ),
    path(
        'schedule/classes/<int:class_id>/delete/',
        views.delete_class,
        name='delete_class'
    ),
]
