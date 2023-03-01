# Generated by Django 3.2.12 on 2022-12-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_kicks_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kicks',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kicks',
            name='sku',
            field=models.CharField(blank=True, default=' ', max_length=200, null=True, unique=True),
        ),
    ]