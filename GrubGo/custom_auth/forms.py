from django import forms
from .models import CustomUser, School
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SchoolModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.school_code


class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.USER_JOB_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "role",
        ]

    def clean(self):
        cleaned_data = super().clean()

        # Iterate over a copy of cleaned_data to avoid modifying the dictionary during iteration
        for field in cleaned_data.copy():
            if cleaned_data[field] is None:
                self.add_error(field, "This field is required")

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
