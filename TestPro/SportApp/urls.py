# Sports\urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.Sports, name="Sports"),
]
