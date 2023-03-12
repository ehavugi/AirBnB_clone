#!/usr/bin/python3
"""
Tests for BaseModel  class

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for base model.
    """
    testCase = BaseModel()

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

    def test_created_at(self):
        """
        Test created at attribute.
        """
        self.assertTrue(hasattr(self.testCase, "created_at"))
        self.assertIsInstance(self.testCase.created_at, datetime)

    def test_updated_at(self):
        """
        Test updated_at attributed
            does it exist?
            is it of a datetime  class
        """
        self.assertTrue(hasattr(self.testCase, "updated_at"))
        self.assertIsInstance(self.testCase.updated_at, datetime)

    def test_save(self):
        """
        test save
            does BaseModel have save attribute?
            does is updated_at changed to new value(higher) when saved

        """
        self.assertTrue(hasattr(self.testCase, "save"))
        self.testCase.save()
        self.assertTrue(self.testCase.updated_at > self.testCase.created_at)

    def test_to_dict(self):
        """
        test to_dict
            does BaseModel have to_dict attr
            is return of call to to_dict return a dictionary?
            does the returned dictionary has following keys
            ['updated_at', "created at", "__class__"]
        """
        self.assertTrue(hasattr(self.testCase, "to_dict"))
        self.assertIsInstance(self.testCase.to_dict(), dict)
        self.assertIn("updated_at", self.testCase.to_dict())
        self.assertIn("created_at", self.testCase.to_dict())
        self.assertIn("__class__", self.testCase.to_dict())
