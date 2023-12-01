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
from django.core.exceptions import ObjectDoesNotExist


class UserListView(APIView):
    """
    User list view
    """

    def get(self, request):
        """
        GET request handler
        """
        users = User.get_all()
        users_list = [user.to_dict(user) for user in users]
        return JsonResponse(users_list, safe=False)


class PostUserView(APIView):
    """
    User POST view
    """

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
            user_dict = User.to_dict(new_user)
            return JsonResponse(user_dict, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserWithIdView(APIView):
    """
    Retrieve a user from the users table with the id passed to the url
    """

    def get(self, request, user_id):
        """
        GET request handler
        """
        try:
            user = User.get_by_id(user_id)
            user_dict = User.to_dict(user)
            return JsonResponse(user_dict)
        except ObjectDoesNotExist:
            return JsonResponse({"error": f"User with id {str(user_id)} does not exist"},
                                status=status.HTTP_404_NOT_FOUND)


class DeleteUserWithIdView(APIView):
    """
    This view handles Deleting a user from the users table using the user_id passed t the URL
    """

    def delete(self, request, user_id):
        """
        Delete request handler
        """
        try:
            user = User.get_by_id(user_id)
            user.delete()
            return JsonResponse({"status": "Success user has been successfully deleted"})
        except ObjectDoesNotExist:
            return JsonResponse({"error": f"User with id {str(user_id)} does not exist"},
                                status=status.HTTP_404_NOT_FOUND)

