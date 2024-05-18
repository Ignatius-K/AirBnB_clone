#!/usr/bin/python3

"""Module tests the base_model.py"""

import unittest
from models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    """Test Base Model"""

    def setUp(self):
        super().setUp()

    def test_instance_type(self):
        """Test instance type"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_has_ID_attribute(self):
        """Test if has id attribute"""
        base_model = BaseModel()
        try:
            base_model.id
        except AttributeError:
            self.fail("Base Model does not have ID attribute")

    def test_ID_valid(self):
        """Test if ID is valid"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_has_created_at_attribute(self):
        """Test if has created_at atribute"""
        base_model = BaseModel()
        try:
            base_model.created_at
        except AttributeError:
            self.fail("Base Model does not have created_at attribute")

    def test_has_updated_at_attribute(self):
        """Test if has updated_at atribute"""
        base_model = BaseModel()
        try:
            base_model.updated_at
        except AttributeError:
            self.fail("Base Model does not have updated_at attribute")

    def test_save(self):
        """Test if save updates the updated_at attr"""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        current_updated_at = base_model.updated_at
        self.assertTrue(current_updated_at > initial_updated_at)
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """Tests if instance is properly converted to dict"""
        class_key = "__class__"
        base_model = BaseModel()
        base_model_json = base_model.to_dict()
        self.assertIsInstance(base_model_json, dict)
        try:
            base_model_json[class_key]
        except KeyError:
            self.fail("Model JSON representation doesnt have class attr")

    def tearDown(self):
        super().tearDown()
