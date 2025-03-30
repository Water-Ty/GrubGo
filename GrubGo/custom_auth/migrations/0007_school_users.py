# Generated by Django 5.1.7 on 2025-03-30 17:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_auth", "0006_alter_customuser_school"),
    ]

    operations = [
        migrations.AddField(
            model_name="school",
            name="users",
            field=models.ManyToManyField(
                related_name="schools", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
