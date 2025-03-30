from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    CustomUserCreationView,
    CustomLoginView,
    CustomLogoutView,
    ConfirmLogout,
)

app_name = "custom_auth"

urlpatterns = [
    path("register/", CustomUserCreationView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/confirm", ConfirmLogout.as_view(), name="confirmlogout"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
