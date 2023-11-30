#!/usr/bin/env python3

"""
Base model for all models
"""

# Built-in modules
from datetime import datetime
from django.db import models
from typing import Any, Dict, List, Optional, Union
from uuid import uuid4


class BaseModel(models.Model):
    """
    Base model for all models
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.id}"



    @classmethod
    def to_dict(cls, obj: "BaseModel") -> Dict[str, Any]:
        """
        Returns a dictionary representation of the object
        """
        model_dict = {}
        for field in obj._meta.fields:
            field_name = field.name
            field_value = getattr(obj, field_name)

            # Convert special types to a serializable format if needed
            if isinstance(field, models.DateTimeField):
                field_value = field_value.isoformat()
            elif isinstance(field, models.UUIDField):
                field_value = str(field_value)

            model_dict[field_name] = field_value

        return model_dict

    @classmethod
    def get_all(cls) -> List["BaseModel"]:
        """
        Returns all the objects in the database
        """

        return cls.objects.all()

    @classmethod
    def get_by_id(cls, id: Union[str, uuid4]) -> Optional["BaseModel"]:
        """
        Returns the object with the given id
        """

        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_by_ids(cls, ids: List[Union[str, uuid4]]) -> List["BaseModel"]:
        """
        Returns the objects with the given ids
        """

        return cls.objects.filter(id__in=ids)

    @classmethod
    def get_by_ids_str(cls, ids: List[str]) -> List["BaseModel"]:
        """
        Returns the objects with the given ids
        """

        return cls.objects.filter(id__in=[uuid4(id) for id in ids])

    @classmethod
    def save(cls):
        """
        Saves the object in the database
        """

        cls.save()

    @classmethod
    def delete(cls):
        """
        Deletes the object from the database
        """

        cls.objects.delete()

    @classmethod
    def find_obj_by(cls, **kwargs):
        """
        Returns the object with the given kwargs
        """

        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None

    def update(self, **kwargs):
        """
        Updates the object with the given kwargs
        """

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    @classmethod
    def count(cls):
        """
        Returns the number of objects in the database
        """

        return cls.objects.count()