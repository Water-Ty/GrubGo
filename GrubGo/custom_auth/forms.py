from django import forms
from .models import CustomUser, School

class SchoolModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Return the school code when displaying the option
        return obj.school_code  # Display only the school code in the form field

class CustomUserCreationForm(forms.ModelForm):
    school_ = SchoolModelChoiceField(queryset=School.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role', 'school_']

    def clean(self):
        clean_data = super().clean()

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2 and password1 and password2:
            raise forms.ValidationError("Passwords don't match")

        return clean_data