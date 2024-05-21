#!/usr/bin/python3

"""Module for User type"""

from models.base_model import BaseModel


class User(BaseModel):
    """"Define User class

    Args:
        first_name (str): User's first name
        last_name (str): User's last name
        email (str): User's email
        password (str): user's password
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """Define User instance

        Args:
            kwargs: User attributes
        """
        super().__init__(*args, **kwargs)
