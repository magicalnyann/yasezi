from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.event, name='evento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
