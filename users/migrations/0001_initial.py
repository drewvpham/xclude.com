# Generated by Django 2.2.7 on 2019-12-02 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profiles_pics')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(max_length=35, null=True)),
                ('race', models.CharField(max_length=35, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('orientation', models.CharField(max_length=35, null=True)),
                ('autoplay', models.BooleanField(default=True)),
                ('random', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_uploader', models.BooleanField(default=False)),
                ('exclude_tags', models.ManyToManyField(blank=True, related_name='exclude_tags', to='videos.Tag')),
                ('favorite_tags', models.ManyToManyField(blank=True, related_name='favorite_tags', to='videos.Tag')),
                ('favorite_videos', models.ManyToManyField(blank=True, to='videos.Video')),
                ('follows', models.ManyToManyField(related_name='followers', to='users.Profile')),
                ('friends', models.ManyToManyField(related_name='friends_with', to='users.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
