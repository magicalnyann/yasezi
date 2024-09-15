"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('recomm/', views.recomm, name='recomm'),
    path('recomm/<int:content_id>/', views.recomm_detail, name='recomm_detail'),
    path('<int:content_id>/', views.detail, name='detail'),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update,name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]