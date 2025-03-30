# views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomUserCreationView(FormView):
    template_name = "auth/user_creation_form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("main:home")
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "auth/user_login_form.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("main:home")
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # If the request is GET, redirect to the confirmation page
        if request.method == "GET":
            return redirect("custom_auth:confirmlogout")
        # If the request is POST, proceed with logout
        return super().dispatch(request, *args, **kwargs)


class ConfirmLogout(TemplateView, LoginRequiredMixin):
    template_name = "auth/user_logout_form.html"

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is already authenticated
        if not (request.user.is_authenticated):
            return redirect(
                "custom_auth:login"
            )  # Redirect to your home page or dashboard
        return super().dispatch(request, *args, **kwargs)
