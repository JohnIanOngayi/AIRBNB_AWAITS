#!/usr/bin/python3

"""
Test Module for class BaseModel
"""

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    unittest Test class for class BaseModel
    """

    def setUp(self):
        """
        Set up method for class TestBaseModel
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.A = BaseModel()
        self.B = BaseModel()
        self.C = BaseModel()

    def test_init(self):
        """
        Test the class instaniation behaviour
        """
        self.assertNotEqual(self.A.id, self.B.id)
        self.assertGreater(self.A.updated_at, self.A.created_at)
        self.assertGreater(self.B.created_at, self.A.created_at)

    def test_str(self):
        """
        Test the class string method
        """
        self.assertEqual(self.A.__str__,
                         f"[BaseModel] ({self.A.id}) {self.A.__dict__}")
        self.assertEqual(self.B.__str__,
                         f"[BaseModel] ({self.B.id}) {self.B.__dict__}")


if __name__ == "__main__":
    unittest.main()
