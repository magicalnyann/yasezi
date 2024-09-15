# home/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('company/', views.company, name='company'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)