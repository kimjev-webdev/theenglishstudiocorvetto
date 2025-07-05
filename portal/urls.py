from django.urls import path
from .views import (
    portal_dashboard,
    portal_logout_view,
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)
from django.contrib.auth.views import LoginView

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='portal/login.html'),
        name='portal_login'
    ),
    path(
        'logout/',
        portal_logout_view,
        name='portal_logout'
    ),
    path(
        '',
        portal_dashboard,
        name='portal_dashboard'
    ),

    # Blog CRUD routes
    path('blog/', BlogListView.as_view(), name='blog_edit'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path(
        'blog/edit/<int:pk>/',
        BlogUpdateView.as_view(),
        name='blog_edit'
    ),
    path(
        'blog/delete/<int:pk>/',
        BlogDeleteView.as_view(),
        name='blog_delete'
    ),
]
