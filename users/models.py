from django.contrib.auth.models import AbstractUser
from django.db import models
from videos.models import Video, Tag

class CustomUser(AbstractUser):
    favorite_videos = models.ManyToManyField(Video, blank=True)
    favorite_tags = models.ManyToManyField(Tag, blank=True, related_name='favorite_tags')
    exclude_tags = models.ManyToManyField(Tag, blank=True, related_name='exclude_tags')
    gender = models.CharField(max_length=35, null=True)
    race = models.CharField(max_length=35, null=True)
    dob = models.CharField(max_length=35, null=True)
    orientation = models.CharField(max_length=35, null=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    friends = models.ManyToManyField('self', related_name='friends_with', symmetrical=False)

    def __str__(self):
        return self.username
