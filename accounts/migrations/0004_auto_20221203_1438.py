# Generated by Django 3.2.12 on 2022-12-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221202_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='nick_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='zipCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
