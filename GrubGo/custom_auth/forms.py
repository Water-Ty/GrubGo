from django import forms
from .models import CustomUser, School
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):

    def clean(self):
        cleaned_data = super().clean()  # Call the parent clean method

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')


        return cleaned_data