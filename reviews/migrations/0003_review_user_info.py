# Generated by Django 3.2.12 on 2022-12-08 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20221208_1358'),
        ('reviews', '0002_auto_20221208_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_info',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, to='accounts.userinfo'),
            preserve_default=False,
        ),
    ]
