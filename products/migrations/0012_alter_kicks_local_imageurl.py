# Generated by Django 3.2.12 on 2022-12-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_kicks_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kicks',
            name='local_imageUrl',
            field=models.CharField(default='http://localhost:8000/media/images/defaultImg.png', max_length=500),
        ),
    ]
