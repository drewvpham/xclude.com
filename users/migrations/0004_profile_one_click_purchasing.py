# Generated by Django 2.2.7 on 2019-12-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191202_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='one_click_purchasing',
            field=models.BooleanField(default=False),
        ),
    ]
