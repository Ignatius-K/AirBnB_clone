#!/usr/bin/python3

"""Test for module user.py"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test User"""

    def test_create_user(self):
        """Test user instance"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(type(user), User)
        self.assertNotEqual(type(user), BaseModel)
        self.assertIsNotNone(user.id)
