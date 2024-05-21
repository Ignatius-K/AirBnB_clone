#!/usr/bin/python3

"""Define console for AirBnB"""

import cmd
import models
from models import *


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    __models = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, line):
        """Create a base-model instance"""
        model_type = self.__class__.get_model(line)
        if not model_type:
            return
        model = model_type()
        model.save()
        print(model.id)

    def do_show(self, line):
        """Print string repr of instance based on class_name and ID"""
        model_type = self.__class__.get_model(line)
        if not model_type:
            return
        model_id = self.__class__.get_model_id(line)
        if not model_id:
            return
        model_key = f"{model_type.__name__}.{model_id}"
        model = models.storage.all().get(model_key)
        if not model:
            print("** no instance found **")
            return
        print(model)

    def do_destroy(self, line):
        """Delete instance based on class_name and id"""
        model_type = self.__class__.get_model(line)
        if not model_type:
            return
        model_id = self.__class__.get_model_id(line)
        if not model_id:
            return
        model_key = f"{model_type.__name__}.{model_id}"
        model = models.storage.all().get(model_key)
        if not model:
            print("** no instance found **")
            return
        del models.storage.all()[model_key]
        models.storage.save()

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        model_type = self.__class__.get_model(line)
        if not model_type:
            return
        model_id = self.__class__.get_model_id(line)
        if not model_id:
            return
        model_key = f"{model_type.__name__}.{model_id}"
        model = models.storage.all().get(model_key)
        if not model:
            print("** no instance found **")
            return
        update_attr_map = self.__class__.get_attr(line)
        for key, value in update_attr_map.items():
            model.__setattr__(key, value)
        model.save()
        print(model)

    def do_all(self, line):
        """Print all instances based on or not on class name"""
        if not line:
            print([str(model) for _, model in models.storage.all().items()])
            return
        _type = self.__class__.get_model(line)
        if not _type:
            return
        all_models = models.storage.all().items()
        print([str(model) for _, model in all_models if type(model) is _type])

    @classmethod
    def get_attr(cls, line):
        """Gets attributes from command line args

        Args:
            line (str): The command

        Return:
            (dict): Attributes dict if exist else None
        """
        temp_args = line.split()[2:]
        if len(temp_args) == 0:
            print("** attribute name missing **")
            return (None)
        if len(temp_args) == 1:
            print("** value missing **")
            return (None)
        args = {}
        args[temp_args[0]] = temp_args[1].strip("\"")
        return (args)

    @classmethod
    def get_model_id(cls, line):
        """Get model ID

        Args:
            line (str): The command-line args

        Return:
            (str): The Id if exists else None
        """
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return (None)
        return args[1]

    @classmethod
    def get_model(cls, line):
        """Gets the model or class

        Args:
            line (str): The command-line args

        Return:
            model (type): The model
        """
        if not line:
            print("** class name missing **")
            return (None)
        args = line.split()
        if args[0] not in cls.__models.keys():
            print("** class doesn't exist **")
            return (None)
        return (cls.__models.__getitem__(args[0]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
