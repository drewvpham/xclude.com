from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from memberships.models import UserMembership
from .models import Video


class VideoListView(ListView):
    model = Video
