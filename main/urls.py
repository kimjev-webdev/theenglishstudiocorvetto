from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar, name='schedule'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
