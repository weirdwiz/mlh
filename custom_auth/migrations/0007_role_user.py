# Generated by Django 2.1.1 on 2018-12-01 07:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('custom_auth', '0006_auto_20181201_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
