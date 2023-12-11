#!/usr/bin/env python3
"""Handles user signup"""

import logging
from django.shortcuts import render, redirect
from blog.forms.signup import SignupForm
from django.contrib.auth import login as login_user
from django.contrib import messages
from blog.models.user import User

# Configure logging to write to a file
logging.basicConfig(
    filename='signup_logs.log',  # Specify the file path for the log
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s [%(levelname)s] - %(message)s',
)


def home(request):
    """Handles home page"""
    return render(request, 'blog/category.html')


def signup(request):
    """Handles user signup"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            clean_email = form.cleaned_data['email']
            clean_username = form.cleaned_data['username']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password1']
            u_dict = {
             'username': clean_username,
             'email': clean_email,
             'first_name': first_name,
             'last_name': last_name,
             'password': password
            }
            # Check if email or username already exists
            if User.find_obj_by(email=clean_email):
                messages.error('Email already exists')
            if User.find_obj_by(username=clean_username):
                messages.error('Username already exists')

            # If there are errors, log and render the form with the errors
            if form.errors:
                logging.error(f"Form validation errors: {form.errors}")
                return render(request, 'blog/register.html', {'form': form})

            # If email and username are unique, proceed with account creation
            user = User(**u_dict)
            print("User object before saving:", user)  # Add this line to check the user object
            user.save()
            login_user(request, user)  # Log in the user after signup
            messages.success(request, 'Account created successfully')
            print(f"User {user.username} created and logged in successfully")
            logging.info(f"User {user.username} created and logged in successfully")

            # You can redirect the user to another page or log them in, etc.
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignupForm()

    return render(request, 'blog/register.html', {'form': form})
