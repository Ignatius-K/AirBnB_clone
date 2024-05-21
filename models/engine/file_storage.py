#!/usr/bin/python3

"""Module defines File Storage"""

import json
import os
from models.base_model import CLASS_KEY, BaseModel
from models import *


DEFAULT_FILE_PATH = "file.json"


class FileStorage:

    """Defines File Storage engine

    __file_path (str): The path to the JSON file
    __objects: (dict): The serialized objects in JSON file
    """
    __file_path = DEFAULT_FILE_PATH
    __objects = {}

    def all(self):
        """Returns all serialized objects"""
        return (self.__objects)

    def new(self, obj: BaseModel):
        """Adds new object in objects

        Args:
            obj: The object to add
        """
        obj_json = obj.to_dict()
        obj_key = f"{obj_json.get(CLASS_KEY)}.{obj_json.get('id')}"
        self.__objects.__setitem__(obj_key, obj)

    def save(self):
        """Saves the objects to JSON file"""
        data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Reloads the objects in JSON

        Note:
            - Only if JSON file exists
            - If file doesn't exist, dont raise exception
        """
        file_path = FileStorage.__file_path
        if not (os.path.exists(file_path) and os.path.isfile(file_path)):
            return

        data = None
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            return
        FileStorage.__objects = {k: globals()[k.split(".")[0]](**v) for k, v in data.items()}
