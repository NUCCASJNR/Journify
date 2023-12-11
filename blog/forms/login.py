#!/usr/bin/env python3

"""Contains login form"""

from django import forms
from blog.models.user import User


class LoginForm(forms.Form):
    """Login form
    params:
    username: Username
    password: Password
    """
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_details(self, username: str, password: str):
        """Validate username"""
        try:
            query = {'username': username, 'password': password}
            user = User.find_obj_by(**{query})
            if user:
                return user
        except forms.ValidationError:
            return "Invalid username or password"
