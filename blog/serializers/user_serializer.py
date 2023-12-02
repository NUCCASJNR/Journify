#!/usr/bin/env python3

"""
User serializer for the API
"""

from rest_framework import serializers
from blog.models.user import User


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer class
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'bio', 'profile_picture')