# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('company/', views.company, name='company'),
]