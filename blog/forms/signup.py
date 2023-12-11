from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from blog.models.user import User


class SignupForm(UserCreationForm):
    """
    Signup Form
    """
    email = forms.EmailField(max_length=255)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_email(self):
        """
        Validates email
        """
        email = self.cleaned_data['email']
        try:
            check_email = User.find_obj_by(**{'email': email})
            if check_email:
                raise forms.ValidationError("Email already exists")
        except ValidationError as e:
            raise forms.ValidationError(e)

        return email

    def clean_username(self):
        """
        Validates username
        """
        username = self.cleaned_data['username']
        try:
            check_username = User.find_obj_by(**{'username': username})
            if check_username:
                raise forms.ValidationError("Username already exists")
        except ValidationError as e:
            raise forms.ValidationError(e)

        return username
