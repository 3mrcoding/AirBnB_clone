#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
import models
from datetime import datetime


class BaseModel:
    """A Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """A Initialize a new BaseModel
        Args:
        *args (any): Unused.
        **kwargs (dict): Key/value pairs of attributes.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            for i, j in kwargs.items():
                if i == "__class__":
                    continue
                elif i == "created_at":
                    self.created_at = datetime.strptime
                    (j, "%Y-%m-%dT%H:%M:%S.%f")
                elif i == "updated_at":
                    self.updated_at = datetime.strptime
                    (j, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, i, j)
        else:
            models.storage.new(self)

    def __str__(self):
        """A Return the print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A Save new object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A Save new object as a dict"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = datetime.isoformat(datetime.now())
        rdict["updated_at"] = datetime.isoformat(datetime.now())
        rdict["__class__"] = self.__class__.__name__
        return rdict
