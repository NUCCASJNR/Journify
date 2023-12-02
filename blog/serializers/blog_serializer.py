#!/usr/bin/env python3
"""Blog serializer"""

from rest_framework import serializers
from blog.models.post import BlogPost


class BlogSerializer(serializers.ModelSerializer):
    """
    Blog Serializer class
    """
    class Meta:
        model = BlogPost
        fields = ('id', 'created_at', 'updated_at', 'title', 'content', 'sub_title',
                  'author_id')
