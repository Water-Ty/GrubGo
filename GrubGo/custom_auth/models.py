from django.db import models
from django.shortcuts import reverse
import random
from django.contrib.auth import get_user_model

# Create your models here.


from django.contrib.auth.models import AbstractUser

from GrubGo.order.models import Order


class CustomUser(AbstractUser):
    USER_JOB_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("chef", "Chef"),
    ]
    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, null=True, blank=True, related_name="created_schools"
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
    school_name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    school_description = models.TextField(null=False, blank=False, unique=False, default="My Unique Orginization!")
    school_code = models.CharField(
        max_length=7, unique=True, blank=True, null=True,
    )
    users = models.ManyToManyField(CustomUser, related_name='schools', blank=True)
    orders = models.ManyToManyField(Order, related_name='schools', blank=True)


    def __str__(self):
        return self.school_name
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



    def get_absolute_url(self):
        return reverse('school:detail-schools', kwargs={'school_code': self.school_code})

