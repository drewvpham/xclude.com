# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from videos.models import Video, Tag
#
#
# class CustomUser(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     favorite_videos = models.ManyToManyField(Video, blank=True)
#     favorite_tags = models.ManyToManyField(Tag, blank=True, related_name='favorite_tags')
#     exclude_tags = models.ManyToManyField(Tag, blank=True, related_name='exclude_tags')
#     gender = models.CharField(max_length=35, null=True)
#     race = models.CharField(max_length=35, null=True)
#     dob = models.DateField(null=True, blank=True)
#     orientation = models.CharField(max_length=35, null=True)
#     follows = models.ManyToManyField('self', related_name='followers', symmetrical=False)
#     friends = models.ManyToManyField('self', related_name='friends_with', symmetrical=False)
#     autoplay = models.BooleanField(default=True)
#     random = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_uploader = models.BooleanField(default=False)

#
#     def __str__(self):
#         return self.username

from django.db import models
from videos.models import Video, Tag

# Create your models here.
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        # user.password = password # bad - do not do this

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username, email, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(
        max_length=300,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='Username must be alphanumeric',
                           code='invalid_username'
                           )],
        unique=True
    )
    email = models.EmailField(
         max_length=255,
         unique=True,
         verbose_name='email address'
         )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
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
        'self', related_name='followers', symmetrical=False)
    friends = models.ManyToManyField(
        'self', related_name='friends_with', symmetrical=False)
    autoplay = models.BooleanField(default=True)
    random = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_uploader = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
