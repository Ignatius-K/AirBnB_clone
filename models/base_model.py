#!/usr/bin/python3

"""Defines model to be subclassed by all models"""

import uuid
from datetime import datetime

CLASS_KEY = "__class__"

class BaseModel:
    """Base Model defining common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Define BaseModel instance

        Args:
            id (str): Instance ID
            created_at (str): The time when instance created
            updated_at (str): The time when instance last updated
        """
        if len(kwargs.items()) > 0:
            self.from_dict(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return instance string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert base_model instance to dict"""
        temp = {}
        temp[CLASS_KEY] = type(self).__name__
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                value = value.isoformat()
            temp[key] = value
        return (temp)

    def from_dict(self, values: dict):
        """Create an instance from dict

        Args:
            values (dict): The dict_values
        """
        date_keys = ["created_at", "updated_at"]
        for key, value in values.items():
            if key == CLASS_KEY:
                continue
            if key in date_keys:
                value = datetime.fromisoformat(value)
            setattr(self, key, value)
