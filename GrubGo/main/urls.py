from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", TestView.as_view(), name="home"),
]
