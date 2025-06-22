from django.urls import path
from . import views

urlpatterns = [
    # Public calendar views (front-end)
    path(
        'schedule/',
        views.calendar_view,
        name='schedule'
    ),  # ⬅ front-end calendar view
    path(
        'schedule/<int:year>/<int:month>/',
        views.calendar_view,
        name='calendar_by_date'
    ),

    # Admin portal to manage classes and events (back-end)
    path('portal/schedule/', views.event_list_view, name='schedule_portal'),

    # Event AJAX endpoints
    path(
        'portal/schedule/events/create/',
        views.create_event,
        name='create_event'
    ),
    path(
        'portal/schedule/events/<int:event_id>/edit/',
        views.update_event,
        name='update_event'
    ),
    path(
        'portal/schedule/events/<int:event_id>/delete/',
        views.delete_event,
        name='delete_event'
    ),

    # Class AJAX endpoints
    path(
        'portal/schedule/classes/create/',
        views.create_class,
        name='create_class'
    ),
    path(
        'portal/schedule/classes/<int:class_id>/edit/',
        views.update_class,
        name='update_class'
    ),
    path(
        'portal/schedule/classes/<int:class_id>/delete/',
        views.delete_class,
        name='delete_class'
    ),
]
