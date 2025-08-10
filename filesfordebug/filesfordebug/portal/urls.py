from django.urls import path
from django.contrib.auth.views import LoginView
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
]
