from django import forms
from custom_auth.models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ("school_name", "school_description")


class JoinSchool(forms.Form):
    school_code = forms.CharField(max_length=7, label="Enter School Code")

    def clean_school_code(self):
        code = self.cleaned_data.get("school_code")
        if not School.objects.filter(school_code=code).exists():
            raise forms.ValidationError("Invalid school code. Please try again.")
        return code


class JoinSchoolForm(forms.Form):
    school_code = forms.CharField(
        max_length=7,  # Assuming the school code is 7 characters
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter School Code"}),
    )
