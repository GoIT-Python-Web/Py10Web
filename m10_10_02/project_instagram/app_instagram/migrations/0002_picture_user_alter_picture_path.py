# Generated by Django 4.2 on 2023-04-19 18:18

import app_instagram.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_instagram", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="picture",
            name="user",
            field=models.ForeignKey(
                default=4,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="picture",
            name="path",
            field=models.ImageField(upload_to=app_instagram.models.update_filename),
        ),
    ]
