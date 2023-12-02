#!/usr/bin/env python3
"""
Post model
"""

from .base_model import BaseModel, models
from .user import User
from .category import Category


class BlogPost(BaseModel):
    """
    Post model class
    columns:
    - title: title of the post
    content: content of the post
    sub_title: subtitle of the post
    author: author of the post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    sub_title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        db_table = 'blog_posts'

    def __str__(self) -> str:
        super().__str__()
        return f"Post {self.id} {self.title}"
