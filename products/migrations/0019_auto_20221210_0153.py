# Generated by Django 3.2.12 on 2022-12-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_kicks_release_date_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kicks',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kicks',
            name='colorway',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='kicks',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='kicks',
            name='product_type',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='kicks',
            name='retailPrice',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kicks',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
