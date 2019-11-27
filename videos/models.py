from django.db import models
from memberships.models import Membership
from django.conf import settings
from django_extensions.db.fields import AutoSlugField

class Tag(models.Model):
    name = models.CharField(max_length=35)
    slug = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=False)

class Video(models.Model):
    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from="title")
    description = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    thumbnail = models.ImageField()
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    modified_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Rating(models.Model):
    score = models.IntegerField(null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LikedVideos(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class SavedVideos(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

class WatchedVideos(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='sender')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name = 'receiver')
    subject = models.CharField(max_length=35)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
