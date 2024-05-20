#!/usr/bin/python3

"""Module defines tests for file_storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test File Storage class"""

    def setUp(self):
        self.storage = FileStorage()
        super().setUp()

    def test_all(self):
        """Test all objs returned"""
        model = BaseModel()
        for key, value in self.storage.all().items():
            self.assertIsInstance(value, BaseModel)

    def test_new(self):
        """Test if new object is added to objects"""
        model = BaseModel()
        self.storage.new(model)
        self.assertIsInstance(self.storage.all(), dict)
        all_models = self.storage.all()
        test_model_key = f"{type(model).__name__}.{model.id}"
        model_from_storage = all_models.get(test_model_key)
        self.assertEqual(model_from_storage.id, model.id)

    def test_reload(self):
        """Test if objects are reloaded"""
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("File storage engine raises error")

    def test_save(self):
        """Test save to file"""
        all_models = self.storage.all()
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        model_key = f"{type(model).__name__}.{model.id}"
        self.assertIn(model_key, all_models.keys())

    def test_creating_model_from_dict(self):
        """Test creating model from dict"""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertNotEqual(model, new_model)

    def tearDown(self):
        super().tearDown()
