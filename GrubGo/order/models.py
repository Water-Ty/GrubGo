from django.db import models
from custom_auth.models import School, CustomUser

# Create your models here.


class Order(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    food_choice = models.TextField(default="Give me something random!")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user} for {self.school}"
