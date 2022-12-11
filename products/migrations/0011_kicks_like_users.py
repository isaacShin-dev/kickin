# Generated by Django 3.2.12 on 2022-12-02 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_alter_kicks_local_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='kicks',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_users', to=settings.AUTH_USER_MODEL),
        ),
    ]