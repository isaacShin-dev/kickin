# Generated by Django 3.2.12 on 2022-12-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_kicks_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='kicks',
            name='product_type',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kicks',
            name='release_date_year',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kicks',
            name='retailPriceKrw',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kicks',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]
