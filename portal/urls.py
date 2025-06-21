# portal/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='portal/login.html'), name='portal_login'),
    path('logout/', LogoutView.as_view(next_page='portal_login'), name='portal_logout'),
    path('', views.portal_dashboard, name='portal_dashboard'),
]
