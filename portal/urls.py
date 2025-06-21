# portal/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='portal/login.html'), name='portal_login'),
    path('logout/', LogoutView.as_view(next_page='portal_login'), name='portal_logout'),
    path('', views.portal_dashboard, name='portal_dashboard'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]

from .views import (
    BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView
)
