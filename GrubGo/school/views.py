from django.shortcuts import reverse, Http404, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SchoolForm, JoinSchool
from custom_auth.models import School
from order.models import Order

# Create your views here.


class AddSchoolForm(CreateView, LoginRequiredMixin):
    model = School
    form_class = SchoolForm
    template_name = "school/AddSchool.html"
    success_url = reverse_lazy("school:list-schools")

    def form_valid(self, form):
        # Save the new school
        response = super().form_valid(form)

        # After saving, associate the current user with the school
        school = self.object  # `self.object` is the newly created school
        school.users.add(
            self.request.user
        )  # Add the logged-in user to the `users` field of the school

        # Return the response
        return response


class ListSchoolsView(ListView, LoginRequiredMixin):

    model = School
    template_name = "school/ListSchools.html"
    context_object_name = "schools"

    def get_queryset(self):
        return School.objects.filter(users=self.request.user)


class SchoolDetailView(DetailView, LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(school=self.object)
        return context

    model = School
    context_object_name = "school"
    template_name = "school/SchoolDetailView.html"

    def get_object(self, queryset=None):
        school_code = self.kwargs["school_code"]
        try:
            school = School.objects.get(school_code=school_code)
        except School.DoesNotExist:
            # Log the error or print debugging info
            print(f"School with school_code '{school_code}' not found.")
            # You can return None or handle it differently
            school = None

        if school is None:
            # Instead of raising 404, you can return a custom message or handle it
            print(f"School not found with code {school_code}.")
            raise Http404("School not found.")

        return school


class JoinSchoolView(LoginRequiredMixin, FormView):
    template_name = "school/JoinSchool.html"
    form_class = JoinSchool
    success_url = reverse_lazy("school:list-schools")

    def form_valid(self, form):
        # Get the current logged-in user
        user = self.request.user

        # Get the school code entered by the user
        school_code = form.cleaned_data["school_code"]

        # Try to get the school by code
        school = get_object_or_404(School, school_code=school_code)

        # Check if the user is already associated with the school
        if school in user.schools.all():
            # If already in the same school, show a message and redirect
            messages.error(self.request, "You are already a member of this school.")
            return redirect("school:list-schools")  # Redirect to the list of schools

        # Associate the user with the school
        school.users.add(user)  # Correctly add the user to the school
        school.save()  # Save the school object after modification

        # Success message
        messages.success(
            self.request, f"You've successfully joined {school.school_name}!"
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid school code. Please try again.")
        return super().form_invalid(form)
