from .base_model import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models

"""
User model
"""


class User(AbstractUser, BaseModel):
    """
    User model class
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    class Meta:
        db_table = 'users'
