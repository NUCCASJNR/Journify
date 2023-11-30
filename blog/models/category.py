#!/usr/bin/env python3
"""
Category model
"""

from .base_model import BaseModel, models


class Category(BaseModel):
    """
    Category model class
    columns:
    - name: name of the category
    """
    name = models.CharField(max_length=50, unique=True, default="Miscellaneous")

    class Meta:
        db_table = 'categories'

    def __str__(self) -> str:
        super().__str__()
        return f"Category {self.id} {self.name}"