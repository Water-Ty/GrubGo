from django.urls import path
from .views import AddSchoolForm, ListSchoolsView, SchoolDetailView, JoinSchoolView
app_name = "school"

urlpatterns = [
    path("add-school/", AddSchoolForm.as_view(), name="add-school"),
    path("list-schools/", ListSchoolsView.as_view(), name="list-schools"),
    path("school/<str:school_code>/", SchoolDetailView.as_view(), name="detail-schools"),
    path("join/", JoinSchoolView.as_view(), name="join-school"),
]