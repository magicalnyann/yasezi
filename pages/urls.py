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
from .views import like_lounge, dislike_lounge

urlpatterns = [
path('commu/', views.commu, name='commu'),
path('add_lounge/', views.add_lounge, name='add_lounge'),
path('lounge/<int:lounge_id>/', views.commu_detail, name='commu_detail'),
path('lounge/<int:lounge_id>/edit/', views.lounge_edit, name='lounge_edit'),
path('lounge/<int:lounge_id>/del/', views.lounge_del, name='lounge_del'),
path('lounge/<int:lounge_id>/like/', like_lounge, name='like_lounge'),
path('lounge/<int:lounge_id>/dislike/', dislike_lounge, name='dislike_lounge'),
path('lounge/comments/<int:lounge_id>/', views.make_comments, name='make_comments'),
path('lounge/comments/<int:lounge_id>/dedet/<int:parent_comment_id>/', views.dedet, name='dedet'),
path('comments/<int:comment_id>/toggle_like/', views.toggle_like, name='toggle_like'),
path('replies/<int:reply_id>/toggle_like/', views.toggle_reply_like, name='toggle_reply_like'),
]