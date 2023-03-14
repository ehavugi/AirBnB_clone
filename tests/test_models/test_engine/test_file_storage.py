#!/usr/bin/python3
"""
Unit tests for City class.

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.city import City
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for fileStorage
    """

    def test_reload(self):
        """
        storage.all() returns a dictionary type
        """
        storage.reload()
        new = storage.all()
        self.assertIsInstance(new, dict)

    def test_new(self):
        """
        Increases  number of stored elements by 1
        """
        old = (storage.all()).copy()
        testCase = BaseModel()
        testCase.my_number = 1001
        storage.new(testCase)
        new = storage.all()
        self.assertEqual(len(new) - len(old), 1)
