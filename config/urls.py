"""
URL configuration for the_english_studio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Handles language switching via /i18n/setlang/
    path('i18n/', include('django.conf.urls.i18n')),
    path('contact/', include('contact.urls')),
]

urlpatterns += i18n_patterns(
    # Admin dashboard
    path('admin/', admin.site.urls),

    # Main site URLs (homepage and other views from your app)
    path('', include('main.urls')),
)
