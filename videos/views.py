from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from memberships.models import UserMembership
from .models import Video


class VideoListView(ListView):
    model = Video


class VideoDetailView(DetailView):
    model = Video

class VideoCreateView(CreateView):
    model = Video
    fields = ['title','description', 'videofile','thumbnail', 'private', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['description']

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.uploader:
            return True
        return False


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.uploader:
            return True
        return False
