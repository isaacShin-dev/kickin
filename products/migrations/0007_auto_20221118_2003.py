# Generated by Django 3.2.12 on 2022-11-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20221118_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kicks',
            name='category',
        ),
        migrations.RemoveField(
            model_name='kicks',
            name='shoe',
        ),
        migrations.AlterField(
            model_name='kicks',
            name='sku',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
