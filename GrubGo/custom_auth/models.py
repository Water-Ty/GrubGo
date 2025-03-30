from django.db import models
import random

# Create your models here.


from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_JOB_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("chef", "Chef"),
    ]
    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, null=True, blank=True
    )
    role = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        choices=USER_JOB_CHOICES,
        default="student",
    )
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    credit = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.username


class School(models.Model):
    school_name = models.CharField(max_length=200, null=False, blank=False)
    school_code = models.CharField(
        max_length=7, unique=True, blank=True, null=True
    )  # Add this field

    @property
    def formatted_code(self):
        return f"{self.school_code:07d}"

    def generate_school_code(self):
        """Generate a unique 7-digit numeric school code."""
        while True:
            code = "".join(random.choices("0123456789", k=7))
            if not School.objects.filter(school_code=code).exists():
                break
        return code

    def save(self, *args, **kwargs):
        if not self.school_code:
            self.school_code = self.generate_school_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.school_name
