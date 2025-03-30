from django import forms
from custom_auth.models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ("school_name",)