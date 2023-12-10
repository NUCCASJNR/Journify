#!/usr/bin/env python3
"""Handles user signup"""

from django.shortcuts import render, redirect
from blog.forms.signup import SignupForm
from django.contrib.auth import login as login_user
from django.contrib import messages
from rest_framework import serializers
from blog.models.user import User


def home(request):
    """Handles home page"""
    return render(request, 'blog/category.html')


def signup(request):
    """Handles user signup"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            clean_email = form.cleaned_data['email']
            clean_username = form.cleaned_data['username']

            # Check if email or username already exists
            if User.find_obj_by(email=clean_email):
                form.add_error('email', 'Email already exists')
            if User.find_obj_by(username=clean_username):
                form.add_error('username', 'Username already exists')

            # If there are errors, render the form with the errors
            if form.errors:
                return render(request, 'blog/register.html', {'form': form})
            form.save()
            # If email and username are unique, proceed with account creation
            user = User.save(**form.cleaned_data)
            login(request, user)  # Log in the user after signup
            messages.success(request, 'Account created successfully')
            # You can redirect the user to another page or log them in, etc.
            return redirect('home')  # Assuming you have a URL named 'home'
    else:
        form = SignupForm()

    return render(request, 'blog/register.html', {'form': form})
# Compare this snippet from blog/views/signup.py:
