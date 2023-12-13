#!/usr/bin/env python3

"""Login view"""

from django.shortcuts import render, redirect
from blog.forms.login import LoginForm, authenticate_by_email
from blog.models.user import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):
    """Login view"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, f'Hi {username.title()}, welcome back!')
                    return redirect('dashboard')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


@login_required
def dashboard(request):
    """Dashboard view"""
    return render(request, 'blog/category.html')


@login_required
def logout(request):
    """Logout view"""
    auth_logout(request)
