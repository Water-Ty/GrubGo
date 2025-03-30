from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SchoolForm, JoinSchool
from custom_auth.models import School


# Create your views here.

class AddSchoolForm(CreateView, LoginRequiredMixin):
    model = School
    form_class = SchoolForm
    template_name = "school/AddSchool.html"
    success_url = reverse_lazy("school:list-schools")

class ListSchoolsView(ListView, LoginRequiredMixin):
    model = School
    template_name = "school/ListSchools.html"
    context_object_name = "schools"

class JoinSchoolView(CreateView, LoginRequiredMixin):
