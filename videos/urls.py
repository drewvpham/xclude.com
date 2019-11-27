from django.urls import path

from .views import *



urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    path('', VideoListView.as_view(), name='list'),
]

app_name = 'videos'
