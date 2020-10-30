# NewsApp\urls.py

from django.urls import path

from . import views
from .views import News

urlpatterns = [
    # path('', News, 'News'),
    path("", views.News, name="News"),
]
