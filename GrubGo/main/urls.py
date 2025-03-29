from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
]