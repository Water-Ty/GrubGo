from django.urls import path
from .views import AddSchoolForm, ListSchoolsView
app_name = "school"

urlpatterns = [
    path("add-school/", AddSchoolForm.as_view(), name="add-school"),
    path("list-schools/", ListSchoolsView.as_view(), name="list-schools"),
]