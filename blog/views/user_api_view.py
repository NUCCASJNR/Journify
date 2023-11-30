#!/usr/bin/env python3
"""
User serializer for the API
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models.user import User
from blog.serializers import UserSerializer
from django.http import JsonResponse


class UserListView(APIView):
    """
    User list view
    """
    def get(self, request):
        """
        GET request handler
        """
        users = User.get_all()
        users_list = [user.to_dict for user in users]
        return JsonResponse(users_list, safe=False)

    def post(self, request):
        """
        POST request handler
        """
        serializer = UserSerializer(data=request.data)
        required_fields = ['username', 'email', 'password', 'first_name', 'last_name']
        for field in required_fields:
            if field not in serializer.initial_data:
                return JsonResponse({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            new_user = serializer.save()
            user_dict = new_user.to_dict()
            return JsonResponse(user_dict, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)