from django import forms
from .models import FoodChoice, Order

class OrderForm(forms.ModelForm):
    food_choice = forms.ModelMultipleChoiceField(queryset=FoodChoice.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Order
        fields = []