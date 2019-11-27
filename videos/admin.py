from django.contrib import admin

# Register your models here.
from .models import Tag, Video, Comment, Message, Chat

admin.site.register([Tag, Video, Comment, Message, Chat])
