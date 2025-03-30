from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import OrderForm
from .models import Order
from django.shortcuts import get_object_or_404
from custom_auth.models import School
# Create your views here.


class OrderView(CreateView):
    model = Order
    template_name = "orders/Order.html"
    form_class = OrderForm
    success_url = reverse_lazy("main:home")
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        school_code = self.kwargs.get("school_code")
        self.object.school = get_object_or_404(School, school_code=school_code)  # Assuming `code` is the field identifying the school

        self.object.food_choice = form.cleaned_data['food_choice']
        self.object.save()
        return super().form_valid(form)
