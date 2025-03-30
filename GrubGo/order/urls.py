from django.urls import path
from .views import OrderView
app_name = "order"

urlpatterns = [path("<str:school_code>", OrderView.as_view(), name="order")]
