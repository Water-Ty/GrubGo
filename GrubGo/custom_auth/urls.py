from django.urls import path

from .views import CustomUserCreationView

urlpatterns = [
    path('test/', CustomUserCreationView.as_view(), name='test'),
]