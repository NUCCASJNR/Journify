#!/usr/bin/env python3

"""Contains login form"""

from django import forms
from blog.models.user import User
from django.contrib.auth.hashers import check_password


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


def authenticate_by_email(email, password):
    """
    Authenticate by email and password
    """
    user = User
    try:
        u = user.objects.get(email=email)
        if u:
            return user
        else:
            return None
    except User.DoesNotExist:
        return False
