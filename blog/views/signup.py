#!/usr/bin/env python3
"""Handles user signup"""
from django.contrib.auth import authenticate
from rest_framework import serializers
from blog.models.user import User
from blog.serializers.user_serializer import UserSerializer
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect


def home(request):
    """Home page"""
    return render(request, 'blog/category.html')