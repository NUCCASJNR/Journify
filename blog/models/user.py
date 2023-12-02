from blog.models.base_model import BaseModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from datetime import datetime

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

    # Add related_name to resolve clashes with auth.User.groups
    groups = models.ManyToManyField(Group, blank=True, related_name='blog_user_groups')

    # Add related_name to resolve clashes with auth.User.user_permissions
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='blog_user_permissions')

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the username to the email
        """
        # self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    # @classmethod
    # def up(cls, ):
    #     cls.save()
    #     self.updated_at = datetime.now()