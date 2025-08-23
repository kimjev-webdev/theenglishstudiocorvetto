from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import (
    portal_dashboard,
    portal_logout_view,
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    FlyerListView,
    FlyerCreateView,
    FlyerUpdateView,
    FlyerDeleteView,
)

urlpatterns = [
    # Login + logout
    path(
        'login/',
        LoginView.as_view(
            template_name='portal/login.html',
            success_url=reverse_lazy('portal:portal_dashboard')
        ),
        name='portal_login'
    ),
    path('logout/', portal_logout_view, name='portal_logout'),

    # Dashboard
    path('', portal_dashboard, name='portal_dashboard'),

    # Blog CRUD
    path(
        'blog/',
        BlogListView.as_view(),
        name='blog_list'
    ),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path(
        'blog/delete/<int:pk>/',
        BlogDeleteView.as_view(),
        name='blog_delete'
    ),


    # Flyer CRUD
    path('flyers/', FlyerListView.as_view(), name='flyer_list'),
    path('flyers/new/', FlyerCreateView.as_view(), name='flyer_create'),
    path(
        'flyers/<int:pk>/edit/',
        FlyerUpdateView.as_view(),
        name='flyer_update'
    ),
    path(
        'flyers/<int:pk>/delete/',
        FlyerDeleteView.as_view(),
        name='flyer_delete'
    ),

    path("flyers/reorder/", views.flyers_reorder, name="flyers_reorder"),


    # User management
    path("users/", views.portal_users_list, name="portal_users"),
    path("users/create/", views.portal_user_create, name="portal_user_create"),
    path(
        "users/<int:user_id>/edit/",
        views.portal_user_edit,
        name="portal_user_edit"
    ),
    path(
        "users/<int:user_id>/delete/",
        views.portal_user_delete,
        name="portal_user_delete"
    ),

    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="portal/password_reset_form.html",
            email_template_name="portal/emails/password_reset_email.txt",
            subject_template_name="portal/emails/password_reset_subject.txt",
            success_url=reverse_lazy("portal:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="portal/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="portal/password_reset_confirm.html",
            success_url=reverse_lazy("portal:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="portal/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),

]
