# Generated by Django 3.2.12 on 2022-09-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='media/user.png', null=True, upload_to=''),
        ),
    ]