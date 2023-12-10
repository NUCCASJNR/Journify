from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from blog.models.user import User
from django import forms


class SignupForm(UserCreationForm):
    """
    Signup Form
    """
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')

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

    def clean(self):
        """
        Validates password match
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
