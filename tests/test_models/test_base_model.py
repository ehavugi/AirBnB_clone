#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
"""
tests for base model

"""


class TestBaseModel(unittest.TestCase):
    """
    Test cases for base model.
    """
    def test_uuid(self):
        """
        test uuid is well assigned to instances
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(hasattr(b1, "id"))
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b2.id, str)
