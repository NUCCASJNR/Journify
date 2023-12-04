#!/usr/bin/env python3

"""BlogPost API View"""

from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status
from blog.models.post import BlogPost, User
from blog.serializers.blog_serializer import BlogSerializer
from django.http import JsonResponse
from blog.serializers.user_serializer import UserSerializer
from django.core.exceptions import ObjectDoesNotExist, ValidationError


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
            u_id = new_post['user_id']
            try:
                user = User.get_by_id(u_id)
                if user:
                    user_serializer = UserSerializer(u_id)
                    serialized_user = user_serializer.data

                    # Include the serialized User object in the response
                    post_dict = new_post.to_dict(new_post)
                    post_dict['user_id'] = serialized_user
                    return JsonResponse(post_dict, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return JsonResponse({"error": f"Invalid UUID: {e}"}, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                return JsonResponse({'error': f"user with {u_id} doesn't exist"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountAllPostViews(APIView):
    """View for counting the number of posts"""

    def get(self, request):
        """Count Posts"""
        posts = BlogPost.count()
        return JsonResponse({"No of posts": posts}, status=status.HTTP_200_OK)


class ListAUserBlogPosts(APIView):
    """Handles listing a user's blog posts"""

    def get(self, request, user_id):
        """
        List all the blogposts of a user
        """
        try:
            user = User.get_by_id(user_id)
            if user:
                blogs = BlogPost.find_obj_by(**{'user_id': user_id})
                blog_serializer = BlogSerializer(blogs, many=True)
                serialized_blogs = blog_serializer.data
                if not serialized_blogs:
                    return JsonResponse({"status": f"User with id: {user_id} doesn't have any blog posts yet"})
                return JsonResponse(serialized_blogs, safe=False)
        except ValidationError:
            return JsonResponse({'error': f"user with {user_id} doesn't exist"}, status=status.HTTP_403_FORBIDDEN)


class GetBlogPostView(APIView):
    """Handles getting a blog post"""

    def get(self, request, post_id):
        """
        GET request handler
        """
        try:
            blog = BlogPost.get_by_id(post_id)
            blog_dict = BlogPost.to_dict(blog)
            blog_dict['user_id'] = UserSerializer(blog_dict['user_id']).data['id']
            return JsonResponse(blog_dict)
        except ValidationError:
            return JsonResponse({"error": f"BlogPost with id {str(post_id)} does not exist"},
                                status=status.HTTP_404_NOT_FOUND)