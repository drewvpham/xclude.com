from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from videos.models import Video, Tag
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    favorite_videos = models.ManyToManyField(Video, blank=True)
    favorite_tags = models.ManyToManyField(
        Tag, blank=True, related_name='favorite_tags')
    exclude_tags = models.ManyToManyField(
        Tag, blank=True, related_name='exclude_tags')
    gender = models.CharField(max_length=35, null=True)
    race = models.CharField(max_length=35, null=True)
    dob = models.DateField(null=True, blank=True)
    orientation = models.CharField(max_length=35, null=True)
    follows = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False, blank=True)
    friends = models.ManyToManyField(
        'self', related_name='friends_with', symmetrical=False, blank=True)
    autoplay = models.BooleanField(default=True)
    random = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_uploader = models.BooleanField(default=False)
    one_click_purchasing = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=User)
