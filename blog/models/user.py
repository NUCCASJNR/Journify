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
    username = models.CharField(max_length=50, unique=True, blank=False)
    email = models.CharField(max_length=50, unique=True, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    bio = models.TextField(max_length=500, blank=True)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    # Add related_name to resolve clashes with auth.User.groups
    groups = models.ManyToManyField(Group, blank=True, related_name='blog_user_groups')

    # Add related_name to resolve clashes with auth.User.user_permissions
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='blog_user_permissions')

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)

    # @classmethod
    # def up(cls, ):
    #     cls.save()
    #     self.updated_at = datetime.now()