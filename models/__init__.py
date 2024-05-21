#!/usr/bin/python3

"""__init__ for models package"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

storage = FileStorage()
storage.reload()

__all__ = [
    "BaseModel",
    "User",
]
