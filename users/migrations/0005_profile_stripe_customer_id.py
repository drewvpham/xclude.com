# Generated by Django 2.2.7 on 2019-12-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_one_click_purchasing'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
