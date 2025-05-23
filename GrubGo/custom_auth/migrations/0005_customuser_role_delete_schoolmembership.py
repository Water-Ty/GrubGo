# Generated by Django 5.1.7 on 2025-03-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "custom_auth",
            "0004_schoolmembership_status_alter_schoolmembership_role_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("student", "Student"),
                    ("teacher", "Teacher"),
                    ("chef", "Chef"),
                ],
                default="student",
                max_length=200,
            ),
        ),
        migrations.DeleteModel(
            name="SchoolMembership",
        ),
    ]
