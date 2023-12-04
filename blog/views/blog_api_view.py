#!/usr/bin/env python3

"""BlogPost API View"""

from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status
from blog.models.post import BlogPost, User
from blog.serializers.blog_serializer import BlogSerializer
from django.http import JsonResponse
from blog.serializers.user_serializer import UserSerializer


class BlogListView(APIView):
    """BlogListView Class"""

    def get(self, request):
        """
        GET request handler
        """
        blogs = BlogPost.get_all()
        blogs_list = [blog.to_dict(blog) for blog in blogs]

        # Serialize User objects in blogs_list
        for blog in blogs_list:
            blog['user_id'] = UserSerializer(blog['user_id']).data['id']

        if not blogs_list:
            return JsonResponse({"status": "opps no blogposts here yet try get users to post"})
        return JsonResponse(blogs_list, safe=False)


class BlogAddView(APIView):
    """BlogAddView List"""

    def post(self, request):
        """
        POST request handler
        """
        serializer = BlogSerializer(data=request.data)
        required_fields = ['title', 'content', 'user_id']
        for field in required_fields:
            if field not in serializer.initial_data:
                return JsonResponse({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            new_post = BlogPost.custom_save(**serializer.validated_data)

            # Serialize the User object in the response
            user_serializer = UserSerializer(new_post.user_id)
            serialized_user = user_serializer.data

            # Include the serialized User object in the response
            post_dict = new_post.to_dict(new_post)
            post_dict['user_id'] = serialized_user

            return JsonResponse(post_dict, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
