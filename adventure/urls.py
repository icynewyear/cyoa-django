"""CYOAGen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from .views import AdventureListView, AdventureDetailView, AdventureUpdateView, AdventureCreateView, RoomPlayView, register_view

urlpatterns = [
    path('', AdventureListView.as_view(), name= 'adventure-list'),
    path('register/', register_view, name="register"),
    path('create/', AdventureCreateView.as_view(), name= 'adventure-create'),
    path('<slug:slug>/', AdventureDetailView.as_view(), name= 'adventure-detail'),
    path('<slug:slug>/edit', AdventureUpdateView.as_view(), name= 'adventure-update'),
    path('<slug:adv_slug>/<int:pk>/play', RoomPlayView.as_view(), name = 'play-room'),
]
