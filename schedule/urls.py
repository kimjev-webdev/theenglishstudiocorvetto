from django.urls import path
from . import views

urlpatterns = [
    # ===== Public calendar (mounted at /schedule/) =====
    path("", views.calendar_view, name="schedule"),
    path(
        "<int:year>/<int:month>/",
        views.calendar_view,
        name="calendar_by_date",
    ),

    # ===== Admin list UI (mounted at /schedule/portal/) =====
    path("portal/", views.event_list_view, name="schedule_portal"),

    # ===== Events AJAX (used by the JS) =====
    # -> /schedule/portal/_/events/create/
    path("portal/_/events/create/", views.create_event, name="create_event"),
    # -> /schedule/portal/_/events/<id>/edit/
    path(
        "portal/_/events/<int:event_id>/edit/",
        views.update_event,
        name="update_event",
    ),
    # -> /schedule/portal/_/events/<id>/delete/
    path(
        "portal/_/events/<int:event_id>/delete/",
        views.delete_event,
        name="delete_event",
    ),

    # ===== Classes AJAX (used by the JS) =====
    # -> /schedule/portal/_/classes/create/
    path("portal/_/classes/create/", views.create_class, name="create_class"),
    # -> /schedule/portal/_/classes/<id>/edit/
    path(
        "portal/_/classes/<int:class_id>/edit/",
        views.update_class,
        name="update_class",
    ),
    # -> /schedule/portal/_/classes/<id>/delete/
    path(
        "portal/_/classes/<int:class_id>/delete/",
        views.delete_class,
        name="delete_class",
    ),
]
