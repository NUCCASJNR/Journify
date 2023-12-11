#!/usr/bin/env python3

"""Login view"""

from django.shortcuts import render, redirect
from blog.forms.login import LoginForm
from blog.models.user import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    """Login view"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                # form.validate_details(username, password)
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user)
                    messages.success(request, f'Hi {username.title()}, welcome back!')
                    return redirect('dashboard')
            except Exception as e:
                messages.error(str(e))
    else:
        form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})


def dashboard(request):
    """Dashboard view"""
    return render(request, 'blog/category.html')