# Generated by Django 3.2.12 on 2022-12-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20221205_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='nick_name',
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
