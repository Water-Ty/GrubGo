# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm

class CustomUserCreationView(FormView):
    template_name = 'auth/user_creation_form.html'  # Template to render the form
    form_class = CustomUserCreationForm  # Form class already knows about the model
    success_url = reverse_lazy('main:test')  # Redirect after form submission

    def form_valid(self, form):
        # Save the form (which is bound to CustomUser model) if valid
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)