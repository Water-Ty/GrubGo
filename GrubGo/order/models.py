from django.db import models
from custom_auth.models import School, CustomUser
# Create your models here.


class FoodChoice(models.Model):
    food_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    def __str__(self):
        return self.food_name


class Order(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    food_choice = models.ManyToManyField(FoodChoice)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)

    def __str__(self):
        return f"Order {self.id} by {self.user} for {self.school.school_name}"

    def calculate_total_price(self):
        self.total_price = sum(item.price for item in self.food_choice.all())
        self.save()
